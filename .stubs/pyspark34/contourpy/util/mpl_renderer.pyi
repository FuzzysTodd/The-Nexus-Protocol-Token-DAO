import contourpy._contourpy as cpy
import io
import numpy as np
from contourpy import FillType as FillType, LineType as LineType
from contourpy.util.mpl_util import filled_to_mpl_paths as filled_to_mpl_paths, lines_to_mpl_paths as lines_to_mpl_paths, mpl_codes_to_offsets as mpl_codes_to_offsets
from contourpy.util.renderer import Renderer as Renderer
from matplotlib.axes import Axes as Axes
from matplotlib.figure import Figure as Figure
from numpy.typing import ArrayLike as ArrayLike
from typing import Any

class MplRenderer(Renderer):
    def __init__(self, nrows: int = 1, ncols: int = 1, figsize: tuple[float, float] = (9, 9), show_frame: bool = True, backend: str | None = None, gridspec_kw: dict[str, Any] | None = None) -> None: ...
    def __del__(self) -> None: ...
    def filled(self, filled: cpy.FillReturn, fill_type: FillType, ax: Axes | int = 0, color: str = 'C0', alpha: float = 0.7) -> None:
        '''Plot filled contours on a single Axes.

        Args:
            filled (sequence of arrays): Filled contour data as returned by
                :func:`~contourpy.ContourGenerator.filled`.
            fill_type (FillType): Type of ``filled`` data, as returned by
                :attr:`~contourpy.ContourGenerator.fill_type`.
            ax (int or Maplotlib Axes, optional): Which axes to plot on, default ``0``.
            color (str, optional): Color to plot with. May be a string color or the letter ``"C"``
                followed by an integer in the range ``"C0"`` to ``"C9"`` to use a color from the
                ``tab10`` colormap. Default ``"C0"``.
            alpha (float, optional): Opacity to plot with, default ``0.7``.
        '''
    def grid(self, x: ArrayLike, y: ArrayLike, ax: Axes | int = 0, color: str = 'black', alpha: float = 0.1, point_color: str | None = None, quad_as_tri_alpha: float = 0) -> None:
        '''Plot quad grid lines on a single Axes.

        Args:
            x (array-like of shape (ny, nx) or (nx,)): The x-coordinates of the grid points.
            y (array-like of shape (ny, nx) or (ny,)): The y-coordinates of the grid points.
            ax (int or Matplotlib Axes, optional): Which Axes to plot on, default ``0``.
            color (str, optional): Color to plot grid lines, default ``"black"``.
            alpha (float, optional): Opacity to plot lines with, default ``0.1``.
            point_color (str, optional): Color to plot grid points or ``None`` if grid points
                should not be plotted, default ``None``.
            quad_as_tri_alpha (float, optional): Opacity to plot ``quad_as_tri`` grid, default 0.

        Colors may be a string color or the letter ``"C"`` followed by an integer in the range
        ``"C0"`` to ``"C9"`` to use a color from the ``tab10`` colormap.

        Warning:
            ``quad_as_tri_alpha > 0`` plots all quads as though they are unmasked.
        '''
    def lines(self, lines: cpy.LineReturn, line_type: LineType, ax: Axes | int = 0, color: str = 'C0', alpha: float = 1.0, linewidth: float = 1) -> None:
        '''Plot contour lines on a single Axes.

        Args:
            lines (sequence of arrays): Contour line data as returned by
                :func:`~contourpy.ContourGenerator.lines`.
            line_type (LineType): Type of ``lines`` data, as returned by
                :attr:`~contourpy.ContourGenerator.line_type`.
            ax (int or Matplotlib Axes, optional): Which Axes to plot on, default ``0``.
            color (str, optional): Color to plot lines. May be a string color or the letter ``"C"``
                followed by an integer in the range ``"C0"`` to ``"C9"`` to use a color from the
                ``tab10`` colormap. Default ``"C0"``.
            alpha (float, optional): Opacity to plot lines with, default ``1.0``.
            linewidth (float, optional): Width of lines, default ``1``.
        '''
    def mask(self, x: ArrayLike, y: ArrayLike, z: ArrayLike | np.ma.MaskedArray[Any, Any], ax: Axes | int = 0, color: str = 'black') -> None:
        '''Plot masked out grid points as circles on a single Axes.

        Args:
            x (array-like of shape (ny, nx) or (nx,)): The x-coordinates of the grid points.
            y (array-like of shape (ny, nx) or (ny,)): The y-coordinates of the grid points.
            z (masked array of shape (ny, nx): z-values.
            ax (int or Matplotlib Axes, optional): Which Axes to plot on, default ``0``.
            color (str, optional): Circle color, default ``"black"``.
        '''
    def save(self, filename: str, transparent: bool = False) -> None:
        """Save plots to SVG or PNG file.

        Args:
            filename (str): Filename to save to.
            transparent (bool, optional): Whether background should be transparent, default
                ``False``.
        """
    def save_to_buffer(self) -> io.BytesIO:
        """Save plots to an ``io.BytesIO`` buffer.

        Return:
            BytesIO: PNG image buffer.
        """
    def show(self) -> None:
        """Show plots in an interactive window, in the usual Matplotlib manner.
        """
    def title(self, title: str, ax: Axes | int = 0, color: str | None = None) -> None:
        '''Set the title of a single Axes.

        Args:
            title (str): Title text.
            ax (int or Matplotlib Axes, optional): Which Axes to set the title of, default ``0``.
            color (str, optional): Color to set title. May be a string color or the letter ``"C"``
                followed by an integer in the range ``"C0"`` to ``"C9"`` to use a color from the
                ``tab10`` colormap. Default is ``None`` which uses Matplotlib\'s default title color
                that depends on the stylesheet in use.
        '''
    def z_values(self, x: ArrayLike, y: ArrayLike, z: ArrayLike, ax: Axes | int = 0, color: str = 'green', fmt: str = '.1f', quad_as_tri: bool = False) -> None:
        '''Show ``z`` values on a single Axes.

        Args:
            x (array-like of shape (ny, nx) or (nx,)): The x-coordinates of the grid points.
            y (array-like of shape (ny, nx) or (ny,)): The y-coordinates of the grid points.
            z (array-like of shape (ny, nx): z-values.
            ax (int or Matplotlib Axes, optional): Which Axes to plot on, default ``0``.
            color (str, optional): Color of added text. May be a string color or the letter ``"C"``
                followed by an integer in the range ``"C0"`` to ``"C9"`` to use a color from the
                ``tab10`` colormap. Default ``"green"``.
            fmt (str, optional): Format to display z-values, default ``".1f"``.
            quad_as_tri (bool, optional): Whether to show z-values at the ``quad_as_tri`` centers
                of quads.

        Warning:
            ``quad_as_tri=True`` shows z-values for all quads, even if masked.
        '''

