from .namespace import Namespace as Namespace
from torch import nn as nn
from typing import Dict, Iterable, List, Tuple

class SkipLayout:
    """Represents a skip connection layout across partitions."""
    by_ns_name: Dict[Tuple[Namespace, str], Tuple[int, int]]
    by_partition: List[List[Tuple[int, Namespace, str]]]
    def __init__(self, num_partitions: int, skip_routes: Dict[Tuple[Namespace, str], Tuple[int, int]]) -> None: ...
    def copy_policy(self, next_j: int) -> Iterable[Tuple[int, Namespace, str]]:
        """Generates skip routes for the given destination partition number.
        The skip routes are sorted by source partition number in ascending
        order.

        Yields:
            Each tuple of (source partition number, namespace, name).

        """
    def requires_copy(self, ns: Namespace, name: str) -> bool:
        """Whether the given namespace and name requires partition-to-partition
        copy or not.
        """

def inspect_skip_layout(partitions: List[nn.Sequential]) -> SkipLayout:
    """Inspects the skip connection layout in the given partitions."""
