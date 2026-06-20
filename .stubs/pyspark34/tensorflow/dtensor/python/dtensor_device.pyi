from _typeshed import Incomplete
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.dtensor.python import config as config, gen_dtensor_ops as gen_dtensor_ops, layout as layout_lib
from tensorflow.python.eager import context as context, core as core
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_util as tensor_util
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops
from typing import Any, List, Sequence, Set

class DTensorDevice:
    """Wraps a custom device which attempts to propagate tensor layouts."""
    name: Incomplete
    def __init__(self, meshes: List[layout_lib.Mesh], is_async: bool = True, in_flight_nodes_limit: int = 8) -> None:
        '''Create a new DTensorDevice which executes ops on `underlying_device`.

    Args:
      meshes: A list of `Mesh` objects indicating groups of devices to execute
        on. These may also be registered lazily.
      is_async: Indicates whether DTensor operations on this client will return
        immediately (with "non-ready" handles) or block until executed. This is
        on by default and is exposed as an option for ease of debugging.
      in_flight_nodes_limit: Indicates the limit of in-flight nodes before
        enqueueing of async operations to DTensorDevice is blocked. This limit
        is per mesh. 0 for no limits from DTensor. Default is 8.
    '''
    @property
    def meshes(self) -> Set[layout_lib.Mesh]: ...
    def copy_to_mesh(self, tensor, new_layout) -> ops.Tensor:
        """Copy `tensor` to `device` with the given layout."""
    def pack(self, tensors: Sequence[Any], layout: layout_lib.Layout) -> Any:
        """Packs tensors into a DTensor handle on this DTensor device.

    Packing and unpacking are inverse operations:

    ```
    * unpack(pack(tensors)) == tensors
    * pack(unpack(dtensor)) == dtensor
    ```

    Refer to `dtensor.pack` for more information.

    Args:
      tensors: The list of tensors to pack into a DTensor.
      layout: The layout of the DTensor to be created.

    Returns:
      A DTensor created from the individual component tensors.

    Raises:
      RuntimeError: When not called eagerly.
    """
    def unpack(self, dtensor: Any) -> Sequence[Any]:
        """Unpacks a DTensor handle on this DTensor device.

    Packing and unpacking are inverse operations:

    ```
    * unpack(pack(tensors)) == tensors
    * pack(unpack(dtensor)) == dtensor
    ```

    Refer to `dtensor.unpack` for more information.

    Args:
      dtensor: The DTensor to unpack.

    Returns:
      The raw underlying tensor components of the DTensor.

    Raises:
      RuntimeError: When not called eagerly.
    """
    def fetch_layout(self, dtensor: Any) -> layout_lib.Layout:
        """Fetches the layout of the DTensor.

    Args:
      dtensor: The DTensor whose layout is to be fetched.

    Returns:
      The `Layout` of this DTensor.

    Raises:
      RuntimeError: When not called eagerly.
    """
    def is_dtensor(self, tensor: Any) -> bool:
        """Check whether the input tensor is a DTensor.

    In Python, a DTensor has the same type as a `tf.Tensor`. This method will
    let you check and handle the tensor differently if a tf.Tensor is a DTensor.

    Args:
      tensor: an object to be checked.

    Returns:
      bool, True if the given tensor is a DTensor.
    """
    def set_same_shape_policy(self, enabled) -> None:
        """Guess layouts using the layouts of other tensors with the same shape.

    This is the default behavior, and is quite safe. The `default_layout` scope
    overrides shape-based guesses.

    Args:
      enabled: A boolean indicating whether to use the policy.
    """
    def set_tpu_core_ids(self, mesh_name, tpu_core_ids) -> None:
        """Sets the singleton global device ID-to-physical core ID map.

    Args:
      mesh_name: The name of a mesh. If empty, set the default mapping.
      tpu_core_ids: TPU core IDs sorted by TF task/device ordinal.
    """
    def clear_tpu_core_ids(self) -> None: ...
    def tpu_core_ids_to_locations(self, tpu_core_ids):
        """Translates TPU core IDs to TPU core locations.

    Args:
      tpu_core_ids: A list of TPU core IDs. Each one is an unsigned integer.

    Returns:
      A list of corresponding TPU core locations.
    """
    def tpu_core_locations_to_ids(self, tpu_core_locations):
        """Translates TPU core locations to TPU core IDs.

    Args:
      tpu_core_locations: A list of TPU core locations. Each one is a list of
        four unsigned integers, [x, y, z, core].

    Returns:
      A list of corresponding TPU core IDs.
    """
    def set_iterator_element_layouts(self, iterator_resource_dtensor, layouts: List[layout_lib.Layout]):
        """Sets the element layouts on an iterator resource tensor.

    Args:
      iterator_resource_dtensor: a DTensor created by packing the individiual
        iterator resource tensors.
      layouts: the flattened list of layouts to be applied to the elements
        emitted by the iterator resource DTensor.
    """
