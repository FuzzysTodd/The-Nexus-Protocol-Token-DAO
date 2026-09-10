from _typeshed import Incomplete
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.util.tf_export import tf_export as tf_export

class DeviceSpecV2:
    '''Represents a (possibly partial) specification for a TensorFlow device.

  `DeviceSpec`s are used throughout TensorFlow to describe where state is stored
  and computations occur. Using `DeviceSpec` allows you to parse device spec
  strings to verify their validity, merge them or compose them programmatically.

  Example:

  ```python
  # Place the operations on device "GPU:0" in the "ps" job.
  device_spec = DeviceSpec(job="ps", device_type="GPU", device_index=0)
  with tf.device(device_spec.to_string()):
    # Both my_var and squared_var will be placed on /job:ps/device:GPU:0.
    my_var = tf.Variable(..., name="my_variable")
    squared_var = tf.square(my_var)
  ```

  With eager execution disabled (by default in TensorFlow 1.x and by calling
  disable_eager_execution() in TensorFlow 2.x), the following syntax
  can be used:

  ```python
  tf.compat.v1.disable_eager_execution()

  # Same as previous
  device_spec = DeviceSpec(job="ps", device_type="GPU", device_index=0)
  # No need of .to_string() method.
  with tf.device(device_spec):
    my_var = tf.Variable(..., name="my_variable")
    squared_var = tf.square(my_var)
  ```

  If a `DeviceSpec` is partially specified, it will be merged with other
  `DeviceSpec`s according to the scope in which it is defined. `DeviceSpec`
  components defined in inner scopes take precedence over those defined in
  outer scopes.

  ```python
  gpu0_spec = DeviceSpec(job="ps", device_type="GPU", device_index=0)
  with tf.device(DeviceSpec(job="train").to_string()):
    with tf.device(gpu0_spec.to_string()):
      # Nodes created here will be assigned to /job:ps/device:GPU:0.
    with tf.device(DeviceSpec(device_type="GPU", device_index=1).to_string()):
      # Nodes created here will be assigned to /job:train/device:GPU:1.
  ```

  A `DeviceSpec` consists of 5 components -- each of
  which is optionally specified:

  * Job: The job name.
  * Replica: The replica index.
  * Task: The task index.
  * Device type: The device type string (e.g. "CPU" or "GPU").
  * Device index: The device index.
  '''
    def __init__(self, job: Incomplete | None = None, replica: Incomplete | None = None, task: Incomplete | None = None, device_type: Incomplete | None = None, device_index: Incomplete | None = None) -> None:
        '''Create a new `DeviceSpec` object.

    Args:
      job: string.  Optional job name.
      replica: int.  Optional replica index.
      task: int.  Optional task index.
      device_type: Optional device type string (e.g. "CPU" or "GPU")
      device_index: int.  Optional device index.  If left unspecified, device
        represents \'any\' device_index.
    '''
    def to_string(self):
        """Return a string representation of this `DeviceSpec`.

    Returns:
      a string of the form
      /job:<name>/replica:<id>/task:<id>/device:<device_type>:<id>.
    """
    @classmethod
    def from_string(cls, spec):
        """Construct a `DeviceSpec` from a string.

    Args:
      spec: a string of the form
       /job:<name>/replica:<id>/task:<id>/device:CPU:<id> or
       /job:<name>/replica:<id>/task:<id>/device:GPU:<id> as cpu and gpu are
         mutually exclusive. All entries are optional.

    Returns:
      A DeviceSpec.
    """
    def parse_from_string(self, spec):
        '''Parse a `DeviceSpec` name into its components.

    **2.x behavior change**:

    In TensorFlow 1.x, this function mutates its own state and returns itself.
    In 2.x, DeviceSpecs are immutable, and this function will return a
      DeviceSpec which contains the spec.

    * Recommended:

      ```
      # my_spec and my_updated_spec are unrelated.
      my_spec = tf.DeviceSpec.from_string("/CPU:0")
      my_updated_spec = tf.DeviceSpec.from_string("/GPU:0")
      with tf.device(my_updated_spec):
        ...
      ```

    * Will work in 1.x and 2.x (though deprecated in 2.x):

      ```
      my_spec = tf.DeviceSpec.from_string("/CPU:0")
      my_updated_spec = my_spec.parse_from_string("/GPU:0")
      with tf.device(my_updated_spec):
        ...
      ```

    * Will NOT work in 2.x:

      ```
      my_spec = tf.DeviceSpec.from_string("/CPU:0")
      my_spec.parse_from_string("/GPU:0")  # <== Will not update my_spec
      with tf.device(my_spec):
        ...
      ```

    In general, `DeviceSpec.from_string` should completely replace
    `DeviceSpec.parse_from_string`, and `DeviceSpec.replace` should
    completely replace setting attributes directly.

    Args:
      spec: an optional string of the form
       /job:<name>/replica:<id>/task:<id>/device:CPU:<id> or
       /job:<name>/replica:<id>/task:<id>/device:GPU:<id> as cpu and gpu are
         mutually exclusive. All entries are optional.

    Returns:
      The `DeviceSpec`.

    Raises:
      ValueError: if the spec was not valid.
    '''
    def make_merged_spec(self, dev):
        '''Returns a new DeviceSpec which incorporates `dev`.

    When combining specs, `dev` will take precedence over the current spec.
    So for instance:
    ```
    first_spec = tf.DeviceSpec(job=0, device_type="CPU")
    second_spec = tf.DeviceSpec(device_type="GPU")
    combined_spec = first_spec.make_merged_spec(second_spec)
    ```

    is equivalent to:
    ```
    combined_spec = tf.DeviceSpec(job=0, device_type="GPU")
    ```

    Args:
      dev: a `DeviceSpec`

    Returns:
      A new `DeviceSpec` which combines `self` and `dev`
    '''
    def replace(self, **kwargs):
        '''Convenience method for making a new DeviceSpec by overriding fields.

    For instance:
    ```
    my_spec = DeviceSpec=(job="my_job", device="CPU")
    my_updated_spec = my_spec.replace(device="GPU")
    my_other_spec = my_spec.replace(device=None)
    ```

    Args:
      **kwargs: This method takes the same args as the DeviceSpec constructor

    Returns:
      A DeviceSpec with the fields specified in kwargs overridden.
    '''
    @property
    def job(self): ...
    @property
    def replica(self): ...
    @property
    def task(self): ...
    @property
    def device_type(self): ...
    @property
    def device_index(self): ...
    def __eq__(self, other):
        """Checks if the `other` DeviceSpec is same as the current instance, eg have

       same value for all the internal fields.

    Args:
      other: Another DeviceSpec

    Returns:
      Return `True` if `other` is also a DeviceSpec instance and has same value
      as the current instance.
      Return `False` otherwise.
    """
    def __hash__(self): ...

class DeviceSpecV1(DeviceSpecV2):
    __doc__: Incomplete
    @DeviceSpecV2.job.setter
    def job(self, job) -> None: ...
    @DeviceSpecV2.replica.setter
    def replica(self, replica) -> None: ...
    @DeviceSpecV2.task.setter
    def task(self, task) -> None: ...
    @DeviceSpecV2.device_type.setter
    def device_type(self, device_type) -> None: ...
    @DeviceSpecV2.device_index.setter
    def device_index(self, device_index) -> None: ...
    def __hash__(self): ...
    def to_string(self): ...
    def parse_from_string(self, spec): ...
    def merge_from(self, dev) -> None:
        '''Merge the properties of "dev" into this `DeviceSpec`.

    Note: Will be removed in TensorFlow 2.x since DeviceSpecs will become
          immutable.

    Args:
      dev: a `DeviceSpec`.
    '''
