from _typeshed import Incomplete
from collections.abc import Sequence
from dataclasses import dataclass
from matplotlib.axis import Axis as Axis
from matplotlib.scale import ScaleBase as ScaleBase
from matplotlib.ticker import Formatter, Locator
from numpy.typing import ArrayLike, NDArray as NDArray
from pandas import Series
from seaborn._core.plot import Plot as Plot
from seaborn._core.properties import Property as Property
from seaborn._core.rules import categorical_order as categorical_order
from seaborn._core.typing import Default as Default, default as default
from typing import Any, Callable, Tuple

TransFuncs = Tuple[Callable[[ArrayLike], ArrayLike], Callable[[ArrayLike], ArrayLike]]
Pipeline = Sequence[Callable[[Any], Any] | None]

class Scale:
    """Base class for objects that map data values to visual properties."""
    values: tuple | str | list | dict | None
    def __post_init__(self) -> None: ...
    def tick(self) -> None: ...
    def label(self) -> None: ...
    def __call__(self, data: Series) -> ArrayLike: ...

@dataclass
class Boolean(Scale):
    """
    A scale with a discrete domain of True and False values.

    The behavior is similar to the :class:`Nominal` scale, but property
    mappings and legends will use a [True, False] ordering rather than
    a sort using numeric rules. Coordinate variables accomplish this by
    inverting axis limits so as to maintain underlying numeric positioning.
    Input data are cast to boolean values, respecting missing data.

    """
    values: tuple | list | dict | None = ...
    def tick(self, locator: Locator | None = None): ...
    def label(self, formatter: Formatter | None = None): ...
    def __init__(self, values) -> None: ...

@dataclass
class Nominal(Scale):
    """
    A categorical scale without relative importance / magnitude.
    """
    values: tuple | str | list | dict | None = ...
    order: list | None = ...
    def tick(self, locator: Locator | None = None) -> Nominal:
        """
        Configure the selection of ticks for the scale's axis or legend.

        .. note::
            This API is under construction and will be enhanced over time.
            At the moment, it is probably not very useful.

        Parameters
        ----------
        locator : :class:`matplotlib.ticker.Locator` subclass
            Pre-configured matplotlib locator; other parameters will not be used.

        Returns
        -------
        Copy of self with new tick configuration.

        """
    def label(self, formatter: Formatter | None = None) -> Nominal:
        """
        Configure the selection of labels for the scale's axis or legend.

        .. note::
            This API is under construction and will be enhanced over time.
            At the moment, it is probably not very useful.

        Parameters
        ----------
        formatter : :class:`matplotlib.ticker.Formatter` subclass
            Pre-configured matplotlib formatter; other parameters will not be used.

        Returns
        -------
        scale
            Copy of self with new tick configuration.

        """
    def __init__(self, values, order) -> None: ...

@dataclass
class Ordinal(Scale): ...
@dataclass
class Discrete(Scale): ...

@dataclass
class ContinuousBase(Scale):
    values: tuple | str | None = ...
    norm: tuple | None = ...
    def __init__(self, values, norm) -> None: ...

