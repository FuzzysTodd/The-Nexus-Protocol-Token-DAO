from _typeshed import Incomplete

class SaveSpec:
    """Class used to describe tensor slices that need to be saved."""
    slice_spec: Incomplete
    name: Incomplete
    dtype: Incomplete
    device: Incomplete
    def __init__(self, tensor, slice_spec, name, dtype: Incomplete | None = None, device: Incomplete | None = None) -> None:
        """Creates a `SaveSpec` object.

    Args:
      tensor: the tensor to save or callable that produces a tensor to save.
        If the value is `None`, the `SaveSpec` is ignored.
      slice_spec: the slice to be saved. See `Variable.SaveSliceInfo`.
      name: the name to save the tensor under.
      dtype: The data type of the Tensor. Required if `tensor` is callable.
        Used for error checking in the restore op.
      device: The device generating and consuming this tensor. Required if
        `tensor` is callable. Used to group objects to save by device.
    """
    @property
    def tensor(self): ...

class SaveableObject:
    """Base class for saving and restoring saveable objects."""
    op: Incomplete
    specs: Incomplete
    name: Incomplete
    def __init__(self, op, specs, name) -> None:
        '''Creates a `SaveableObject` object.

    Args:
      op: the "producer" object that this class wraps; it produces a list of
        tensors to save.  E.g., a "Variable" object saving its backing tensor.
      specs: a list of SaveSpec, each element of which describes one tensor to
        save under this object. All Tensors must be on the same device.
      name: the name to save the object under.
    '''
    @property
    def device(self):
        """The device for SaveSpec Tensors."""
    def restore(self, restored_tensors, restored_shapes) -> None:
        """Restores this object from 'restored_tensors'.

    Args:
      restored_tensors: the tensors that were loaded from a checkpoint
      restored_shapes: the shapes this object should conform to after
        restore, or None.

    Returns:
      An operation that restores the state of the object.

    Raises:
      ValueError: If the object cannot be restored using the provided
        parameters.
    """
