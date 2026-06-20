from dataclasses import dataclass
from matplotlib.artist import Artist as Artist
from numpy import ndarray
from pandas import DataFrame
from seaborn._core.exceptions import PlotSpecError as PlotSpecError
from seaborn._core.properties import DashPattern as DashPattern, DashPatternWithOffset as DashPatternWithOffset, PROPERTIES as PROPERTIES, Property as Property, RGBATuple as RGBATuple
from seaborn._core.scales import Scale as Scale
from typing import Any

class Mappable:
    def __init__(self, val: Any = None, depend: str | None = None, rc: str | None = None, auto: bool = False, grouping: bool = True) -> None:
        """
        Property that can be mapped from data or set directly, with flexible defaults.

        Parameters
        ----------
        val : Any
            Use this value as the default.
        depend : str
            Use the value of this feature as the default.
        rc : str
            Use the value of this rcParam as the default.
        auto : bool
            The default value will depend on other parameters at compile time.
        grouping : bool
            If True, use the mapped variable to define groups.

        """
    @property
    def depend(self) -> Any:
        """Return the name of the feature to source a default value from."""
    @property
    def grouping(self) -> bool: ...
    @property
    def default(self) -> Any:
        """Get the default value for this feature, or access the relevant rcParam."""
MappableBool = bool | Mappable
MappableString = str | Mappable
MappableFloat = float | Mappable
MappableColor = str | tuple | Mappable
MappableStyle = str | DashPattern | DashPatternWithOffset | Mappable

@dataclass
class Mark:
    """Base class for objects that visually represent data."""
    artist_kws: dict = ...
    def __init__(self, artist_kws) -> None: ...

def resolve_properties(mark: Mark, data: DataFrame, scales: dict[str, Scale]) -> dict[str, Any]: ...
def resolve_color(mark: Mark, data: DataFrame | dict, prefix: str = '', scales: dict[str, Scale] | None = None) -> RGBATuple | ndarray:
    '''
    Obtain a default, specified, or mapped value for a color feature.

    This method exists separately to support the relationship between a
    color and its corresponding alpha. We want to respect alpha values that
    are passed in specified (or mapped) color values but also make use of a
    separate `alpha` variable, which can be mapped. This approach may also
    be extended to support mapping of specific color channels (i.e.
    luminance, chroma) in the future.

    Parameters
    ----------
    mark :
        Mark with the color property.
    data :
        Container with data values for features that will be semantically mapped.
    prefix :
        Support "color", "fillcolor", etc.

    '''
def document_properties(mark): ...
