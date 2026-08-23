from _typeshed import Incomplete
from matplotlib import cbook as cbook
from matplotlib.lines import Line2D as Line2D
from matplotlib.patches import Rectangle as Rectangle

def update_from_first_child(tgt, src) -> None: ...

class HandlerBase:
    """
    A base class for default legend handlers.

    The derived classes are meant to override *create_artists* method, which
    has the following signature::

      def create_artists(self, legend, orig_handle,
                         xdescent, ydescent, width, height, fontsize,
                         trans):

    The overridden method needs to create artists of the given
    transform that fits in the given dimension (xdescent, ydescent,
    width, height) that are scaled by fontsize if necessary.

    """
    def __init__(self, xpad: float = 0.0, ypad: float = 0.0, update_func: Incomplete | None = None) -> None:
        """
        Parameters
        ----------

        xpad : float, optional
            Padding in x-direction.
        ypad : float, optional
            Padding in y-direction.
        update_func : callable, optional
            Function for updating the legend handler properties from another
            legend handler, used by `~HandlerBase.update_prop`.
        """
    def update_prop(self, legend_handle, orig_handle, legend) -> None: ...
    def adjust_drawing_area(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize): ...
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        """
        Return the artist that this HandlerBase generates for the given
        original artist/handle.

        Parameters
        ----------
        legend : `~matplotlib.legend.Legend`
            The legend for which these legend artists are being created.
        orig_handle : :class:`matplotlib.artist.Artist` or similar
            The object for which these legend artists are being created.
        fontsize : int
            The fontsize in pixels. The artists being created should
            be scaled according to the given fontsize.
        handlebox : `~matplotlib.offsetbox.OffsetBox`
            The box which has been created to hold this legend entry's
            artists. Artists created in the `legend_artist` method must
            be added to this handlebox inside this method.

        """
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans) -> None:
        """
        Return the legend artists generated.

        Parameters
        ----------
        legend : `~matplotlib.legend.Legend`
            The legend for which these legend artists are being created.
        orig_handle : `~matplotlib.artist.Artist` or similar
            The object for which these legend artists are being created.
        xdescent, ydescent, width, height : int
            The rectangle (*xdescent*, *ydescent*, *width*, *height*) that the
            legend artists being created should fit within.
        fontsize : int
            The fontsize in pixels. The legend artists being created should
            be scaled according to the given fontsize.
        trans :  `~matplotlib.transforms.Transform`
            The transform that is applied to the legend artists being created.
            Typically from unit coordinates in the handler box to screen
            coordinates.
        """

class HandlerNpoints(HandlerBase):
    """
    A legend handler that shows *numpoints* points in the legend entry.
    """
    def __init__(self, marker_pad: float = 0.3, numpoints: Incomplete | None = None, **kwargs) -> None:
        """
        Parameters
        ----------
        marker_pad : float
            Padding between points in legend entry.
        numpoints : int
            Number of points to show in legend entry.
        **kwargs
            Keyword arguments forwarded to `.HandlerBase`.
        """
    def get_numpoints(self, legend): ...
    def get_xdata(self, legend, xdescent, ydescent, width, height, fontsize): ...

class HandlerNpointsYoffsets(HandlerNpoints):
    """
    A legend handler that shows *numpoints* in the legend, and allows them to
    be individually offset in the y-direction.
    """
    def __init__(self, numpoints: Incomplete | None = None, yoffsets: Incomplete | None = None, **kwargs) -> None:
        """
        Parameters
        ----------
        numpoints : int
            Number of points to show in legend entry.
        yoffsets : array of floats
            Length *numpoints* list of y offsets for each point in
            legend entry.
        **kwargs
            Keyword arguments forwarded to `.HandlerNpoints`.
        """
    def get_ydata(self, legend, xdescent, ydescent, width, height, fontsize): ...

class HandlerLine2DCompound(HandlerNpoints):
    """
    Original handler for `.Line2D` instances, that relies on combining
    a line-only with a marker-only artist.  May be deprecated in the future.
    """
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): ...

