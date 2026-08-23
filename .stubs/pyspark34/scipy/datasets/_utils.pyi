from ._registry import method_files_map as method_files_map
from _typeshed import Incomplete

def clear_cache(datasets: Incomplete | None = None) -> None:
    """
    Cleans the scipy datasets cache directory.

    If a scipy.datasets method or a list/tuple of the same is
    provided, then clear_cache removes all the data files
    associated to the passed dataset method callable(s).

    By default, it removes all the cached data files.

    Parameters
    ----------
    datasets : callable or list/tuple of callable or None

    Examples
    --------
    >>> from scipy import datasets
    >>> ascent_array = datasets.ascent()
    >>> ascent_array.shape
    (512, 512)
    >>> datasets.clear_cache([datasets.ascent])
    Cleaning the file ascent.dat for dataset ascent
    """
