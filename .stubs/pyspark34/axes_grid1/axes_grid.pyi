from .axes_divider import Divider as Divider, Size as Size, SubplotDivider as SubplotDivider
from .mpl_axes import Axes as Axes
from _typeshed import Incomplete

class CbarAxesBase:
    orientation: Incomplete
    def __init__(self, *args, orientation, **kwargs) -> None: ...
    def colorbar(self, mappable, *, ticks: Incomplete | None = None, **kwargs): ...
    def toggle_label(self, b) -> None: ...
    def cla(self) -> None: ...

class Grid:
    """
    A grid of Axes.

    In Matplotlib, the Axes location (and size) is specified in normalized
    figure coordinates. This may not be ideal for images that needs to be
    displayed with a given aspect ratio; for example, it is difficult to
    display multiple images of a same size with some fixed padding between
    them.  AxesGrid can be used in such case.
    """
    ngrids: Incomplete
    axes_all: Incomplete
    axes_column: Incomplete
    axes_row: Incomplete
    axes_llc: Incomplete
    def __init__(self, fig, rect, nrows_ncols, ngrids: Incomplete | None = None, direction: str = 'row', axes_pad: float = 0.02, *, share_all: bool = False, share_x: bool = True, share_y: bool = True, label_mode: str = 'L', axes_class: Incomplete | None = None, aspect: bool = False) -> None:
        '''
        Parameters
        ----------
        fig : `.Figure`
            The parent figure.
        rect : (float, float, float, float), (int, int, int), int, or     `~.SubplotSpec`
            The axes position, as a ``(left, bottom, width, height)`` tuple,
            as a three-digit subplot position code (e.g., ``(1, 2, 1)`` or
            ``121``), or as a `~.SubplotSpec`.
        nrows_ncols : (int, int)
            Number of rows and columns in the grid.
        ngrids : int or None, default: None
            If not None, only the first *ngrids* axes in the grid are created.
        direction : {"row", "column"}, default: "row"
            Whether axes are created in row-major ("row by row") or
            column-major order ("column by column").  This also affects the
            order in which axes are accessed using indexing (``grid[index]``).
        axes_pad : float or (float, float), default: 0.02
            Padding or (horizontal padding, vertical padding) between axes, in
            inches.
        share_all : bool, default: False
            Whether all axes share their x- and y-axis.  Overrides *share_x*
            and *share_y*.
        share_x : bool, default: True
            Whether all axes of a column share their x-axis.
        share_y : bool, default: True
            Whether all axes of a row share their y-axis.
        label_mode : {"L", "1", "all", "keep"}, default: "L"
            Determines which axes will get tick labels:

            - "L": All axes on the left column get vertical tick labels;
              all axes on the bottom row get horizontal tick labels.
            - "1": Only the bottom left axes is labelled.
            - "all": All axes are labelled.
            - "keep": Do not do anything.

        axes_class : subclass of `matplotlib.axes.Axes`, default: None
        aspect : bool, default: False
            Whether the axes aspect ratio follows the aspect ratio of the data
            limits.
        '''
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def get_geometry(self):
        """
        Return the number of rows and columns of the grid as (nrows, ncols).
        """
    def set_axes_pad(self, axes_pad) -> None:
        """
        Set the padding between the axes.

        Parameters
        ----------
        axes_pad : (float, float)
            The padding (horizontal pad, vertical pad) in inches.
        """
    def get_axes_pad(self):
        """
        Return the axes padding.

        Returns
        -------
        hpad, vpad
            Padding (horizontal pad, vertical pad) in inches.
        """
    def set_aspect(self, aspect) -> None:
        """Set the aspect of the SubplotDivider."""
    def get_aspect(self):
        """Return the aspect of the SubplotDivider."""
    def set_label_mode(self, mode) -> None:
        '''
        Define which axes have tick labels.

        Parameters
        ----------
        mode : {"L", "1", "all", "keep"}
            The label mode:

            - "L": All axes on the left column get vertical tick labels;
              all axes on the bottom row get horizontal tick labels.
            - "1": Only the bottom left axes is labelled.
            - "all": All axes are labelled.
            - "keep": Do not do anything.
        '''
    def get_divider(self): ...
    def set_axes_locator(self, locator) -> None: ...
    def get_axes_locator(self): ...

class ImageGrid(Grid):
    def __init__(self, fig, rect, nrows_ncols, ngrids: Incomplete | None = None, direction: str = 'row', axes_pad: float = 0.02, *, share_all: bool = False, aspect: bool = True, label_mode: str = 'L', cbar_mode: Incomplete | None = None, cbar_location: str = 'right', cbar_pad: Incomplete | None = None, cbar_size: str = '5%', cbar_set_cax: bool = True, axes_class: Incomplete | None = None) -> None:
        '''
        Parameters
        ----------
        fig : `.Figure`
            The parent figure.
        rect : (float, float, float, float) or int
            The axes position, as a ``(left, bottom, width, height)`` tuple or
            as a three-digit subplot position code (e.g., "121").
        nrows_ncols : (int, int)
            Number of rows and columns in the grid.
        ngrids : int or None, default: None
            If not None, only the first *ngrids* axes in the grid are created.
        direction : {"row", "column"}, default: "row"
            Whether axes are created in row-major ("row by row") or
            column-major order ("column by column").  This also affects the
            order in which axes are accessed using indexing (``grid[index]``).
        axes_pad : float or (float, float), default: 0.02in
            Padding or (horizontal padding, vertical padding) between axes, in
            inches.
        share_all : bool, default: False
            Whether all axes share their x- and y-axis.
        aspect : bool, default: True
            Whether the axes aspect ratio follows the aspect ratio of the data
            limits.
        label_mode : {"L", "1", "all"}, default: "L"
            Determines which axes will get tick labels:

            - "L": All axes on the left column get vertical tick labels;
              all axes on the bottom row get horizontal tick labels.
            - "1": Only the bottom left axes is labelled.
            - "all": all axes are labelled.

        cbar_mode : {"each", "single", "edge", None}, default: None
            Whether to create a colorbar for "each" axes, a "single" colorbar
            for the entire grid, colorbars only for axes on the "edge"
            determined by *cbar_location*, or no colorbars.  The colorbars are
            stored in the :attr:`cbar_axes` attribute.
        cbar_location : {"left", "right", "bottom", "top"}, default: "right"
        cbar_pad : float, default: None
            Padding between the image axes and the colorbar axes.
        cbar_size : size specification (see `.Size.from_any`), default: "5%"
            Colorbar size.
        cbar_set_cax : bool, default: True
            If True, each axes in the grid has a *cax* attribute that is bound
            to associated *cbar_axes*.
        axes_class : subclass of `matplotlib.axes.Axes`, default: None
        '''
AxesGrid = ImageGrid
