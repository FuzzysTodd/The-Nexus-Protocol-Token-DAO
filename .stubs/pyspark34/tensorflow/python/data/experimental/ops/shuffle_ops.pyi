from _typeshed import Incomplete
from tensorflow.python.data.experimental.ops import random_access as random_access
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import random_seed as random_seed
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_dataset_ops as gen_dataset_ops, math_ops as math_ops, stateless_random_ops as stateless_random_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

class _ShuffleAndRepeatDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that fuses `shuffle` and `repeat`."""
    def __init__(self, input_dataset, buffer_size, count: Incomplete | None = None, seed: Incomplete | None = None) -> None: ...

def shuffle_and_repeat(buffer_size, count: Incomplete | None = None, seed: Incomplete | None = None):
    """Shuffles and repeats a Dataset, reshuffling with each repetition.

  >>> d = tf.data.Dataset.from_tensor_slices([1, 2, 3])
  >>> d = d.apply(tf.data.experimental.shuffle_and_repeat(2, count=2))
  >>> [elem.numpy() for elem in d] # doctest: +SKIP
  [2, 3, 1, 1, 3, 2]

  ```python
  dataset.apply(
    tf.data.experimental.shuffle_and_repeat(buffer_size, count, seed))
  ```

  produces the same output as

  ```python
  dataset.shuffle(
    buffer_size, seed=seed, reshuffle_each_iteration=True).repeat(count)
  ```

  In each repetition, this dataset fills a buffer with `buffer_size` elements,
  then randomly samples elements from this buffer, replacing the selected
  elements with new elements. For perfect shuffling, set the buffer size equal
  to the full size of the dataset.

  For instance, if your dataset contains 10,000 elements but `buffer_size` is
  set to 1,000, then `shuffle` will initially select a random element from
  only the first 1,000 elements in the buffer. Once an element is selected,
  its space in the buffer is replaced by the next (i.e. 1,001-st) element,
  maintaining the 1,000 element buffer.

  Args:
    buffer_size: A `tf.int64` scalar `tf.Tensor`, representing the maximum
      number elements that will be buffered when prefetching.
    count: (Optional.) A `tf.int64` scalar `tf.Tensor`, representing the number
      of times the dataset should be repeated. The default behavior (if `count`
      is `None` or `-1`) is for the dataset be repeated indefinitely.
    seed: (Optional.) A `tf.int64` scalar `tf.Tensor`, representing the random
      seed that will be used to create the distribution. See
      `tf.random.set_seed` for behavior.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """
def index_shuffle(file_infos, reader_factory, seed: Incomplete | None = None, reshuffle_each_iteration: bool = False, num_parallel_calls=...):
    '''Creates a (globally) shuffled dataset from the given set of files.

  Unlike `tf.data.Dataset.shuffle()`, which uses an in-memory buffer to shuffle
  elements of input dataset in a streaming fashion,
  `tf.data.experimental.index_shuffle()` performs a global shuffle of element
  indices and then reads the data in a shuffled order. The advantage of
  `index_shuffle()` is that it can perform global shuffle of datasets that do
  not fit into memory (as long as the array of their indices does) and that the
  shuffling logic it provides is compatible with symbolic checkpointing. The
  disadvantage of `index_shuffle()` is that reading data in a shuffled random
  order will in general not be as efficient as reading data sequentially.

  Args:
    file_infos: A list of dictionaries that describe each file of the input
      dataset. Each dictionary is expected to contain the "path" key, which
      identifies the path of the file and the "num_elements" key, which
      identifies the number of elements in the file. In addition, the "skip"
      and "take" keys can be used to identify the number of elements to skip
      and take respectively. By default, no elements are skipped and all
      elements are taken.
    reader_factory: A function that maps a sequence of filenames to an instance
      of `tf.data.Dataset` that reads data from the files.
    seed: (Optional.) A `tf.int64` scalar `tf.Tensor`, representing the random
      seed that will be used to shuffle the order of elements. Default to
      non-deterministic seed.
    reshuffle_each_iteration: (Optional.) A `tf.bool` scalar `tf.Tensor`, that
      determines whether to change the shuffle order each iteration. Defaults to
      `False`.
    num_parallel_calls: (Optional.) A `tf.int64` scalar `tf.Tensor`, that
      determines the maximum number of random access operations to perform
      in parallel. By default, the tf.data runtime uses autotuning to determine
      the value dynamically.

  Returns:
    A `tf.data.Dataset` object, representing a globally shuffled dataset of
    the input data.
  '''
