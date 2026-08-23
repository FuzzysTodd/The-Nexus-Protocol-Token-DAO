from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

INFINITE: int
UNKNOWN: int

def cardinality(dataset):
    """Returns the cardinality of `dataset`, if known.

  The operation returns the cardinality of `dataset`. The operation may return
  `tf.data.experimental.INFINITE_CARDINALITY` if `dataset` contains an infinite
  number of elements or `tf.data.experimental.UNKNOWN_CARDINALITY` if the
  analysis fails to determine the number of elements in `dataset` (e.g. when the
  dataset source is a file).

  >>> dataset = tf.data.Dataset.range(42)
  >>> print(tf.data.experimental.cardinality(dataset).numpy())
  42
  >>> dataset = dataset.repeat()
  >>> cardinality = tf.data.experimental.cardinality(dataset)
  >>> print((cardinality == tf.data.experimental.INFINITE_CARDINALITY).numpy())
  True
  >>> dataset = dataset.filter(lambda x: True)
  >>> cardinality = tf.data.experimental.cardinality(dataset)
  >>> print((cardinality == tf.data.experimental.UNKNOWN_CARDINALITY).numpy())
  True

  Args:
    dataset: A `tf.data.Dataset` for which to determine cardinality.

  Returns:
    A scalar `tf.int64` `Tensor` representing the cardinality of `dataset`. If
    the cardinality is infinite or unknown, the operation returns the named
    constant `INFINITE_CARDINALITY` and `UNKNOWN_CARDINALITY` respectively.
  """
def assert_cardinality(expected_cardinality):
    '''Asserts the cardinality of the input dataset.

  NOTE: The following assumes that "examples.tfrecord" contains 42 records.

  >>> dataset = tf.data.TFRecordDataset("examples.tfrecord")
  >>> cardinality = tf.data.experimental.cardinality(dataset)
  >>> print((cardinality == tf.data.experimental.UNKNOWN_CARDINALITY).numpy())
  True
  >>> dataset = dataset.apply(tf.data.experimental.assert_cardinality(42))
  >>> print(tf.data.experimental.cardinality(dataset).numpy())
  42

  Args:
    expected_cardinality: The expected cardinality of the input dataset.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.

  Raises:
    FailedPreconditionError: The assertion is checked at runtime (when iterating
      the dataset) and an error is raised if the actual and expected cardinality
      differ.
  '''

class _AssertCardinalityDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that assert the cardinality of its input."""
    def __init__(self, input_dataset, expected_cardinality) -> None: ...
