from _typeshed import Incomplete
from matplotlib import cbook as cbook
from matplotlib.artist import Artist as Artist

class Container(tuple):
    """
    Base class for containers.

    Containers are classes that collect semantically related Artists such as
    the bars of a bar plot.
    """
    def __new__(cls, *args, **kwargs): ...
    def __init__(self, kl, label: Incomplete | None = None) -> None: ...
    def remove(self): ...
    def get_children(self): ...
    get_label: Incomplete
    set_label: Incomplete
    add_callback: Incomplete
    remove_callback: Incomplete
    pchanged: Incomplete

class BarContainer(Container):
    """
    Container for the artists of bar plots (e.g. created by `.Axes.bar`).

    The container can be treated as a tuple of the *patches* themselves.
    Additionally, you can access these and further parameters by the
    attributes.

    Attributes
    ----------
    patches : list of :class:`~matplotlib.patches.Rectangle`
        The artists of the bars.

    errorbar : None or :class:`~matplotlib.container.ErrorbarContainer`
        A container for the error bar artists if error bars are present.
        *None* otherwise.

    datavalues : None or array-like
        The underlying data values corresponding to the bars.

    orientation : {'vertical', 'horizontal'}, default: None
        If 'vertical', the bars are assumed to be vertical.
        If 'horizontal', the bars are assumed to be horizontal.

    """
    patches: Incomplete
    errorbar: Incomplete
    datavalues: Incomplete
    orientation: Incomplete
    def __init__(self, patches, errorbar: Incomplete | None = None, *, datavalues: Incomplete | None = None, orientation: Incomplete | None = None, **kwargs) -> None: ...

class ErrorbarContainer(Container):
    """
    Container for the artists of error bars (e.g. created by `.Axes.errorbar`).

    The container can be treated as the *lines* tuple itself.
    Additionally, you can access these and further parameters by the
    attributes.

    Attributes
    ----------
    lines : tuple
        Tuple of ``(data_line, caplines, barlinecols)``.

        - data_line : :class:`~matplotlib.lines.Line2D` instance of
          x, y plot markers and/or line.
        - caplines : tuple of :class:`~matplotlib.lines.Line2D` instances of
          the error bar caps.
        - barlinecols : list of :class:`~matplotlib.collections.LineCollection`
          with the horizontal and vertical error ranges.

    has_xerr, has_yerr : bool
        ``True`` if the errorbar has x/y errors.

    """
    lines: Incomplete
    has_xerr: Incomplete
    has_yerr: Incomplete
    def __init__(self, lines, has_xerr: bool = False, has_yerr: bool = False, **kwargs) -> None: ...

class StemContainer(Container):
    """
    Container for the artists created in a :meth:`.Axes.stem` plot.

    The container can be treated like a namedtuple ``(markerline, stemlines,
    baseline)``.

    Attributes
    ----------
    markerline :  :class:`~matplotlib.lines.Line2D`
        The artist of the markers at the stem heads.

    stemlines : list of :class:`~matplotlib.lines.Line2D`
        The artists of the vertical lines for all stems.

    baseline : :class:`~matplotlib.lines.Line2D`
        The artist of the horizontal baseline.
    """
    markerline: Incomplete
    stemlines: Incomplete
    baseline: Incomplete
    def __init__(self, markerline_stemlines_baseline, **kwargs) -> None:
        """
        Parameters
        ----------
        markerline_stemlines_baseline : tuple
            Tuple of ``(markerline, stemlines, baseline)``.
            ``markerline`` contains the `.LineCollection` of the markers,
            ``stemlines`` is a `.LineCollection` of the main lines,
            ``baseline`` is the `.Line2D` of the baseline.
        """
