from ..utils import experimental as experimental, logging as logging
from _typeshed import Incomplete

logger: Incomplete

class ParallelBackendConfig:
    backend_name: Incomplete

def parallel_map(function, iterable, num_proc, types, disable_tqdm, desc, single_map_nested_func):
    """
    **Experimental.** Apply a function to iterable elements in parallel, where the implementation uses either
    multiprocessing.Pool or joblib for parallelization.

    Args:
        function (`Callable[[Any], Any]`): Function to be applied to `iterable`.
        iterable (`list`, `tuple` or `np.ndarray`): Iterable elements to apply function to.
        num_proc (`int`): Number of processes (if no backend specified) or jobs (using joblib).
        types (`tuple`): Additional types (besides `dict` values) to apply `function` recursively to their elements.
        disable_tqdm (`bool`): Whether to disable the tqdm progressbar.
        desc (`str`): Prefix for the tqdm progressbar.
        single_map_nested_func (`Callable`): Map function that applies `function` to an element from `iterable`.
            Takes a tuple of function, data_struct, types, rank, disable_tqdm, desc as input, where data_struct is an
            element of `iterable`, and `rank` is used for progress bar.
    """
def parallel_backend(backend_name: str):
    """
    **Experimental.**  Configures the parallel backend for parallelized dataset loading, which uses the parallelization
    implemented by joblib.

    Args:
        backend_name (str): Name of backend for parallelization implementation, has to be supported by joblib.

     Example usage:
     ```py
     with parallel_backend('spark'):
       dataset = load_dataset(..., num_proc=2)
     ```
    """
