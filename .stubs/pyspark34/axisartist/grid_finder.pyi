from _typeshed import Incomplete
from matplotlib import ticker as mticker
from matplotlib.transforms import Transform

class ExtremeFinderSimple:
    """
    A helper class to figure out the range of grid lines that need to be drawn.
    """
    nx: Incomplete
    ny: Incomplete
    def __init__(self, nx, ny) -> None:
        """
        Parameters
        ----------
        nx, ny : int
            The number of samples in each direction.
        """
    def __call__(self, transform_xy, x1, y1, x2, y2):
        """
        Compute an approximation of the bounding box obtained by applying
        *transform_xy* to the box delimited by ``(x1, y1, x2, y2)``.

        The intended use is to have ``(x1, y1, x2, y2)`` in axes coordinates,
        and have *transform_xy* be the transform from axes coordinates to data
        coordinates; this method then returns the range of data coordinates
        that span the actual axes.

        The computation is done by sampling ``nx * ny`` equispaced points in
        the ``(x1, y1, x2, y2)`` box and finding the resulting points with
        extremal coordinates; then adding some padding to take into account the
        finite sampling.

        As each sampling step covers a relative range of *1/nx* or *1/ny*,
        the padding is computed by expanding the span covered by the extremal
        coordinates by these fractions.
        """

class _User2DTransform(Transform):
    """A transform defined by two user-set functions."""
    input_dims: int
    output_dims: int
    def __init__(self, forward, backward) -> None:
        """
        Parameters
        ----------
        forward, backward : callable
            The forward and backward transforms, taking ``x`` and ``y`` as
            separate arguments and returning ``(tr_x, tr_y)``.
        """
    def transform_non_affine(self, values): ...
    def inverted(self): ...

class GridFinder:
    extreme_finder: Incomplete
    grid_locator1: Incomplete
    grid_locator2: Incomplete
    tick_formatter1: Incomplete
    tick_formatter2: Incomplete
    def __init__(self, transform, extreme_finder: Incomplete | None = None, grid_locator1: Incomplete | None = None, grid_locator2: Incomplete | None = None, tick_formatter1: Incomplete | None = None, tick_formatter2: Incomplete | None = None) -> None:
        """
        transform : transform from the image coordinate (which will be
        the transData of the axes to the world coordinate).

        or transform = (transform_xy, inv_transform_xy)

        locator1, locator2 : grid locator for 1st and 2nd axis.
        """
    def get_grid_info(self, x1, y1, x2, y2):
        """
        lon_values, lat_values : list of grid values. if integer is given,
                           rough number of grids in each direction.
        """
    def set_transform(self, aux_trans) -> None: ...
    def get_transform(self): ...
    update_transform = set_transform
    def transform_xy(self, x, y): ...
    def inv_transform_xy(self, x, y): ...
    def update(self, **kwargs) -> None: ...

class MaxNLocator(mticker.MaxNLocator):
    def __init__(self, nbins: int = 10, steps: Incomplete | None = None, trim: bool = True, integer: bool = False, symmetric: bool = False, prune: Incomplete | None = None) -> None: ...
    def __call__(self, v1, v2): ...

class FixedLocator:
    def __init__(self, locs) -> None: ...
    def __call__(self, v1, v2): ...

class FormatterPrettyPrint:
    def __init__(self, useMathText: bool = True) -> None: ...
    def __call__(self, direction, factor, values): ...

class DictFormatter:
    def __init__(self, format_dict, formatter: Incomplete | None = None) -> None:
        """
        format_dict : dictionary for format strings to be used.
        formatter : fall-back formatter
        """
    def __call__(self, direction, factor, values):
        """
        factor is ignored if value is found in the dictionary
        """
