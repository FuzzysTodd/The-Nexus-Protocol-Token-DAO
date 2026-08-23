import tensorflow as tf
from _typeshed import Incomplete

fn_args: Incomplete
MAX_DIRECTORY_CREATION_ATTEMPTS: int

def parse_input_fn_result(result):
    """Gets features, labels, and hooks from the result of an Estimator input_fn.

  Args:
    result: output of an input_fn to an estimator, which should be one of:
      * A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a tuple
        (features, labels) with same constraints as below.
      * A tuple (features, labels): Where `features` is a `Tensor` or a
        dictionary of string feature name to `Tensor` and `labels` is a `Tensor`
        or a dictionary of string label name to `Tensor`. Both `features` and
        `labels` are consumed by `model_fn`. They should satisfy the expectation
        of `model_fn` from inputs.

  Returns:
    Tuple of features, labels, and input_hooks, where features are as described
    above, labels are as described above or None, and input_hooks are a list
    of SessionRunHooks to be included when running.

  Raises:
    ValueError: if the result is a list or tuple of length != 2.
  """
def parse_iterator_result(result):
    """Gets features, labels from result."""

class _DatasetInitializerHook(tf.compat.v1.train.SessionRunHook):
    """Creates a SessionRunHook that initializes the passed iterator."""
    def __init__(self, iterator) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...

class DistributedIteratorInitializerHook(tf.compat.v1.train.SessionRunHook):
    """Creates a SessionRunHook that initializes the passed iterator."""
    def __init__(self, iterator) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...

class MultiHostDatasetInitializerHook(tf.compat.v1.train.SessionRunHook):
    """Creates a SessionRunHook that initializes all passed iterators."""
    def __init__(self, dataset_initializers) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
