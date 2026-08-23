import types as python_types
from _typeshed import Incomplete
from keras.utils import io_utils as io_utils, tf_inspect as tf_inspect

def func_dump(func):
    """Serializes a user defined function.

    Args:
        func: the function to serialize.

    Returns:
        A tuple `(code, defaults, closure)`.
    """
def func_load(code, defaults: Incomplete | None = None, closure: Incomplete | None = None, globs: Incomplete | None = None):
    """Deserializes a user defined function.

    Args:
        code: bytecode of the function.
        defaults: defaults of the function.
        closure: closure of the function.
        globs: dictionary of global objects.

    Returns:
        A function object.
    """
def has_arg(fn, name, accept_all: bool = False):
    """Checks if a callable accepts a given keyword argument.

    Args:
        fn: Callable to inspect.
        name: Check if `fn` can be called with `name` as a keyword argument.
        accept_all: What to return if there is no parameter called `name` but
          the function accepts a `**kwargs` argument.

    Returns:
        bool, whether `fn` accepts a `name` keyword argument.
    """

class Progbar:
    '''Displays a progress bar.

    Args:
        target: Total number of steps expected, None if unknown.
        width: Progress bar width on screen.
        verbose: Verbosity mode, 0 (silent), 1 (verbose), 2 (semi-verbose)
        stateful_metrics: Iterable of string names of metrics that should *not*
          be averaged over time. Metrics in this list will be displayed as-is.
          All others will be averaged by the progbar before display.
        interval: Minimum visual progress update interval (in seconds).
        unit_name: Display name for step counts (usually "step" or "sample").
    '''
    target: Incomplete
    width: Incomplete
    verbose: Incomplete
    interval: Incomplete
    unit_name: Incomplete
    stateful_metrics: Incomplete
    def __init__(self, target, width: int = 30, verbose: int = 1, interval: float = 0.05, stateful_metrics: Incomplete | None = None, unit_name: str = 'step') -> None: ...
    def update(self, current, values: Incomplete | None = None, finalize: Incomplete | None = None) -> None:
        """Updates the progress bar.

        Args:
            current: Index of current step.
            values: List of tuples: `(name, value_for_last_step)`. If `name` is
              in `stateful_metrics`, `value_for_last_step` will be displayed
              as-is. Else, an average of the metric over time will be
              displayed.
            finalize: Whether this is the last update for the progress bar. If
              `None`, defaults to `current >= self.target`.
        """
    def add(self, n, values: Incomplete | None = None) -> None: ...

def make_batches(size, batch_size):
    """Returns a list of batch indices (tuples of indices).

    Args:
        size: Integer, total size of the data to slice into batches.
        batch_size: Integer, batch size.

    Returns:
        A list of tuples of array indices.
    """
def slice_arrays(arrays, start: Incomplete | None = None, stop: Incomplete | None = None):
    """Slice an array or list of arrays.

    This takes an array-like, or a list of
    array-likes, and outputs:
        - arrays[start:stop] if `arrays` is an array-like
        - [x[start:stop] for x in arrays] if `arrays` is a list

    Can also work on list/array of indices: `slice_arrays(x, indices)`

    Args:
        arrays: Single array or list of arrays.
        start: can be an integer index (start index) or a list/array of indices
        stop: integer (stop index); should be None if `start` was a list.

    Returns:
        A slice of the array(s).

    Raises:
        ValueError: If the value of start is a list and stop is not None.
    """
def to_list(x):
    """Normalizes a list/tensor into a list.

    If a tensor is passed, we return
    a list of size 1 containing the tensor.

    Args:
        x: target object to be normalized.

    Returns:
        A list.
    """
def to_snake_case(name): ...
def is_all_none(structure): ...
def check_for_unexpected_keys(name, input_dict, expected_values) -> None: ...
def validate_kwargs(kwargs, allowed_kwargs, error_message: str = 'Keyword argument not understood:') -> None:
    """Checks that all keyword arguments are in the set of allowed keys."""
def default(method):
    """Decorates a method to detect overrides in subclasses."""
def is_default(method):
    """Check if a method is decorated with the `default` wrapper."""
def populate_dict_with_module_objects(target_dict, modules, obj_filter) -> None: ...

class LazyLoader(python_types.ModuleType):
    """Lazily import a module, mainly to avoid pulling in large dependencies."""
    def __init__(self, local_name, parent_module_globals, name) -> None: ...
    def __getattr__(self, item): ...
