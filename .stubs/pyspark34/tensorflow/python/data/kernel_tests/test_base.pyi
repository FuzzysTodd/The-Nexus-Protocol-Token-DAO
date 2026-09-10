from _typeshed import Incomplete
from tensorflow.python.data.experimental.ops import random_access as random_access
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest, structure as structure
from tensorflow.python.eager import context as context
from tensorflow.python.framework import combinations as combinations, config as config, constant_op as constant_op, dtypes as dtypes, errors as errors, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import array_ops as array_ops, gen_dataset_ops as gen_dataset_ops, gen_experimental_dataset_ops as gen_experimental_dataset_ops, lookup_ops as lookup_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.platform import test as test

def default_test_combinations():
    """Returns the default test combinations for tf.data tests."""
def eager_only_combinations():
    """Returns the default test combinations for eager mode only tf.data tests."""
def graph_only_combinations():
    """Returns the default test combinations for graph mode only tf.data tests."""
def v1_only_combinations():
    """Returns the default test combinations for v1 only tf.data tests."""
def v2_only_combinations():
    """Returns the default test combinations for v2 only tf.data tests."""
def v2_eager_only_combinations():
    """Returns the default test combinations for v2 eager only tf.data tests."""

class DatasetTestBase(test.TestCase):
    """Base class for dataset tests."""
    def assert_op_cancelled(self, op) -> None: ...
    def assertValuesEqual(self, expected, actual) -> None:
        """Asserts that two values are equal."""
    def getNext(self, dataset, requires_initialization: bool = False, shared_name: Incomplete | None = None):
        """Returns a callable that returns the next element of the dataset.

    Example use:
    ```python
    # In both graph and eager modes
    dataset = ...
    get_next = self.getNext(dataset)
    result = self.evaluate(get_next())
    ```

    Args:
      dataset: A dataset whose elements will be returned.
      requires_initialization: Indicates that when the test is executed in graph
        mode, it should use an initializable iterator to iterate through the
        dataset (e.g. when it contains stateful nodes). Defaults to False.
      shared_name: (Optional.) If non-empty, the returned iterator will be
        shared under the given name across multiple sessions that share the same
        devices (e.g. when using a remote server).
    Returns:
      A callable that returns the next element of `dataset`. Any `TensorArray`
      objects `dataset` outputs are stacked.
    """
    def getDatasetOutput(self, dataset, requires_initialization: bool = False): ...
    def getIteratorOutput(self, get_next):
        """Evaluates `get_next` until end of input, returning the results."""
    def assertDatasetProduces(self, dataset, expected_output: Incomplete | None = None, expected_shapes: Incomplete | None = None, expected_error: Incomplete | None = None, requires_initialization: bool = False, num_test_iterations: int = 1, assert_items_equal: bool = False, expected_error_iter: int = 1) -> None:
        """Asserts that a dataset produces the expected output / error.

    Args:
      dataset: A dataset to check for the expected output / error.
      expected_output: A list of elements that the dataset is expected to
        produce.
      expected_shapes: A list of TensorShapes which is expected to match
        output_shapes of dataset.
      expected_error: A tuple `(type, predicate)` identifying the expected error
        `dataset` should raise. The `type` should match the expected exception
        type, while `predicate` should either be 1) a unary function that inputs
        the raised exception and returns a boolean indicator of success or 2) a
        regular expression that is expected to match the error message
        partially.
      requires_initialization: Indicates that when the test is executed in graph
        mode, it should use an initializable iterator to iterate through the
        dataset (e.g. when it contains stateful nodes). Defaults to False.
      num_test_iterations: Number of times `dataset` will be iterated. Defaults
        to 1.
      assert_items_equal: Tests expected_output has (only) the same elements
        regardless of order.
      expected_error_iter: How many times to iterate before expecting an error,
        if an error is expected.
    """
    def assertDatasetsEqual(self, dataset1, dataset2) -> None:
        """Checks that datasets are equal. Supports both graph and eager mode."""
    def assertDatasetsRaiseSameError(self, dataset1, dataset2, exception_class, replacements: Incomplete | None = None) -> None:
        """Checks that datasets raise the same error on the first get_next call."""
    def structuredDataset(self, dataset_structure, shape: Incomplete | None = None, dtype=...):
        """Returns a singleton dataset with the given structure."""
    def verifyRandomAccess(self, dataset, expected) -> None: ...
    def verifyRandomAccessInfiniteCardinality(self, dataset, expected) -> None:
        """Tests randomly accessing elements of a dataset."""
    def textFileInitializer(self, vals): ...
    def keyValueTensorInitializer(self, vals): ...
    def datasetInitializer(self, vals): ...
    def lookupTableInitializer(self, init_source, vals):
        '''Returns a lookup table initializer for the given source and values.

    Args:
      init_source: One of ["textfile", "keyvalue", "dataset"], indicating what
        type of initializer to use.
      vals: The initializer values. The keys will be `range(len(vals))`.
    '''
    def graphRoundTrip(self, dataset, allow_stateful: bool = False):
        """Converts a dataset to a graph and back."""
    def structuredElement(self, element_structure, shape: Incomplete | None = None, dtype=...):
        """Returns an element with the given structure."""
    def checkDeterminism(self, dataset_fn, expect_determinism, expected_elements) -> None:
        """Tests whether a dataset produces its elements deterministically.

    `dataset_fn` takes a delay_ms argument, which tells it how long to delay
    production of the first dataset element. This gives us a way to trigger
    out-of-order production of dataset elements.

    Args:
      dataset_fn: A function taking a delay_ms argument.
      expect_determinism: Whether to expect deterministic ordering.
      expected_elements: The elements expected to be produced by the dataset,
        assuming the dataset produces elements in deterministic order.
    """
    def configureDevicesForMultiDeviceTest(self, num_devices):
        """Configures number of logical devices for multi-device tests.

    It returns a list of device names. If invoked in GPU-enabled runtime, the
    last device name will be for a GPU device. Otherwise, all device names will
    be for a CPU device.

    Args:
      num_devices: The number of devices to configure.

    Returns:
      A list of device names to use for a multi-device test.
    """
