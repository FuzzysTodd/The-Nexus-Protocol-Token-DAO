from . import error_codes as error_codes
from _typeshed import Incomplete

class OpError(Exception):
    """A generic error that is raised when TensorFlow execution fails.

    Whenever possible, the session will raise a more specific subclass
    of `OpError` from the `tf.errors` module.
    """
    def __init__(self, node_def, op, message, error_code) -> None:
        """Creates a new `OpError` indicating that a particular op failed.

        Args:
          node_def: The `node_def_pb2.NodeDef` proto representing the op that
            failed, if known; otherwise None.
          op: The `ops.Operation` that failed, if known; otherwise None.
          message: The message string describing the failure.
          error_code: The `error_codes.Code` describing the error.
        """
    @property
    def message(self):
        """The error message that describes the error."""
    @property
    def op(self):
        """The operation that failed, if known.

        *N.B.* If the failed op was synthesized at runtime, e.g. a `Send`
        or `Recv` op, there will be no corresponding
        @{tf.Operation}
        object.  In that case, this will return `None`, and you should
        instead use the @{tf.OpError.node_def} to
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
    """Raised when an operation or step is cancelled.

    For example, a long-running operation (e.g.
    @{tf.QueueBase.enqueue} may be
    cancelled by running another operation (e.g.
    @{tf.QueueBase.close},
    or by @{tf.Session.close}.
    A step that is running such a long-running operation will fail by raising
    `CancelledError`.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates a `CancelledError`."""

class UnknownError(OpError):
    """Unknown error.

    An example of where this error may be returned is if a Status value
    received from another address space belongs to an error-space that
    is not known to this address space. Also errors raised by APIs that
    do not return enough error information may be converted to this
    error.

    @@__init__
    """
    def __init__(self, node_def, op, message, error_code=...) -> None:
        """Creates an `UnknownError`."""

class InvalidArgumentError(OpError):
    """Raised when an operation receives an invalid argument.

    This may occur, for example, if an operation is receives an input
    tensor that has an invalid value or shape. For example, the
    @{tf.matmul} op will raise this
    error if it receives an input that is not a matrix, and the
    @{tf.reshape} op will raise
    this error if the new shape does not match the number of elements in the input
    tensor.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates an `InvalidArgumentError`."""

class DeadlineExceededError(OpError):
    """Raised when a deadline expires before an operation could complete.

    This exception is not currently used.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates a `DeadlineExceededError`."""

class NotFoundError(OpError):
    """Raised when a requested entity (e.g., a file or directory) was not
    found.

    For example, running the
    @{tf.WholeFileReader.read}
    operation could raise `NotFoundError` if it receives the name of a file that
    does not exist.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates a `NotFoundError`."""

class AlreadyExistsError(OpError):
    """Raised when an entity that we attempted to create already exists.

    For example, running an operation that saves a file
    (e.g. @{tf.train.Saver.save})
    could potentially raise this exception if an explicit filename for an
    existing file was passed.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates an `AlreadyExistsError`."""

class PermissionDeniedError(OpError):
    """Raised when the caller does not have permission to run an operation.

    For example, running the
    @{tf.WholeFileReader.read}
    operation could raise `PermissionDeniedError` if it receives the name of a
    file for which the user does not have the read file permission.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates a `PermissionDeniedError`."""

class UnauthenticatedError(OpError):
    """The request does not have valid authentication credentials.

    This exception is not currently used.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates an `UnauthenticatedError`."""

class ResourceExhaustedError(OpError):
    """Some resource has been exhausted.

    For example, this error might be raised if a per-user quota is
    exhausted, or perhaps the entire file system is out of space.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates a `ResourceExhaustedError`."""

class FailedPreconditionError(OpError):
    """Operation was rejected because the system is not in a state to execute
    it.

    This exception is most commonly raised when running an operation
    that reads a @{tf.Variable}
    before it has been initialized.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates a `FailedPreconditionError`."""

class AbortedError(OpError):
    """The operation was aborted, typically due to a concurrent action.

    For example, running a
    @{tf.QueueBase.enqueue}
    operation may raise `AbortedError` if a
    @{tf.QueueBase.close} operation
    previously ran.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates an `AbortedError`."""

class OutOfRangeError(OpError):
    '''Raised when an operation iterates past the valid input range.

    This exception is raised in "end-of-file" conditions, such as when a
    @{tf.QueueBase.dequeue}
    operation is blocked on an empty queue, and a
    @{tf.QueueBase.close}
    operation executes.

    @@__init__
    '''
    def __init__(self, node_def, op, message) -> None:
        """Creates an `OutOfRangeError`."""

class UnimplementedError(OpError):
    """Raised when an operation has not been implemented.

    Some operations may raise this error when passed otherwise-valid
    arguments that it does not currently support. For example, running
    the @{tf.nn.max_pool} operation
    would raise this error if pooling was requested on the batch dimension,
    because this is not yet supported.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates an `UnimplementedError`."""

class InternalError(OpError):
    """Raised when the system experiences an internal error.

    This exception is raised when some invariant expected by the runtime
    has been broken. Catching this exception is not recommended.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates an `InternalError`."""

class UnavailableError(OpError):
    """Raised when the runtime is currently unavailable.

    This exception is not currently used.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates an `UnavailableError`."""

class DataLossError(OpError):
    """Raised when unrecoverable data loss or corruption is encountered.

    For example, this may be raised by running a
    @{tf.WholeFileReader.read}
    operation, if the file is truncated while it is being read.

    @@__init__
    """
    def __init__(self, node_def, op, message) -> None:
        """Creates a `DataLossError`."""

def exception_type_from_error_code(error_code): ...
def error_code_from_exception_type(cls): ...

class raise_exception_on_not_ok_status:
    """Context manager to check for C API status."""
    def __enter__(self): ...
    def __exit__(self, type_arg: type[BaseException] | None, value_arg: BaseException | None, traceback_arg: types.TracebackType | None): ...
