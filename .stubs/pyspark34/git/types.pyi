from _typeshed import Incomplete
from git.objects import Blob as Blob, Commit as Commit, TagObject as TagObject, Tree as Tree
from git.repo import Repo as Repo
from typing import Any, Callable, Dict, NoReturn, Protocol, TypedDict

PathLike: Incomplete
TBD = Any
Tree_ish: Incomplete
Commit_ish: Incomplete
Lit_commit_ish: Incomplete
Lit_config_levels: Incomplete
CallableProgress = Callable[[int, str | float, str | float | None, str], None] | None
ConfigLevels_Tup: Incomplete

def assert_never(inp: NoReturn, raise_error: bool = True, exc: Exception | None = None) -> None:
    """For use in exhaustive checking of literal or Enum in if/else chain.
    Should only be reached if all members not handled OR attempt to pass non-members through chain.

    If all members handled, type is Empty. Otherwise, will cause mypy error.
    If non-members given, should cause mypy error at variable creation.

    If raise_error is True, will also raise AssertionError or the Exception passed to exc.
    """

class Files_TD(TypedDict):
    insertions: int
    deletions: int
    lines: int

class Total_TD(TypedDict):
    insertions: int
    deletions: int
    lines: int
    files: int

class HSH_TD(TypedDict):
    total: Total_TD
    files: Dict[PathLike, Files_TD]

class Has_Repo(Protocol):
    repo: Repo

class Has_id_attribute(Protocol): ...
