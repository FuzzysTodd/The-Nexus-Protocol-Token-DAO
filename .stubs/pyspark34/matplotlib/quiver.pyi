import matplotlib.artist as martist
import matplotlib.collections as mcollections
from _typeshed import Incomplete
from matplotlib import cbook as cbook
from matplotlib.patches import CirclePolygon as CirclePolygon

class QuiverKey(martist.Artist):
    """Labelled arrow for use as a quiver plot scale key."""
    halign: Incomplete
    valign: Incomplete
    pivot: Incomplete
    Q: Incomplete
    X: Incomplete
    Y: Incomplete
    U: Incomplete
    angle: Incomplete
    coord: Incomplete
    color: Incomplete
    label: Incomplete
    labelpos: Incomplete
    labelcolor: Incomplete
    fontproperties: Incomplete
    kw: Incomplete
    text: Incomplete
    zorder: Incomplete
    def __init__(self, Q, X, Y, U, label, *, angle: int = 0, coordinates: str = 'axes', color: Incomplete | None = None, labelsep: float = 0.1, labelpos: str = 'N', labelcolor: Incomplete | None = None, fontproperties: Incomplete | None = None, **kwargs) -> None:
        """
        Add a key to a quiver plot.

        The positioning of the key depends on *X*, *Y*, *coordinates*, and
        *labelpos*.  If *labelpos* is 'N' or 'S', *X*, *Y* give the position of
        the middle of the key arrow.  If *labelpos* is 'E', *X*, *Y* positions
        the head, and if *labelpos* is 'W', *X*, *Y* positions the tail; in
        either of these two cases, *X*, *Y* is somewhere in the middle of the
        arrow+label key object.

        Parameters
        ----------
        Q : `~matplotlib.quiver.Quiver`
            A `.Quiver` object as returned by a call to `~.Axes.quiver()`.
        X, Y : float
            The location of the key.
        U : float
            The length of the key.
        label : str
            The key label (e.g., length and units of the key).
        angle : float, default: 0
            The angle of the key arrow, in degrees anti-clockwise from the
            x-axis.
        coordinates : {'axes', 'figure', 'data', 'inches'}, default: 'axes'
            Coordinate system and units for *X*, *Y*: 'axes' and 'figure' are
            normalized coordinate systems with (0, 0) in the lower left and
            (1, 1) in the upper right; 'data' are the axes data coordinates
            (used for the locations of the vectors in the quiver plot itself);
            'inches' is position in the figure in inches, with (0, 0) at the
            lower left corner.
        color : color
            Overrides face and edge colors from *Q*.
        labelpos : {'N', 'S', 'E', 'W'}
            Position the label above, below, to the right, to the left of the
            arrow, respectively.
        labelsep : float, default: 0.1
            Distance in inches between the arrow and the label.
        labelcolor : color, default: :rc:`text.color`
            Label color.
        fontproperties : dict, optional
            A dictionary with keyword arguments accepted by the
            `~matplotlib.font_manager.FontProperties` initializer:
            *family*, *style*, *variant*, *size*, *weight*.
        **kwargs
            Any additional keyword arguments are used to override vector
            properties taken from *Q*.
        """
    @property
    def labelsep(self): ...
    stale: bool
    def draw(self, renderer) -> None: ...
    def set_figure(self, fig) -> None: ...
    def contains(self, mouseevent): ...

class Quiver(mcollections.PolyCollection):
    """
    Specialized PolyCollection for arrows.

    The only API method is set_UVC(), which can be used
    to change the size, orientation, and color of the
    arrows; their locations are fixed when the class is
    instantiated.  Possibly this method will be useful
    in animations.

    Much of the work in this class is done in the draw()
    method so that as much information as possible is available
    about the plot.  In subsequent draw() calls, recalculation
    is limited to things that might have changed, so there
    should be no performance penalty from putting the calculations
    in the draw() method.
    """
    X: Incomplete
    Y: Incomplete
    XY: Incomplete
    N: Incomplete
    scale: Incomplete
    headwidth: Incomplete
    headlength: Incomplete
    headaxislength: Incomplete
    minshaft: Incomplete
    minlength: Incomplete
    units: Incomplete
    scale_units: Incomplete
    angles: Incomplete
    width: Incomplete
    pivot: Incomplete
    transform: Incomplete
    polykw: Incomplete
    def __init__(self, ax, *args, scale: Incomplete | None = None, headwidth: int = 3, headlength: int = 5, headaxislength: float = 4.5, minshaft: int = 1, minlength: int = 1, units: str = 'width', scale_units: Incomplete | None = None, angles: str = 'uv', width: Incomplete | None = None, color: str = 'k', pivot: str = 'tail', **kwargs) -> None:
        """
        The constructor takes one required argument, an Axes
        instance, followed by the args and kwargs described
        by the following pyplot interface documentation:
        %s
        """
    def get_datalim(self, transData): ...
    stale: bool
    def draw(self, renderer) -> None: ...
    U: Incomplete
    V: Incomplete
    Umask: Incomplete
    def set_UVC(self, U, V, C: Incomplete | None = None) -> None: ...
    quiver_doc: Incomplete

class Barbs(mcollections.PolyCollection):
    """
    Specialized PolyCollection for barbs.

    The only API method is :meth:`set_UVC`, which can be used to
    change the size, orientation, and color of the arrows.  Locations
    are changed using the :meth:`set_offsets` collection method.
    Possibly this method will be useful in animations.

    There is one internal function :meth:`_find_tails` which finds
    exactly what should be put on the barb given the vector magnitude.
    From there :meth:`_make_barbs` is used to find the vertices of the
    polygon to represent the barb based on this information.
    """
    sizes: Incomplete
    fill_empty: Incomplete
    barb_increments: Incomplete
    rounding: Incomplete
    flip: Incomplete
    x: Incomplete
    y: Incomplete
    def __init__(self, ax, *args, pivot: str = 'tip', length: int = 7, barbcolor: Incomplete | None = None, flagcolor: Incomplete | None = None, sizes: Incomplete | None = None, fill_empty: bool = False, barb_increments: Incomplete | None = None, rounding: bool = True, flip_barb: bool = False, **kwargs) -> None:
        """
        The constructor takes one required argument, an Axes
        instance, followed by the args and kwargs described
        by the following pyplot interface documentation:
        %(barbs_doc)s
        """
    u: Incomplete
    v: Incomplete
    stale: bool
    def set_UVC(self, U, V, C: Incomplete | None = None) -> None: ...
    def set_offsets(self, xy) -> None:
        """
        Set the offsets for the barb polygons.  This saves the offsets passed
        in and masks them as appropriate for the existing U/V data.

        Parameters
        ----------
        xy : sequence of pairs of floats
        """
    barbs_doc: Incomplete
