import dataclasses
from _typeshed import Incomplete
from typing import Tuple

NORMAL_HISTOGRAM_BPS: Incomplete

@dataclasses.dataclass(frozen=True)
class CompressedHistogramValue:
    """Represents a value in a compressed histogram.

    Attributes:
      basis_point: Compression point represented in basis point, 1/100th of a
        percent.
      value: Cumulative weight at the basis point.
    """
    basis_point: float
    value: float
    def as_tuple(self) -> Tuple[float, float]:
        """Returns the basis point and the value as a tuple."""
    def __init__(self, basis_point, value) -> None: ...

def compress_histogram_proto(histo, bps=...):
    """Creates fixed size histogram by adding compression to accumulated state.

    This routine transforms a histogram at a particular step by interpolating its
    variable number of buckets to represent their cumulative weight at a constant
    number of compression points. This significantly reduces the size of the
    histogram and makes it suitable for a two-dimensional area plot where the
    output of this routine constitutes the ranges for a single x coordinate.

    Args:
      histo: A HistogramProto object.
      bps: Compression points represented in basis points, 1/100ths of a percent.
          Defaults to normal distribution.

    Returns:
      List of values for each basis point.
    """
def compress_histogram(buckets, bps=...):
    """Creates fixed size histogram by adding compression to accumulated state.

    This routine transforms a histogram at a particular step by linearly
    interpolating its variable number of buckets to represent their cumulative
    weight at a constant number of compression points. This significantly reduces
    the size of the histogram and makes it suitable for a two-dimensional area
    plot where the output of this routine constitutes the ranges for a single x
    coordinate.

    Args:
      buckets: A list of buckets, each of which is a 3-tuple of the form
        `(min, max, count)`.
      bps: Compression points represented in basis points, 1/100ths of a percent.
          Defaults to normal distribution.

    Returns:
      List of values for each basis point.
    """
