from _typeshed import Incomplete
from tensorflow.python.framework import errors_impl as errors_impl
from tensorflow.python.platform import flags as flags
from tensorflow.python.training import py_checkpoint_reader as py_checkpoint_reader

FLAGS: Incomplete

def print_tensors_in_checkpoint_file(file_name, tensor_name, all_tensors, all_tensor_names: bool = False, count_exclude_pattern: str = '') -> None:
    """Prints tensors in a checkpoint file.

  If no `tensor_name` is provided, prints the tensor names and shapes
  in the checkpoint file.

  If `tensor_name` is provided, prints the content of the tensor.

  Args:
    file_name: Name of the checkpoint file.
    tensor_name: Name of the tensor in the checkpoint file to print.
    all_tensors: Boolean indicating whether to print all tensors.
    all_tensor_names: Boolean indicating whether to print all tensor names.
    count_exclude_pattern: Regex string, pattern to exclude tensors when count.
  """
def parse_numpy_printoption(kv_str) -> None:
    """Sets a single numpy printoption from a string of the form 'x=y'.

  See documentation on numpy.set_printoptions() for details about what values
  x and y can take. x can be any option listed there other than 'formatter'.

  Args:
    kv_str: A string of the form 'x=y', such as 'threshold=100000'

  Raises:
    argparse.ArgumentTypeError: If the string couldn't be used to set any
        nump printoption.
  """
def main(unused_argv) -> None: ...
