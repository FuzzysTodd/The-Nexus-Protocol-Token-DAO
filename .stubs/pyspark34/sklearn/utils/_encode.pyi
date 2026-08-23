from . import is_scalar_nan as is_scalar_nan
from _typeshed import Incomplete
from collections import Counter
from typing import NamedTuple

class MissingValues(NamedTuple):
    """Data class for missing data information"""
    nan: bool
    none: bool
    def to_list(self):
        """Convert tuple to a list where None is always first."""

class _nandict(dict):
    """Dictionary with support for nans."""
    nan_value: Incomplete
    def __init__(self, mapping) -> None: ...
    def __missing__(self, key): ...

class _NaNCounter(Counter):
    """Counter with support for nan values."""
    def __init__(self, items) -> None: ...
    def __missing__(self, key): ...
