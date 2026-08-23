from . import art3d as art3d, axis3d as axis3d, proj3d as proj3d
from _typeshed import Incomplete
from matplotlib.axes import Axes

class Axes3D(Axes):
    """
    3D Axes object.

    .. note::

        As a user, you do not instantiate Axes directly, but use Axes creation
        methods instead; e.g. from `.pyplot` or `.Figure`:
        `~.pyplot.subplots`, `~.pyplot.subplot_mosaic` or `.Figure.add_axes`.
    """
    name: str
    dist: Incomplete
    vvec: Incomplete
    eye: Incomplete
    sx: Incomplete
    sy: Incomplete
    initial_azim: Incomplete
    initial_elev: Incomplete
    initial_roll: Incomplete
    computed_zorder: Incomplete
    xy_viewLim: Incomplete
    zz_viewLim: Incomplete
    xy_dataLim: Incomplete
    zz_dataLim: Incomplete
    M: Incomplete
    fmt_zdata: Incomplete
    def __init__(self, fig, rect: Incomplete | None = None, *args, elev: int = 30, azim: int = -60, roll: int = 0, sharez: Incomplete | None = None, proj_type: str = 'persp', box_aspect: Incomplete | None = None, computed_zorder: bool = True, focal_length: Incomplete | None = None, **kwargs) -> None:
        """
        Parameters
        ----------
        fig : Figure
            The parent figure.
        rect : tuple (left, bottom, width, height), default: None.
            The ``(left, bottom, width, height)`` axes position.
        elev : float, default: 30
            The elevation angle in degrees rotates the camera above and below
            the x-y plane, with a positive angle corresponding to a location
            above the plane.
        azim : float, default: -60
            The azimuthal angle in degrees rotates the camera about the z axis,
            with a positive angle corresponding to a right-handed rotation. In
            other words, a positive azimuth rotates the camera about the origin
            from its location along the +x axis towards the +y axis.
        roll : float, default: 0
            The roll angle in degrees rotates the camera about the viewing
            axis. A positive angle spins the camera clockwise, causing the
            scene to rotate counter-clockwise.
        sharez : Axes3D, optional
            Other Axes to share z-limits with.
        proj_type : {'persp', 'ortho'}
            The projection type, default 'persp'.
        box_aspect : 3-tuple of floats, default: None
            Changes the physical dimensions of the Axes3D, such that the ratio
            of the axis lengths in display units is x:y:z.
            If None, defaults to 4:4:3
        computed_zorder : bool, default: True
            If True, the draw order is computed based on the average position
            of the `.Artist`\\s along the view direction.
            Set to False if you want to manually control the order in which
            Artists are drawn on top of each other using their *zorder*
            attribute. This can be used for fine-tuning if the automatic order
            does not produce the desired result. Note however, that a manual
            zorder will only be correct for a limited view angle. If the figure
            is rotated by the user, it will look wrong from certain angles.
        focal_length : float, default: None
            For a projection type of 'persp', the focal length of the virtual
            camera. Must be > 0. If None, defaults to 1.
            For a projection type of 'ortho', must be set to either None
            or infinity (numpy.inf). If None, defaults to infinity.
            The focal length can be computed from a desired Field Of View via
            the equation: focal_length = 1/tan(FOV/2)

        **kwargs
            Other optional keyword arguments:

            %(Axes3D:kwdoc)s
        """
    stale: bool
    def set_axis_off(self) -> None: ...
    def set_axis_on(self) -> None: ...
    def convert_zunits(self, z):
        """
        For artists in an Axes, if the zaxis has units support,
        convert *z* using zaxis unit type
        """
    def set_top_view(self) -> None: ...
    def get_zaxis(self):
        """Return the ``ZAxis`` (`~.axis3d.Axis`) instance."""
    get_zgridlines: Incomplete
    get_zticklines: Incomplete
    w_xaxis: Incomplete
    w_yaxis: Incomplete
    w_zaxis: Incomplete
    def unit_cube(self, vals: Incomplete | None = None): ...
    def tunit_cube(self, vals: Incomplete | None = None, M: Incomplete | None = None): ...
    def tunit_edges(self, vals: Incomplete | None = None, M: Incomplete | None = None): ...
    def set_aspect(self, aspect, adjustable: Incomplete | None = None, anchor: Incomplete | None = None, share: bool = False) -> None:
        """
        Set the aspect ratios.

        Parameters
        ----------
        aspect : {'auto', 'equal', 'equalxy', 'equalxz', 'equalyz'}
            Possible values:

            =========   ==================================================
            value       description
            =========   ==================================================
            'auto'      automatic; fill the position rectangle with data.
            'equal'     adapt all the axes to have equal aspect ratios.
            'equalxy'   adapt the x and y axes to have equal aspect ratios.
            'equalxz'   adapt the x and z axes to have equal aspect ratios.
            'equalyz'   adapt the y and z axes to have equal aspect ratios.
            =========   ==================================================

        adjustable : None or {'box', 'datalim'}, optional
            If not *None*, this defines which parameter will be adjusted to
            meet the required aspect. See `.set_adjustable` for further
            details.

        anchor : None or str or 2-tuple of float, optional
            If not *None*, this defines where the Axes will be drawn if there
            is extra space due to aspect constraints. The most common way to
            specify the anchor are abbreviations of cardinal directions:

            =====   =====================
            value   description
            =====   =====================
            'C'     centered
            'SW'    lower left corner
            'S'     middle of bottom edge
            'SE'    lower right corner
            etc.
            =====   =====================

            See `~.Axes.set_anchor` for further details.

        share : bool, default: False
            If ``True``, apply the settings to all shared Axes.

        See Also
        --------
        mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect
        """
    def set_box_aspect(self, aspect, *, zoom: int = 1) -> None:
        """
        Set the Axes box aspect.

        The box aspect is the ratio of height to width in display
        units for each face of the box when viewed perpendicular to
        that face.  This is not to be confused with the data aspect (see
        `~.Axes3D.set_aspect`). The default ratios are 4:4:3 (x:y:z).

        To simulate having equal aspect in data space, set the box
        aspect to match your data range in each dimension.

        *zoom* controls the overall size of the Axes3D in the figure.

        Parameters
        ----------
        aspect : 3-tuple of floats or None
            Changes the physical dimensions of the Axes3D, such that the ratio
            of the axis lengths in display units is x:y:z.
            If None, defaults to (4, 4, 3).

        zoom : float, default: 1
            Control overall size of the Axes3D in the figure. Must be > 0.
        """
    def apply_aspect(self, position: Incomplete | None = None) -> None: ...
    def draw(self, renderer): ...
    def get_axis_position(self): ...
    def update_datalim(self, xys, **kwargs) -> None:
        """
        Not implemented in `~mpl_toolkits.mplot3d.axes3d.Axes3D`.
        """
    get_autoscalez_on: Incomplete
    set_autoscalez_on: Incomplete
    def set_zmargin(self, m) -> None:
        """
        Set padding of Z data limits prior to autoscaling.

        *m* times the data interval will be added to each end of that interval
        before it is used in autoscaling.  If *m* is negative, this will clip
        the data range instead of expanding it.

        For example, if your data is in the range [0, 2], a margin of 0.1 will
        result in a range [-0.2, 2.2]; a margin of -0.1 will result in a range
        of [0.2, 1.8].

        Parameters
        ----------
        m : float greater than -0.5
        """
    def margins(self, *margins, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None, tight: bool = True):
        """
        Set or retrieve autoscaling margins.

        See `.Axes.margins` for full documentation.  Because this function
        applies to 3D Axes, it also takes a *z* argument, and returns
        ``(xmargin, ymargin, zmargin)``.
        """
    def autoscale(self, enable: bool = True, axis: str = 'both', tight: Incomplete | None = None) -> None:
        """
        Convenience method for simple axis view autoscaling.

        See `.Axes.autoscale` for full documentation.  Because this function
        applies to 3D Axes, *axis* can also be set to 'z', and setting *axis*
        to 'both' autoscales all three axes.
        """
    def auto_scale_xyz(self, X, Y, Z: Incomplete | None = None, had_data: Incomplete | None = None) -> None: ...
    def autoscale_view(self, tight: Incomplete | None = None, scalex: bool = True, scaley: bool = True, scalez: bool = True) -> None:
        """
        Autoscale the view limits using the data limits.

        See `.Axes.autoscale_view` for full documentation.  Because this
        function applies to 3D Axes, it also takes a *scalez* argument.
        """
    def get_w_lims(self):
        """Get 3D world limits."""
    def set_zlim(self, bottom: Incomplete | None = None, top: Incomplete | None = None, emit: bool = True, auto: bool = False, *, zmin: Incomplete | None = None, zmax: Incomplete | None = None):
        """
        Set 3D z limits.

        See `.Axes.set_ylim` for full documentation
        """
    set_xlim3d: Incomplete
    set_ylim3d: Incomplete
    set_zlim3d = set_zlim
    def get_xlim(self): ...
    def get_ylim(self): ...
    def get_zlim(self):
        """Get 3D z limits."""
    get_zscale: Incomplete
    set_xscale: Incomplete
    set_yscale: Incomplete
    set_zscale: Incomplete
    get_zticks: Incomplete
    set_zticks: Incomplete
    get_zmajorticklabels: Incomplete
    get_zminorticklabels: Incomplete
    get_zticklabels: Incomplete
    set_zticklabels: Incomplete
    zaxis_date: Incomplete
    def clabel(self, *args, **kwargs) -> None:
        """Currently not implemented for 3D axes, and returns *None*."""
    elev: Incomplete
    azim: Incomplete
    roll: Incomplete
    def view_init(self, elev: Incomplete | None = None, azim: Incomplete | None = None, roll: Incomplete | None = None, vertical_axis: str = 'z') -> None:
        '''
        Set the elevation and azimuth of the axes in degrees (not radians).

        This can be used to rotate the axes programmatically.

        To look normal to the primary planes, the following elevation and
        azimuth angles can be used. A roll angle of 0, 90, 180, or 270 deg
        will rotate these views while keeping the axes at right angles.

        ==========   ====  ====
        view plane   elev  azim
        ==========   ====  ====
        XY           90    -90
        XZ           0     -90
        YZ           0     0
        -XY          -90   90
        -XZ          0     90
        -YZ          0     180
        ==========   ====  ====

        Parameters
        ----------
        elev : float, default: None
            The elevation angle in degrees rotates the camera above the plane
            pierced by the vertical axis, with a positive angle corresponding
            to a location above that plane. For example, with the default
            vertical axis of \'z\', the elevation defines the angle of the camera
            location above the x-y plane.
            If None, then the initial value as specified in the `Axes3D`
            constructor is used.
        azim : float, default: None
            The azimuthal angle in degrees rotates the camera about the
            vertical axis, with a positive angle corresponding to a
            right-handed rotation. For example, with the default vertical axis
            of \'z\', a positive azimuth rotates the camera about the origin from
            its location along the +x axis towards the +y axis.
            If None, then the initial value as specified in the `Axes3D`
            constructor is used.
        roll : float, default: None
            The roll angle in degrees rotates the camera about the viewing
            axis. A positive angle spins the camera clockwise, causing the
            scene to rotate counter-clockwise.
            If None, then the initial value as specified in the `Axes3D`
            constructor is used.
        vertical_axis : {"z", "x", "y"}, default: "z"
            The axis to align vertically. *azim* rotates about this axis.
        '''
    def set_proj_type(self, proj_type, focal_length: Incomplete | None = None) -> None:
        """
        Set the projection type.

        Parameters
        ----------
        proj_type : {'persp', 'ortho'}
            The projection type.
        focal_length : float, default: None
            For a projection type of 'persp', the focal length of the virtual
            camera. Must be > 0. If None, defaults to 1.
            The focal length can be computed from a desired Field Of View via
            the equation: focal_length = 1/tan(FOV/2)
        """
    def get_proj(self):
        """Create the projection matrix from the current viewing position."""
    button_pressed: Incomplete
    def mouse_init(self, rotate_btn: int = 1, pan_btn: int = 2, zoom_btn: int = 3) -> None:
        """
        Set the mouse buttons for 3D rotation and zooming.

        Parameters
        ----------
        rotate_btn : int or list of int, default: 1
            The mouse button or buttons to use for 3D rotation of the axes.
        pan_btn : int or list of int, default: 2
            The mouse button or buttons to use to pan the 3D axes.
        zoom_btn : int or list of int, default: 3
            The mouse button or buttons to use to zoom the 3D axes.
        """
    def disable_mouse_rotation(self) -> None:
        """Disable mouse buttons for 3D rotation, panning, and zooming."""
    def can_zoom(self):
        """
        Return whether this Axes supports the zoom box button functionality.
        """
    def can_pan(self):
        """
        Return whether this Axes supports the pan button functionality.
        """
    def sharez(self, other) -> None:
        """
        Share the z-axis with *other*.

        This is equivalent to passing ``sharez=other`` when constructing the
        Axes, and cannot be used if the z-axis is already being shared with
        another Axes.
        """
    def clear(self) -> None: ...
    def format_zdata(self, z):
        """
        Return *z* string formatted.  This function will use the
        :attr:`fmt_zdata` attribute if it is callable, else will fall
        back on the zaxis major formatter
        """
    def format_coord(self, xd, yd):
        """
        Given the 2D view coordinates attempt to guess a 3D coordinate.
        Looks for the nearest edge to the point and then assumes that
        the point is at the same z location as the nearest point on the edge.
        """
    def drag_pan(self, button, key, x, y) -> None: ...
    def set_zlabel(self, zlabel, fontdict: Incomplete | None = None, labelpad: Incomplete | None = None, **kwargs):
        """
        Set zlabel.  See doc for `.set_ylabel` for description.
        """
    def get_zlabel(self):
        """
        Get the z-label text string.
        """
    def get_frame_on(self):
        """Get whether the 3D axes panels are drawn."""
    def set_frame_on(self, b) -> None:
        """
        Set whether the 3D axes panels are drawn.

        Parameters
        ----------
        b : bool
        """
    def grid(self, visible: bool = True, **kwargs) -> None:
        """
        Set / unset 3D grid.

        .. note::

            Currently, this function does not behave the same as
            `.axes.Axes.grid`, but it is intended to eventually support that
            behavior.
        """
    def tick_params(self, axis: str = 'both', **kwargs) -> None:
        """
        Convenience method for changing the appearance of ticks and
        tick labels.

        See `.Axes.tick_params` for full documentation.  Because this function
        applies to 3D Axes, *axis* can also be set to 'z', and setting *axis*
        to 'both' autoscales all three axes.

        Also, because of how Axes3D objects are drawn very differently
        from regular 2D axes, some of these settings may have
        ambiguous meaning.  For simplicity, the 'z' axis will
        accept settings as if it was like the 'y' axis.

        .. note::
           Axes3D currently ignores some of these settings.
        """
    def invert_zaxis(self) -> None:
        """
        Invert the z-axis.
        """
    zaxis_inverted: Incomplete
    def get_zbound(self):
        """
        Return the lower and upper z-axis bounds, in increasing order.
        """
    def set_zbound(self, lower: Incomplete | None = None, upper: Incomplete | None = None) -> None:
        """
        Set the lower and upper numerical bounds of the z-axis.

        This method will honor axes inversion regardless of parameter order.
        It will not change the autoscaling setting (`.get_autoscalez_on()`).
        """
    def text(self, x, y, z, s, zdir: Incomplete | None = None, **kwargs):
        """
        Add text to the plot.

        Keyword arguments will be passed on to `.Axes.text`, except for the
        *zdir* keyword, which sets the direction to be used as the z
        direction.
        """
    text3D = text
    text2D: Incomplete
    def plot(self, xs, ys, *args, zdir: str = 'z', **kwargs):
        """
        Plot 2D or 3D data.

        Parameters
        ----------
        xs : 1D array-like
            x coordinates of vertices.
        ys : 1D array-like
            y coordinates of vertices.
        zs : float or 1D array-like
            z coordinates of vertices; either one for all points or one for
            each point.
        zdir : {'x', 'y', 'z'}, default: 'z'
            When plotting 2D data, the direction to use as z.
        **kwargs
            Other arguments are forwarded to `matplotlib.axes.Axes.plot`.
        """
    plot3D = plot
    def plot_surface(self, X, Y, Z, *, norm: Incomplete | None = None, vmin: Incomplete | None = None, vmax: Incomplete | None = None, lightsource: Incomplete | None = None, **kwargs):
        """
        Create a surface plot.

        By default, it will be colored in shades of a solid color, but it also
        supports colormapping by supplying the *cmap* argument.

        .. note::

           The *rcount* and *ccount* kwargs, which both default to 50,
           determine the maximum number of samples used in each direction.  If
           the input data is larger, it will be downsampled (by slicing) to
           these numbers of points.

        .. note::

           To maximize rendering speed consider setting *rstride* and *cstride*
           to divisors of the number of rows minus 1 and columns minus 1
           respectively. For example, given 51 rows rstride can be any of the
           divisors of 50.

           Similarly, a setting of *rstride* and *cstride* equal to 1 (or
           *rcount* and *ccount* equal the number of rows and columns) can use
           the optimized path.

        Parameters
        ----------
        X, Y, Z : 2D arrays
            Data values.

        rcount, ccount : int
            Maximum number of samples used in each direction.  If the input
            data is larger, it will be downsampled (by slicing) to these
            numbers of points.  Defaults to 50.

        rstride, cstride : int
            Downsampling stride in each direction.  These arguments are
            mutually exclusive with *rcount* and *ccount*.  If only one of
            *rstride* or *cstride* is set, the other defaults to 10.

            'classic' mode uses a default of ``rstride = cstride = 10`` instead
            of the new default of ``rcount = ccount = 50``.

        color : color-like
            Color of the surface patches.

        cmap : Colormap
            Colormap of the surface patches.

        facecolors : array-like of colors.
            Colors of each individual patch.

        norm : Normalize
            Normalization for the colormap.

        vmin, vmax : float
            Bounds for the normalization.

        shade : bool, default: True
            Whether to shade the facecolors.  Shading is always disabled when
            *cmap* is specified.

        lightsource : `~matplotlib.colors.LightSource`
            The lightsource to use when *shade* is True.

        **kwargs
            Other keyword arguments are forwarded to `.Poly3DCollection`.
        """
    def plot_wireframe(self, X, Y, Z, **kwargs):
        """
        Plot a 3D wireframe.

        .. note::

           The *rcount* and *ccount* kwargs, which both default to 50,
           determine the maximum number of samples used in each direction.  If
           the input data is larger, it will be downsampled (by slicing) to
           these numbers of points.

        Parameters
        ----------
        X, Y, Z : 2D arrays
            Data values.

        rcount, ccount : int
            Maximum number of samples used in each direction.  If the input
            data is larger, it will be downsampled (by slicing) to these
            numbers of points.  Setting a count to zero causes the data to be
            not sampled in the corresponding direction, producing a 3D line
            plot rather than a wireframe plot.  Defaults to 50.

        rstride, cstride : int
            Downsampling stride in each direction.  These arguments are
            mutually exclusive with *rcount* and *ccount*.  If only one of
            *rstride* or *cstride* is set, the other defaults to 1.  Setting a
            stride to zero causes the data to be not sampled in the
            corresponding direction, producing a 3D line plot rather than a
            wireframe plot.

            'classic' mode uses a default of ``rstride = cstride = 1`` instead
            of the new default of ``rcount = ccount = 50``.

        **kwargs
            Other keyword arguments are forwarded to `.Line3DCollection`.
        """
    def plot_trisurf(self, *args, color: Incomplete | None = None, norm: Incomplete | None = None, vmin: Incomplete | None = None, vmax: Incomplete | None = None, lightsource: Incomplete | None = None, **kwargs):
        """
        Plot a triangulated surface.

        The (optional) triangulation can be specified in one of two ways;
        either::

          plot_trisurf(triangulation, ...)

        where triangulation is a `~matplotlib.tri.Triangulation` object, or::

          plot_trisurf(X, Y, ...)
          plot_trisurf(X, Y, triangles, ...)
          plot_trisurf(X, Y, triangles=triangles, ...)

        in which case a Triangulation object will be created.  See
        `.Triangulation` for an explanation of these possibilities.

        The remaining arguments are::

          plot_trisurf(..., Z)

        where *Z* is the array of values to contour, one per point
        in the triangulation.

        Parameters
        ----------
        X, Y, Z : array-like
            Data values as 1D arrays.
        color
            Color of the surface patches.
        cmap
            A colormap for the surface patches.
        norm : Normalize
            An instance of Normalize to map values to colors.
        vmin, vmax : float, default: None
            Minimum and maximum value to map.
        shade : bool, default: True
            Whether to shade the facecolors.  Shading is always disabled when
            *cmap* is specified.
        lightsource : `~matplotlib.colors.LightSource`
            The lightsource to use when *shade* is True.
        **kwargs
            All other keyword arguments are passed on to
            :class:`~mpl_toolkits.mplot3d.art3d.Poly3DCollection`

        Examples
        --------
        .. plot:: gallery/mplot3d/trisurf3d.py
        .. plot:: gallery/mplot3d/trisurf3d_2.py
        """
    def add_contour_set(self, cset, extend3d: bool = False, stride: int = 5, zdir: str = 'z', offset: Incomplete | None = None) -> None: ...
    def add_contourf_set(self, cset, zdir: str = 'z', offset: Incomplete | None = None) -> None: ...
    def contour(self, X, Y, Z, *args, extend3d: bool = False, stride: int = 5, zdir: str = 'z', offset: Incomplete | None = None, **kwargs):
        """
        Create a 3D contour plot.

        Parameters
        ----------
        X, Y, Z : array-like,
            Input data. See `.Axes.contour` for supported data shapes.
        extend3d : bool, default: False
            Whether to extend contour in 3D.
        stride : int
            Step size for extending contour.
        zdir : {'x', 'y', 'z'}, default: 'z'
            The direction to use.
        offset : float, optional
            If specified, plot a projection of the contour lines at this
            position in a plane normal to *zdir*.
        data : indexable object, optional
            DATA_PARAMETER_PLACEHOLDER

        *args, **kwargs
            Other arguments are forwarded to `matplotlib.axes.Axes.contour`.

        Returns
        -------
        matplotlib.contour.QuadContourSet
        """
    contour3D = contour
    def tricontour(self, *args, extend3d: bool = False, stride: int = 5, zdir: str = 'z', offset: Incomplete | None = None, **kwargs):
        """
        Create a 3D contour plot.

        .. note::
            This method currently produces incorrect output due to a
            longstanding bug in 3D PolyCollection rendering.

        Parameters
        ----------
        X, Y, Z : array-like
            Input data. See `.Axes.tricontour` for supported data shapes.
        extend3d : bool, default: False
            Whether to extend contour in 3D.
        stride : int
            Step size for extending contour.
        zdir : {'x', 'y', 'z'}, default: 'z'
            The direction to use.
        offset : float, optional
            If specified, plot a projection of the contour lines at this
            position in a plane normal to *zdir*.
        data : indexable object, optional
            DATA_PARAMETER_PLACEHOLDER
        *args, **kwargs
            Other arguments are forwarded to `matplotlib.axes.Axes.tricontour`.

        Returns
        -------
        matplotlib.tri._tricontour.TriContourSet
        """
    def contourf(self, X, Y, Z, *args, zdir: str = 'z', offset: Incomplete | None = None, **kwargs):
        """
        Create a 3D filled contour plot.

        Parameters
        ----------
        X, Y, Z : array-like
            Input data. See `.Axes.contourf` for supported data shapes.
        zdir : {'x', 'y', 'z'}, default: 'z'
            The direction to use.
        offset : float, optional
            If specified, plot a projection of the contour lines at this
            position in a plane normal to *zdir*.
        data : indexable object, optional
            DATA_PARAMETER_PLACEHOLDER
        *args, **kwargs
            Other arguments are forwarded to `matplotlib.axes.Axes.contourf`.

        Returns
        -------
        matplotlib.contour.QuadContourSet
        """
    contourf3D = contourf
    def tricontourf(self, *args, zdir: str = 'z', offset: Incomplete | None = None, **kwargs):
        """
        Create a 3D filled contour plot.

        .. note::
            This method currently produces incorrect output due to a
            longstanding bug in 3D PolyCollection rendering.

        Parameters
        ----------
        X, Y, Z : array-like
            Input data. See `.Axes.tricontourf` for supported data shapes.
        zdir : {'x', 'y', 'z'}, default: 'z'
            The direction to use.
        offset : float, optional
            If specified, plot a projection of the contour lines at this
            position in a plane normal to zdir.
        data : indexable object, optional
            DATA_PARAMETER_PLACEHOLDER
        *args, **kwargs
            Other arguments are forwarded to
            `matplotlib.axes.Axes.tricontourf`.

        Returns
        -------
        matplotlib.tri._tricontour.TriContourSet
        """
    def add_collection3d(self, col, zs: int = 0, zdir: str = 'z'):
        """
        Add a 3D collection object to the plot.

        2D collection types are converted to a 3D version by
        modifying the object and adding z coordinate information.

        Supported are:

        - PolyCollection
        - LineCollection
        - PatchCollection
        """
    def scatter(self, xs, ys, zs: int = 0, zdir: str = 'z', s: int = 20, c: Incomplete | None = None, depthshade: bool = True, *args, **kwargs):
        """
        Create a scatter plot.

        Parameters
        ----------
        xs, ys : array-like
            The data positions.
        zs : float or array-like, default: 0
            The z-positions. Either an array of the same length as *xs* and
            *ys* or a single value to place all points in the same plane.
        zdir : {'x', 'y', 'z', '-x', '-y', '-z'}, default: 'z'
            The axis direction for the *zs*. This is useful when plotting 2D
            data on a 3D Axes. The data must be passed as *xs*, *ys*. Setting
            *zdir* to 'y' then plots the data to the x-z-plane.

            See also :doc:`/gallery/mplot3d/2dcollections3d`.

        s : float or array-like, default: 20
            The marker size in points**2. Either an array of the same length
            as *xs* and *ys* or a single value to make all markers the same
            size.
        c : color, sequence, or sequence of colors, optional
            The marker color. Possible values:

            - A single color format string.
            - A sequence of colors of length n.
            - A sequence of n numbers to be mapped to colors using *cmap* and
              *norm*.
            - A 2D array in which the rows are RGB or RGBA.

            For more details see the *c* argument of `~.axes.Axes.scatter`.
        depthshade : bool, default: True
            Whether to shade the scatter markers to give the appearance of
            depth. Each call to ``scatter()`` will perform its depthshading
            independently.
        data : indexable object, optional
            DATA_PARAMETER_PLACEHOLDER
        **kwargs
            All other keyword arguments are passed on to `~.axes.Axes.scatter`.

        Returns
        -------
        paths : `~matplotlib.collections.PathCollection`
        """
    scatter3D = scatter
    def bar(self, left, height, zs: int = 0, zdir: str = 'z', *args, **kwargs):
        """
        Add 2D bar(s).

        Parameters
        ----------
        left : 1D array-like
            The x coordinates of the left sides of the bars.
        height : 1D array-like
            The height of the bars.
        zs : float or 1D array-like
            Z coordinate of bars; if a single value is specified, it will be
            used for all bars.
        zdir : {'x', 'y', 'z'}, default: 'z'
            When plotting 2D data, the direction to use as z ('x', 'y' or 'z').
        data : indexable object, optional
            DATA_PARAMETER_PLACEHOLDER
        **kwargs
            Other keyword arguments are forwarded to
            `matplotlib.axes.Axes.bar`.

        Returns
        -------
        mpl_toolkits.mplot3d.art3d.Patch3DCollection
        """
    def bar3d(self, x, y, z, dx, dy, dz, color: Incomplete | None = None, zsort: str = 'average', shade: bool = True, lightsource: Incomplete | None = None, *args, **kwargs):
        """
        Generate a 3D barplot.

        This method creates three-dimensional barplot where the width,
        depth, height, and color of the bars can all be uniquely set.

        Parameters
        ----------
        x, y, z : array-like
            The coordinates of the anchor point of the bars.

        dx, dy, dz : float or array-like
            The width, depth, and height of the bars, respectively.

        color : sequence of colors, optional
            The color of the bars can be specified globally or
            individually. This parameter can be:

            - A single color, to color all bars the same color.
            - An array of colors of length N bars, to color each bar
              independently.
            - An array of colors of length 6, to color the faces of the
              bars similarly.
            - An array of colors of length 6 * N bars, to color each face
              independently.

            When coloring the faces of the boxes specifically, this is
            the order of the coloring:

            1. -Z (bottom of box)
            2. +Z (top of box)
            3. -Y
            4. +Y
            5. -X
            6. +X

        zsort : str, optional
            The z-axis sorting scheme passed onto `~.art3d.Poly3DCollection`

        shade : bool, default: True
            When true, this shades the dark sides of the bars (relative
            to the plot's source of light).

        lightsource : `~matplotlib.colors.LightSource`
            The lightsource to use when *shade* is True.

        data : indexable object, optional
            DATA_PARAMETER_PLACEHOLDER

        **kwargs
            Any additional keyword arguments are passed onto
            `~.art3d.Poly3DCollection`.

        Returns
        -------
        collection : `~.art3d.Poly3DCollection`
            A collection of three-dimensional polygons representing the bars.
        """
    def set_title(self, label, fontdict: Incomplete | None = None, loc: str = 'center', **kwargs): ...
    def quiver(self, X, Y, Z, U, V, W, *, length: int = 1, arrow_length_ratio: float = 0.3, pivot: str = 'tail', normalize: bool = False, **kwargs):
        """
        Plot a 3D field of arrows.

        The arguments can be array-like or scalars, so long as they can be
        broadcast together. The arguments can also be masked arrays. If an
        element in any of argument is masked, then that corresponding quiver
        element will not be plotted.

        Parameters
        ----------
        X, Y, Z : array-like
            The x, y and z coordinates of the arrow locations (default is
            tail of arrow; see *pivot* kwarg).

        U, V, W : array-like
            The x, y and z components of the arrow vectors.

        length : float, default: 1
            The length of each quiver.

        arrow_length_ratio : float, default: 0.3
            The ratio of the arrow head with respect to the quiver.

        pivot : {'tail', 'middle', 'tip'}, default: 'tail'
            The part of the arrow that is at the grid point; the arrow
            rotates about this point, hence the name *pivot*.

        normalize : bool, default: False
            Whether all arrows are normalized to have the same length, or keep
            the lengths defined by *u*, *v*, and *w*.

        data : indexable object, optional
            DATA_PARAMETER_PLACEHOLDER

        **kwargs
            Any additional keyword arguments are delegated to
            :class:`.Line3DCollection`
        """
    quiver3D = quiver
    def voxels(self, *args, facecolors: Incomplete | None = None, edgecolors: Incomplete | None = None, shade: bool = True, lightsource: Incomplete | None = None, **kwargs):
        """
        ax.voxels([x, y, z,] /, filled, facecolors=None, edgecolors=None, **kwargs)

        Plot a set of filled voxels

        All voxels are plotted as 1x1x1 cubes on the axis, with
        ``filled[0, 0, 0]`` placed with its lower corner at the origin.
        Occluded faces are not plotted.

        Parameters
        ----------
        filled : 3D np.array of bool
            A 3D array of values, with truthy values indicating which voxels
            to fill

        x, y, z : 3D np.array, optional
            The coordinates of the corners of the voxels. This should broadcast
            to a shape one larger in every dimension than the shape of
            *filled*.  These can be used to plot non-cubic voxels.

            If not specified, defaults to increasing integers along each axis,
            like those returned by :func:`~numpy.indices`.
            As indicated by the ``/`` in the function signature, these
            arguments can only be passed positionally.

        facecolors, edgecolors : array-like, optional
            The color to draw the faces and edges of the voxels. Can only be
            passed as keyword arguments.
            These parameters can be:

            - A single color value, to color all voxels the same color. This
              can be either a string, or a 1D rgb/rgba array
            - ``None``, the default, to use a single color for the faces, and
              the style default for the edges.
            - A 3D `~numpy.ndarray` of color names, with each item the color
              for the corresponding voxel. The size must match the voxels.
            - A 4D `~numpy.ndarray` of rgb/rgba data, with the components
              along the last axis.

        shade : bool, default: True
            Whether to shade the facecolors.

        lightsource : `~matplotlib.colors.LightSource`
            The lightsource to use when *shade* is True.

        **kwargs
            Additional keyword arguments to pass onto
            `~mpl_toolkits.mplot3d.art3d.Poly3DCollection`.

        Returns
        -------
        faces : dict
            A dictionary indexed by coordinate, where ``faces[i, j, k]`` is a
            `.Poly3DCollection` of the faces drawn for the voxel
            ``filled[i, j, k]``. If no faces were drawn for a given voxel,
            either because it was not asked to be drawn, or it is fully
            occluded, then ``(i, j, k) not in faces``.

        Examples
        --------
        .. plot:: gallery/mplot3d/voxels.py
        .. plot:: gallery/mplot3d/voxels_rgb.py
        .. plot:: gallery/mplot3d/voxels_torus.py
        .. plot:: gallery/mplot3d/voxels_numpy_logo.py
        """
    def errorbar(self, x, y, z, zerr: Incomplete | None = None, yerr: Incomplete | None = None, xerr: Incomplete | None = None, fmt: str = '', barsabove: bool = False, errorevery: int = 1, ecolor: Incomplete | None = None, elinewidth: Incomplete | None = None, capsize: Incomplete | None = None, capthick: Incomplete | None = None, xlolims: bool = False, xuplims: bool = False, ylolims: bool = False, yuplims: bool = False, zlolims: bool = False, zuplims: bool = False, **kwargs):
        """
        Plot lines and/or markers with errorbars around them.

        *x*/*y*/*z* define the data locations, and *xerr*/*yerr*/*zerr* define
        the errorbar sizes. By default, this draws the data markers/lines as
        well the errorbars. Use fmt='none' to draw errorbars only.

        Parameters
        ----------
        x, y, z : float or array-like
            The data positions.

        xerr, yerr, zerr : float or array-like, shape (N,) or (2, N), optional
            The errorbar sizes:

            - scalar: Symmetric +/- values for all data points.
            - shape(N,): Symmetric +/-values for each data point.
            - shape(2, N): Separate - and + values for each bar. First row
              contains the lower errors, the second row contains the upper
              errors.
            - *None*: No errorbar.

            Note that all error arrays should have *positive* values.

        fmt : str, default: ''
            The format for the data points / data lines. See `.plot` for
            details.

            Use 'none' (case-insensitive) to plot errorbars without any data
            markers.

        ecolor : color, default: None
            The color of the errorbar lines.  If None, use the color of the
            line connecting the markers.

        elinewidth : float, default: None
            The linewidth of the errorbar lines. If None, the linewidth of
            the current style is used.

        capsize : float, default: :rc:`errorbar.capsize`
            The length of the error bar caps in points.

        capthick : float, default: None
            An alias to the keyword argument *markeredgewidth* (a.k.a. *mew*).
            This setting is a more sensible name for the property that
            controls the thickness of the error bar cap in points. For
            backwards compatibility, if *mew* or *markeredgewidth* are given,
            then they will over-ride *capthick*. This may change in future
            releases.

        barsabove : bool, default: False
            If True, will plot the errorbars above the plot
            symbols. Default is below.

        xlolims, ylolims, zlolims : bool, default: False
            These arguments can be used to indicate that a value gives only
            lower limits. In that case a caret symbol is used to indicate
            this. *lims*-arguments may be scalars, or array-likes of the same
            length as the errors. To use limits with inverted axes,
            `~.Axes.set_xlim` or `~.Axes.set_ylim` must be called before
            `errorbar`. Note the tricky parameter names: setting e.g.
            *ylolims* to True means that the y-value is a *lower* limit of the
            True value, so, only an *upward*-pointing arrow will be drawn!

        xuplims, yuplims, zuplims : bool, default: False
            Same as above, but for controlling the upper limits.

        errorevery : int or (int, int), default: 1
            draws error bars on a subset of the data. *errorevery* =N draws
            error bars on the points (x[::N], y[::N], z[::N]).
            *errorevery* =(start, N) draws error bars on the points
            (x[start::N], y[start::N], z[start::N]). e.g. errorevery=(6, 3)
            adds error bars to the data at (x[6], x[9], x[12], x[15], ...).
            Used to avoid overlapping error bars when two series share x-axis
            values.

        Returns
        -------
        errlines : list
            List of `~mpl_toolkits.mplot3d.art3d.Line3DCollection` instances
            each containing an errorbar line.
        caplines : list
            List of `~mpl_toolkits.mplot3d.art3d.Line3D` instances each
            containing a capline object.
        limmarks : list
            List of `~mpl_toolkits.mplot3d.art3d.Line3D` instances each
            containing a marker with an upper or lower limit.

        Other Parameters
        ----------------
        data : indexable object, optional
            DATA_PARAMETER_PLACEHOLDER

        **kwargs
            All other keyword arguments for styling errorbar lines are passed
            `~mpl_toolkits.mplot3d.art3d.Line3DCollection`.

        Examples
        --------
        .. plot:: gallery/mplot3d/errorbar3d.py
        """
    def get_tightbbox(self, renderer: Incomplete | None = None, call_axes_locator: bool = True, bbox_extra_artists: Incomplete | None = None, *, for_layout_only: bool = False): ...
    def stem(self, x, y, z, *, linefmt: str = 'C0-', markerfmt: str = 'C0o', basefmt: str = 'C3-', bottom: int = 0, label: Incomplete | None = None, orientation: str = 'z'):
        """
        Create a 3D stem plot.

        A stem plot draws lines perpendicular to a baseline, and places markers
        at the heads. By default, the baseline is defined by *x* and *y*, and
        stems are drawn vertically from *bottom* to *z*.

        Parameters
        ----------
        x, y, z : array-like
            The positions of the heads of the stems. The stems are drawn along
            the *orientation*-direction from the baseline at *bottom* (in the
            *orientation*-coordinate) to the heads. By default, the *x* and *y*
            positions are used for the baseline and *z* for the head position,
            but this can be changed by *orientation*.

        linefmt : str, default: 'C0-'
            A string defining the properties of the vertical lines. Usually,
            this will be a color or a color and a linestyle:

            =========  =============
            Character  Line Style
            =========  =============
            ``'-'``    solid line
            ``'--'``   dashed line
            ``'-.'``   dash-dot line
            ``':'``    dotted line
            =========  =============

            Note: While it is technically possible to specify valid formats
            other than color or color and linestyle (e.g. 'rx' or '-.'), this
            is beyond the intention of the method and will most likely not
            result in a reasonable plot.

        markerfmt : str, default: 'C0o'
            A string defining the properties of the markers at the stem heads.

        basefmt : str, default: 'C3-'
            A format string defining the properties of the baseline.

        bottom : float, default: 0
            The position of the baseline, in *orientation*-coordinates.

        label : str, default: None
            The label to use for the stems in legends.

        orientation : {'x', 'y', 'z'}, default: 'z'
            The direction along which stems are drawn.

        data : indexable object, optional
            DATA_PARAMETER_PLACEHOLDER

        Returns
        -------
        `.StemContainer`
            The container may be treated like a tuple
            (*markerline*, *stemlines*, *baseline*)

        Examples
        --------
        .. plot:: gallery/mplot3d/stem3d_demo.py
        """
    stem3D = stem

def get_test_data(delta: float = 0.05):
    """Return a tuple X, Y, Z with a test data set."""