class MplTestRenderer(MplRenderer):
    """Test renderer implemented using Matplotlib.

    No whitespace around plots and no spines/ticks displayed.
    Uses Agg backend, so can only save to file/buffer, cannot call ``show()``.
    """
    def __init__(self, nrows: int = 1, ncols: int = 1, figsize: tuple[float, float] = (9, 9)) -> None: ...

class MplDebugRenderer(MplRenderer):
    """Debug renderer implemented using Matplotlib.

    Extends ``MplRenderer`` to add extra information to help in debugging such as markers, arrows,
    text, etc.
    """
    def __init__(self, nrows: int = 1, ncols: int = 1, figsize: tuple[float, float] = (9, 9), show_frame: bool = True) -> None: ...
    def filled(self, filled: cpy.FillReturn, fill_type: FillType, ax: Axes | int = 0, color: str = 'C1', alpha: float = 0.7, line_color: str = 'C0', line_alpha: float = 0.7, point_color: str = 'C0', start_point_color: str = 'red', arrow_size: float = 0.1) -> None: ...
    def lines(self, lines: cpy.LineReturn, line_type: LineType, ax: Axes | int = 0, color: str = 'C0', alpha: float = 1.0, linewidth: float = 1, point_color: str = 'C0', start_point_color: str = 'red', arrow_size: float = 0.1) -> None: ...
    def point_numbers(self, x: ArrayLike, y: ArrayLike, z: ArrayLike, ax: Axes | int = 0, color: str = 'red') -> None: ...
    def quad_numbers(self, x: ArrayLike, y: ArrayLike, z: ArrayLike, ax: Axes | int = 0, color: str = 'blue') -> None: ...
    def z_levels(self, x: ArrayLike, y: ArrayLike, z: ArrayLike, lower_level: float, upper_level: float | None = None, ax: Axes | int = 0, color: str = 'green') -> None: ...
