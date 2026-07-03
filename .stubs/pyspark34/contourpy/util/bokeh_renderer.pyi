import io
import numpy as np
from bokeh.models import GridPlot as GridPlot
from bokeh.palettes import Palette as Palette
from bokeh.plotting import figure
from contourpy import FillType as FillType, LineType as LineType
from contourpy._contourpy import FillReturn as FillReturn, LineReturn as LineReturn
from contourpy.util.bokeh_util import filled_to_bokeh as filled_to_bokeh, lines_to_bokeh as lines_to_bokeh
from contourpy.util.renderer import Renderer as Renderer
from numpy.typing import ArrayLike as ArrayLike
from selenium.webdriver.remote.webdriver import WebDriver as WebDriver
from typing import Any

class BokehRenderer(Renderer):
    def __init__(self, nrows: int = 1, ncols: int = 1, figsize: tuple[float, float] = (9, 9), show_frame: bool = True, want_svg: bool = False) -> None: ...
    def filled(self, filled: FillReturn, fill_type: FillType, ax: figure | int = 0, color: str = 'C0', alpha: float = 0.7) -> None:
        '''Plot filled contours on a single plot.

        Args:
            filled (sequence of arrays): Filled contour data as returned by
                :func:`~contourpy.ContourGenerator.filled`.
            fill_type (FillType): Type of ``filled`` data, as returned by
                :attr:`~contourpy.ContourGenerator.fill_type`.
            ax (int or Bokeh Figure, optional): Which plot to use, default ``0``.
            color (str, optional): Color to plot with. May be a string color or the letter ``"C"``
                followed by an integer in the range ``"C0"`` to ``"C9"`` to use a color from the
                ``Category10`` palette. Default ``"C0"``.
            alpha (float, optional): Opacity to plot with, default ``0.7``.
        '''
    def grid(self, x: ArrayLike, y: ArrayLike, ax: figure | int = 0, color: str = 'black', alpha: float = 0.1, point_color: str | None = None, quad_as_tri_alpha: float = 0) -> None:
        '''Plot quad grid lines on a single plot.

        Args:
            x (array-like of shape (ny, nx) or (nx,)): The x-coordinates of the grid points.
            y (array-like of shape (ny, nx) or (ny,)): The y-coordinates of the grid points.
            ax (int or Bokeh Figure, optional): Which plot to use, default ``0``.
            color (str, optional): Color to plot grid lines, default ``"black"``.
            alpha (float, optional): Opacity to plot lines with, default ``0.1``.
            point_color (str, optional): Color to plot grid points or ``None`` if grid points
                should not be plotted, default ``None``.
            quad_as_tri_alpha (float, optional): Opacity to plot ``quad_as_tri`` grid, default
                ``0``.

        Colors may be a string color or the letter ``"C"`` followed by an integer in the range
        ``"C0"`` to ``"C9"`` to use a color from the ``Category10`` palette.

        Warning:
            ``quad_as_tri_alpha > 0`` plots all quads as though they are unmasked.
        '''
    def lines(self, lines: LineReturn, line_type: LineType, ax: figure | int = 0, color: str = 'C0', alpha: float = 1.0, linewidth: float = 1) -> None:
        '''Plot contour lines on a single plot.

        Args:
            lines (sequence of arrays): Contour line data as returned by
                :func:`~contourpy.ContourGenerator.lines`.
            line_type (LineType): Type of ``lines`` data, as returned by
                :attr:`~contourpy.ContourGenerator.line_type`.
            ax (int or Bokeh Figure, optional): Which plot to use, default ``0``.
            color (str, optional): Color to plot lines. May be a string color or the letter ``"C"``
                followed by an integer in the range ``"C0"`` to ``"C9"`` to use a color from the
                ``Category10`` palette. Default ``"C0"``.
            alpha (float, optional): Opacity to plot lines with, default ``1.0``.
            linewidth (float, optional): Width of lines, default ``1``.

        Note:
            Assumes all lines are open line strips not closed line loops.
        '''
    def mask(self, x: ArrayLike, y: ArrayLike, z: ArrayLike | np.ma.MaskedArray[Any, Any], ax: figure | int = 0, color: str = 'black') -> None:
        '''Plot masked out grid points as circles on a single plot.

        Args:
            x (array-like of shape (ny, nx) or (nx,)): The x-coordinates of the grid points.
            y (array-like of shape (ny, nx) or (ny,)): The y-coordinates of the grid points.
            z (masked array of shape (ny, nx): z-values.
            ax (int or Bokeh Figure, optional): Which plot to use, default ``0``.
            color (str, optional): Circle color, default ``"black"``.
        '''
    def save(self, filename: str, transparent: bool = False, *, webdriver: WebDriver | None = None) -> None:
        """Save plots to SVG or PNG file.

        Args:
            filename (str): Filename to save to.
            transparent (bool, optional): Whether background should be transparent, default
                ``False``.
            webdriver (WebDriver, optional): Selenium WebDriver instance to use to create the image.

        Warning:
            To output to SVG file, ``want_svg=True`` must have been passed to the constructor.
        """
    def save_to_buffer(self, *, webdriver: WebDriver | None = None) -> io.BytesIO:
        """Save plots to an ``io.BytesIO`` buffer.

        Args:
            webdriver (WebDriver, optional): Selenium WebDriver instance to use to create the image.

        Return:
            BytesIO: PNG image buffer.
        """
    def show(self) -> None:
        """Show plots in web browser, in usual Bokeh manner.
        """
    def title(self, title: str, ax: figure | int = 0, color: str | None = None) -> None:
        '''Set the title of a single plot.

        Args:
            title (str): Title text.
            ax (int or Bokeh Figure, optional): Which plot to set the title of, default ``0``.
            color (str, optional): Color to set title. May be a string color or the letter ``"C"``
                followed by an integer in the range ``"C0"`` to ``"C9"`` to use a color from the
                ``Category10`` palette. Default ``None`` which is ``black``.
        '''
    def z_values(self, x: ArrayLike, y: ArrayLike, z: ArrayLike, ax: figure | int = 0, color: str = 'green', fmt: str = '.1f', quad_as_tri: bool = False) -> None:
        '''Show ``z`` values on a single plot.

        Args:
            x (array-like of shape (ny, nx) or (nx,)): The x-coordinates of the grid points.
            y (array-like of shape (ny, nx) or (ny,)): The y-coordinates of the grid points.
            z (array-like of shape (ny, nx): z-values.
            ax (int or Bokeh Figure, optional): Which plot to use, default ``0``.
            color (str, optional): Color of added text. May be a string color or the letter ``"C"``
                followed by an integer in the range ``"C0"`` to ``"C9"`` to use a color from the
                ``Category10`` palette. Default ``"green"``.
            fmt (str, optional): Format to display z-values, default ``".1f"``.
            quad_as_tri (bool, optional): Whether to show z-values at the ``quad_as_tri`` centres
                of quads.

        Warning:
            ``quad_as_tri=True`` shows z-values for all quads, even if masked.
        '''
