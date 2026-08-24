from tensorflow.core.framework import kernel_def_pb2 as kernel_def_pb2
from tensorflow.python.util import compat as compat

def get_all_registered_kernels():
    """Returns a KernelList proto of all registered kernels.
  """
def get_registered_kernels_for_op(name):
    """Returns a KernelList proto of registered kernels for a given op.

  Args:
    name: A string representing the name of the op whose kernels to retrieve.
  """
