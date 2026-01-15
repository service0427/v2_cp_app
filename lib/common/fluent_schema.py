"""
FluentSchema - APK 기반 자동 스키마 생성기
==========================================

APK의 smali 파일을 파싱하여 스키마 정의를 자동 추출하고,
런타임에 스키마를 동적으로 생성합니다.

사용법:
    from lib.common.fluent_schema import FluentSchema

    # 스키마 빌더 생성
    schema = FluentSchema('SrpProductClick')

    # 데이터 설정
    schema.set('q', '게이밍 의자')
    schema.set('productId', '12345')

    # 또는 context에서 자동 매핑
    schema.from_context(context, {
        'q': 'INPUT.q',
        'productId': 'RESULT.ROOT.productId'
    })

    # 전송용 딕셔너리 생성
    payload = schema.build(context)
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from functools import lru_cache


# APK 디컴파일 경로
DECOMPILED_PATH = Path("/home/tech/v2_cp_app/coupang_apk/decompiled")

# 스키마 캐시 파일
SCHEMA_CACHE_PATH = Path("/home/tech/v2_cp_app/lib/common/schema_cache.json")


class SchemaDefinition:
    """스키마 정의 - smali에서 추출"""

    def __init__(self, name: str):
        self.name = name
        self.schema_id: Optional[int] = None
        self.schema_version: Optional[int] = None
        self.mandatory_fields: List[str] = []
        self.extra_fields: List[str] = []
        self.fixed_values: Dict[str, str] = {}
        self.smali_path: Optional[str] = None

    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'schema_id': self.schema_id,
            'schema_version': self.schema_version,
            'mandatory_fields': self.mandatory_fields,
            'extra_fields': self.extra_fields,
            'fixed_values': self.fixed_values,
            'smali_path': self.smali_path
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'SchemaDefinition':
        schema = cls(data['name'])
        schema.schema_id = data.get('schema_id')
        schema.schema_version = data.get('schema_version')
        schema.mandatory_fields = data.get('mandatory_fields', [])
        schema.extra_fields = data.get('extra_fields', [])
        schema.fixed_values = data.get('fixed_values', {})
        schema.smali_path = data.get('smali_path')
        return schema


class SmaliParser:
    """smali 파일 파서"""

    @staticmethod
    def parse(smali_path: Path) -> SchemaDefinition:
        """smali 파일에서 스키마 정의 추출"""
        with open(smali_path, 'r') as f:
            content = f.read()

        schema = SchemaDefinition(smali_path.stem)
        schema.smali_path = str(smali_path)

        # 스키마 ID와 버전 추출
        id_pattern = re.search(
            r'const-string v\d+, "(\d+)".*?iput-object v\d+, v0, L.*?;->I0:Ljava/lang/String;',
            content, re.DOTALL
        )
        if id_pattern:
            schema.schema_id = int(id_pattern.group(1))

        version_pattern = re.search(
            r'iput-object v\d+, v0, L.*?;->I0:Ljava/lang/String;.*?const-string v\d+, "(\d+)".*?iput-object v\d+, v0, L.*?;->J0:Ljava/lang/String;',
            content, re.DOTALL
        )
        if version_pattern:
            schema.schema_version = int(version_pattern.group(1))

        # getMandatory 메서드에서 필드 추출
        method_match = re.search(
            r'\.method public getMandatory\(\)Ljava/util/Map;(.*?)\.end method',
            content, re.DOTALL
        )
        if method_match:
            method_body = method_match.group(1)
            SmaliParser._extract_fields_and_fixed(method_body, schema)

        # getExtra 메서드에서 필드 추출
        extra_match = re.search(
            r'\.method public getExtra\(\)Ljava/util/Map;(.*?)\.end method',
            content, re.DOTALL
        )
        if extra_match:
            fields = SmaliParser._extract_field_names(extra_match.group(1))
            schema.extra_fields = fields

        return schema

    @staticmethod
    def _extract_field_names(method_body: str) -> List[str]:
        """메서드 본문에서 필드명 추출"""
        fields = []
        lines = method_body.split('\n')
        current_field = None

        for line in lines:
            const_match = re.search(r'const-string v\d+, "([^"]+)"', line)
            if const_match:
                current_field = const_match.group(1)
            put_match = re.search(r'invoke-interface.*Map;->put', line)
            if put_match and current_field:
                fields.append(current_field)
                current_field = None

        return fields

    @staticmethod
    def _extract_fields_and_fixed(method_body: str, schema: SchemaDefinition):
        """필드명과 고정값 추출"""
        lines = method_body.split('\n')
        i = 0
        seen_fields = set()

        while i < len(lines):
            line = lines[i]
            const1 = re.search(r'const-string v(\d+), "([^"]+)"', line)

            if const1:
                key = const1.group(2)

                # 다음 줄들에서 iget 또는 const-string 찾기
                for j in range(i+1, min(i+10, len(lines))):
                    # iget: 동적 필드
                    if 'iget-object' in lines[j] or 'iget' in lines[j]:
                        if key not in seen_fields:
                            schema.mandatory_fields.append(key)
                            seen_fields.add(key)
                        break

                    # const-string 다음에 바로 put: 고정값
                    const2 = re.search(r'const-string v(\d+), "([^"]+)"', lines[j])
                    if const2:
                        value = const2.group(2)
                        # 다음에 put이 있는지 확인
                        for k in range(j+1, min(j+5, len(lines))):
                            if 'Map;->put' in lines[k]:
                                # 메타 필드인 경우 고정값으로
                                if key in ['logCategory', 'logType', 'eventName', 'domain', 'pageName']:
                                    schema.fixed_values[key] = value
                                elif key not in seen_fields:
                                    schema.mandatory_fields.append(key)
                                    seen_fields.add(key)
                                break
                        break
            i += 1


class SchemaRegistry:
    """스키마 레지스트리 - 모든 스키마 정의 관리"""

    _instance = None
    _schemas: Dict[str, SchemaDefinition] = {}
    _schemas_by_id: Dict[int, SchemaDefinition] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_cache()
        return cls._instance

    def _load_cache(self):
        """캐시에서 스키마 로드"""
        if SCHEMA_CACHE_PATH.exists():
            try:
                with open(SCHEMA_CACHE_PATH, 'r') as f:
                    data = json.load(f)
                for item in data:
                    schema = SchemaDefinition.from_dict(item)
                    self._schemas[schema.name.lower()] = schema
                    if schema.schema_id:
                        self._schemas_by_id[schema.schema_id] = schema
                print(f"[FluentSchema] Loaded {len(self._schemas)} schemas from cache")
            except Exception as e:
                print(f"[FluentSchema] Cache load failed: {e}")

    def _save_cache(self):
        """스키마를 캐시에 저장"""
        data = [s.to_dict() for s in self._schemas.values()]
        with open(SCHEMA_CACHE_PATH, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get(self, name_or_id) -> Optional[SchemaDefinition]:
        """스키마 가져오기 (이름 또는 ID)"""
        if isinstance(name_or_id, int):
            if name_or_id in self._schemas_by_id:
                return self._schemas_by_id[name_or_id]
        else:
            key = name_or_id.lower()
            if key in self._schemas:
                return self._schemas[key]

        # 캐시에 없으면 smali에서 파싱
        return self._parse_from_smali(name_or_id)

    def _parse_from_smali(self, name_or_id) -> Optional[SchemaDefinition]:
        """smali 파일에서 스키마 파싱"""
        # 이름으로 검색
        for smali_file in DECOMPILED_PATH.rglob("*.smali"):
            if "$" in smali_file.name:
                continue

            if isinstance(name_or_id, str):
                if name_or_id.lower() in smali_file.stem.lower():
                    schema = SmaliParser.parse(smali_file)
                    if schema.schema_id:
                        self._schemas[schema.name.lower()] = schema
                        self._schemas_by_id[schema.schema_id] = schema
                        self._save_cache()
                        return schema

        return None

    def build_cache(self, limit: int = 100):
        """주요 스키마 캐시 빌드"""
        count = 0
        for smali_file in DECOMPILED_PATH.rglob("*.smali"):
            if "$" in smali_file.name:
                continue
            if "schema" not in str(smali_file).lower():
                continue

            try:
                schema = SmaliParser.parse(smali_file)
                if schema.schema_id:
                    self._schemas[schema.name.lower()] = schema
                    self._schemas_by_id[schema.schema_id] = schema
                    count += 1
                    if count >= limit:
                        break
            except Exception as e:
                pass

        self._save_cache()
        print(f"[FluentSchema] Built cache with {count} schemas")


class FluentSchema:
    """
    Fluent 스키마 빌더

    APK 기반으로 스키마를 자동 생성하며,
    context에서 값을 자동으로 매핑합니다.
    """

    def __init__(self, schema_name_or_id):
        self.registry = SchemaRegistry()
        self.definition = self.registry.get(schema_name_or_id)

        if not self.definition:
            raise ValueError(f"Schema not found: {schema_name_or_id}")

        self.data: Dict[str, Any] = {}
        self.extra: Dict[str, Any] = {}

    def set(self, key: str, value: Any) -> 'FluentSchema':
        """필드 값 설정"""
        if key in self.definition.extra_fields:
            self.extra[key] = value
        else:
            self.data[key] = value
        return self

    def set_many(self, values: Dict[str, Any]) -> 'FluentSchema':
        """여러 필드 값 설정"""
        for key, value in values.items():
            self.set(key, value)
        return self

    def from_context(self, context: dict, mapping: Dict[str, str]) -> 'FluentSchema':
        """
        context에서 값 자동 매핑

        mapping 예:
            {
                'q': 'INPUT.q',
                'productId': 'RESULT.ROOT.productId',
                'searchId': 'RESULT.ROOT.searchId'
            }
        """
        for field, path in mapping.items():
            value = self._get_nested(context, path)
            if value is not None:
                self.set(field, value)
        return self

    def _get_nested(self, obj: dict, path: str) -> Any:
        """중첩된 딕셔너리에서 값 가져오기"""
        keys = path.split('.')
        current = obj
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current

    def build(self, context: dict = None) -> dict:
        """전송용 딕셔너리 생성"""
        from lib.common.utils import generate_common_payload

        # 고정값 먼저 적용
        data = dict(self.definition.fixed_values)

        # 동적 값 적용
        data.update(self.data)

        return {
            'common': generate_common_payload(context) if context else {},
            'meta': {
                'schemaId': self.definition.schema_id,
                'schemaVersion': self.definition.schema_version
            },
            'data': data,
            'extra': self.extra
        }

    @classmethod
    def quick_build(cls, schema_id: int, context: dict, data: dict = None, extra: dict = None) -> dict:
        """
        빠른 스키마 생성

        사용법:
            payload = FluentSchema.quick_build(124, context, {
                'q': context['INPUT']['q'],
                'productId': context['RESULT']['ROOT']['productId']
            })
        """
        from lib.common.utils import generate_common_payload

        registry = SchemaRegistry()
        definition = registry.get(schema_id)

        if not definition:
            raise ValueError(f"Schema ID {schema_id} not found")

        # 고정값 + 동적 데이터
        final_data = dict(definition.fixed_values)
        if data:
            final_data.update(data)

        return {
            'common': generate_common_payload(context),
            'meta': {
                'schemaId': definition.schema_id,
                'schemaVersion': definition.schema_version
            },
            'data': final_data,
            'extra': extra or {}
        }


# 자주 사용하는 스키마 매핑 정의
COMMON_MAPPINGS = {
    # Schema 124: SrpProductClick
    124: {
        'q': 'INPUT.q',
        'productId': 'RESULT.ROOT.productId',
        'vendorItemId': 'RESULT.ROOT.vendorItemId',
        'itemId': 'RESULT.ROOT.itemId',
        'itemProductId': 'RESULT.ROOT.itemProductId',
        'searchId': 'RESULT.ROOT.searchId',
        'searchCount': 'RESULT.ROOT.searchCount',
        'rank': 'RESULT.SEARCH.srp_rank',
        'searchViewType': 'RESULT.SEARCH.searchViewType',
    },

    # Schema 116: SrpPageView
    116: {
        'q': 'INPUT.q',
        'searchId': 'RESULT.ROOT.searchId',
        'searchCount': 'RESULT.ROOT.searchCount',
        'searchViewType': 'RESULT.SEARCH.searchViewType',
        'isCoupick': 'RESULT.SEARCH.isCoupick',
        'rankOfCoupick': 'RESULT.SEARCH.rankOfCoupick',
    }
}


def build_schema(schema_id: int, context: dict, overrides: dict = None) -> dict:
    """
    스키마 빌드 헬퍼 함수

    자동 매핑 + 오버라이드 지원

    사용법:
        payload = build_schema(124, context, {
            'isCoupick': True,
            'rank': 5
        })
    """
    schema = FluentSchema(schema_id)

    # 자동 매핑 적용
    if schema_id in COMMON_MAPPINGS:
        schema.from_context(context, COMMON_MAPPINGS[schema_id])

    # 오버라이드 적용
    if overrides:
        schema.set_many(overrides)

    return schema.build(context)


if __name__ == '__main__':
    # 캐시 빌드
    registry = SchemaRegistry()
    registry.build_cache(limit=50)
