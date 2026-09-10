import matplotlib.artist as martist
from _typeshed import Incomplete
from matplotlib import cbook as cbook

GRIDLINE_INTERPOLATION_STEPS: int

class Tick(martist.Artist):
    """
    Abstract base class for the axis ticks, grid lines and labels.

    Ticks mark a position on an Axis. They contain two lines as markers and
    two labels; one each for the bottom and top positions (in case of an
    `.XAxis`) or for the left and right positions (in case of a `.YAxis`).

    Attributes
    ----------
    tick1line : `~matplotlib.lines.Line2D`
        The left/bottom tick marker.
    tick2line : `~matplotlib.lines.Line2D`
        The right/top tick marker.
    gridline : `~matplotlib.lines.Line2D`
        The grid line associated with the label position.
    label1 : `~matplotlib.text.Text`
        The left/bottom tick label.
    label2 : `~matplotlib.text.Text`
        The right/top tick label.

    """
    axes: Incomplete
    tick1line: Incomplete
    tick2line: Incomplete
    gridline: Incomplete
    label1: Incomplete
    label2: Incomplete
    def __init__(self, axes, loc, *, size: Incomplete | None = None, width: Incomplete | None = None, color: Incomplete | None = None, tickdir: Incomplete | None = None, pad: Incomplete | None = None, labelsize: Incomplete | None = None, labelcolor: Incomplete | None = None, zorder: Incomplete | None = None, gridOn: Incomplete | None = None, tick1On: bool = True, tick2On: bool = True, label1On: bool = True, label2On: bool = False, major: bool = True, labelrotation: int = 0, grid_color: Incomplete | None = None, grid_linestyle: Incomplete | None = None, grid_linewidth: Incomplete | None = None, grid_alpha: Incomplete | None = None, **kwargs) -> None:
        """
        bbox is the Bound2D bounding box in display coords of the Axes
        loc is the tick location in data coords
        size is the tick size in points
        """
    @property
    def label(self): ...
    def get_tickdir(self): ...
    def get_tick_padding(self):
        """Get the length of the tick outside of the Axes."""
    def get_children(self): ...
    stale: bool
    def set_clip_path(self, clippath, transform: Incomplete | None = None) -> None: ...
    def get_pad_pixels(self): ...
    def contains(self, mouseevent):
        """
        Test whether the mouse event occurred in the Tick marks.

        This function always returns false.  It is more useful to test if the
        axis as a whole contains the mouse rather than the set of tick marks.
        """
    def set_pad(self, val) -> None:
        """
        Set the tick label pad in points

        Parameters
        ----------
        val : float
        """
    def get_pad(self):
        """Get the value of the tick label pad in points."""
    def get_loc(self):
        """Return the tick location (data coords) as a scalar."""
    def draw(self, renderer) -> None: ...
    def set_label1(self, s) -> None:
        """
        Set the label1 text.

        Parameters
        ----------
        s : str
        """
    set_label = set_label1
    def set_label2(self, s) -> None:
        """
        Set the label2 text.

        Parameters
        ----------
        s : str
        """
    def set_url(self, url) -> None:
        """
        Set the url of label1 and label2.

        Parameters
        ----------
        url : str
        """
    def get_view_interval(self) -> None:
        """
        Return the view limits ``(min, max)`` of the axis the tick belongs to.
        """
    def update_position(self, loc) -> None:
        """Set the location of tick in data coords with scalar *loc*."""

class XTick(Tick):
    """
    Contains all the Artists needed to make an x tick - the tick line,
    the label text and the grid line
    """
    def __init__(self, *args, **kwargs) -> None: ...
    stale: bool
    def update_position(self, loc) -> None:
        """Set the location of tick in data coords with scalar *loc*."""
    def get_view_interval(self): ...

class YTick(Tick):
    """
    Contains all the Artists needed to make a Y tick - the tick line,
    the label text and the grid line
    """
    def __init__(self, *args, **kwargs) -> None: ...
    stale: bool
    def update_position(self, loc) -> None:
        """Set the location of tick in data coords with scalar *loc*."""
    def get_view_interval(self): ...

