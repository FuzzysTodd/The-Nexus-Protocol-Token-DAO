import numpy as np
from contourpy._contourpy import ContourGenerator as ContourGenerator, FillType as FillType, LineType as LineType, Mpl2005ContourGenerator as Mpl2005ContourGenerator, Mpl2014ContourGenerator as Mpl2014ContourGenerator, SerialContourGenerator as SerialContourGenerator, ThreadedContourGenerator as ThreadedContourGenerator, ZInterp as ZInterp, max_threads as max_threads
from contourpy._version import __version__ as __version__
from numpy.typing import ArrayLike
from typing import Any

__all__ = ['__version__', 'contour_generator', 'max_threads', 'FillType', 'LineType', 'ContourGenerator', 'Mpl2005ContourGenerator', 'Mpl2014ContourGenerator', 'SerialContourGenerator', 'ThreadedContourGenerator', 'ZInterp']

def contour_generator(x: ArrayLike | None = None, y: ArrayLike | None = None, z: ArrayLike | np.ma.MaskedArray[Any, Any] | None = None, *, name: str = 'serial', corner_mask: bool | None = None, line_type: LineType | str | None = None, fill_type: FillType | str | None = None, chunk_size: int | tuple[int, int] | None = None, chunk_count: int | tuple[int, int] | None = None, total_chunk_count: int | None = None, quad_as_tri: bool = False, z_interp: ZInterp | str | None = ..., thread_count: int = 0) -> ContourGenerator:
    '''Create and return a contour generator object.

    The class and properties of the contour generator are determined by the function arguments,
    with sensible defaults.

    Args:
        x (array-like of shape (ny, nx) or (nx,), optional): The x-coordinates of the ``z`` values.
            May be 2D with the same shape as ``z.shape``, or 1D with length ``nx = z.shape[1]``.
            If not specified are assumed to be ``np.arange(nx)``. Must be ordered monotonically.
        y (array-like of shape (ny, nx) or (ny,), optional): The y-coordinates of the ``z`` values.
            May be 2D with the same shape as ``z.shape``, or 1D with length ``ny = z.shape[0]``.
            If not specified are assumed to be ``np.arange(ny)``. Must be ordered monotonically.
        z (array-like of shape (ny, nx), may be a masked array): The 2D gridded values to calculate
            the contours of.  May be a masked array, and any invalid values (``np.inf`` or
            ``np.nan``) will also be masked out.
        name (str): Algorithm name, one of ``"serial"``, ``"threaded"``, ``"mpl2005"`` or
            ``"mpl2014"``, default ``"serial"``.
        corner_mask (bool, optional): Enable/disable corner masking, which only has an effect if
            ``z`` is a masked array. If ``False``, any quad touching a masked point is masked out.
            If ``True``, only the triangular corners of quads nearest these points are always masked
            out, other triangular corners comprising three unmasked points are contoured as usual.
            If not specified, uses the default provided by the algorithm ``name``.
        line_type (LineType, optional): The format of contour line data returned from calls to
            :meth:`~contourpy.ContourGenerator.lines`. If not specified, uses the default provided
            by the algorithm ``name``.
        fill_type (FillType, optional): The format of filled contour data returned from calls to
            :meth:`~contourpy.ContourGenerator.filled`. If not specified, uses the default provided
            by the algorithm ``name``.
        chunk_size (int or tuple(int, int), optional): Chunk size in (y, x) directions, or the same
            size in both directions if only one value is specified.
        chunk_count (int or tuple(int, int), optional): Chunk count in (y, x) directions, or the
            same count in both directions if only one value is specified.
        total_chunk_count (int, optional): Total number of chunks.
        quad_as_tri (bool): Enable/disable treating quads as 4 triangles, default ``False``.
            If ``False``, a contour line within a quad is a straight line between points on two of
            its edges. If ``True``, each full quad is divided into 4 triangles using a virtual point
            at the centre (mean x, y of the corner points) and a contour line is piecewise linear
            within those triangles. Corner-masked triangles are not affected by this setting, only
            full unmasked quads.
        z_interp (ZInterp): How to interpolate ``z`` values when determining where contour lines
            intersect the edges of quads and the ``z`` values of the central points of quads,
            default ``ZInterp.Linear``.
        thread_count (int): Number of threads to use for contour calculation, default 0. Threads can
            only be used with an algorithm ``name`` that supports threads (currently only
            ``name="threaded"``) and there must be at least the same number of chunks as threads.
            If ``thread_count=0`` and ``name="threaded"`` then it uses the maximum number of threads
            as determined by the C++11 call ``std::thread::hardware_concurrency()``. If ``name`` is
            something other than ``"threaded"`` then the ``thread_count`` will be set to ``1``.

    Return:
        :class:`~contourpy._contourpy.ContourGenerator`.

    Note:
        A maximum of one of ``chunk_size``, ``chunk_count`` and ``total_chunk_count`` may be
        specified.

    Warning:
        The ``name="mpl2005"`` algorithm does not implement chunking for contour lines.
    '''
