from _typeshed import Incomplete

SCHEME_KEYS: Incomplete

class Scheme:
    """A Scheme holds paths which are used as the base directories for
    artifacts associated with a Python package.
    """
    platlib: Incomplete
    purelib: Incomplete
    headers: Incomplete
    scripts: Incomplete
    data: Incomplete
    def __init__(self, platlib: str, purelib: str, headers: str, scripts: str, data: str) -> None: ...
