from _typeshed import Incomplete

class ClrError(Exception):
    hresult: Incomplete
    name: Incomplete
    message: Incomplete
    comment: Incomplete
    def __init__(self, hresult: int, name: str | None = None, message: str | None = None, comment: str | None = None) -> None: ...
