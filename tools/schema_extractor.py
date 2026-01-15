#!/usr/bin/env python3
"""
APK Schema Extractor
====================
smali 파일에서 스키마 정의를 자동 추출하여 Python 코드 생성

사용법:
    python schema_extractor.py SrpProductClick
    python schema_extractor.py --all  # 모든 스키마 추출
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

DECOMPILED_PATH = Path("/home/tech/v2_cp_app/coupang_apk/decompiled")


class SmaliSchemaParser:
    """smali 파일에서 스키마 정의 추출"""

    def __init__(self, smali_content: str):
        self.content = smali_content
        self.schema_id: Optional[str] = None
        self.schema_version: Optional[str] = None
        self.mandatory_fields: List[Tuple[str, str]] = []  # (field_name, field_type)
        self.extra_fields: List[Tuple[str, str]] = []
        self.fixed_values: Dict[str, str] = {}  # 하드코딩된 값들

    def parse(self):
        """스키마 파싱"""
        self._extract_schema_id_version()
        self._extract_mandatory_fields()
        self._extract_extra_fields()
        self._extract_fixed_values()

    def _extract_schema_id_version(self):
        """스키마 ID와 버전 추출"""
        # getId() 메서드에서 반환하는 필드 찾기
        id_match = re.search(r'\.method public getId\(\).*?iget-object v0, p0, L.*?;->(.*?):.*?return-object v0',
                            self.content, re.DOTALL)

        # 생성자에서 스키마 ID 추출 (const-string으로 설정되는 값)
        # 패턴: const-string v1, "124" 다음에 iput-object v1 ... ->I0:Ljava/lang/String;
        id_pattern = re.search(r'const-string v\d+, "(\d+)".*?iput-object v\d+, v0, L.*?;->I0:Ljava/lang/String;',
                               self.content, re.DOTALL)
        if id_pattern:
            self.schema_id = id_pattern.group(1)

        # 버전 추출 (바로 다음에 오는 const-string)
        version_pattern = re.search(r'iput-object v\d+, v0, L.*?;->I0:Ljava/lang/String;.*?const-string v\d+, "(\d+)".*?iput-object v\d+, v0, L.*?;->J0:Ljava/lang/String;',
                                    self.content, re.DOTALL)
        if version_pattern:
            self.schema_version = version_pattern.group(1)

    def _extract_mandatory_fields(self):
        """getMandatory() 메서드에서 필드 추출"""
        # getMandatory 메서드 찾기
        method_match = re.search(r'\.method public getMandatory\(\)Ljava/util/Map;(.*?)\.end method',
                                self.content, re.DOTALL)
        if not method_match:
            return

        method_body = method_match.group(1)

        # const-string으로 필드명 추출
        field_pattern = re.findall(r'const-string v\d+, "([^"]+)".*?invoke-interface \{v\d+, v\d+, v\d+\}, Ljava/util/Map;->put',
                                   method_body, re.DOTALL)

        # 더 정확한 패턴으로 재추출
        lines = method_body.split('\n')
        current_field = None
        for line in lines:
            const_match = re.search(r'const-string v\d+, "([^"]+)"', line)
            if const_match:
                current_field = const_match.group(1)
            put_match = re.search(r'invoke-interface.*Map;->put', line)
            if put_match and current_field:
                # 필드 타입 추정 (이전 iget 명령어에서)
                self.mandatory_fields.append((current_field, 'dynamic'))
                current_field = None

    def _extract_extra_fields(self):
        """getExtra() 메서드에서 필드 추출"""
        method_match = re.search(r'\.method public getExtra\(\)Ljava/util/Map;(.*?)\.end method',
                                self.content, re.DOTALL)
        if not method_match:
            return

        method_body = method_match.group(1)
        lines = method_body.split('\n')
        current_field = None
        for line in lines:
            const_match = re.search(r'const-string v\d+, "([^"]+)"', line)
            if const_match:
                current_field = const_match.group(1)
            put_match = re.search(r'invoke-interface.*Map;->put', line)
            if put_match and current_field:
                self.extra_fields.append((current_field, 'dynamic'))
                current_field = None

    def _extract_fixed_values(self):
        """하드코딩된 고정값 추출"""
        # getMandatory에서 연속된 두 const-string 패턴 찾기 (key, value)
        method_match = re.search(r'\.method public getMandatory\(\)Ljava/util/Map;(.*?)\.end method',
                                self.content, re.DOTALL)
        if not method_match:
            return

        method_body = method_match.group(1)
        lines = method_body.split('\n')

        # 두 개의 연속된 const-string을 찾아 key-value 쌍으로 매핑
        # 패턴: const-string v1, "logType" → const-string v2, "click" → put(v0, v1, v2)
        i = 0
        while i < len(lines) - 10:
            line = lines[i]
            const1 = re.search(r'const-string v(\d+), "([^"]+)"', line)
            if const1:
                key = const1.group(2)
                # 다음 줄들에서 바로 다음 const-string 찾기
                for j in range(i+1, min(i+8, len(lines))):
                    const2 = re.search(r'const-string v(\d+), "([^"]+)"', lines[j])
                    if const2:
                        value = const2.group(2)
                        # 이 값 뒤에 put 호출이 있는지 확인
                        for k in range(j+1, min(j+5, len(lines))):
                            if 'Map;->put' in lines[k]:
                                # key가 메타 필드이고 value가 단순 문자열인 경우만
                                if key in ['logCategory', 'logType', 'eventName', 'domain', 'pageName']:
                                    self.fixed_values[key] = value
                                break
                        break
            i += 1


def find_schema_files() -> Dict[str, Path]:
    """모든 스키마 smali 파일 찾기"""
    schemas = {}
    for smali_file in DECOMPILED_PATH.rglob("*.smali"):
        if "schema" in str(smali_file).lower():
            # $Builder, $Companion 등 제외
            if "$" not in smali_file.name:
                name = smali_file.stem
                schemas[name] = smali_file
    return schemas


def extract_schema(schema_name: str) -> Optional[Dict]:
    """특정 스키마 추출"""
    schemas = find_schema_files()

    # 정확한 이름 또는 부분 매칭
    target_file = None
    for name, path in schemas.items():
        if schema_name.lower() in name.lower():
            target_file = path
            break

    if not target_file:
        print(f"Schema '{schema_name}' not found")
        return None

    print(f"Parsing: {target_file}")

    with open(target_file, 'r') as f:
        content = f.read()

    parser = SmaliSchemaParser(content)
    parser.parse()

    return {
        'name': target_file.stem,
        'file': str(target_file),
        'schema_id': parser.schema_id,
        'schema_version': parser.schema_version,
        'mandatory_fields': parser.mandatory_fields,
        'extra_fields': parser.extra_fields,
        'fixed_values': parser.fixed_values
    }


def generate_python_schema(schema_info: Dict) -> str:
    """Python 스키마 코드 생성"""
    name = schema_info['name']
    schema_id = schema_info['schema_id']
    version = schema_info['schema_version']
    mandatory = schema_info['mandatory_fields']
    extra = schema_info['extra_fields']
    fixed = schema_info['fixed_values']

    code = f'''# Auto-generated from APK: {name}
# Schema ID: {schema_id}, Version: {version}

def build_{name.lower()}(context: dict) -> dict:
    """
    {name} 스키마 생성
    APK 경로: {schema_info['file'].split('decompiled/')[-1]}
    """
    return {{
        'common': generate_common_payload(context),
        'meta': {{
            'schemaId': {schema_id},
            'schemaVersion': {version}
        }},
        'data': {{
'''

    # Fixed values
    for key, value in fixed.items():
        code += f"            '{key}': '{value}',\n"

    # Dynamic mandatory fields
    for field_name, field_type in mandatory:
        if field_name not in fixed:
            code += f"            '{field_name}': None,  # TODO: context에서 추출\n"

    code += '''        },
        'extra': {
'''

    for field_name, field_type in extra:
        code += f"            '{field_name}': None,  # TODO: context에서 추출\n"

    code += '''        }
    }
'''
    return code


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python schema_extractor.py <SchemaName>")
        print("       python schema_extractor.py --list")
        print("       python schema_extractor.py --all")
        return

    arg = sys.argv[1]

    if arg == '--list':
        schemas = find_schema_files()
        print(f"\n=== Found {len(schemas)} Schema Files ===\n")
        for name in sorted(schemas.keys())[:50]:
            print(f"  - {name}")
        if len(schemas) > 50:
            print(f"  ... and {len(schemas) - 50} more")
        return

    if arg == '--all':
        schemas = find_schema_files()
        results = []
        for name, path in list(schemas.items())[:10]:  # 처음 10개만
            info = extract_schema(name)
            if info and info['schema_id']:
                results.append(info)
                print(f"  ✓ {name}: ID={info['schema_id']}, Ver={info['schema_version']}")

        # JSON으로 저장
        with open('/home/tech/v2_cp_app/tools/schemas_extracted.json', 'w') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\nSaved to schemas_extracted.json")
        return

    # 단일 스키마 추출
    info = extract_schema(arg)
    if info:
        print(f"\n=== {info['name']} ===")
        print(f"Schema ID: {info['schema_id']}")
        print(f"Version: {info['schema_version']}")
        print(f"Fixed Values: {info['fixed_values']}")
        print(f"Mandatory Fields ({len(info['mandatory_fields'])}): {[f[0] for f in info['mandatory_fields'][:10]]}...")
        print(f"Extra Fields ({len(info['extra_fields'])}): {[f[0] for f in info['extra_fields'][:5]]}...")

        print("\n=== Generated Python Code ===\n")
        print(generate_python_schema(info))


if __name__ == '__main__':
    main()
