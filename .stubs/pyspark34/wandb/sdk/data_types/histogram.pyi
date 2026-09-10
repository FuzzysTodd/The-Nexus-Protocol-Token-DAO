import numpy as np
from ..wandb_run import Run as LocalRun
from .base_types.wb_value import WBValue as WBValue
from _typeshed import Incomplete
from typing import Sequence, Tuple
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact

NumpyHistogram = Tuple[np.ndarray, np.ndarray]

class Histogram(WBValue):
    """wandb class for histograms.

    This object works just like numpy's histogram function
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html

    Examples:
        Generate histogram from a sequence
        ```python
        wandb.Histogram([1, 2, 3])
        ```

        Efficiently initialize from np.histogram.
        ```python
        hist = np.histogram(data)
        wandb.Histogram(np_histogram=hist)
        ```

    Arguments:
        sequence: (array_like) input data for histogram
        np_histogram: (numpy histogram) alternative input of a precomputed histogram
        num_bins: (int) Number of bins for the histogram.  The default number of bins
            is 64.  The maximum number of bins is 512

    Attributes:
        bins: ([float]) edges of bins
        histogram: ([int]) number of elements falling in each bin
    """
    MAX_LENGTH: int
    histogram: Incomplete
    bins: Incomplete
    def __init__(self, sequence: Sequence | None = None, np_histogram: NumpyHistogram | None = None, num_bins: int = 64) -> None: ...
    def to_json(self, run: LocalRun | Artifact | None = None) -> dict: ...
    def __sizeof__(self) -> int:
        """Estimated size in bytes.

        Currently the factor of 1.7 is used to account for the JSON encoding. We use
        this in tb_watcher.TBHistory.
        """
