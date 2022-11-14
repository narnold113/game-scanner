from dataclasses import dataclass, field

from ..game_source import GameSource


@dataclass
class AmazonLunaGameSource(GameSource):
    page_id: str = field(default=None)

    url: str = "https://proxy-prod.us-east-1.tempo.digital.a2z.com/getPage"
    request_headers = {
        "x-amz-locale": "en_US",
        "x-amz-platform": "retail_web",
        "x-amz-marketplace-id": "ATVPDKIKX0DER",
    }
    request_payload = {
        "timeout": 10000,
        "featureScheme": "RETAIL_WEB_V1",
        "pageContext": {
            "pageUri": "channel",
            "pageId": page_id,
            "productStage": "Release",
        },
        "clientContext": {
            "browserMetadata": {
                "browserType": "Edge",
                "browserVersion": "107.0.1418.42",
                "deviceModel": "",
                "deviceType": "unknown",
                "osName": "Mac OS",
                "osVersion": "12.6.1",
            }
        },
        "inputContext": {"gamepadTypes": []},
        "dynamicFeatures": ["RESPONSE_V2"],
    }
