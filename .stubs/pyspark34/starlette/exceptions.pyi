from _typeshed import Incomplete

__all__ = ['HTTPException', 'WebSocketException']

class HTTPException(Exception):
    status_code: Incomplete
    detail: Incomplete
    headers: Incomplete
    def __init__(self, status_code: int, detail: str | None = None, headers: dict | None = None) -> None: ...

class WebSocketException(Exception):
    code: Incomplete
    reason: Incomplete
    def __init__(self, code: int, reason: str | None = None) -> None: ...
