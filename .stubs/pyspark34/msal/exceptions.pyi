from _typeshed import Incomplete

class MsalError(Exception):
    msg: str
    kwargs: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class MsalServiceError(MsalError):
    msg: str
