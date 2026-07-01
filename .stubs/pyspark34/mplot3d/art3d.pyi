from . import proj3d as proj3d
from _typeshed import Incomplete
from matplotlib import lines, text as mtext
from matplotlib.collections import LineCollection, PatchCollection, PathCollection, PolyCollection
from matplotlib.patches import Patch

def get_dir_vector(zdir):
    """
    Return a direction vector.

    Parameters
    ----------
    zdir : {'x', 'y', 'z', None, 3-tuple}
        The direction. Possible values are:

        - 'x': equivalent to (1, 0, 0)
        - 'y': equivalent to (0, 1, 0)
        - 'z': equivalent to (0, 0, 1)
        - *None*: equivalent to (0, 0, 0)
        - an iterable (x, y, z) is converted to a NumPy array, if not already

    Returns
    -------
    x, y, z : array-like
        The direction vector.
    """

class Text3D(mtext.Text):
    """
    Text object with 3D position and direction.

    Parameters
    ----------
    x, y, z : float
        The position of the text.
    text : str
        The text string to display.
    zdir : {'x', 'y', 'z', None, 3-tuple}
        The direction of the text. See `.get_dir_vector` for a description of
        the values.

    Other Parameters
    ----------------
    **kwargs
         All other parameters are passed on to `~matplotlib.text.Text`.
   """
    def __init__(self, x: int = 0, y: int = 0, z: int = 0, text: str = '', zdir: str = 'z', **kwargs) -> None: ...
    def get_position_3d(self):
        """Return the (x, y, z) position of the text."""
    def set_position_3d(self, xyz, zdir: Incomplete | None = None) -> None:
        """
        Set the (*x*, *y*, *z*) position of the text.

        Parameters
        ----------
        xyz : (float, float, float)
            The position in 3D space.
        zdir : {'x', 'y', 'z', None, 3-tuple}
            The direction of the text. If unspecified, the *zdir* will not be
            changed. See `.get_dir_vector` for a description of the values.
        """
    stale: bool
    def set_z(self, z) -> None:
        """
        Set the *z* position of the text.

        Parameters
        ----------
        z : float
        """
    def set_3d_properties(self, z: int = 0, zdir: str = 'z') -> None:
        """
        Set the *z* position and direction of the text.

        Parameters
        ----------
        z : float
            The z-position in 3D space.
        zdir : {'x', 'y', 'z', 3-tuple}
            The direction of the text. Default: 'z'.
            See `.get_dir_vector` for a description of the values.
        """
    def draw(self, renderer) -> None: ...
    def get_tightbbox(self, renderer: Incomplete | None = None) -> None: ...

def text_2d_to_3d(obj, z: int = 0, zdir: str = 'z') -> None:
    """
    Convert a `.Text` to a `.Text3D` object.

    Parameters
    ----------
    z : float
        The z-position in 3D space.
    zdir : {'x', 'y', 'z', 3-tuple}
        The direction of the text. Default: 'z'.
        See `.get_dir_vector` for a description of the values.
    """

class Line3D(lines.Line2D):
    """
    3D line object.

    .. note:: Use `get_data_3d` to obtain the data associated with the line.
            `~.Line2D.get_data`, `~.Line2D.get_xdata`, and `~.Line2D.get_ydata` return
            the x- and y-coordinates of the projected 2D-line, not the x- and y-data of
            the 3D-line. Similarly, use `set_data_3d` to set the data, not
            `~.Line2D.set_data`, `~.Line2D.set_xdata`, and `~.Line2D.set_ydata`.
    """
    def __init__(self, xs, ys, zs, *args, **kwargs) -> None:
        """

        Parameters
        ----------
        xs : array-like
            The x-data to be plotted.
        ys : array-like
            The y-data to be plotted.
        zs : array-like
            The z-data to be plotted.
        *args, **kwargs :
            Additional arguments are passed to `~matplotlib.lines.Line2D`.
        """
    stale: bool
    def set_3d_properties(self, zs: int = 0, zdir: str = 'z') -> None:
        """
        Set the *z* position and direction of the line.

        Parameters
        ----------
        zs : float or array of floats
            The location along the *zdir* axis in 3D space to position the
            line.
        zdir : {'x', 'y', 'z'}
            Plane to plot line orthogonal to. Default: 'z'.
            See `.get_dir_vector` for a description of the values.
        """
    def set_data_3d(self, *args) -> None:
        """
        Set the x, y and z data

        Parameters
        ----------
        x : array-like
            The x-data to be plotted.
        y : array-like
            The y-data to be plotted.
        z : array-like
            The z-data to be plotted.

        Notes
        -----
        Accepts x, y, z arguments or a single array-like (x, y, z)
        """
    def get_data_3d(self):
        """
        Get the current data

        Returns
        -------
        verts3d : length-3 tuple or array-like
            The current data as a tuple or array-like.
        """
    def draw(self, renderer) -> None: ...

