from _typeshed import Incomplete
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.framework import errors as errors

class _NotOkStatusException(Exception):
    """Exception class to handle not ok Status."""
    message: Incomplete
    code: Incomplete
    payloads: Incomplete
    def __init__(self, message, code, payloads) -> None: ...

class _FallbackException(Exception):
    """Exception class to handle fallback from the fastpath.

  The fastpath that we refer to here is the one implemented to reduce per-op
  overheads (TFE_Py_FastPathExecute_C). If the conditions for executing the op
  on the fastpath are not met, we fallback to a safer (and more complete)
  slowpath, and this Exception is raised to signal that transition.
  """
class _SymbolicException(Exception):
    """Exception class to handle use of symbolic tensors when executing eagerly.

  `keras.Input()` creates symbolic tensors (in a FuncGraph managed by the
  Keras backend) while in eager execution. This exception is used to
  identify this case (raised in `convert_to_tensor` cause generated functions
  for ops to construct graphs instead of executing the kernel).
  """