class Ticker:
    """
    A container for the objects defining tick position and format.

    Attributes
    ----------
    locator : `~matplotlib.ticker.Locator` subclass
        Determines the positions of the ticks.
    formatter : `~matplotlib.ticker.Formatter` subclass
        Determines the format of the tick labels.
    """
    def __init__(self) -> None: ...
    @property
    def locator(self): ...
    @locator.setter
    def locator(self, locator) -> None: ...
    @property
    def formatter(self): ...
    @formatter.setter
    def formatter(self, formatter) -> None: ...

class _LazyTickList:
    """
    A descriptor for lazy instantiation of tick lists.

    See comment above definition of the ``majorTicks`` and ``minorTicks``
    attributes.
    """
    def __init__(self, major) -> None: ...
    def __get__(self, instance, cls): ...

class Axis(martist.Artist):
    """
    Base class for `.XAxis` and `.YAxis`.

    Attributes
    ----------
    isDefault_label : bool

    axes : `~matplotlib.axes.Axes`
        The `~.axes.Axes` to which the Axis belongs.
    major : `~matplotlib.axis.Ticker`
        Determines the major tick positions and their label format.
    minor : `~matplotlib.axis.Ticker`
        Determines the minor tick positions and their label format.
    callbacks : `~matplotlib.cbook.CallbackRegistry`

    label : `~matplotlib.text.Text`
        The axis label.
    labelpad : float
        The distance between the axis label and the tick labels.
        Defaults to :rc:`axes.labelpad` = 4.
    offsetText : `~matplotlib.text.Text`
        A `.Text` object containing the data offset of the ticks (if any).
    pickradius : float
        The acceptance radius for containment tests. See also `.Axis.contains`.
    majorTicks : list of `.Tick`
        The major ticks.
    minorTicks : list of `.Tick`
        The minor ticks.
    """
    OFFSETTEXTPAD: int
    isDefault_label: bool
    axes: Incomplete
    major: Incomplete
    minor: Incomplete
    callbacks: Incomplete
    label: Incomplete
    offsetText: Incomplete
    labelpad: Incomplete
    pickradius: Incomplete
    def __init__(self, axes, pickradius: int = 15) -> None:
        """
        Parameters
        ----------
        axes : `~matplotlib.axes.Axes`
            The `~.axes.Axes` to which the created Axis belongs.
        pickradius : float
            The acceptance radius for containment tests. See also
            `.Axis.contains`.
        """
    @property
    def isDefault_majloc(self): ...
    @isDefault_majloc.setter
    def isDefault_majloc(self, value) -> None: ...
    @property
    def isDefault_majfmt(self): ...
    @isDefault_majfmt.setter
    def isDefault_majfmt(self, value) -> None: ...
    @property
    def isDefault_minloc(self): ...
    @isDefault_minloc.setter
    def isDefault_minloc(self, value) -> None: ...
    @property
    def isDefault_minfmt(self): ...
    @isDefault_minfmt.setter
    def isDefault_minfmt(self, value) -> None: ...
    majorTicks: Incomplete
    minorTicks: Incomplete
    def get_remove_overlapping_locs(self): ...
    def set_remove_overlapping_locs(self, val) -> None: ...
    remove_overlapping_locs: Incomplete
    stale: bool
    def set_label_coords(self, x, y, transform: Incomplete | None = None) -> None:
        """
        Set the coordinates of the label.

        By default, the x coordinate of the y label and the y coordinate of the
        x label are determined by the tick label bounding boxes, but this can
        lead to poor alignment of multiple labels if there are multiple axes.

        You can also specify the coordinate system of the label with the
        transform.  If None, the default coordinate system will be the axes
        coordinate system: (0, 0) is bottom left, (0.5, 0.5) is center, etc.
        """
    def get_transform(self): ...
    def get_scale(self):
        """Return this Axis' scale (as a str)."""
    def limit_range_for_scale(self, vmin, vmax): ...
    def get_children(self): ...
    converter: Incomplete
    units: Incomplete
    def clear(self) -> None:
        """
        Clear the axis.

        This resets axis properties to their default values:

        - the label
        - the scale
        - locators, formatters and ticks
        - major and minor grid
        - units
        - registered callbacks
        """
    def reset_ticks(self) -> None:
        """
        Re-initialize the major and minor Tick lists.

        Each list starts with a single fresh Tick.
        """
    def set_tick_params(self, which: str = 'major', reset: bool = False, **kwargs) -> None:
        """
        Set appearance parameters for ticks, ticklabels, and gridlines.

        For documentation of keyword arguments, see
        :meth:`matplotlib.axes.Axes.tick_params`.

        See Also
        --------
        .Axis.get_tick_params
            View the current style settings for ticks, ticklabels, and
            gridlines.
        """
    def get_tick_params(self, which: str = 'major'):
        """
        Get appearance parameters for ticks, ticklabels, and gridlines.

        .. versionadded:: 3.7

        Parameters
        ----------
        which : {'major', 'minor'}, default: 'major'
            The group of ticks for which the parameters are retrieved.

        Returns
        -------
        dict
            Properties for styling tick elements added to the axis.

        Notes
        -----
        This method returns the appearance parameters for styling *new*
        elements added to this axis and may be different from the values
        on current elements if they were modified directly by the user
        (e.g., via ``set_*`` methods on individual tick objects).

        Examples
        --------
        ::

            >>> ax.yaxis.set_tick_params(labelsize=30, labelcolor='red',
                                         direction='out', which='major')
            >>> ax.yaxis.get_tick_params(which='major')
            {'direction': 'out',
            'left': True,
            'right': False,
            'labelleft': True,
            'labelright': False,
            'gridOn': False,
            'labelsize': 30,
            'labelcolor': 'red'}
            >>> ax.yaxis.get_tick_params(which='minor')
            {'left': True,
            'right': False,
            'labelleft': True,
            'labelright': False,
            'gridOn': False}


        """
    def set_clip_path(self, clippath, transform: Incomplete | None = None) -> None: ...
    def get_view_interval(self) -> None:
        """Return the ``(min, max)`` view limits of this axis."""
    def set_view_interval(self, vmin, vmax, ignore: bool = False) -> None:
        """
        Set the axis view limits.  This method is for internal use; Matplotlib
        users should typically use e.g. `~.Axes.set_xlim` or `~.Axes.set_ylim`.

        If *ignore* is False (the default), this method will never reduce the
        preexisting view limits, only expand them if *vmin* or *vmax* are not
        within them.  Moreover, the order of *vmin* and *vmax* does not matter;
        the orientation of the axis will not change.

        If *ignore* is True, the view limits will be set exactly to ``(vmin,
        vmax)`` in that order.
        """
    def get_data_interval(self) -> None:
        """Return the ``(min, max)`` data limits of this axis."""
    def set_data_interval(self, vmin, vmax, ignore: bool = False) -> None:
        """
        Set the axis data limits.  This method is for internal use.

        If *ignore* is False (the default), this method will never reduce the
        preexisting data limits, only expand them if *vmin* or *vmax* are not
        within them.  Moreover, the order of *vmin* and *vmax* does not matter;
        the orientation of the axis will not change.

        If *ignore* is True, the data limits will be set exactly to ``(vmin,
        vmax)`` in that order.
        """
    def get_inverted(self):
        '''
        Return whether this Axis is oriented in the "inverse" direction.

        The "normal" direction is increasing to the right for the x-axis and to
        the top for the y-axis; the "inverse" direction is increasing to the
        left for the x-axis and to the bottom for the y-axis.
        '''
    def set_inverted(self, inverted) -> None:
        '''
        Set whether this Axis is oriented in the "inverse" direction.

        The "normal" direction is increasing to the right for the x-axis and to
        the top for the y-axis; the "inverse" direction is increasing to the
        left for the x-axis and to the bottom for the y-axis.
        '''
    def set_default_intervals(self) -> None:
        """
        Set the default limits for the axis data and view interval if they
        have not been not mutated yet.
        """
    def get_ticklabel_extents(self, renderer):
        """Get the extents of the tick labels on either side of the axes."""
    def get_tightbbox(self, renderer: Incomplete | None = None, *, for_layout_only: bool = False):
        """
        Return a bounding box that encloses the axis. It only accounts
        tick labels, axis label, and offsetText.

        If *for_layout_only* is True, then the width of the label (if this
        is an x-axis) or the height of the label (if this is a y-axis) is
        collapsed to near zero.  This allows tight/constrained_layout to ignore
        too-long labels when doing their layout.
        """
    def get_tick_padding(self): ...
    def draw(self, renderer, *args, **kwargs) -> None: ...
    def get_gridlines(self):
        """Return this Axis' grid lines as a list of `.Line2D`\\s."""
    def get_label(self):
        """Return the axis label as a Text instance."""
    def get_offset_text(self):
        """Return the axis offsetText as a Text instance."""
    def get_pickradius(self):
        """Return the depth of the axis used by the picker."""
    def get_majorticklabels(self):
        """Return this Axis' major tick labels, as a list of `~.text.Text`."""
    def get_minorticklabels(self):
        """Return this Axis' minor tick labels, as a list of `~.text.Text`."""
    def get_ticklabels(self, minor: bool = False, which: Incomplete | None = None):
        """
        Get this Axis' tick labels.

        Parameters
        ----------
        minor : bool
           Whether to return the minor or the major ticklabels.

        which : None, ('minor', 'major', 'both')
           Overrides *minor*.

           Selects which ticklabels to return

        Returns
        -------
        list of `~matplotlib.text.Text`
        """
    def get_majorticklines(self):
        """Return this Axis' major tick lines as a list of `.Line2D`\\s."""
    def get_minorticklines(self):
        """Return this Axis' minor tick lines as a list of `.Line2D`\\s."""
    def get_ticklines(self, minor: bool = False):
        """Return this Axis' tick lines as a list of `.Line2D`\\s."""
    def get_majorticklocs(self):
        """Return this Axis' major tick locations in data coordinates."""
    def get_minorticklocs(self):
        """Return this Axis' minor tick locations in data coordinates."""
    def get_ticklocs(self, *, minor: bool = False):
        """
        Return this Axis' tick locations in data coordinates.

        The locations are not clipped to the current axis limits and hence
        may contain locations that are not visible in the output.

        Parameters
        ----------
        minor : bool, default: False
            True to return the minor tick directions,
            False to return the major tick directions.

        Returns
        -------
        numpy array of tick locations
        """
    def get_ticks_direction(self, minor: bool = False):
        """
        Get the tick directions as a numpy array

        Parameters
        ----------
        minor : bool, default: False
            True to return the minor tick directions,
            False to return the major tick directions.

        Returns
        -------
        numpy array of tick directions
        """
    def get_label_text(self):
        """Get the text of the label."""
    def get_major_locator(self):
        """Get the locator of the major ticker."""
    def get_minor_locator(self):
        """Get the locator of the minor ticker."""
    def get_major_formatter(self):
        """Get the formatter of the major ticker."""
    def get_minor_formatter(self):
        """Get the formatter of the minor ticker."""
    def get_major_ticks(self, numticks: Incomplete | None = None):
        """Return the list of major `.Tick`\\s."""
    def get_minor_ticks(self, numticks: Incomplete | None = None):
        """Return the list of minor `.Tick`\\s."""
    def grid(self, visible: Incomplete | None = None, which: str = 'major', **kwargs) -> None:
        """
        Configure the grid lines.

        Parameters
        ----------
        visible : bool or None
            Whether to show the grid lines.  If any *kwargs* are supplied, it
            is assumed you want the grid on and *visible* will be set to True.

            If *visible* is *None* and there are no *kwargs*, this toggles the
            visibility of the lines.

        which : {'major', 'minor', 'both'}
            The grid lines to apply the changes on.

        **kwargs : `~matplotlib.lines.Line2D` properties
            Define the line properties of the grid, e.g.::

                grid(color='r', linestyle='-', linewidth=2)
        """
    def update_units(self, data):
        """
        Introspect *data* for units converter and update the
        ``axis.converter`` instance if necessary. Return *True*
        if *data* is registered for unit conversion.
        """
    def have_units(self): ...
    def convert_units(self, x): ...
    def set_units(self, u) -> None:
        """
        Set the units for axis.

        Parameters
        ----------
        u : units tag

        Notes
        -----
        The units of any shared axis will also be updated.
        """
    def get_units(self):
        """Return the units for axis."""
    def set_label_text(self, label, fontdict: Incomplete | None = None, **kwargs):
        """
        Set the text value of the axis label.

        Parameters
        ----------
        label : str
            Text string.
        fontdict : dict
            Text properties.
        **kwargs
            Merged into fontdict.
        """
    def set_major_formatter(self, formatter) -> None:
        """
        Set the formatter of the major ticker.

        In addition to a `~matplotlib.ticker.Formatter` instance,
        this also accepts a ``str`` or function.

        For a ``str`` a `~matplotlib.ticker.StrMethodFormatter` is used.
        The field used for the value must be labeled ``'x'`` and the field used
        for the position must be labeled ``'pos'``.
        See the  `~matplotlib.ticker.StrMethodFormatter` documentation for
        more information.

        For a function, a `~matplotlib.ticker.FuncFormatter` is used.
        The function must take two inputs (a tick value ``x`` and a
        position ``pos``), and return a string containing the corresponding
        tick label.
        See the  `~matplotlib.ticker.FuncFormatter` documentation for
        more information.

        Parameters
        ----------
        formatter : `~matplotlib.ticker.Formatter`, ``str``, or function
        """
    def set_minor_formatter(self, formatter) -> None:
        """
        Set the formatter of the minor ticker.

        In addition to a `~matplotlib.ticker.Formatter` instance,
        this also accepts a ``str`` or function.
        See `.Axis.set_major_formatter` for more information.

        Parameters
        ----------
        formatter : `~matplotlib.ticker.Formatter`, ``str``, or function
        """
    def set_major_locator(self, locator) -> None:
        """
        Set the locator of the major ticker.

        Parameters
        ----------
        locator : `~matplotlib.ticker.Locator`
        """
    def set_minor_locator(self, locator) -> None:
        """
        Set the locator of the minor ticker.

        Parameters
        ----------
        locator : `~matplotlib.ticker.Locator`
        """
    def set_pickradius(self, pickradius) -> None:
        """
        Set the depth of the axis used by the picker.

        Parameters
        ----------
        pickradius : float
            The acceptance radius for containment tests.
            See also `.Axis.contains`.
        """
    def set_ticklabels(self, labels, *, minor: bool = False, fontdict: Incomplete | None = None, **kwargs):
        """
        [*Discouraged*] Set this Axis' tick labels with list of string labels.

        .. admonition:: Discouraged

            The use of this method is discouraged, because of the dependency on
            tick positions. In most cases, you'll want to use
            ``Axes.set_[x/y/z]ticks(positions, labels)`` or ``Axis.set_ticks``
            instead.

            If you are using this method, you should always fix the tick
            positions before, e.g. by using `.Axis.set_ticks` or by explicitly
            setting a `~.ticker.FixedLocator`. Otherwise, ticks are free to
            move and the labels may end up in unexpected positions.

        Parameters
        ----------
        labels : sequence of str or of `.Text`\\s
            Texts for labeling each tick location in the sequence set by
            `.Axis.set_ticks`; the number of labels must match the number of
            locations.

        minor : bool
            If True, set minor ticks instead of major ticks.

        fontdict : dict, optional
            A dictionary controlling the appearance of the ticklabels.
            The default *fontdict* is::

               {'fontsize': rcParams['axes.titlesize'],
                'fontweight': rcParams['axes.titleweight'],
                'verticalalignment': 'baseline',
                'horizontalalignment': loc}

        **kwargs
            Text properties.

        Returns
        -------
        list of `.Text`\\s
            For each tick, includes ``tick.label1`` if it is visible, then
            ``tick.label2`` if it is visible, in that order.
        """
    def set_ticks(self, ticks, labels: Incomplete | None = None, *, minor: bool = False, **kwargs):
        """
        Set this Axis' tick locations and optionally labels.

        If necessary, the view limits of the Axis are expanded so that all
        given ticks are visible.

        Parameters
        ----------
        ticks : list of floats
            List of tick locations.  The axis `.Locator` is replaced by a
            `~.ticker.FixedLocator`.

            Some tick formatters will not label arbitrary tick positions;
            e.g. log formatters only label decade ticks by default. In
            such a case you can set a formatter explicitly on the axis
            using `.Axis.set_major_formatter` or provide formatted
            *labels* yourself.
        labels : list of str, optional
            List of tick labels. If not set, the labels are generated with
            the axis tick `.Formatter`.
        minor : bool, default: False
            If ``False``, set the major ticks; if ``True``, the minor ticks.
        **kwargs
            `.Text` properties for the labels. These take effect only if you
            pass *labels*. In other cases, please use `~.Axes.tick_params`.

        Notes
        -----
        The mandatory expansion of the view limits is an intentional design
        choice to prevent the surprise of a non-visible tick. If you need
        other limits, you should set the limits explicitly after setting the
        ticks.
        """
    def axis_date(self, tz: Incomplete | None = None) -> None:
        """
        Set up axis ticks and labels to treat data along this Axis as dates.

        Parameters
        ----------
        tz : str or `datetime.tzinfo`, default: :rc:`timezone`
            The timezone used to create date labels.
        """
    def get_tick_space(self) -> None:
        """Return the estimated number of ticks that can fit on the axis."""
    def get_label_position(self):
        """
        Return the label position (top or bottom)
        """
    def set_label_position(self, position) -> None:
        """
        Set the label position (top or bottom)

        Parameters
        ----------
        position : {'top', 'bottom'}
        """
    def get_minpos(self) -> None: ...