def line_2d_to_3d(line, zs: int = 0, zdir: str = 'z') -> None:
    """
    Convert a `.Line2D` to a `.Line3D` object.

    Parameters
    ----------
    zs : float
        The location along the *zdir* axis in 3D space to position the line.
    zdir : {'x', 'y', 'z'}
        Plane to plot line orthogonal to. Default: 'z'.
        See `.get_dir_vector` for a description of the values.
    """

class Line3DCollection(LineCollection):
    """
    A collection of 3D lines.
    """
    stale: bool
    def set_sort_zpos(self, val) -> None:
        """Set the position to use for z-sorting."""
    def set_segments(self, segments) -> None:
        """
        Set 3D segments.
        """
    def do_3d_projection(self):
        """
        Project the points according to renderer matrix.
        """

def line_collection_2d_to_3d(col, zs: int = 0, zdir: str = 'z') -> None:
    """Convert a `.LineCollection` to a `.Line3DCollection` object."""

class Patch3D(Patch):
    """
    3D patch object.
    """
    def __init__(self, *args, zs=(), zdir: str = 'z', **kwargs) -> None:
        """
        Parameters
        ----------
        verts :
        zs : float
            The location along the *zdir* axis in 3D space to position the
            patch.
        zdir : {'x', 'y', 'z'}
            Plane to plot patch orthogonal to. Default: 'z'.
            See `.get_dir_vector` for a description of the values.
        """
    def set_3d_properties(self, verts, zs: int = 0, zdir: str = 'z') -> None:
        """
        Set the *z* position and direction of the patch.

        Parameters
        ----------
        verts :
        zs : float
            The location along the *zdir* axis in 3D space to position the
            patch.
        zdir : {'x', 'y', 'z'}
            Plane to plot patch orthogonal to. Default: 'z'.
            See `.get_dir_vector` for a description of the values.
        """
    def get_path(self): ...
    def do_3d_projection(self): ...

class PathPatch3D(Patch3D):
    """
    3D PathPatch object.
    """
    def __init__(self, path, *, zs=(), zdir: str = 'z', **kwargs) -> None:
        """
        Parameters
        ----------
        path :
        zs : float
            The location along the *zdir* axis in 3D space to position the
            path patch.
        zdir : {'x', 'y', 'z', 3-tuple}
            Plane to plot path patch orthogonal to. Default: 'z'.
            See `.get_dir_vector` for a description of the values.
        """
    def set_3d_properties(self, path, zs: int = 0, zdir: str = 'z') -> None:
        """
        Set the *z* position and direction of the path patch.

        Parameters
        ----------
        path :
        zs : float
            The location along the *zdir* axis in 3D space to position the
            path patch.
        zdir : {'x', 'y', 'z', 3-tuple}
            Plane to plot path patch orthogonal to. Default: 'z'.
            See `.get_dir_vector` for a description of the values.
        """
    def do_3d_projection(self): ...

def patch_2d_to_3d(patch, z: int = 0, zdir: str = 'z') -> None:
    """Convert a `.Patch` to a `.Patch3D` object."""
def pathpatch_2d_to_3d(pathpatch, z: int = 0, zdir: str = 'z') -> None:
    """Convert a `.PathPatch` to a `.PathPatch3D` object."""

