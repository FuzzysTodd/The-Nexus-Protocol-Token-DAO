import numpy as np
from pandas.errors import PerformanceWarning as PerformanceWarning
from pandas.util._exceptions import find_stack_level as find_stack_level

def fallback_performancewarning(version: str | None = None) -> None:
    """
    Raise a PerformanceWarning for falling back to ExtensionArray's
    non-pyarrow method
    """
def pyarrow_array_to_numpy_and_mask(arr, dtype: np.dtype) -> tuple[np.ndarray, np.ndarray]:
    """
    Convert a primitive pyarrow.Array to a numpy array and boolean mask based
    on the buffers of the Array.

    At the moment pyarrow.BooleanArray is not supported.

    Parameters
    ----------
    arr : pyarrow.Array
    dtype : numpy.dtype

    Returns
    -------
    (data, mask)
        Tuple of two numpy arrays with the raw data (with specified dtype) and
        a boolean mask (validity mask, so False means missing)
    """
