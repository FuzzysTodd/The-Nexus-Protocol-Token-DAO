from _typeshed import Incomplete
from tensorflow.core.lib.core import error_codes_pb2 as error_codes_pb2
from tensorflow.python.framework import c_api_util as c_api_util
from tensorflow.python.util import compat as compat, deprecation as deprecation, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export

class InaccessibleTensorError(ValueError): ...
class OperatorNotAllowedInGraphError(TypeError):
    """Raised when an unsupported operator is present in Graph execution.

  For example, using a `tf.Tensor` as a Python `bool` inside a Graph will
  raise `OperatorNotAllowedInGraphError`. Iterating over values inside a
  `tf.Tensor` is also not supported in Graph execution.

  Example:
  >>> @tf.function
  ... def iterate_over(t):
  ...   a,b,c = t
  ...   return a
  >>>
  >>> iterate_over(tf.constant([1, 2, 3]))
  Traceback (most recent call last):
  ...
  OperatorNotAllowedInGraphError: ...

  """

class OpError(Exception):
    """The base class for TensorFlow exceptions.

  Usually, TensorFlow will raise a more specific subclass of `OpError` from the
  `tf.errors` module.
  """
    def __init__(self, node_def, op, message, error_code, *args) -> None:
        """Creates a new `OpError` indicating that a particular op failed.

    Args:
      node_def: The `node_def_pb2.NodeDef` proto representing the op that
        failed, if known; otherwise None.
      op: The `ops.Operation` that failed, if known; otherwise None. During
        eager execution, this field is always `None`.
      message: The message string describing the failure.
      error_code: The `error_codes_pb2.Code` describing the error.
      *args: If not empty, it should contain a dictionary describing details
        about the error. This argument is inspired by Abseil payloads:
        https://github.com/abseil/abseil-cpp/blob/master/absl/status/status.h
    """
    def __reduce__(self): ...
    @property
    def message(self):
        """The error message that describes the error."""
    @property
    def op(self):
        """The operation that failed, if known.

    *N.B.* If the failed op was synthesized at runtime, e.g. a `Send`
    or `Recv` op, there will be no corresponding
    `tf.Operation`
    object.  In that case, this will return `None`, and you should
    instead use the `tf.errors.OpError.node_def` to
    discover information about the op.

    Returns:
      The `Operation` that failed, or None.
    """
    @property
    def error_code(self):
        """The integer error code that describes the error."""
    @property
    def node_def(self):
        """The `NodeDef` proto representing the op that failed."""
    @property
    def experimental_payloads(self):
        """A dictionary describing the details of the error."""

OK: Incomplete
CANCELLED: Incomplete
UNKNOWN: Incomplete
INVALID_ARGUMENT: Incomplete
DEADLINE_EXCEEDED: Incomplete
NOT_FOUND: Incomplete
ALREADY_EXISTS: Incomplete
PERMISSION_DENIED: Incomplete
UNAUTHENTICATED: Incomplete
RESOURCE_EXHAUSTED: Incomplete
FAILED_PRECONDITION: Incomplete
ABORTED: Incomplete
OUT_OF_RANGE: Incomplete
UNIMPLEMENTED: Incomplete
INTERNAL: Incomplete
UNAVAILABLE: Incomplete
DATA_LOSS: Incomplete

class CancelledError(OpError):
    """Raised when an operation is cancelled.

  For example, a long-running operation e.g.`tf.queue.QueueBase.enqueue`, or a
  `tf.function` call may be cancelled by either running another operation e.g.
  `tf.queue.QueueBase.close` or a remote worker failure.

  This long-running operation will fail by raising `CancelledError`.

  Example:
  >>> q = tf.queue.FIFOQueue(10, tf.float32, ((),))
  >>> q.enqueue((10.0,))
  >>> q.close()
  >>> q.enqueue((10.0,))
  Traceback (most recent call last):
    ...
  CancelledError: ...

  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates a `CancelledError`."""

class UnknownError(OpError):
    """Unknown error.

  An example of where this error may be returned is if a Status value
  received from another address space belongs to an error-space that
  is not known to this address space. Also, errors raised by APIs that
  do not return enough error information may be converted to this
  error.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates an `UnknownError`."""

class InvalidArgumentError(OpError):
    """Raised when an operation receives an invalid argument.

  This error is typically raised when an op receives mismatched arguments.

  Example:

  >>> tf.reshape([1, 2, 3], (2,))
  Traceback (most recent call last):
     ...
  InvalidArgumentError: ...
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates an `InvalidArgumentError`."""

