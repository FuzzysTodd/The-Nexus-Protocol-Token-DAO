from _typeshed import Incomplete
from tensorflow.python.checkpoint import checkpoint_management as checkpoint_management
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.eager import context as context
from tensorflow.python.framework import combinations as combinations, dtypes as dtypes, errors as errors, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import lookup_ops as lookup_ops, variables as variables
from tensorflow.python.ops.ragged import ragged_tensor_value as ragged_tensor_value
from tensorflow.python.platform import gfile as gfile, test as test
from tensorflow.python.util import nest as nest

def remove_variants(get_next_op):
    """Remove variants from a nest structure, so sess.run will execute."""
def default_test_combinations():
    """Returns the default test combinations for testing checkpointing."""

class CheckpointTestBase(test.TestCase):
    """Base test class for checkpointing datasets."""
    def tearDown(self) -> None: ...
    def verify_unused_iterator(self, ds_fn, num_outputs, sparse_tensors: bool = False, verify_exhausted: bool = True) -> None:
        """Verifies that saving and restoring an unused iterator works.

    Args:
      ds_fn: 0-argument function that returns a Dataset.
      num_outputs: Total number of outputs expected from this Dataset.
      sparse_tensors: Whether dataset is built from SparseTensor(s).
      verify_exhausted: Whether to verify that the iterator has been exhausted
        after producing `num_outputs` elements.

    Raises:
      AssertionError if any test fails.
    """
    def verify_fully_used_iterator(self, ds_fn, num_outputs, sparse_tensors: bool = False) -> None:
        """Verifies that saving and restoring a fully used iterator works.

    Note that this only checks saving and restoring an iterator from which
    `num_outputs` items have been produced but does not check for an
    exhausted iterator, i.e., one from which an OutOfRange error has been
    returned.

    Args:
      ds_fn: 0-argument function that returns a Dataset.
      num_outputs: Total number of outputs expected from this Dataset.
      sparse_tensors: Whether dataset is built from SparseTensor(s).

    Raises:
      AssertionError if test fails.
    """
    def verify_exhausted_iterator(self, ds_fn, num_outputs, sparse_tensors: bool = False) -> None:
        """Verifies that saving and restoring an exhausted iterator works.

    An exhausted iterator is one which has returned an OutOfRange error.

    Args:
      ds_fn: 0-argument function that returns a Dataset.
      num_outputs: Total number of outputs expected from this Dataset.
      sparse_tensors: Whether dataset is built from SparseTensor(s).

    Raises:
      AssertionError if any test fails.
    """
    def verify_multiple_breaks(self, ds_fn, num_outputs, num_breaks: int = 10, sparse_tensors: bool = False, verify_exhausted: bool = True) -> None:
        """Attempts to save/restore at multiple break points.

    Args:
      ds_fn: 0-argument function that returns a Dataset.
      num_outputs: Total number of outputs expected from this Dataset.
      num_breaks: The number of break points. These are uniformly spread in [0,
        num_outputs] both inclusive.
      sparse_tensors: Whether dataset is built from SparseTensor(s).
      verify_exhausted: Whether to verify that the iterator has been exhausted
        after producing `num_outputs` elements.

    Raises:
      AssertionError if any test fails.
    """
    def verify_reset_restored_iterator(self, ds_fn, num_outputs, break_point: Incomplete | None = None, sparse_tensors: bool = False, verify_exhausted: bool = True) -> None:
        """Attempts to re-initialize a restored iterator.

    This is useful when restoring a training checkpoint during validation.

    Args:
      ds_fn: 0-argument function that returns a Dataset.
      num_outputs: Total number of outputs expected from this Dataset.
      break_point: Break point. Optional. Defaults to num_outputs/2.
      sparse_tensors: Whether dataset is built from SparseTensor(s).
      verify_exhausted: Whether to verify that the iterator has been exhausted
        after producing `num_outputs` elements.

    Raises:
      AssertionError if any test fails.
    """
    def verify_error_on_save(self, ds_fn, num_outputs, error, break_point: Incomplete | None = None, sparse_tensors: bool = False) -> None:
        """Attempts to save a non-saveable iterator.

    Args:
      ds_fn: 0-argument function that returns a Dataset.
      num_outputs: Total number of outputs expected from this Dataset.
      error: Declared error when trying to save iterator.
      break_point: Break point. Optional. Defaults to num_outputs/2.
      sparse_tensors: Whether dataset is built from SparseTensor(s).

    Raises:
      AssertionError if any test fails.
    """
    def verify_run_with_breaks(self, ds_fn, break_points, num_outputs, sparse_tensors: bool = False, verify_exhausted: bool = True) -> None:
        """Verifies that ds_fn() produces the same outputs with and without breaks.

    1. Builds a Dataset using `ds_fn` and produces `num_outputs` items from it
       *without* stopping at break points.
    2. Builds a Dataset using `ds_fn` and produces `num_outputs` items from it
       with stopping at break points.

    Deep matches outputs from 1 and 2.

    Args:
      ds_fn: 0-argument function that returns a Dataset.
      break_points: A list of integers. For each `break_point` in
        `break_points`, we produce outputs till `break_point` number of items
        have been produced and then checkpoint the state. The current graph and
        session are destroyed and a new graph and session are used to produce
        outputs till next checkpoint or till `num_outputs` elements have been
        produced. `break_point` must be <= `num_outputs`.
      num_outputs: Total number of outputs expected from this Dataset.
      sparse_tensors: Whether dataset is built from SparseTensor(s).
      verify_exhausted: Whether to verify that the iterator has been exhausted
        after producing `num_outputs` elements.

    Raises:
      AssertionError if any test fails.
    """
    def gen_outputs(self, ds_fn, break_points, num_outputs, ckpt_saved: bool = False, sparse_tensors: bool = False, verify_exhausted: bool = True, save_checkpoint_at_end: bool = True):
        """Generates elements from input dataset while stopping at break points.

    Produces `num_outputs` outputs and saves the state of the iterator in the
    Saver checkpoint.

    Args:
      ds_fn: 0-argument function that returns the dataset.
      break_points: A list of integers. For each `break_point` in
        `break_points`, we produce outputs till `break_point` number of items
        have been produced and then checkpoint the state. The current graph and
        session are destroyed and a new graph and session are used to produce
        outputs till next checkpoint or till `num_outputs` elements have been
        produced. `break_point` must be <= `num_outputs`.
      num_outputs: The total number of outputs to produce from the iterator.
      ckpt_saved: Whether a checkpoint already exists.
      sparse_tensors:  Whether dataset is built from SparseTensor(s).
      verify_exhausted: Whether to verify that the iterator has been exhausted
        after producing `num_outputs` elements.
      save_checkpoint_at_end: Whether to save a checkpoint after producing all
        outputs. If False, checkpoints are saved each break point but not at the
        end. Note that checkpoints overwrite each other so there is always only
        a single checkpoint available. Defaults to True.

    Returns:
      A list of `num_outputs` items.
    """
    def match(self, expected, actual) -> None:
        """Matches nested structures.

    Recursively matches shape and values of `expected` and `actual`.
    Handles scalars, numpy arrays and other python sequence containers
    e.g. list, dict, as well as SparseTensorValue and RaggedTensorValue.

    Args:
      expected: Nested structure 1.
      actual: Nested structure 2.

    Raises:
      AssertionError if matching fails.
    """
    def does_not_match(self, expected, actual) -> None: ...
    def gen_break_points(self, num_outputs, num_samples: int = 10):
        """Generates `num_samples` unique break points in [0, num_outputs]."""
