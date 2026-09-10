from _typeshed import Incomplete

logger: Incomplete
CLIENT_REQUEST_ID: str
CLIENT_CURRENT_TELEMETRY: str
CLIENT_LAST_TELEMETRY: str
NON_SILENT_CALL: int
FORCE_REFRESH: int
AT_ABSENT: int
AT_EXPIRED: int
AT_AGING: int
RESERVED: int

class _TelemetryContext:
    '''It is used for handling the telemetry context for current OAuth2 "exchange".'''
    def __init__(self, buffer, lock, api_id, correlation_id: Incomplete | None = None, refresh_reason: Incomplete | None = None) -> None: ...
    def generate_headers(self): ...
    def hit_an_access_token(self) -> None: ...
    def update_telemetry(self, auth_result) -> None: ...