class Patch3DCollection(PatchCollection):
    """
    A collection of 3D patches.
    """
    def __init__(self, *args, zs: int = 0, zdir: str = 'z', depthshade: bool = True, **kwargs) -> None:
        """
        Create a collection of flat 3D patches with its normal vector
        pointed in *zdir* direction, and located at *zs* on the *zdir*
        axis. 'zs' can be a scalar or an array-like of the same length as
        the number of patches in the collection.

        Constructor arguments are the same as for
        :class:`~matplotlib.collections.PatchCollection`. In addition,
        keywords *zs=0* and *zdir='z'* are available.

        Also, the keyword argument *depthshade* is available to indicate
        whether to shade the patches in order to give the appearance of depth
        (default is *True*). This is typically desired in scatter plots.
        """
    def get_depthshade(self): ...
    stale: bool
    def set_depthshade(self, depthshade) -> None:
        """
        Set whether depth shading is performed on collection members.

        Parameters
        ----------
        depthshade : bool
            Whether to shade the patches in order to give the appearance of
            depth.
        """
    def set_sort_zpos(self, val) -> None:
        """Set the position to use for z-sorting."""
    def set_3d_properties(self, zs, zdir) -> None:
        """
        Set the *z* positions and direction of the patches.

        Parameters
        ----------
        zs : float or array of floats
            The location or locations to place the patches in the collection
            along the *zdir* axis.
        zdir : {'x', 'y', 'z'}
            Plane to plot patches orthogonal to.
            All patches must have the same direction.
            See `.get_dir_vector` for a description of the values.
        """
    def do_3d_projection(self): ...
    def get_facecolor(self): ...
    def get_edgecolor(self): ...

class Path3DCollection(PathCollection):
    """
    A collection of 3D paths.
    """
    def __init__(self, *args, zs: int = 0, zdir: str = 'z', depthshade: bool = True, **kwargs) -> None:
        """
        Create a collection of flat 3D paths with its normal vector
        pointed in *zdir* direction, and located at *zs* on the *zdir*
        axis. 'zs' can be a scalar or an array-like of the same length as
        the number of paths in the collection.

        Constructor arguments are the same as for
        :class:`~matplotlib.collections.PathCollection`. In addition,
        keywords *zs=0* and *zdir='z'* are available.

        Also, the keyword argument *depthshade* is available to indicate
        whether to shade the patches in order to give the appearance of depth
        (default is *True*). This is typically desired in scatter plots.
        """
    def draw(self, renderer) -> None: ...
    stale: bool
    def set_sort_zpos(self, val) -> None:
        """Set the position to use for z-sorting."""
    def set_3d_properties(self, zs, zdir) -> None:
        """
        Set the *z* positions and direction of the paths.

        Parameters
        ----------
        zs : float or array of floats
            The location or locations to place the paths in the collection
            along the *zdir* axis.
        zdir : {'x', 'y', 'z'}
            Plane to plot paths orthogonal to.
            All paths must have the same direction.
            See `.get_dir_vector` for a description of the values.
        """
    def set_sizes(self, sizes, dpi: float = 72.0) -> None: ...
    def set_linewidth(self, lw) -> None: ...
    def get_depthshade(self): ...
    def set_depthshade(self, depthshade) -> None:
        """
        Set whether depth shading is performed on collection members.

        Parameters
        ----------
        depthshade : bool
            Whether to shade the patches in order to give the appearance of
            depth.
        """
    def do_3d_projection(self): ...
    def get_facecolor(self): ...
    def get_edgecolor(self): ...

def patch_collection_2d_to_3d(col, zs: int = 0, zdir: str = 'z', depthshade: bool = True) -> None:
    '''
    Convert a `.PatchCollection` into a `.Patch3DCollection` object
    (or a `.PathCollection` into a `.Path3DCollection` object).

    Parameters
    ----------
    zs : float or array of floats
        The location or locations to place the patches in the collection along
        the *zdir* axis. Default: 0.
    zdir : {\'x\', \'y\', \'z\'}
        The axis in which to place the patches. Default: "z".
        See `.get_dir_vector` for a description of the values.
    depthshade
        Whether to shade the patches to give a sense of depth. Default: *True*.

    '''

