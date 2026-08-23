import git.diff as git_diff
from . import util
from .base import IndexObjUnion, IndexObject
from .blob import Blob
from git.repo import Repo
from git.types import Literal, PathLike
from git.util import IterableList
from typing import Any, Callable, Iterator, List, Tuple

__all__ = ['TreeModifier', 'Tree']

TreeCacheTup = Tuple[bytes, int, str]

class TreeModifier:
    """A utility class providing methods to alter the underlying cache in a list-like fashion.

    Once all adjustments are complete, the _cache, which really is a reference to
    the cache of a tree, will be sorted. Assuring it will be in a serializable state"""
    def __init__(self, cache: List[TreeCacheTup]) -> None: ...
    def set_done(self) -> TreeModifier:
        """Call this method once you are done modifying the tree information.
        It may be called several times, but be aware that each call will cause
        a sort operation

        :return self:"""
    def add(self, sha: bytes, mode: int, name: str, force: bool = False) -> TreeModifier:
        """Add the given item to the tree. If an item with the given name already
        exists, nothing will be done, but a ValueError will be raised if the
        sha and mode of the existing item do not match the one you add, unless
        force is True

        :param sha: The 20 or 40 byte sha of the item to add
        :param mode: int representing the stat compatible mode of the item
        :param force: If True, an item with your name and information will overwrite
            any existing item with the same name, no matter which information it has
        :return: self"""
    def add_unchecked(self, binsha: bytes, mode: int, name: str) -> None:
        """Add the given item to the tree, its correctness is assumed, which
        puts the caller into responsibility to assure the input is correct.
        For more information on the parameters, see ``add``

        :param binsha: 20 byte binary sha"""
    def __delitem__(self, name: str) -> None:
        """Deletes an item with the given name if it exists"""

class Tree(IndexObject, git_diff.Diffable, util.Traversable, util.Serializable):
    """Tree objects represent an ordered list of Blobs and other Trees.

    ``Tree as a list``::

        Access a specific blob using the
        tree['filename'] notation.

        You may as well access by index
        blob = tree[0]
    """
    type: Literal['tree']
    commit_id: int
    blob_id: int
    symlink_id: int
    tree_id: int
    def __init__(self, repo: Repo, binsha: bytes, mode: int = ..., path: PathLike | None = None) -> None: ...
    def join(self, file: str) -> IndexObjUnion:
        """Find the named object in this tree's contents

        :return: ``git.Blob`` or ``git.Tree`` or ``git.Submodule``
        :raise KeyError: if given file or tree does not exist in tree"""
    def __truediv__(self, file: str) -> IndexObjUnion:
        """For PY3 only"""
    @property
    def trees(self) -> List['Tree']:
        """:return: list(Tree, ...) list of trees directly below this tree"""
    @property
    def blobs(self) -> List[Blob]:
        """:return: list(Blob, ...) list of blobs directly below this tree"""
    @property
    def cache(self) -> TreeModifier:
        """
        :return: An object allowing to modify the internal cache. This can be used
            to change the tree's contents. When done, make sure you call ``set_done``
            on the tree modifier, or serialization behaviour will be incorrect.
            See the ``TreeModifier`` for more information on how to alter the cache"""
    def traverse(self, predicate: Callable[[IndexObjUnion | TraversedTreeTup, int], bool] = ..., prune: Callable[[IndexObjUnion | TraversedTreeTup, int], bool] = ..., depth: int = -1, branch_first: bool = True, visit_once: bool = False, ignore_self: int = 1, as_edge: bool = False) -> Iterator[IndexObjUnion] | Iterator[TraversedTreeTup]:
        """For documentation, see util.Traversable._traverse()
        Trees are set to visit_once = False to gain more performance in the traversal"""
    def list_traverse(self, *args: Any, **kwargs: Any) -> IterableList[IndexObjUnion]:
        """
        :return: IterableList with the results of the traversal as produced by
            traverse()
            Tree -> IterableList[Union['Submodule', 'Tree', 'Blob']]
        """
    def __getslice__(self, i: int, j: int) -> List[IndexObjUnion]: ...
    def __iter__(self) -> Iterator[IndexObjUnion]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, item: str | int | slice) -> IndexObjUnion: ...
    def __contains__(self, item: IndexObjUnion | PathLike) -> bool: ...
    def __reversed__(self) -> Iterator[IndexObjUnion]: ...
