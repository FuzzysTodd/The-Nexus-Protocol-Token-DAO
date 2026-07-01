import tarfile

class SafetyError(tarfile.TarError):
    def __init__(self, msg, *args, **kw) -> None: ...

class CaseInsensitiveFileSystemError(OSError):
    def __init__(self) -> None: ...
