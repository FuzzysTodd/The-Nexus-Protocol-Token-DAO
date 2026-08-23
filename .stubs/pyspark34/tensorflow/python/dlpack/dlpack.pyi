from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import context as context
from tensorflow.python.util.tf_export import tf_export as tf_export

def to_dlpack(tf_tensor):
    """Returns the dlpack capsule representing the tensor.

  This operation ensures the underlying data memory is ready when returns.

    ```python
    a = tf.tensor([1, 10])
    dlcapsule = tf.experimental.dlpack.to_dlpack(a)
    # dlcapsule represents the dlpack data structure
    ```

  Args:
    tf_tensor: Tensorflow eager tensor, to be converted to dlpack capsule.

  Returns:
    A PyCapsule named as dltensor, which shares the underlying memory to other
     framework. This PyCapsule can be consumed only once.
  """
def from_dlpack(dlcapsule):
    """Returns the Tensorflow eager tensor.

  The returned tensor uses the memory shared by dlpack capsules from other
  framework.

    ```python
    a = tf.experimental.dlpack.from_dlpack(dlcapsule)
    # `a` uses the memory shared by dlpack
    ```

  Args:
    dlcapsule: A PyCapsule named as dltensor

  Returns:
    A Tensorflow eager tensor
  """
