from _typeshed import Incomplete
from fontTools.misc import cython as cython
from numbers import Integral, Real

COMPILED: Incomplete
MAX_LOOKBACK: int

def iup_segment(coords: _PointSegment, rc1: _Point, rd1: _Delta, rc2: _Point, rd2: _Delta):
    """Given two reference coordinates `rc1` & `rc2` and their respective
    delta vectors `rd1` & `rd2`, returns interpolated deltas for the set of
    coordinates `coords`."""
def iup_contour(deltas: _DeltaOrNoneSegment, coords: _PointSegment) -> _DeltaSegment:
    """For the contour given in `coords`, interpolate any missing
    delta values in delta vector `deltas`.

    Returns fully filled-out delta vector."""
def iup_delta(deltas: _DeltaOrNoneSegment, coords: _PointSegment, ends: _Endpoints) -> _DeltaSegment:
    """For the outline given in `coords`, with contour endpoints given
    in sorted increasing order in `ends`, interpolate any missing
    delta values in delta vector `deltas`.

    Returns fully filled-out delta vector."""
def can_iup_in_between(deltas: _DeltaSegment, coords: _PointSegment, i: Integral, j: Integral, tolerance: Real):
    """Return true if the deltas for points at `i` and `j` (`i < j`) can be
    successfully used to interpolate deltas for points in between them within
    provided error tolerance."""
def iup_contour_optimize(deltas: _DeltaSegment, coords: _PointSegment, tolerance: Real = 0.0) -> _DeltaOrNoneSegment:
    """For contour with coordinates `coords`, optimize a set of delta
    values `deltas` within error `tolerance`.

    Returns delta vector that has most number of None items instead of
    the input delta.
    """
def iup_delta_optimize(deltas: _DeltaSegment, coords: _PointSegment, ends: _Endpoints, tolerance: Real = 0.0) -> _DeltaOrNoneSegment:
    """For the outline given in `coords`, with contour endpoints given
    in sorted increasing order in `ends`, optimize a set of delta
    values `deltas` within error `tolerance`.

    Returns delta vector that has most number of None items instead of
    the input delta.
    """
