from _typeshed import Incomplete

logger: Incomplete

class CrossPlatLock:
    """Offers a mechanism for waiting until another process is finished interacting with a shared
    resource. This is specifically written to interact with a class of the same name in the .NET
    extensions library.
    """
    def __init__(self, lockfile_path) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