class XAxis(Axis):
    axis_name: str
    def __init__(self, *args, **kwargs) -> None: ...
    def contains(self, mouseevent):
        """Test whether the mouse event occurred in the x-axis."""
    label_position: Incomplete
    stale: bool
    def set_label_position(self, position) -> None:
        """
        Set the label position (top or bottom)

        Parameters
        ----------
        position : {'top', 'bottom'}
        """
    def get_text_heights(self, renderer):
        """
        Return how much space should be reserved for text above and below the
        Axes, as a pair of floats.
        """
    def set_ticks_position(self, position) -> None:
        """
        Set the ticks position.

        Parameters
        ----------
        position : {'top', 'bottom', 'both', 'default', 'none'}
            'both' sets the ticks to appear on both positions, but does not
            change the tick labels.  'default' resets the tick positions to
            the default: ticks on both positions, labels at bottom.  'none'
            can be used if you don't want any ticks. 'none' and 'both'
            affect only the ticks, not the labels.
        """
    def tick_top(self) -> None:
        """
        Move ticks and ticklabels (if present) to the top of the Axes.
        """
    def tick_bottom(self) -> None:
        """
        Move ticks and ticklabels (if present) to the bottom of the Axes.
        """
    def get_ticks_position(self):
        '''
        Return the ticks position ("top", "bottom", "default", or "unknown").
        '''
    get_view_interval: Incomplete
    set_view_interval: Incomplete
    get_data_interval: Incomplete
    set_data_interval: Incomplete
    def get_minpos(self): ...
    def set_default_intervals(self) -> None: ...
    def get_tick_space(self): ...

