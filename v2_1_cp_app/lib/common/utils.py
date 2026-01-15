import time
import uuid
import datetime
import random

def get_current_time_iso():
    """Returns current time in ISO format with timezone (Korean Standard Time)"""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0900"

def generate_common_payload(context, event_time=None):
    """
    Generates the 'common' dictionary used in bulksubmit payloads.

    Args:
        context (dict): The shared context containing device profile values.
                        New structure: context['DEVICE'] for device info
        event_time (str, optional): Specific event time string.
                                    If None, current time is generated.

    Variable fields from context['DEVICE']:
        - pcid, app_session_id, device_uuid, model, os_version
        - width, height (for resolution)
    """
    if not event_time:
        event_time = get_current_time_iso()

    # Get DEVICE info from new context structure
    device = context.get('DEVICE', {})

    # Build resolution from context
    resolution = f"{device.get('width', 1080)}x{device.get('height', 2340)}"

    return {
        'platform': 'android',
        'libraryVersion': '0.6.7',
        'pcid': device.get('pcid'),
        'lang': 'ko-KR',
        'appCode': 'coupang',
        'market': 'KR',
        'resolution': resolution,
        'eventTime': event_time,
        # 'memberSrl': str(random.randint(2000000, 300000000)),
        'memberSrl': '',
        'app': {
            'osVersion': device.get('os_version'),
            'model': device.get('model'),
            'appVersionName': '9.0.4',
            'appVersionCode': 2409040,
            'uuid': device.get('device_uuid')
        },
        'location': {
            'region': 'KR',
            'locale': 'ko-KR',
            'mcc': '',
            'timezone': 'Asia/Seoul'
        },
        'appId': 'com.coupang.mobile',
        'appSessionId': device.get('app_session_id'),
        'systemLanguage': 'ko'
    }

