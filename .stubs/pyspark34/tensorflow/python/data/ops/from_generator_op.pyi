from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, structured_function as structured_function
from tensorflow.python.data.util import nest as nest, structure as structure
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops, script_ops as script_ops

class _GeneratorDataset(dataset_ops.DatasetSource):
    """A `Dataset` that generates elements by invoking a function."""
    def __init__(self, init_args, init_func, next_func, finalize_func, output_signature, name: Incomplete | None = None) -> None:
        '''Constructs a `_GeneratorDataset`.

    Args:
      init_args: A (nested) structure representing the arguments to `init_func`.
      init_func: A TensorFlow function that will be called on `init_args` each
        time a C++ iterator over this dataset is constructed. Returns a (nested)
        structure representing the "state" of the dataset.
      next_func: A TensorFlow function that will be called on the result of
        `init_func` to produce each element, and that raises `OutOfRangeError`
        to terminate iteration.
      finalize_func: A TensorFlow function that will be called on the result of
        `init_func` immediately before a C++ iterator over this dataset is
        destroyed. The return value is ignored.
      output_signature: A (nested) structure of `tf.TypeSpec` objects describing
        the output of `next_func`.
      name: Optional. A name for the tf.data transformation.
    '''
    @property
    def element_spec(self): ...
