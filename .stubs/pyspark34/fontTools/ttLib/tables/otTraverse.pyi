from .otBase import BaseTable
from typing import Callable, Deque, Iterable, List, Tuple

__all__ = ['bfs_base_table', 'dfs_base_table', 'SubTablePath']

class SubTablePath(Tuple[BaseTable.SubTableEntry, ...]): ...
AddToFrontierFn = Callable[[Deque[SubTablePath], List[SubTablePath]], None]

def dfs_base_table(root: BaseTable, root_accessor: str | None = None, skip_root: bool = False, predicate: Callable[[SubTablePath], bool] | None = None, iter_subtables_fn: Callable[[BaseTable], Iterable[BaseTable.SubTableEntry]] | None = None) -> Iterable[SubTablePath]:
    """Depth-first search tree of BaseTables.

    Args:
        root (BaseTable): the root of the tree.
        root_accessor (Optional[str]): attribute name for the root table, if any (mostly
            useful for debugging).
        skip_root (Optional[bool]): if True, the root itself is not visited, only its
            children.
        predicate (Optional[Callable[[SubTablePath], bool]]): function to filter out
            paths. If True, the path is yielded and its subtables are added to the
            queue. If False, the path is skipped and its subtables are not traversed.
        iter_subtables_fn (Optional[Callable[[BaseTable], Iterable[BaseTable.SubTableEntry]]]):
            function to iterate over subtables of a table. If None, the default
            BaseTable.iterSubTables() is used.

    Yields:
        SubTablePath: tuples of BaseTable.SubTableEntry(name, table, index) namedtuples
        for each of the nodes in the tree. The last entry in a path is the current
        subtable, whereas preceding ones refer to its parent tables all the way up to
        the root.
    """
def bfs_base_table(root: BaseTable, root_accessor: str | None = None, skip_root: bool = False, predicate: Callable[[SubTablePath], bool] | None = None, iter_subtables_fn: Callable[[BaseTable], Iterable[BaseTable.SubTableEntry]] | None = None) -> Iterable[SubTablePath]:
    """Breadth-first search tree of BaseTables.

    Args:
    the root of the tree.
        root_accessor (Optional[str]): attribute name for the root table, if any (mostly
            useful for debugging).
        skip_root (Optional[bool]): if True, the root itself is not visited, only its
            children.
        predicate (Optional[Callable[[SubTablePath], bool]]): function to filter out
            paths. If True, the path is yielded and its subtables are added to the
            queue. If False, the path is skipped and its subtables are not traversed.
        iter_subtables_fn (Optional[Callable[[BaseTable], Iterable[BaseTable.SubTableEntry]]]):
            function to iterate over subtables of a table. If None, the default
            BaseTable.iterSubTables() is used.

    Yields:
        SubTablePath: tuples of BaseTable.SubTableEntry(name, table, index) namedtuples
        for each of the nodes in the tree. The last entry in a path is the current
        subtable, whereas preceding ones refer to its parent tables all the way up to
        the root.
    """
