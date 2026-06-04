from collections.abc import Generator
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import ops as ops
from tensorflow.python.trackable import base as base
from tensorflow.python.util import tf_contextlib as tf_contextlib
from tensorflow.python.util.tf_export import tf_export as tf_export

class ResourceTracker:
    """An object that tracks a list of resources."""
    def __init__(self) -> None: ...
    @property
    def resources(self): ...
    def add_resource(self, resource) -> None: ...

def resource_tracker_scope(resource_tracker) -> Generator[None, None, None]:
    """A context to manage resource trackers.

  Use this in order to collect up all resources created within a block of code.
  Example usage:

  ```python
  resource_tracker = ResourceTracker()
  with resource_tracker_scope(resource_tracker):
    resource = TrackableResource()

  assert resource_tracker.resources == [resource]

  Args:
    resource_tracker: The passed in ResourceTracker object

  Yields:
    A scope in which the resource_tracker is active.
  """

class _ResourceMetaclass(type):
    """Metaclass for CapturableResource."""
    def __call__(cls, *args, **kwargs): ...

class CapturableResource(base.Trackable, metaclass=_ResourceMetaclass):
    """Holds a Tensor which a tf.function can capture.

  `CapturableResource`s are discovered by traversing the graph of object
  attributes, e.g. during `tf.saved_model.save`. They are excluded from the
  scope-based tracking of `TrackableResource`; generally things that require
  initialization should inherit from `TrackableResource` instead of
  `CapturableResource` directly.
  """
    def __init__(self, device: str = '') -> None:
        '''Initialize the `CapturableResource`.

    Args:
      device: A string indicating a required placement for this resource,
        e.g. "CPU" if this resource must be created on a CPU device. A blank
        device allows the user to place resource creation, so generally this
        should be blank unless the resource only makes sense on one device.
    '''
    @property
    def resource_handle(self):
        """Returns the resource handle associated with this Resource."""
    def __del__(self) -> None: ...

class TrackableResource(CapturableResource):
    """Holds a Tensor which a tf.function can capture.

  A TrackableResource is most useful for stateful Tensors that require
  initialization, such as `tf.lookup.StaticHashTable`. `TrackableResource`s
  are discovered by traversing the graph of object attributes, e.g. during
  `tf.saved_model.save`.

  A TrackableResource has three methods to override:

  * `_create_resource` should create the resource tensor handle.
  * `_initialize` should initialize the resource held at `self.resource_handle`.
  * `_destroy_resource` is called upon a `TrackableResource`'s destruction
    and should decrement the resource's ref count. For most resources, this
    should be done with a call to `tf.raw_ops.DestroyResourceOp`.

  Example usage:

  >>> class DemoResource(tf.saved_model.experimental.TrackableResource):
  ...   def __init__(self):
  ...     super().__init__()
  ...     self._initialize()
  ...   def _create_resource(self):
  ...     return tf.raw_ops.VarHandleOp(dtype=tf.float32, shape=[2])
  ...   def _initialize(self):
  ...     tf.raw_ops.AssignVariableOp(
  ...         resource=self.resource_handle, value=tf.ones([2]))
  ...   def _destroy_resource(self):
  ...     tf.raw_ops.DestroyResourceOp(resource=self.resource_handle)
  >>> class DemoModule(tf.Module):
  ...   def __init__(self):
  ...     self.resource = DemoResource()
  ...   def increment(self, tensor):
  ...     return tensor + tf.raw_ops.ReadVariableOp(
  ...         resource=self.resource.resource_handle, dtype=tf.float32)
  >>> demo = DemoModule()
  >>> demo.increment([5, 1])
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([6., 2.], dtype=float32)>
  """
    def __init__(self, device: str = '') -> None:
        '''Initialize the `TrackableResource`.

    Args:
      device: A string indicating a required placement for this resource,
        e.g. "CPU" if this resource must be created on a CPU device. A blank
        device allows the user to place resource creation, so generally this
        should be blank unless the resource only makes sense on one device.
    '''

class RestoredResource(TrackableResource):
    """Restored SavedResource."""
    def __init__(self, device: str = '') -> None: ...
