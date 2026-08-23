from _typeshed import Incomplete
from typing import Any, Dict, TypeVar

__all__ = ['DirectUrl', 'DirectUrlValidationError', 'DirInfo', 'ArchiveInfo', 'VcsInfo']

T = TypeVar('T')

class DirectUrlValidationError(Exception): ...

class VcsInfo:
    name: str
    vcs: Incomplete
    requested_revision: Incomplete
    commit_id: Incomplete
    def __init__(self, vcs: str, commit_id: str, requested_revision: str | None = None) -> None: ...

class ArchiveInfo:
    name: str
    hashes: Incomplete
    def __init__(self, hash: str | None = None, hashes: Dict[str, str] | None = None) -> None: ...
    @property
    def hash(self) -> str | None: ...
    @hash.setter
    def hash(self, value: str | None) -> None: ...

class DirInfo:
    name: str
    editable: Incomplete
    def __init__(self, editable: bool = False) -> None: ...
InfoType = ArchiveInfo | DirInfo | VcsInfo

class DirectUrl:
    url: Incomplete
    info: Incomplete
    subdirectory: Incomplete
    def __init__(self, url: str, info: InfoType, subdirectory: str | None = None) -> None: ...
    @property
    def redacted_url(self) -> str:
        """url with user:password part removed unless it is formed with
        environment variables as specified in PEP 610, or it is ``git``
        in the case of a git URL.
        """
    def validate(self) -> None: ...
    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> DirectUrl: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_json(cls, s: str) -> DirectUrl: ...
    def to_json(self) -> str: ...
    def is_local_editable(self) -> bool: ...
