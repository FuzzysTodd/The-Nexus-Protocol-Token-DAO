from dataclasses import dataclass
from pandas import DataFrame
from seaborn._core.groupby import GroupBy as GroupBy
from seaborn._core.scales import Scale as Scale
from seaborn._core.typing import Vector as Vector
from seaborn._statistics import EstimateAggregator as EstimateAggregator
from seaborn._stats.base import Stat as Stat
from typing import Callable, ClassVar

@dataclass
class Agg(Stat):
    """
    Aggregate data along the value axis using given method.

    Parameters
    ----------
    func : str or callable
        Name of a :class:`pandas.Series` method or a vector -> scalar function.

    See Also
    --------
    objects.Est : Aggregation with error bars.

    Examples
    --------
    .. include:: ../docstrings/objects.Agg.rst

    """
    func: str | Callable[[Vector], float] = ...
    group_by_orient: ClassVar[bool] = ...
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...
    def __init__(self, func) -> None: ...

@dataclass
class Est(Stat):
    '''
    Calculate a point estimate and error bar interval.

    For additional information about the various `errorbar` choices, see
    the :doc:`errorbar tutorial </tutorial/error_bars>`.

    Parameters
    ----------
    func : str or callable
        Name of a :class:`numpy.ndarray` method or a vector -> scalar function.
    errorbar : str, (str, float) tuple, or callable
        Name of errorbar method (one of "ci", "pi", "se" or "sd"), or a tuple
        with a method name ane a level parameter, or a function that maps from a
        vector to a (min, max) interval.
    n_boot : int
       Number of bootstrap samples to draw for "ci" errorbars.
    seed : int
        Seed for the PRNG used to draw bootstrap samples.

    Examples
    --------
    .. include:: ../docstrings/objects.Est.rst

    '''
    func: str | Callable[[Vector], float] = ...
    errorbar: str | tuple[str, float] = ...
    n_boot: int = ...
    seed: int | None = ...
    group_by_orient: ClassVar[bool] = ...
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...
    def __init__(self, func, errorbar, n_boot, seed) -> None: ...

@dataclass
class Rolling(Stat):
    def __call__(self, data, groupby, orient, scales) -> None: ...
