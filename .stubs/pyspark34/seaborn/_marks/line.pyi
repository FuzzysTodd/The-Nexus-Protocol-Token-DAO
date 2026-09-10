from dataclasses import dataclass
from seaborn._marks.base import Mappable as Mappable, MappableColor as MappableColor, MappableFloat as MappableFloat, MappableString as MappableString, Mark as Mark, document_properties as document_properties, resolve_color as resolve_color, resolve_properties as resolve_properties
from seaborn.external.version import Version as Version

@dataclass
class Path(Mark):
    """
    A mark connecting data points in the order they appear.

    See also
    --------
    Line : A mark connecting data points with sorting along the orientation axis.
    Paths : A faster but less-flexible mark for drawing many paths.

    Examples
    --------
    .. include:: ../docstrings/objects.Path.rst

    """
    color: MappableColor = ...
    alpha: MappableFloat = ...
    linewidth: MappableFloat = ...
    linestyle: MappableString = ...
    marker: MappableString = ...
    pointsize: MappableFloat = ...
    fillcolor: MappableColor = ...
    edgecolor: MappableColor = ...
    edgewidth: MappableFloat = ...
    def __init__(self, artist_kws, color, alpha, linewidth, linestyle, marker, pointsize, fillcolor, edgecolor, edgewidth) -> None: ...

@dataclass
class Line(Path):
    """
    A mark connecting data points with sorting along the orientation axis.

    See also
    --------
    Path : A mark connecting data points in the order they appear.
    Lines : A faster but less-flexible mark for drawing many lines.

    Examples
    --------
    .. include:: ../docstrings/objects.Line.rst

    """
    def __init__(self, artist_kws, color, alpha, linewidth, linestyle, marker, pointsize, fillcolor, edgecolor, edgewidth) -> None: ...

@dataclass
class Paths(Mark):
    """
    A faster but less-flexible mark for drawing many paths.

    See also
    --------
    Path : A mark connecting data points in the order they appear.

    Examples
    --------
    .. include:: ../docstrings/objects.Paths.rst

    """
    color: MappableColor = ...
    alpha: MappableFloat = ...
    linewidth: MappableFloat = ...
    linestyle: MappableString = ...
    def __post_init__(self) -> None: ...
    def __init__(self, artist_kws, color, alpha, linewidth, linestyle) -> None: ...

@dataclass
class Lines(Paths):
    """
    A faster but less-flexible mark for drawing many lines.

    See also
    --------
    Line : A mark connecting data points with sorting along the orientation axis.

    Examples
    --------
    .. include:: ../docstrings/objects.Lines.rst

    """
    def __init__(self, artist_kws, color, alpha, linewidth, linestyle) -> None: ...

@dataclass
class Range(Paths):
    """
    An oriented line mark drawn between min/max values.

    Examples
    --------
    .. include:: ../docstrings/objects.Range.rst

    """
    def __init__(self, artist_kws, color, alpha, linewidth, linestyle) -> None: ...

@dataclass
class Dash(Paths):
    """
    A line mark drawn as an oriented segment for each datapoint.

    Examples
    --------
    .. include:: ../docstrings/objects.Dash.rst

    """
    width: MappableFloat = ...
    def __init__(self, artist_kws, color, alpha, linewidth, linestyle, width) -> None: ...