class YAxis(Axis):
    axis_name: str
    def __init__(self, *args, **kwargs) -> None: ...
    def contains(self, mouseevent): ...
    label_position: Incomplete
    stale: bool
    def set_label_position(self, position) -> None:
        """
        Set the label position (left or right)

        Parameters
        ----------
        position : {'left', 'right'}
        """
    def set_offset_position(self, position) -> None:
        """
        Parameters
        ----------
        position : {'left', 'right'}
        """
    def get_text_widths(self, renderer): ...
    def set_ticks_position(self, position) -> None:
        """
        Set the ticks position.

        Parameters
        ----------
        position : {'left', 'right', 'both', 'default', 'none'}
            'both' sets the ticks to appear on both positions, but does not
            change the tick labels.  'default' resets the tick positions to
            the default: ticks on both positions, labels at left.  'none'
            can be used if you don't want any ticks. 'none' and 'both'
            affect only the ticks, not the labels.
        """
    def tick_right(self) -> None:
        """
        Move ticks and ticklabels (if present) to the right of the Axes.
        """
    def tick_left(self) -> None:
        """
        Move ticks and ticklabels (if present) to the left of the Axes.
        """
    def get_ticks_position(self):
        '''
        Return the ticks position ("left", "right", "default", or "unknown").
        '''
    get_view_interval: Incomplete
    set_view_interval: Incomplete
    get_data_interval: Incomplete
    set_data_interval: Incomplete
    def get_minpos(self): ...
    def set_default_intervals(self) -> None: ...
    def get_tick_space(self): ...