class HandlerLine2D(HandlerNpoints):
    """
    Handler for `.Line2D` instances.

    See Also
    --------
    HandlerLine2DCompound : An earlier handler implementation, which used one
                            artist for the line and another for the marker(s).
    """
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): ...

class HandlerPatch(HandlerBase):
    """
    Handler for `.Patch` instances.
    """
    def __init__(self, patch_func: Incomplete | None = None, **kwargs) -> None:
        """
        Parameters
        ----------
        patch_func : callable, optional
            The function that creates the legend key artist.
            *patch_func* should have the signature::

                def patch_func(legend=legend, orig_handle=orig_handle,
                               xdescent=xdescent, ydescent=ydescent,
                               width=width, height=height, fontsize=fontsize)

            Subsequently, the created artist will have its ``update_prop``
            method called and the appropriate transform will be applied.

        **kwargs
            Keyword arguments forwarded to `.HandlerBase`.
        """
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): ...

class HandlerStepPatch(HandlerBase):
    """
    Handler for `~.matplotlib.patches.StepPatch` instances.
    """
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): ...

class HandlerLineCollection(HandlerLine2D):
    """
    Handler for `.LineCollection` instances.
    """
    def get_numpoints(self, legend): ...
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): ...

class HandlerRegularPolyCollection(HandlerNpointsYoffsets):
    """Handler for `.RegularPolyCollection`\\s."""
    def __init__(self, yoffsets: Incomplete | None = None, sizes: Incomplete | None = None, **kwargs) -> None: ...
    def get_numpoints(self, legend): ...
    def get_sizes(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize): ...
    def update_prop(self, legend_handle, orig_handle, legend) -> None: ...
    def create_collection(self, orig_handle, sizes, offsets, offset_transform): ...
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): ...

class HandlerPathCollection(HandlerRegularPolyCollection):
    """Handler for `.PathCollection`\\s, which are used by `~.Axes.scatter`."""
    def create_collection(self, orig_handle, sizes, offsets, offset_transform): ...

class HandlerCircleCollection(HandlerRegularPolyCollection):
    """Handler for `.CircleCollection`\\s."""
    def create_collection(self, orig_handle, sizes, offsets, offset_transform): ...

class HandlerErrorbar(HandlerLine2D):
    """Handler for Errorbars."""
    def __init__(self, xerr_size: float = 0.5, yerr_size: Incomplete | None = None, marker_pad: float = 0.3, numpoints: Incomplete | None = None, **kwargs) -> None: ...
    def get_err_size(self, legend, xdescent, ydescent, width, height, fontsize): ...
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): ...

class HandlerStem(HandlerNpointsYoffsets):
    """
    Handler for plots produced by `~.Axes.stem`.
    """
    def __init__(self, marker_pad: float = 0.3, numpoints: Incomplete | None = None, bottom: Incomplete | None = None, yoffsets: Incomplete | None = None, **kwargs) -> None:
        """
        Parameters
        ----------
        marker_pad : float, default: 0.3
            Padding between points in legend entry.
        numpoints : int, optional
            Number of points to show in legend entry.
        bottom : float, optional

        yoffsets : array of floats, optional
            Length *numpoints* list of y offsets for each point in
            legend entry.
        **kwargs
            Keyword arguments forwarded to `.HandlerNpointsYoffsets`.
        """
    def get_ydata(self, legend, xdescent, ydescent, width, height, fontsize): ...
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): ...

class HandlerTuple(HandlerBase):
    """
    Handler for Tuple.
    """
    def __init__(self, ndivide: int = 1, pad: Incomplete | None = None, **kwargs) -> None:
        """
        Parameters
        ----------
        ndivide : int, default: 1
            The number of sections to divide the legend area into.  If None,
            use the length of the input tuple.
        pad : float, default: :rc:`legend.borderpad`
            Padding in units of fraction of font size.
        **kwargs
            Keyword arguments forwarded to `.HandlerBase`.
        """
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): ...

class HandlerPolyCollection(HandlerBase):
    """
    Handler for `.PolyCollection` used in `~.Axes.fill_between` and
    `~.Axes.stackplot`.
    """
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans): ...