class DeadlineExceededError(OpError):
    """Raised when a deadline expires before an operation could complete.

  This exception is not currently used.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates a `DeadlineExceededError`."""

class NotFoundError(OpError):
    """Raised when a requested entity (e.g., a file or directory) was not found.

  For example, running the
  `tf.WholeFileReader.read`
  operation could raise `NotFoundError` if it receives the name of a file that
  does not exist.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates a `NotFoundError`."""

class AlreadyExistsError(OpError):
    """Raised when an entity that we attempted to create already exists.

  An API raises this this error to avoid overwriting an existing resource,
  value, etc. Calling a creation API multiple times with the same arguments
  could raise this error if the creation API is not idempotent.

  For example, running an operation that saves a file
  (e.g. `tf.saved_model.save`)
  could potentially raise this exception if an explicit filename for an
  existing file was passed.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates an `AlreadyExistsError`."""

class PermissionDeniedError(OpError):
    """Raised when the caller does not have permission to run an operation.

  For example, running the
  `tf.WholeFileReader.read`
  operation could raise `PermissionDeniedError` if it receives the name of a
  file for which the user does not have the read file permission.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates a `PermissionDeniedError`."""

class UnauthenticatedError(OpError):
    """Raised when the request does not have valid authentication credentials.

  This exception is not currently used.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates an `UnauthenticatedError`."""

class ResourceExhaustedError(OpError):
    """Raised when some resource has been exhausted while running operation.

  For example, this error might be raised if a per-user quota is
  exhausted, or perhaps the entire file system is out of space. If running into
  `ResourceExhaustedError` due to out of memory (OOM), try to use smaller batch
  size or reduce dimension size of model weights.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates a `ResourceExhaustedError`."""

class FailedPreconditionError(OpError):
    """Raised when some prerequisites are not met when running an operation.

  This typically indicates that system is not in state to execute the operation
  and requires preconditions to be met before successfully executing current
  operation.

  For example, this exception is commonly raised when running an operation
  that reads a `tf.Variable` before it has been initialized.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates a `FailedPreconditionError`."""

class AbortedError(OpError):
    """Raised when an operation was aborted, typically due to a concurrent action.

  For example, running a
  `tf.queue.QueueBase.enqueue`
  operation may raise `AbortedError` if a
  `tf.queue.QueueBase.close` operation
  previously ran.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates an `AbortedError`."""

class OutOfRangeError(OpError):
    """Raised when an operation iterates past the valid range.

  Unlike `InvalidArgumentError`, this error indicates a problem may be fixed if
  the system state changes. For example, if a list grows and the operation is
  now within the valid range. `OutOfRangeError` overlaps with
  `FailedPreconditionError` and should be preferred as the more specific error
  when iterating or accessing a range.

  For example, iterating a TF dataset past the last item in the dataset will
  raise this error.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates an `OutOfRangeError`."""

class UnimplementedError(OpError):
    """Raised when an operation has not been implemented.

  Some operations may raise this error when passed otherwise-valid
  arguments that it does not currently support. For example, running
  the `tf.nn.max_pool2d` operation
  would raise this error if pooling was requested on the batch dimension,
  because this is not yet supported.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates an `UnimplementedError`."""

class InternalError(OpError):
    """Raised when the system experiences an internal error.

  This exception is raised when some invariant expected by the runtime
  has been broken. Catching this exception is not recommended.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates an `InternalError`."""

class UnavailableError(OpError):
    """Raised when the runtime is currently unavailable.

  This exception is not currently used.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates an `UnavailableError`."""

class DataLossError(OpError):
    """Raised when unrecoverable data loss or corruption is encountered.

  This could be due to:
  * A truncated file.
  * A corrupted file.
  * Specifying the wrong data format.

  For example, this may be raised by running a
  `tf.WholeFileReader.read`
  operation, if the file is truncated while it is being read.
  """
    def __init__(self, node_def, op, message, *args) -> None:
        """Creates a `DataLossError`."""

def exception_type_from_error_code(error_code): ...
def error_code_from_exception_type(cls): ...

class raise_exception_on_not_ok_status:
    """Context manager to check for C API status."""
    status: Incomplete
    def __enter__(self): ...
    def __exit__(self, type_arg: type[BaseException] | None, value_arg: BaseException | None, traceback_arg: types.TracebackType | None): ...
