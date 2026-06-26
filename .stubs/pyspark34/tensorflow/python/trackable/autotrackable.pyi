from tensorflow.python.eager import def_function as def_function
from tensorflow.python.trackable import base as base, data_structures as data_structures
from tensorflow.python.util.tf_export import tf_export as tf_export

class AutoTrackable(base.Trackable):
    '''Manages dependencies on other objects.

  `Trackable` objects may have dependencies: other `Trackable` objects
  which should be saved if the object declaring the dependency is saved. A
  correctly saveable program has a dependency graph such that if changing a
  global variable affects an object (e.g. changes the behavior of any of its
  methods) then there is a chain of dependencies from the influenced object to
  the variable.

  Dependency edges have names, and are created implicitly when a
  `Trackable` object is assigned to an attribute of another
  `Trackable` object. For example:

  ```
  obj = Trackable()
  obj.v = ResourceVariable(0.)
  ```

  The `Trackable` object `obj` now has a dependency named "v" on a
  variable.

  `Trackable` objects may specify `Tensor`s to be saved and restored
  directly (e.g. a `Variable` indicating how to save itself) rather than through
  dependencies on other objects. See
  `Trackable._gather_saveables_for_checkpoint` for details.
  '''
    def __setattr__(self, name, value) -> None:
        """Support self.foo = trackable syntax."""
    def __delattr__(self, name) -> None: ...
