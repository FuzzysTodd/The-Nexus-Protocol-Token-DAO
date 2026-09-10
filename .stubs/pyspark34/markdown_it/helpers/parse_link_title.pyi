from ..common.utils import charCodeAt as charCodeAt, unescapeAll as unescapeAll

class _Result:
    ok: bool
    pos: int
    lines: int
    str: str
    def __init__(self) -> None: ...

def parseLinkTitle(string: str, pos: int, maximum: int) -> _Result: ...