class Poly3DCollection(PolyCollection):
    """
    A collection of 3D polygons.

    .. note::
        **Filling of 3D polygons**

        There is no simple definition of the enclosed surface of a 3D polygon
        unless the polygon is planar.

        In practice, Matplotlib fills the 2D projection of the polygon. This
        gives a correct filling appearance only for planar polygons. For all
        other polygons, you'll find orientations in which the edges of the
        polygon intersect in the projection. This will lead to an incorrect
        visualization of the 3D area.

        If you need filled areas, it is recommended to create them via
        `~mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf`, which creates a
        triangulation and thus generates consistent surfaces.
    """
    def __init__(self, verts, *args, zsort: str = 'average', shade: bool = False, lightsource: Incomplete | None = None, **kwargs) -> None:
        """
        Parameters
        ----------
        verts : list of (N, 3) array-like
            The sequence of polygons [*verts0*, *verts1*, ...] where each
            element *verts_i* defines the vertices of polygon *i* as a 2D
            array-like of shape (N, 3).
        zsort : {'average', 'min', 'max'}, default: 'average'
            The calculation method for the z-order.
            See `~.Poly3DCollection.set_zsort` for details.
        shade : bool, default: False
            Whether to shade *facecolors* and *edgecolors*. When activating
            *shade*, *facecolors* and/or *edgecolors* must be provided.

            .. versionadded:: 3.7

        lightsource : `~matplotlib.colors.LightSource`, optional
            The lightsource to use when *shade* is True.

            .. versionadded:: 3.7

        *args, **kwargs
            All other parameters are forwarded to `.PolyCollection`.

        Notes
        -----
        Note that this class does a bit of magic with the _facecolors
        and _edgecolors properties.
        """
    stale: bool
    def set_zsort(self, zsort) -> None:
        """
        Set the calculation method for the z-order.

        Parameters
        ----------
        zsort : {'average', 'min', 'max'}
            The function applied on the z-coordinates of the vertices in the
            viewer's coordinate system, to determine the z-order.
        """
    def get_vector(self, segments3d) -> None:
        """Optimize points for projection."""
    def set_verts(self, verts, closed: bool = True) -> None:
        """
        Set 3D vertices.

        Parameters
        ----------
        verts : list of (N, 3) array-like
            The sequence of polygons [*verts0*, *verts1*, ...] where each
            element *verts_i* defines the vertices of polygon *i* as a 2D
            array-like of shape (N, 3).
        closed : bool, default: True
            Whether the polygon should be closed by adding a CLOSEPOLY
            connection at the end.
        """
    def set_verts_and_codes(self, verts, codes) -> None:
        """Set 3D vertices with path codes."""
    def set_3d_properties(self) -> None: ...
    def set_sort_zpos(self, val) -> None:
        """Set the position to use for z-sorting."""
    def do_3d_projection(self):
        """
        Perform the 3D projection for this object.
        """
    def set_facecolor(self, colors) -> None: ...
    def set_edgecolor(self, colors) -> None: ...
    def set_alpha(self, alpha) -> None: ...
    def get_facecolor(self): ...
    def get_edgecolor(self): ...

def poly_collection_2d_to_3d(col, zs: int = 0, zdir: str = 'z') -> None:
    """
    Convert a `.PolyCollection` into a `.Poly3DCollection` object.

    Parameters
    ----------
    zs : float or array of floats
        The location or locations to place the polygons in the collection along
        the *zdir* axis. Default: 0.
    zdir : {'x', 'y', 'z'}
        The axis in which to place the patches. Default: 'z'.
        See `.get_dir_vector` for a description of the values.
    """
def juggle_axes(xs, ys, zs, zdir):
    """
    Reorder coordinates so that 2D *xs*, *ys* can be plotted in the plane
    orthogonal to *zdir*. *zdir* is normally 'x', 'y' or 'z'. However, if
    *zdir* starts with a '-' it is interpreted as a compensation for
    `rotate_axes`.
    """
def rotate_axes(xs, ys, zs, zdir):
    """
    Reorder coordinates so that the axes are rotated with *zdir* along
    the original z axis. Prepending the axis with a '-' does the
    inverse transform, so *zdir* can be 'x', '-x', 'y', '-y', 'z' or '-z'.
    """
