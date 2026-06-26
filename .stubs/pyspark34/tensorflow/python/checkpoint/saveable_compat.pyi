def legacy_saveable_name(name):
    '''Decorator to set the local name to use in the Checkpoint.

  Needed for migrating certain Trackables (see next paragraph) from the legacy
  `_gather_saveables_for_checkpoint` to the new `_serialize_to_tensors`
  function.

  This decorator should be used if the SaveableObject generates tensors with
  different names from the name that is passed to the factory.

  Example migration:

  *Before*

  ```
  class MyTrackable(Trackable):
    def _gather_saveables_for_checkpoint(self):
      return {"key": _MySaveable}

  class _MySaveable(SaveableObject):
    def __init__(self, name):
      specs = [
          SaveSpec(tensor1, "", name + "-1")
          SaveSpec(tensor2, "", name + "-2")
      ]
      super().__init__(None, specs, name)
  ```

  *After*

  ```
  @legacy_saveable_name("key")
  class MyTrackable(Trackable):

    def _serialize_to_tensors(self):
      return {"key-1": tensor1, "key-2": tensor2}
  ```

  Args:
    name: String name of the SaveableObject factory (the key returned in the
       `_gather_saveables_for_checkpoint` function)

  Returns:
    A decorator.
  '''
def get_saveable_name(cls_or_obj): ...
def force_checkpoint_conversion(value: bool = True) -> None:
    """Forces checkpoint to use the new implementation.

  The new checkpoint implementation is changing the saved metadata slightly,
  and therefore may break forward compatibility in newly saved checkpoints. This
  means:

    - Previous versions of TensorFlow may not be able to load new checkpoints.
    - Backwards compatibility is unchanged: Old checkpoints can still be loaded.

  TensorFlow guarantees 3 weeks of forward compatibility, so this flag will be
  removed in the future weeks, after which checkpoint conversion will happen by
  default.

  **What happens when this flag is enabled?**

  The checkpoint will be saved with different metadata, meaning that previous
  versions of TensorFlow (<=2.10) will not be able to load this checkpoint.

  Args:
    value: Boolean value, whether or not to force checkpoint conversion to the
      new implementation.
  """
def force_checkpoint_conversion_enabled(): ...

class CheckpointConversionError(Exception): ...
