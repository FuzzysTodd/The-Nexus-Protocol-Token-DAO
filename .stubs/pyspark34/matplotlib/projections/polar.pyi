import matplotlib.axis as maxis
import matplotlib.ticker as mticker
import matplotlib.transforms as mtransforms
from _typeshed import Incomplete
from matplotlib import cbook as cbook
from matplotlib.axes import Axes as Axes
from matplotlib.path import Path as Path
from matplotlib.spines import Spine as Spine

class PolarTransform(mtransforms.Transform):
    """
    The base polar transform.

    This transform maps polar coordinates :math:`\\theta, r` into Cartesian
    coordinates :math:`x, y = r \\cos(\\theta), r \\sin(\\theta)`
    (but does not fully transform into Axes coordinates or
    handle positioning in screen space).

    This transformation is designed to be applied to data after any scaling
    along the radial axis (e.g. log-scaling) has been applied to the input
    data.

    Path segments at a fixed radius are automatically transformed to circular
    arcs as long as ``path._interpolation_steps > 1``.
    """
    input_dims: int
    output_dims: int
    def __init__(self, axis: Incomplete | None = None, use_rmin: bool = True, _apply_theta_transforms: bool = True, *, scale_transform: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        axis : `~matplotlib.axis.Axis`, optional
            Axis associated with this transform. This is used to get the
            minimum radial limit.
        use_rmin : `bool`, optional
            If ``True``, subtract the minimum radial axis limit before
            transforming to Cartesian coordinates. *axis* must also be
            specified for this to take effect.
        """
    def transform_non_affine(self, tr): ...
    def transform_path_non_affine(self, path): ...
    def inverted(self): ...

class PolarAffine(mtransforms.Affine2DBase):
    """
    The affine part of the polar projection.

    Scales the output so that maximum radius rests on the edge of the axes
    circle and the origin is mapped to (0.5, 0.5). The transform applied is
    the same to x and y components and given by:

    .. math::

        x_{1} = 0.5 \\left [ \\frac{x_{0}}{(r_{\\max} - r_{\\min})} + 1 \\right ]

    :math:`r_{\\min}, r_{\\max}` are the minimum and maximum radial limits after
    any scaling (e.g. log scaling) has been removed.
    """
    def __init__(self, scale_transform, limits) -> None:
        """
        Parameters
        ----------
        scale_transform : `~matplotlib.transforms.Transform`
            Scaling transform for the data. This is used to remove any scaling
            from the radial view limits.
        limits : `~matplotlib.transforms.BboxBase`
            View limits of the data. The only part of its bounds that is used
            is the y limits (for the radius limits).
        """
    def get_matrix(self): ...

class InvertedPolarTransform(mtransforms.Transform):
    """
    The inverse of the polar transform, mapping Cartesian
    coordinate space *x* and *y* back to *theta* and *r*.
    """
    input_dims: int
    output_dims: int
    def __init__(self, axis: Incomplete | None = None, use_rmin: bool = True, _apply_theta_transforms: bool = True) -> None:
        """
        Parameters
        ----------
        axis : `~matplotlib.axis.Axis`, optional
            Axis associated with this transform. This is used to get the
            minimum radial limit.
        use_rmin : `bool`, optional
            If ``True`` add the minimum radial axis limit after
            transforming from Cartesian coordinates. *axis* must also be
            specified for this to take effect.
        """
    def transform_non_affine(self, xy): ...
    def inverted(self): ...

class ThetaFormatter(mticker.Formatter):
    """
    Used to format the *theta* tick labels.  Converts the native
    unit of radians into degrees and adds a degree symbol.
    """
    def __call__(self, x, pos: Incomplete | None = None): ...

class _AxisWrapper:
    def __init__(self, axis) -> None: ...
    def get_view_interval(self): ...
    def set_view_interval(self, vmin, vmax) -> None: ...
    def get_minpos(self): ...
    def get_data_interval(self): ...
    def set_data_interval(self, vmin, vmax) -> None: ...
    def get_tick_space(self): ...

class ThetaLocator(mticker.Locator):
    """
    Used to locate theta ticks.

    This will work the same as the base locator except in the case that the
    view spans the entire circle. In such cases, the previously used default
    locations of every 45 degrees are returned.
    """
    base: Incomplete
    axis: Incomplete
    def __init__(self, base) -> None: ...
    def set_axis(self, axis) -> None: ...
    def __call__(self): ...
    def view_limits(self, vmin, vmax): ...

class ThetaTick(maxis.XTick):
    """
    A theta-axis tick.

    This subclass of `.XTick` provides angular ticks with some small
    modification to their re-positioning such that ticks are rotated based on
    tick location. This results in ticks that are correctly perpendicular to
    the arc spine.

    When 'auto' rotation is enabled, labels are also rotated to be parallel to
    the spine. The label padding is also applied here since it's not possible
    to use a generic axes transform to produce tick-specific padding.
    """
    def __init__(self, axes, *args, **kwargs) -> None: ...
    def update_position(self, loc) -> None: ...

class ThetaAxis(maxis.XAxis):
    """
    A theta Axis.

    This overrides certain properties of an `.XAxis` to provide special-casing
    for an angular axis.
    """
    axis_name: str
    def clear(self) -> None: ...

class RadialLocator(mticker.Locator):
    """
    Used to locate radius ticks.

    Ensures that all ticks are strictly positive.  For all other tasks, it
    delegates to the base `.Locator` (which may be different depending on the
    scale of the *r*-axis).
    """
    base: Incomplete
    def __init__(self, base, axes: Incomplete | None = None) -> None: ...
    def set_axis(self, axis) -> None: ...
    def __call__(self): ...
    def nonsingular(self, vmin, vmax): ...
    def view_limits(self, vmin, vmax): ...

class _ThetaShift(mtransforms.ScaledTranslation):
    """
    Apply a padding shift based on axes theta limits.

    This is used to create padding for radial ticks.

    Parameters
    ----------
    axes : `~matplotlib.axes.Axes`
        The owning axes; used to determine limits.
    pad : float
        The padding to apply, in points.
    mode : {'min', 'max', 'rlabel'}
        Whether to shift away from the start (``'min'``) or the end (``'max'``)
        of the axes, or using the rlabel position (``'rlabel'``).
    """
    axes: Incomplete
    mode: Incomplete
    pad: Incomplete
    def __init__(self, axes, pad, mode) -> None: ...
    def get_matrix(self): ...

class RadialTick(maxis.YTick):
    """
    A radial-axis tick.

    This subclass of `.YTick` provides radial ticks with some small
    modification to their re-positioning such that ticks are rotated based on
    axes limits.  This results in ticks that are correctly perpendicular to
    the spine. Labels are also rotated to be perpendicular to the spine, when
    'auto' rotation is enabled.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def update_position(self, loc) -> None: ...

class RadialAxis(maxis.YAxis):
    """
    A radial Axis.

    This overrides certain properties of a `.YAxis` to provide special-casing
    for a radial axis.
    """
    axis_name: str
    def __init__(self, *args, **kwargs) -> None: ...
    def clear(self) -> None: ...

class _WedgeBbox(mtransforms.Bbox):
    """
    Transform (theta, r) wedge Bbox into axes bounding box.

    Parameters
    ----------
    center : (float, float)
        Center of the wedge
    viewLim : `~matplotlib.transforms.Bbox`
        Bbox determining the boundaries of the wedge
    originLim : `~matplotlib.transforms.Bbox`
        Bbox determining the origin for the wedge, if different from *viewLim*
    """
    def __init__(self, center, viewLim, originLim, **kwargs) -> None: ...
    def get_points(self): ...

class PolarAxes(Axes):
    """
    A polar graph projection, where the input dimensions are *theta*, *r*.

    Theta starts pointing east and goes anti-clockwise.
    """
    name: str
    use_sticky_edges: bool
    def __init__(self, *args, theta_offset: int = 0, theta_direction: int = 1, rlabel_position: float = 22.5, **kwargs) -> None: ...
    def clear(self) -> None: ...
    def get_xaxis_transform(self, which: str = 'grid'): ...
    def get_xaxis_text1_transform(self, pad): ...
    def get_xaxis_text2_transform(self, pad): ...
    def get_yaxis_transform(self, which: str = 'grid'): ...
    def get_yaxis_text1_transform(self, pad): ...
    def get_yaxis_text2_transform(self, pad): ...
    def draw(self, renderer) -> None: ...
    def set_thetamax(self, thetamax) -> None:
        """Set the maximum theta limit in degrees."""
    def get_thetamax(self):
        """Return the maximum theta limit in degrees."""
    def set_thetamin(self, thetamin) -> None:
        """Set the minimum theta limit in degrees."""
    def get_thetamin(self):
        """Get the minimum theta limit in degrees."""
    def set_thetalim(self, *args, **kwargs):
        """
        Set the minimum and maximum theta values.

        Can take the following signatures:

        - ``set_thetalim(minval, maxval)``: Set the limits in radians.
        - ``set_thetalim(thetamin=minval, thetamax=maxval)``: Set the limits
          in degrees.

        where minval and maxval are the minimum and maximum limits. Values are
        wrapped in to the range :math:`[0, 2\\pi]` (in radians), so for example
        it is possible to do ``set_thetalim(-np.pi / 2, np.pi / 2)`` to have
        an axis symmetric around 0. A ValueError is raised if the absolute
        angle difference is larger than a full circle.
        """
    def set_theta_offset(self, offset) -> None:
        """
        Set the offset for the location of 0 in radians.
        """
    def get_theta_offset(self):
        """
        Get the offset for the location of 0 in radians.
        """
    def set_theta_zero_location(self, loc, offset: float = 0.0):
        '''
        Set the location of theta\'s zero.

        This simply calls `set_theta_offset` with the correct value in radians.

        Parameters
        ----------
        loc : str
            May be one of "N", "NW", "W", "SW", "S", "SE", "E", or "NE".
        offset : float, default: 0
            An offset in degrees to apply from the specified *loc*. **Note:**
            this offset is *always* applied counter-clockwise regardless of
            the direction setting.
        '''
    def set_theta_direction(self, direction) -> None:
        """
        Set the direction in which theta increases.

        clockwise, -1:
           Theta increases in the clockwise direction

        counterclockwise, anticlockwise, 1:
           Theta increases in the counterclockwise direction
        """
    def get_theta_direction(self):
        """
        Get the direction in which theta increases.

        -1:
           Theta increases in the clockwise direction

        1:
           Theta increases in the counterclockwise direction
        """
    def set_rmax(self, rmax) -> None:
        """
        Set the outer radial limit.

        Parameters
        ----------
        rmax : float
        """
    def get_rmax(self):
        """
        Returns
        -------
        float
            Outer radial limit.
        """
    def set_rmin(self, rmin) -> None:
        """
        Set the inner radial limit.

        Parameters
        ----------
        rmin : float
        """
    def get_rmin(self):
        """
        Returns
        -------
        float
            The inner radial limit.
        """
    def set_rorigin(self, rorigin) -> None:
        """
        Update the radial origin.

        Parameters
        ----------
        rorigin : float
        """
    def get_rorigin(self):
        """
        Returns
        -------
        float
        """
    def get_rsign(self): ...
    def set_rlim(self, bottom: Incomplete | None = None, top: Incomplete | None = None, emit: bool = True, auto: bool = False, **kwargs):
        """
        Set the radial axis view limits.

        This function behaves like `.Axes.set_ylim`, but additionally supports
        *rmin* and *rmax* as aliases for *bottom* and *top*.

        See Also
        --------
        .Axes.set_ylim
        """
    def get_rlabel_position(self):
        """
        Returns
        -------
        float
            The theta position of the radius labels in degrees.
        """
    def set_rlabel_position(self, value) -> None:
        """
        Update the theta position of the radius labels.

        Parameters
        ----------
        value : number
            The angular position of the radius labels in degrees.
        """
    def set_yscale(self, *args, **kwargs) -> None: ...
    def set_rscale(self, *args, **kwargs): ...
    def set_rticks(self, *args, **kwargs): ...
    def set_thetagrids(self, angles, labels: Incomplete | None = None, fmt: Incomplete | None = None, **kwargs):
        """
        Set the theta gridlines in a polar plot.

        Parameters
        ----------
        angles : tuple with floats, degrees
            The angles of the theta gridlines.

        labels : tuple with strings or None
            The labels to use at each theta gridline. The
            `.projections.polar.ThetaFormatter` will be used if None.

        fmt : str or None
            Format string used in `matplotlib.ticker.FormatStrFormatter`.
            For example '%f'. Note that the angle that is used is in
            radians.

        Returns
        -------
        lines : list of `.lines.Line2D`
            The theta gridlines.

        labels : list of `.text.Text`
            The tick labels.

        Other Parameters
        ----------------
        **kwargs
            *kwargs* are optional `.Text` properties for the labels.

        See Also
        --------
        .PolarAxes.set_rgrids
        .Axis.get_gridlines
        .Axis.get_ticklabels
        """
    def set_rgrids(self, radii, labels: Incomplete | None = None, angle: Incomplete | None = None, fmt: Incomplete | None = None, **kwargs):
        """
        Set the radial gridlines on a polar plot.

        Parameters
        ----------
        radii : tuple with floats
            The radii for the radial gridlines

        labels : tuple with strings or None
            The labels to use at each radial gridline. The
            `matplotlib.ticker.ScalarFormatter` will be used if None.

        angle : float
            The angular position of the radius labels in degrees.

        fmt : str or None
            Format string used in `matplotlib.ticker.FormatStrFormatter`.
            For example '%f'.

        Returns
        -------
        lines : list of `.lines.Line2D`
            The radial gridlines.

        labels : list of `.text.Text`
            The tick labels.

        Other Parameters
        ----------------
        **kwargs
            *kwargs* are optional `.Text` properties for the labels.

        See Also
        --------
        .PolarAxes.set_thetagrids
        .Axis.get_gridlines
        .Axis.get_ticklabels
        """
    def format_coord(self, theta, r): ...
    def get_data_ratio(self):
        """
        Return the aspect ratio of the data itself.  For a polar plot,
        this should always be 1.0
        """
    def can_zoom(self):
        """
        Return whether this Axes supports the zoom box button functionality.

        A polar Axes does not support zoom boxes.
        """
    def can_pan(self):
        """
        Return whether this Axes supports the pan/zoom button functionality.

        For a polar Axes, this is slightly misleading. Both panning and
        zooming are performed by the same button. Panning is performed
        in azimuth while zooming is done along the radial.
        """
    def start_pan(self, x, y, button) -> None: ...
    def end_pan(self) -> None: ...
    def drag_pan(self, button, key, x, y) -> None: ...