@dataclass
class Continuous(ContinuousBase):
    """
    A numeric scale supporting norms and functional transforms.
    """
    values: tuple | str | None = ...
    trans: str | TransFuncs | None = ...
    def tick(self, locator: Locator | None = None, *, at: Sequence[float] | None = None, upto: int | None = None, count: int | None = None, every: float | None = None, between: tuple[float, float] | None = None, minor: int | None = None) -> Continuous:
        '''
        Configure the selection of ticks for the scale\'s axis or legend.

        Parameters
        ----------
        locator : :class:`matplotlib.ticker.Locator` subclass
            Pre-configured matplotlib locator; other parameters will not be used.
        at : sequence of floats
            Place ticks at these specific locations (in data units).
        upto : int
            Choose "nice" locations for ticks, but do not exceed this number.
        count : int
            Choose exactly this number of ticks, bounded by `between` or axis limits.
        every : float
            Choose locations at this interval of separation (in data units).
        between : pair of floats
            Bound upper / lower ticks when using `every` or `count`.
        minor : int
            Number of unlabeled ticks to draw between labeled "major" ticks.

        Returns
        -------
        scale
            Copy of self with new tick configuration.

        '''
    def label(self, formatter: Formatter | None = None, *, like: str | Callable | None = None, base: int | None | Default = ..., unit: str | None = None) -> Continuous:
        '''
        Configure the appearance of tick labels for the scale\'s axis or legend.

        Parameters
        ----------
        formatter : :class:`matplotlib.ticker.Formatter` subclass
            Pre-configured formatter to use; other parameters will be ignored.
        like : str or callable
            Either a format pattern (e.g., `".2f"`), a format string with fields named
            `x` and/or `pos` (e.g., `"${x:.2f}"`), or a callable that consumes a number
            and returns a string.
        base : number
            Use log formatter (with scientific notation) having this value as the base.
            Set to `None` to override the default formatter with a log transform.
        unit : str or (str, str) tuple
            Use  SI prefixes with these units (e.g., with `unit="g"`, a tick value
            of 5000 will appear as `5 kg`). When a tuple, the first element gives the
            separator between the number and unit.

        Returns
        -------
        scale
            Copy of self with new label configuration.

        '''
    def __init__(self, values, norm, trans) -> None: ...

@dataclass
class Temporal(ContinuousBase):
    """
    A scale for date/time data.
    """
    trans = ...
    def tick(self, locator: Locator | None = None, *, upto: int | None = None) -> Temporal:
        '''
        Configure the selection of ticks for the scale\'s axis or legend.

        .. note::
            This API is under construction and will be enhanced over time.

        Parameters
        ----------
        locator : :class:`matplotlib.ticker.Locator` subclass
            Pre-configured matplotlib locator; other parameters will not be used.
        upto : int
            Choose "nice" locations for ticks, but do not exceed this number.

        Returns
        -------
        scale
            Copy of self with new tick configuration.

        '''
    def label(self, formatter: Formatter | None = None, *, concise: bool = False) -> Temporal:
        """
        Configure the appearance of tick labels for the scale's axis or legend.

        .. note::
            This API is under construction and will be enhanced over time.

        Parameters
        ----------
        formatter : :class:`matplotlib.ticker.Formatter` subclass
            Pre-configured formatter to use; other parameters will be ignored.
        concise : bool
            If True, use :class:`matplotlib.dates.ConciseDateFormatter` to make
            the tick labels as compact as possible.

        Returns
        -------
        scale
            Copy of self with new label configuration.

        """
    def __init__(self, values, norm) -> None: ...

class PseudoAxis:
    """
    Internal class implementing minimal interface equivalent to matplotlib Axis.

    Coordinate variables are typically scaled by attaching the Axis object from
    the figure where the plot will end up. Matplotlib has no similar concept of
    and axis for the other mappable variables (color, etc.), but to simplify the
    code, this object acts like an Axis and can be used to scale other variables.

    """
    axis_name: str
    converter: Incomplete
    units: Incomplete
    scale: Incomplete
    major: Incomplete
    minor: Incomplete
    def __init__(self, scale) -> None: ...
    def set_view_interval(self, vmin, vmax) -> None: ...
    def get_view_interval(self): ...
    def set_data_interval(self, vmin, vmax) -> None: ...
    def get_data_interval(self): ...
    def get_tick_space(self): ...
    def set_major_locator(self, locator) -> None: ...
    def set_major_formatter(self, formatter) -> None: ...
    def set_minor_locator(self, locator) -> None: ...
    def set_minor_formatter(self, formatter) -> None: ...
    def set_units(self, units) -> None: ...
    def update_units(self, x) -> None:
        """Pass units to the internal converter, potentially updating its mapping."""
    def convert_units(self, x):
        """Return a numeric representation of the input data."""
    def get_scale(self): ...
    def get_majorticklocs(self): ...
