from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

__all__ = ['ExePathRef', 'ExePathRefToDest', 'PathRefToDest', 'PathRef', 'RefWhen', 'RefMust']

class RefMust:
    NA: str
    COPY: str
    SYMLINK: str

class RefWhen:
    ANY: str
    COPY: str
    SYMLINK: str

class PathRef(metaclass=ABCMeta):
    """Base class that checks if a file reference can be symlink/copied."""
    FS_SUPPORTS_SYMLINK: Incomplete
    FS_CASE_SENSITIVE: Incomplete
    must: Incomplete
    when: Incomplete
    src: Incomplete
    exists: Incomplete
    def __init__(self, src, must=..., when=...) -> None: ...
    @property
    def can_read(self): ...
    @property
    def can_copy(self): ...
    @property
    def can_symlink(self): ...
    @abstractmethod
    def run(self, creator, symlinks): ...
    def method(self, symlinks): ...

class ExePathRef(PathRef, metaclass=ABCMeta):
    """Base class that checks if a executable can be references via symlink/copy."""
    def __init__(self, src, must=..., when=...) -> None: ...
    @property
    def can_symlink(self): ...
    @property
    def can_run(self): ...

class PathRefToDest(PathRef):
    """Link a path on the file system."""
    dest: Incomplete
    def __init__(self, src, dest, must=..., when=...) -> None: ...
    def run(self, creator, symlinks) -> None: ...

class ExePathRefToDest(PathRefToDest, ExePathRef):
    """Link a exe path on the file system."""
    base: Incomplete
    aliases: Incomplete
    dest: Incomplete
    def __init__(self, src, targets, dest, must=..., when=...) -> None: ...
    def run(self, creator, symlinks) -> None: ...
