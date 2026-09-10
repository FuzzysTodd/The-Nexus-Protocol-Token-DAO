from .objects import Commit
from .objects.tree import Tree
from _typeshed import Incomplete
from git.repo.base import Repo
from git.types import PathLike
from typing import Any, Iterator, List, Tuple, Type, TypeVar

__all__ = ['Diffable', 'DiffIndex', 'Diff', 'NULL_TREE']

NULL_TREE: Incomplete

class Diffable:
    """Common interface for all object that can be diffed against another object of compatible type.

    :note:
        Subclasses require a repo member as it is the case for Object instances, for practical
        reasons we do not derive from Object."""
    class Index: ...
    repo: Incomplete
    def diff(self, other: Type['Index'] | Tree | Commit | None | str | object = ..., paths: PathLike | List[PathLike] | Tuple[PathLike, ...] | None = None, create_patch: bool = False, **kwargs: Any) -> DiffIndex:
        """Creates diffs between two items being trees, trees and index or an
        index and the working tree. It will detect renames automatically.

        :param other:
            Is the item to compare us with.
            If None, we will be compared to the working tree.
            If Treeish, it will be compared against the respective tree
            If Index ( type ), it will be compared against the index.
            If git.NULL_TREE, it will compare against the empty tree.
            It defaults to Index to assure the method will not by-default fail
            on bare repositories.

        :param paths:
            is a list of paths or a single path to limit the diff to.
            It will only include at least one of the given path or paths.

        :param create_patch:
            If True, the returned Diff contains a detailed patch that if applied
            makes the self to other. Patches are somewhat costly as blobs have to be read
            and diffed.

        :param kwargs:
            Additional arguments passed to git-diff, such as
            R=True to swap both sides of the diff.

        :return: git.DiffIndex

        :note:
            On a bare repository, 'other' needs to be provided as Index or as
            as Tree/Commit, or a git command error will occur"""
T_Diff = TypeVar('T_Diff', bound='Diff')

class DiffIndex(List[T_Diff]):
    """Implements an Index for diffs, allowing a list of Diffs to be queried by
    the diff properties.

    The class improves the diff handling convenience"""
    change_type: Incomplete
    def iter_change_type(self, change_type: Lit_change_type) -> Iterator[T_Diff]:
        """
        :return:
            iterator yielding Diff instances that match the given change_type

        :param change_type:
            Member of DiffIndex.change_type, namely:

            * 'A' for added paths
            * 'D' for deleted paths
            * 'R' for renamed paths
            * 'M' for paths with modified data
            * 'T' for changed in the type paths
        """

class Diff:
    '''A Diff contains diff information between two Trees.

    It contains two sides a and b of the diff, members are prefixed with
    "a" and "b" respectively to inidcate that.

    Diffs keep information about the changed blob objects, the file mode, renames,
    deletions and new files.

    There are a few cases where None has to be expected as member variable value:

    ``New File``::

        a_mode is None
        a_blob is None
        a_path is None

    ``Deleted File``::

        b_mode is None
        b_blob is None
        b_path is None

    ``Working Tree Blobs``

        When comparing to working trees, the working tree blob will have a null hexsha
        as a corresponding object does not yet exist. The mode will be null as well.
        But the path will be available though.
        If it is listed in a diff the working tree version of the file must
        be different to the version in the index or tree, and hence has been modified.'''
    re_header: Incomplete
    NULL_HEX_SHA: Incomplete
    NULL_BIN_SHA: Incomplete
    a_rawpath: Incomplete
    b_rawpath: Incomplete
    a_mode: Incomplete
    b_mode: Incomplete
    a_blob: Incomplete
    b_blob: Incomplete
    new_file: Incomplete
    deleted_file: Incomplete
    copied_file: Incomplete
    raw_rename_from: Incomplete
    raw_rename_to: Incomplete
    diff: Incomplete
    change_type: Incomplete
    score: Incomplete
    def __init__(self, repo: Repo, a_rawpath: bytes | None, b_rawpath: bytes | None, a_blob_id: str | bytes | None, b_blob_id: str | bytes | None, a_mode: bytes | str | None, b_mode: bytes | str | None, new_file: bool, deleted_file: bool, copied_file: bool, raw_rename_from: bytes | None, raw_rename_to: bytes | None, diff: str | bytes | None, change_type: Lit_change_type | None, score: int | None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def a_path(self) -> str | None: ...
    @property
    def b_path(self) -> str | None: ...
    @property
    def rename_from(self) -> str | None: ...
    @property
    def rename_to(self) -> str | None: ...
    @property
    def renamed(self) -> bool:
        """:returns: True if the blob of our diff has been renamed
        :note: This property is deprecated, please use ``renamed_file`` instead.
        """
    @property
    def renamed_file(self) -> bool:
        """:returns: True if the blob of our diff has been renamed"""
