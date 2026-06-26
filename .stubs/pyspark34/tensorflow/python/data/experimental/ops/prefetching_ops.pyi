from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops, structured_function as structured_function
from tensorflow.python.data.util import structure as structure
from tensorflow.python.eager import def_function as def_function, function as function
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import array_ops as array_ops, functional_ops as functional_ops, gen_dataset_ops as gen_dataset_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

def prefetch_to_device(device, buffer_size: Incomplete | None = None):
    '''A transformation that prefetches dataset values to the given `device`.

  NOTE: Although the transformation creates a `tf.data.Dataset`, the
  transformation must be the final `Dataset` in the input pipeline.

  For example,
  >>> dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])
  >>> dataset = dataset.apply(tf.data.experimental.prefetch_to_device("/cpu:0"))
  >>> for element in dataset:
  ...   print(f\'Tensor {element} is on device {element.device}\')
  Tensor 1 is on device /job:localhost/replica:0/task:0/device:CPU:0
  Tensor 2 is on device /job:localhost/replica:0/task:0/device:CPU:0
  Tensor 3 is on device /job:localhost/replica:0/task:0/device:CPU:0

  Args:
    device: A string. The name of a device to which elements will be prefetched.
    buffer_size: (Optional.) The number of elements to buffer on `device`.
      Defaults to an automatically chosen value.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  '''
def copy_to_device(target_device, source_device: str = '/cpu:0'):
    """A transformation that copies dataset elements to the given `target_device`.

  Args:
    target_device: The name of a device to which elements will be copied.
    source_device: The original device on which `input_dataset` will be placed.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """

class _CopyToDeviceDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that copies elements to another device."""
    def __init__(self, input_dataset, target_device, source_device: str = '/cpu:0') -> None:
        """Constructs a _CopyToDeviceDataset.

    Args:
      input_dataset: `Dataset` to be copied
      target_device: The name of the device to which elements would be copied.
      source_device: Device where input_dataset would be placed.
    """
    def make_one_shot_iterator(self): ...

class _MapOnGpuDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that maps a function over elements in its using a GPU."""
    def __init__(self, input_dataset, map_func, use_inter_op_parallelism: bool = True) -> None:
        """See `Dataset.map()` for details."""
    @property
    def element_spec(self): ...

def map_on_gpu(map_func):
    """Maps `map_func` across the elements of this dataset.

  NOTE: This is a highly experimental version of `tf.data.Dataset.map` that runs
  `map_func` on GPU. It must be used after applying the
  `tf.data.experimental.copy_to_device` transformation with a GPU device
  argument.

  Args:
    map_func: A function mapping a nested structure of tensors (having shapes
      and types defined by `self.output_shapes` and `self.output_types`) to
      another nested structure of tensors.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """
