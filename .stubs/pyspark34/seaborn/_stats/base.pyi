from dataclasses import dataclass
from pandas import DataFrame
from seaborn._core.groupby import GroupBy as GroupBy
from seaborn._core.scales import Scale as Scale
from typing import ClassVar

@dataclass
class Stat:
    """Base class for objects that apply statistical transformations."""
    group_by_orient: ClassVar[bool] = ...
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame:
        """Apply statistical transform to data subgroups and return combined result."""
