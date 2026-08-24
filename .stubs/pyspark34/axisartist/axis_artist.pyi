import matplotlib.artist as martist
import matplotlib.text as mtext
from .axisline_style import AxislineStyle as AxislineStyle
from _typeshed import Incomplete
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D

class AttributeCopier:
    def get_ref_artist(self) -> None:
        """
        Return the underlying artist that actually defines some properties
        (e.g., color) of this artist.
        """
    def get_attribute_from_ref_artist(self, attr_name): ...

class Ticks(AttributeCopier, Line2D):
    """
    Ticks are derived from `.Line2D`, and note that ticks themselves
    are markers. Thus, you should use set_mec, set_mew, etc.

    To change the tick size (length), you need to use
    `set_ticksize`. To change the direction of the ticks (ticks are
    in opposite direction of ticklabels by default), use
    ``set_tick_out(False)``
    """
    locs_angles_labels: Incomplete
    def __init__(self, ticksize, tick_out: bool = False, *, axis: Incomplete | None = None, **kwargs) -> None: ...
    def get_ref_artist(self): ...
    stale: bool
    def set_color(self, color) -> None: ...
    def get_color(self): ...
    def get_markeredgecolor(self): ...
    def get_markeredgewidth(self): ...
    def set_tick_out(self, b) -> None:
        """Set whether ticks are drawn inside or outside the axes."""
    def get_tick_out(self):
        """Return whether ticks are drawn inside or outside the axes."""
    def set_ticksize(self, ticksize) -> None:
        """Set length of the ticks in points."""
    def get_ticksize(self):
        """Return length of the ticks in points."""
    locs_angles: Incomplete
    def set_locs_angles(self, locs_angles) -> None: ...
    def draw(self, renderer) -> None: ...

class LabelBase(mtext.Text):
    """
    A base class for `.AxisLabel` and `.TickLabels`. The position and
    angle of the text are calculated by the offset_ref_angle,
    text_ref_angle, and offset_radius attributes.
    """
    locs_angles_labels: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def draw(self, renderer) -> None: ...
    def get_window_extent(self, renderer: Incomplete | None = None): ...

class AxisLabel(AttributeCopier, LabelBase):
    """
    Axis label. Derived from `.Text`. The position of the text is updated
    in the fly, so changing text position has no effect. Otherwise, the
    properties can be changed as a normal `.Text`.

    To change the pad between tick labels and axis label, use `set_pad`.
    """
    def __init__(self, *args, axis_direction: str = 'bottom', axis: Incomplete | None = None, **kwargs) -> None: ...
    def set_pad(self, pad) -> None:
        """
        Set the internal pad in points.

        The actual pad will be the sum of the internal pad and the
        external pad (the latter is set automatically by the `.AxisArtist`).

        Parameters
        ----------
        pad : float
            The internal pad in points.
        """
    def get_pad(self):
        """
        Return the internal pad in points.

        See `.set_pad` for more details.
        """
    def get_ref_artist(self): ...
    def get_text(self): ...
    def set_default_alignment(self, d) -> None:
        '''
        Set the default alignment. See `set_axis_direction` for details.

        Parameters
        ----------
        d : {"left", "bottom", "right", "top"}
        '''
    def set_default_angle(self, d) -> None:
        '''
        Set the default angle. See `set_axis_direction` for details.

        Parameters
        ----------
        d : {"left", "bottom", "right", "top"}
        '''
    def set_axis_direction(self, d) -> None:
        '''
        Adjust the text angle and text alignment of axis label
        according to the matplotlib convention.

        =====================    ========== ========= ========== ==========
        Property                 left       bottom    right      top
        =====================    ========== ========= ========== ==========
        axislabel angle          180        0         0          180
        axislabel va             center     top       center     bottom
        axislabel ha             right      center    right      center
        =====================    ========== ========= ========== ==========

        Note that the text angles are actually relative to (90 + angle
        of the direction to the ticklabel), which gives 0 for bottom
        axis.

        Parameters
        ----------
        d : {"left", "bottom", "right", "top"}
        '''
    def get_color(self): ...
    def draw(self, renderer) -> None: ...
    def get_window_extent(self, renderer: Incomplete | None = None): ...

class TickLabels(AxisLabel):
    """
    Tick labels. While derived from `.Text`, this single artist draws all
    ticklabels. As in `.AxisLabel`, the position of the text is updated
    in the fly, so changing text position has no effect. Otherwise,
    the properties can be changed as a normal `.Text`. Unlike the
    ticklabels of the mainline Matplotlib, properties of a single
    ticklabel alone cannot be modified.

    To change the pad between ticks and ticklabels, use `~.AxisLabel.set_pad`.
    """
    def __init__(self, *, axis_direction: str = 'bottom', **kwargs) -> None: ...
    def get_ref_artist(self): ...
    def set_axis_direction(self, label_direction) -> None:
        '''
        Adjust the text angle and text alignment of ticklabels
        according to the Matplotlib convention.

        The *label_direction* must be one of [left, right, bottom, top].

        =====================    ========== ========= ========== ==========
        Property                 left       bottom    right      top
        =====================    ========== ========= ========== ==========
        ticklabel angle          90         0         -90        180
        ticklabel va             center     baseline  center     baseline
        ticklabel ha             right      center    right      center
        =====================    ========== ========= ========== ==========

        Note that the text angles are actually relative to (90 + angle
        of the direction to the ticklabel), which gives 0 for bottom
        axis.

        Parameters
        ----------
        label_direction : {"left", "bottom", "right", "top"}

        '''
    def invert_axis_direction(self) -> None: ...
    def draw(self, renderer) -> None: ...
    def set_locs_angles_labels(self, locs_angles_labels) -> None: ...
    def get_window_extents(self, renderer: Incomplete | None = None): ...
    def get_texts_widths_heights_descents(self, renderer):
        """
        Return a list of ``(width, height, descent)`` tuples for ticklabels.

        Empty labels are left out.
        """

class GridlinesCollection(LineCollection):
    def __init__(self, *args, which: str = 'major', axis: str = 'both', **kwargs) -> None:
        '''
        Collection of grid lines.

        Parameters
        ----------
        which : {"major", "minor"}
           Which grid to consider.
        axis : {"both", "x", "y"}
           Which axis to consider.
        *args, **kwargs :
           Passed to `.LineCollection`.
        '''
    def set_which(self, which) -> None:
        '''
        Select major or minor grid lines.

        Parameters
        ----------
        which : {"major", "minor"}
        '''
    def set_axis(self, axis) -> None:
        '''
        Select axis.

        Parameters
        ----------
        axis : {"both", "x", "y"}
        '''
    def set_grid_helper(self, grid_helper) -> None:
        """
        Set grid helper.

        Parameters
        ----------
        grid_helper : `.GridHelperBase` subclass
        """
    def draw(self, renderer) -> None: ...

class AxisArtist(martist.Artist):
    """
    An artist which draws axis (a line along which the n-th axes coord
    is constant) line, ticks, tick labels, and axis label.
    """
    zorder: float
    @property
    def LABELPAD(self): ...
    @LABELPAD.setter
    def LABELPAD(self, v) -> None: ...
    axes: Incomplete
    offset_transform: Incomplete
    axis: Incomplete
    def __init__(self, axes, helper, offset: Incomplete | None = None, axis_direction: str = 'bottom', **kwargs) -> None:
        """
        Parameters
        ----------
        axes : `mpl_toolkits.axisartist.axislines.Axes`
        helper : `~mpl_toolkits.axisartist.axislines.AxisArtistHelper`
        """
    def set_axis_direction(self, axis_direction) -> None:
        '''
        Adjust the direction, text angle, and text alignment of tick labels
        and axis labels following the Matplotlib convention for the rectangle
        axes.

        The *axis_direction* must be one of [left, right, bottom, top].

        =====================    ========== ========= ========== ==========
        Property                 left       bottom    right      top
        =====================    ========== ========= ========== ==========
        ticklabel direction      "-"        "+"       "+"        "-"
        axislabel direction      "-"        "+"       "+"        "-"
        ticklabel angle          90         0         -90        180
        ticklabel va             center     baseline  center     baseline
        ticklabel ha             right      center    right      center
        axislabel angle          180        0         0          180
        axislabel va             center     top       center     bottom
        axislabel ha             right      center    right      center
        =====================    ========== ========= ========== ==========

        Note that the direction "+" and "-" are relative to the direction of
        the increasing coordinate. Also, the text angles are actually
        relative to (90 + angle of the direction to the ticklabel),
        which gives 0 for bottom axis.

        Parameters
        ----------
        axis_direction : {"left", "bottom", "right", "top"}
        '''
    def set_ticklabel_direction(self, tick_direction) -> None:
        '''
        Adjust the direction of the tick labels.

        Note that the *tick_direction*\\s \'+\' and \'-\' are relative to the
        direction of the increasing coordinate.

        Parameters
        ----------
        tick_direction : {"+", "-"}
        '''
    def invert_ticklabel_direction(self) -> None: ...
    def set_axislabel_direction(self, label_direction) -> None:
        '''
        Adjust the direction of the axis label.

        Note that the *label_direction*\\s \'+\' and \'-\' are relative to the
        direction of the increasing coordinate.

        Parameters
        ----------
        label_direction : {"+", "-"}
        '''
    def get_transform(self): ...
    def get_helper(self):
        """
        Return axis artist helper instance.
        """
    def set_axisline_style(self, axisline_style: Incomplete | None = None, **kwargs):
        '''
        Set the axisline style.

        The new style is completely defined by the passed attributes. Existing
        style attributes are forgotten.

        Parameters
        ----------
        axisline_style : str or None
            The line style, e.g. \'->\', optionally followed by a comma-separated
            list of attributes. Alternatively, the attributes can be provided
            as keywords.

            If *None* this returns a string containing the available styles.

        Examples
        --------
        The following two commands are equal:

        >>> set_axisline_style("->,size=1.5")
        >>> set_axisline_style("->", size=1.5)
        '''
    def get_axisline_style(self):
        """Return the current axisline style."""
    def set_label(self, s) -> None: ...
    def get_tightbbox(self, renderer: Incomplete | None = None): ...
    def draw(self, renderer) -> None: ...
    def toggle(self, all: Incomplete | None = None, ticks: Incomplete | None = None, ticklabels: Incomplete | None = None, label: Incomplete | None = None) -> None:
        """
        Toggle visibility of ticks, ticklabels, and (axis) label.
        To turn all off, ::

          axis.toggle(all=False)

        To turn all off but ticks on ::

          axis.toggle(all=False, ticks=True)

        To turn all on but (axis) label off ::

          axis.toggle(all=True, label=False)

        """
