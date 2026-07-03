from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, tensor_util as tensor_util
from tensorflow.python.ops import script_ops as script_ops
from typing import NamedTuple

class MatchDType(NamedTuple('MatchDType', [('arg_number', Incomplete)])):
    """Allows matching the dtype of an argument.

  Used in conjunction with function calls. For example, MatchDType(0) will
  match the DType of the first argument.
  """

def wrap_py_func(f, return_dtypes, args, kwargs: Incomplete | None = None, use_dummy_return: bool = False):
    """Helper that wraps a callable to py_func.

  The helper passes tensor arguments through the py_func interface. Non-tensor
  arguments are allowed, and will be passed to f directly. Note that non-tensor
  arguments are captured by f will not update every time the wrapper is
  called (this is consistent with its argument list, which only includes
  the tensor arguments). In general, it's safest not to reuse this wrapper.

  Args:
    f: Callable
    return_dtypes: None, individual of tuple/list of DType or MatchDType, the
        data type for each of f's return value(s). Set to None if f has no
        return values or use_dummy_return is True. Use MatchDType to define a
        dtype identical to that of `i`th argument (argument 0 is the first);
        an argument must of Tensor type if it is to be used with MatchDType.
    args: Positional arguments for f, as list or tuple.
    kwargs: Keyword arguments for f, as dict with string keys. May be None.
    use_dummy_return: If True, the function will return a dummy value of 1
        and discard its actual return value.
  Returns:
    The return values of f converted to tensor.
  Raises:
    ValueError: if any of the arguments are incorrect.
  """
