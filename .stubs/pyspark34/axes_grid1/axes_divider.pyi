from _typeshed import Incomplete

class Divider:
    """
    An Axes positioning class.

    The divider is initialized with lists of horizontal and vertical sizes
    (:mod:`mpl_toolkits.axes_grid1.axes_size`) based on which a given
    rectangular area will be divided.

    The `new_locator` method then creates a callable object
    that can be used as the *axes_locator* of the axes.
    """
    def __init__(self, fig, pos, horizontal, vertical, aspect: Incomplete | None = None, anchor: str = 'C') -> None:
        """
        Parameters
        ----------
        fig : Figure
        pos : tuple of 4 floats
            Position of the rectangle that will be divided.
        horizontal : list of :mod:`~mpl_toolkits.axes_grid1.axes_size`
            Sizes for horizontal division.
        vertical : list of :mod:`~mpl_toolkits.axes_grid1.axes_size`
            Sizes for vertical division.
        aspect : bool
            Whether overall rectangular area is reduced so that the relative
            part of the horizontal and vertical scales have the same scale.
        anchor : (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', 'N', 'NW', 'W'}
            Placement of the reduced rectangle, when *aspect* is True.
        """
    def get_horizontal_sizes(self, renderer): ...
    def get_vertical_sizes(self, renderer): ...
    def set_position(self, pos) -> None:
        """
        Set the position of the rectangle.

        Parameters
        ----------
        pos : tuple of 4 floats
            position of the rectangle that will be divided
        """
    def get_position(self):
        """Return the position of the rectangle."""
    def set_anchor(self, anchor) -> None:
        """
        Parameters
        ----------
        anchor : (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', 'N', 'NW', 'W'}
            Either an (*x*, *y*) pair of relative coordinates (0 is left or
            bottom, 1 is right or top), 'C' (center), or a cardinal direction
            ('SW', southwest, is bottom left, etc.).

        See Also
        --------
        .Axes.set_anchor
        """
    def get_anchor(self):
        """Return the anchor."""
    def set_horizontal(self, h) -> None:
        """
        Parameters
        ----------
        h : list of :mod:`~mpl_toolkits.axes_grid1.axes_size`
            sizes for horizontal division
        """
    def get_horizontal(self):
        """Return horizontal sizes."""
    def set_vertical(self, v) -> None:
        """
        Parameters
        ----------
        v : list of :mod:`~mpl_toolkits.axes_grid1.axes_size`
            sizes for vertical division
        """
    def get_vertical(self):
        """Return vertical sizes."""
    def set_aspect(self, aspect: bool = False) -> None:
        """
        Parameters
        ----------
        aspect : bool
        """
    def get_aspect(self):
        """Return aspect."""
    def set_locator(self, _locator) -> None: ...
    def get_locator(self): ...
    def get_position_runtime(self, ax, renderer): ...
    def locate(self, nx, ny, nx1: Incomplete | None = None, ny1: Incomplete | None = None, axes: Incomplete | None = None, renderer: Incomplete | None = None):
        """
        Parameters
        ----------
        nx, nx1 : int
            Integers specifying the column-position of the cell. When *nx1* is
            None, a single *nx*-th column is specified. Otherwise, the
            location of columns spanning between *nx* to *nx1* (but excluding
            *nx1*-th column) is specified.
        ny, ny1 : int
            Same as *nx* and *nx1*, but for row positions.
        axes
        renderer
        """
    def new_locator(self, nx, ny, nx1: Incomplete | None = None, ny1: Incomplete | None = None):
        """
        Return a new `.AxesLocator` for the specified cell.

        Parameters
        ----------
        nx, nx1 : int
            Integers specifying the column-position of the
            cell. When *nx1* is None, a single *nx*-th column is
            specified. Otherwise, location of columns spanning between *nx*
            to *nx1* (but excluding *nx1*-th column) is specified.
        ny, ny1 : int
            Same as *nx* and *nx1*, but for row positions.
        """
    def append_size(self, position, size) -> None: ...
    def add_auto_adjustable_area(self, use_axes, pad: float = 0.1, adjust_dirs: Incomplete | None = None) -> None:
        '''
        Add auto-adjustable padding around *use_axes* to take their decorations
        (title, labels, ticks, ticklabels) into account during layout.

        Parameters
        ----------
        use_axes : `~matplotlib.axes.Axes` or list of `~matplotlib.axes.Axes`
            The Axes whose decorations are taken into account.
        pad : float, optional
            Additional padding in inches.
        adjust_dirs : list of {"left", "right", "bottom", "top"}, optional
            The sides where padding is added; defaults to all four sides.
        '''

