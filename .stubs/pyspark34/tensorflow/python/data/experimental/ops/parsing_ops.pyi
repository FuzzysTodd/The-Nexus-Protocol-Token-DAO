from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import structure as structure
from tensorflow.python.framework import dtypes as dtypes, sparse_tensor as sparse_tensor, tensor_spec as tensor_spec
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops, parsing_ops as parsing_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

class _ParseExampleDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that parses `example` dataset into a `dict` dataset."""
    def __init__(self, input_dataset, features, num_parallel_calls, deterministic) -> None: ...
    @property
    def element_spec(self): ...

def parse_example_dataset(features, num_parallel_calls: int = 1, deterministic: Incomplete | None = None):
    """A transformation that parses `Example` protos into a `dict` of tensors.

  Parses a number of serialized `Example` protos given in `serialized`. We refer
  to `serialized` as a batch with `batch_size` many entries of individual
  `Example` protos.

  This op parses serialized examples into a dictionary mapping keys to `Tensor`,
  `SparseTensor`, and `RaggedTensor` objects. `features` is a dict from keys to
  `VarLenFeature`, `RaggedFeature`, `SparseFeature`, and `FixedLenFeature`
  objects. Each `VarLenFeature` and `SparseFeature` is mapped to a
  `SparseTensor`; each `RaggedFeature` is mapped to a `RaggedTensor`; and each
  `FixedLenFeature` is mapped to a `Tensor`. See `tf.io.parse_example` for more
  details about feature dictionaries.

  Args:
   features: A `dict` mapping feature keys to `FixedLenFeature`,
     `VarLenFeature`, `RaggedFeature`, and `SparseFeature` values.
   num_parallel_calls: (Optional.) A `tf.int32` scalar `tf.Tensor`,
      representing the number of parsing processes to call in parallel.
   deterministic: (Optional.) A boolean controlling whether determinism
      should be traded for performance by allowing elements to be produced out
      of order if some parsing calls complete faster than others. If
      `deterministic` is `None`, the
      `tf.data.Options.deterministic` dataset option (`True` by default) is used
      to decide whether to produce elements deterministically.

  Returns:
    A dataset transformation function, which can be passed to
    `tf.data.Dataset.apply`.

  Raises:
    ValueError: if features argument is None.
  """
