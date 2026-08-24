from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops, prefetch_op as prefetch_op
from tensorflow.python.data.util import structure as structure
from tensorflow.python.eager import context as context, def_function as def_function, function as function
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, errors as errors, ops as ops, tensor_spec as tensor_spec, type_spec as type_spec, type_utils as type_utils
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, functional_ops as functional_ops, gen_dataset_ops as gen_dataset_ops, resource_variable_ops as resource_variable_ops

class _PerDeviceGenerator(dataset_ops.DatasetV2):
    """A `dummy` generator dataset."""
    def __init__(self, shard_num, multi_device_iterator_resource, incarnation_id, source_device, element_spec, iterator_is_anonymous) -> None: ...
    @property
    def element_spec(self): ...

class _ReincarnatedPerDeviceGenerator(dataset_ops.DatasetV2):
    """Creates a _PerDeviceGenerator-like dataset with a new incarnation_id.

  Re-uses the functions from the provided per_device_dataset and just switches
  out the function argument corresponding to the incarnation_id.
  """
    def __init__(self, per_device_dataset, incarnation_id) -> None: ...
    @property
    def element_spec(self): ...

class MultiDeviceIterator:
    """An iterator over multiple devices."""
    def __init__(self, dataset, devices, max_buffer_size: int = 1, prefetch_buffer_size: int = 1, source_device: str = '/cpu:0') -> None:
        """Constructs a MultiDeviceIterator.

    Args:
      dataset: The input dataset to be iterated over.
      devices: The list of devices to fetch data to.
      max_buffer_size: Maximum size of the host side per device buffer to keep.
      prefetch_buffer_size: if > 0, then we setup a buffer on each device to
        prefetch into.
      source_device: The host device to place the `dataset` on.  In order to
        prevent deadlocks, if the prefetch_buffer_size is greater than the
        max_buffer_size, we set the max_buffer_size to prefetch_buffer_size.
    """
    def get_next(self, device: Incomplete | None = None):
        """Returns the next element given a `device`, else returns all in a list."""
    def get_next_as_optional(self): ...
    @property
    def initializer(self): ...
    @property
    def element_spec(self): ...

class MultiDeviceIteratorSpec(type_spec.TypeSpec):
    """Type specification for `OwnedMultiDeviceIterator`."""
    def __init__(self, devices, source_device, element_spec) -> None: ...
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value): ...

class OwnedMultiDeviceIterator(composite_tensor.CompositeTensor):
    """An iterator over multiple devices.

  The multi-device iterator resource created through `OwnedMultiDeviceIterator`
  is owned by the Python object and the life time of the underlying resource is
  tied to the life time of the `OwnedMultiDeviceIterator` object. This makes
  `OwnedMultiDeviceIterator` appropriate for use in eager mode and inside of
  tf.functions.
  """
    def __init__(self, dataset: Incomplete | None = None, devices: Incomplete | None = None, max_buffer_size: int = 1, prefetch_buffer_size: int = 1, source_device: str = '/cpu:0', components: Incomplete | None = None, element_spec: Incomplete | None = None) -> None:
        """Constructs an owned MultiDeviceIterator object.

    Args:
      dataset: The input dataset to be iterated over.
      devices: (Required.) The list of devices to fetch data to.
      max_buffer_size: Maximum size of the host side per device buffer to keep.
      prefetch_buffer_size: if > 0, then we setup a buffer on each device to
        prefetch into.
      source_device: The host device to place the `dataset` on.  In order to
        prevent deadlocks, if the prefetch_buffer_size is greater than the
        max_buffer_size, we set the max_buffer_size to prefetch_buffer_size.
      components: Tensor components to construct the MultiDeviceIterator from.
      element_spec: A (nested) structure of `tf.TypeSpec` objects that
        represents the type specification of elements of the iterator.

    Raises:
      RuntimeError: If executed in graph mode or outside of function building
        mode.
      ValueError: If any of the following happens:
        - `devices` is `None`
        - `dataset` is `None` and either `components` or `element_spec` is
          `None`
        - `dataset` is not None and either `components` or `element_spec` is
          provided
    """
    def get_next(self, device: Incomplete | None = None):
        """Returns the next element given a `device`, else returns all in a list."""
    def __iter__(self): ...
    def next(self): ...
    def __next__(self): ...
    def get_next_as_optional(self): ...
    @property
    def element_spec(self): ...