class AxesLocator:
    """
    A callable object which returns the position and size of a given
    `.AxesDivider` cell.
    """
    def __init__(self, axes_divider, nx, ny, nx1: Incomplete | None = None, ny1: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        axes_divider : `~mpl_toolkits.axes_grid1.axes_divider.AxesDivider`
        nx, nx1 : int
            Integers specifying the column-position of the
            cell. When *nx1* is None, a single *nx*-th column is
            specified. Otherwise, location of columns spanning between *nx*
            to *nx1* (but excluding *nx1*-th column) is specified.
        ny, ny1 : int
            Same as *nx* and *nx1*, but for row positions.
        """
    def __call__(self, axes, renderer): ...
    def get_subplotspec(self): ...

class SubplotDivider(Divider):
    """
    The Divider class whose rectangle area is specified as a subplot geometry.
    """
    figure: Incomplete
    def __init__(self, fig, *args, horizontal: Incomplete | None = None, vertical: Incomplete | None = None, aspect: Incomplete | None = None, anchor: str = 'C') -> None:
        """
        Parameters
        ----------
        fig : `~matplotlib.figure.Figure`

        *args : tuple (*nrows*, *ncols*, *index*) or int
            The array of subplots in the figure has dimensions ``(nrows,
            ncols)``, and *index* is the index of the subplot being created.
            *index* starts at 1 in the upper left corner and increases to the
            right.

            If *nrows*, *ncols*, and *index* are all single digit numbers, then
            *args* can be passed as a single 3-digit number (e.g. 234 for
            (2, 3, 4)).
        """
    def get_position(self):
        """Return the bounds of the subplot box."""
    def get_subplotspec(self):
        """Get the SubplotSpec instance."""
    def set_subplotspec(self, subplotspec) -> None:
        """Set the SubplotSpec instance."""

class AxesDivider(Divider):
    """
    Divider based on the preexisting axes.
    """
    def __init__(self, axes, xref: Incomplete | None = None, yref: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        axes : :class:`~matplotlib.axes.Axes`
        xref
        yref
        """
    def new_horizontal(self, size, pad: Incomplete | None = None, pack_start: bool = False, **kwargs):
        '''
        Helper method for ``append_axes("left")`` and ``append_axes("right")``.

        See the documentation of `append_axes` for more details.

        :meta private:
        '''
    def new_vertical(self, size, pad: Incomplete | None = None, pack_start: bool = False, **kwargs):
        '''
        Helper method for ``append_axes("top")`` and ``append_axes("bottom")``.

        See the documentation of `append_axes` for more details.

        :meta private:
        '''
    def append_axes(self, position, size, pad: Incomplete | None = None, *, axes_class: Incomplete | None = None, **kwargs):
        '''
        Add a new axes on a given side of the main axes.

        Parameters
        ----------
        position : {"left", "right", "bottom", "top"}
            Where the new axes is positioned relative to the main axes.
        size : :mod:`~mpl_toolkits.axes_grid1.axes_size` or float or str
            The axes width or height.  float or str arguments are interpreted
            as ``axes_size.from_any(size, AxesX(<main_axes>))`` for left or
            right axes, and likewise with ``AxesY`` for bottom or top axes.
        pad : :mod:`~mpl_toolkits.axes_grid1.axes_size` or float or str
            Padding between the axes.  float or str arguments are interpreted
            as for *size*.  Defaults to :rc:`figure.subplot.wspace` times the
            main Axes width (left or right axes) or :rc:`figure.subplot.hspace`
            times the main Axes height (bottom or top axes).
        axes_class : subclass type of `~.axes.Axes`, optional
            The type of the new axes.  Defaults to the type of the main axes.
        **kwargs
            All extra keywords arguments are passed to the created axes.
        '''
    def get_aspect(self): ...
    def get_position(self): ...
    def get_anchor(self): ...
    def get_subplotspec(self): ...

class HBoxDivider(SubplotDivider):
    """
    A `.SubplotDivider` for laying out axes horizontally, while ensuring that
    they have equal heights.

    Examples
    --------
    .. plot:: gallery/axes_grid1/demo_axes_hbox_divider.py
    """
    def new_locator(self, nx, nx1: Incomplete | None = None):
        """
        Create a new `.AxesLocator` for the specified cell.

        Parameters
        ----------
        nx, nx1 : int
            Integers specifying the column-position of the
            cell. When *nx1* is None, a single *nx*-th column is
            specified. Otherwise, location of columns spanning between *nx*
            to *nx1* (but excluding *nx1*-th column) is specified.
        """
    def locate(self, nx, ny, nx1: Incomplete | None = None, ny1: Incomplete | None = None, axes: Incomplete | None = None, renderer: Incomplete | None = None): ...

class VBoxDivider(SubplotDivider):
    """
    A `.SubplotDivider` for laying out axes vertically, while ensuring that
    they have equal widths.
    """
    def new_locator(self, ny, ny1: Incomplete | None = None):
        """
        Create a new `.AxesLocator` for the specified cell.

        Parameters
        ----------
        ny, ny1 : int
            Integers specifying the row-position of the
            cell. When *ny1* is None, a single *ny*-th row is
            specified. Otherwise, location of rows spanning between *ny*
            to *ny1* (but excluding *ny1*-th row) is specified.
        """
    def locate(self, nx, ny, nx1: Incomplete | None = None, ny1: Incomplete | None = None, axes: Incomplete | None = None, renderer: Incomplete | None = None): ...

def make_axes_locatable(axes): ...
def make_axes_area_auto_adjustable(ax, use_axes: Incomplete | None = None, pad: float = 0.1, adjust_dirs: Incomplete | None = None) -> None:
    """
    Add auto-adjustable padding around *ax* to take its decorations (title,
    labels, ticks, ticklabels) into account during layout, using
    `.Divider.add_auto_adjustable_area`.

    By default, padding is determined from the decorations of *ax*.
    Pass *use_axes* to consider the decorations of other Axes instead.
    """
