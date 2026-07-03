import enum
from _typeshed import Incomplete
from tensorboard import version as version
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete

class AsyncCallFuture:
    """Encapsulates the future value of a retriable async gRPC request.

    Abstracts over the set of futures returned by a set of gRPC calls
    comprising a single logical gRPC request with retries.  Communicates
    to the caller the result or exception resulting from the request.

    Args:
      completion_event: The constructor should provide a `threding.Event` which
        will be used to communicate when the set of gRPC requests is complete.
    """
    def __init__(self, completion_event) -> None: ...
    def result(self, timeout):
        """Analogous to `grpc.Future.result`. Returns the value or exception.

        This method will wait until the full set of gRPC requests is complete
        and then act as `grpc.Future.result` for the single gRPC invocation
        corresponding to the first successful call or final failure, as
        appropriate.

        Args:
          timeout: How long to wait in seconds before giving up and raising.

        Returns:
          The result of the future corresponding to the single gRPC
          corresponding to the successful call.

        Raises:
          * `grpc.FutureTimeoutError` if timeout seconds elapse before the gRPC
          calls could complete, including waits and retries.
          * The exception corresponding to the last non-retryable gRPC request
          in the case that a successful gRPC request was not made.
        """

def async_call_with_retries(api_method, request, clock: Incomplete | None = None):
    """Initiate an asynchronous call to a gRPC stub, with retry logic.

    This is similar to the `async_call` API, except that the call is handled
    asynchronously, and the completion may be handled by another thread. The
    caller must provide a `done_callback` argument which will handle the
    result or exception rising from the gRPC completion.

    Retries are handled with jittered exponential backoff to spread out failures
    due to request spikes.

    This only supports unary-unary RPCs: i.e., no streaming on either end.

    Args:
      api_method: Callable for the API method to invoke.
      request: Request protocol buffer to pass to the API method.
      clock: an interface object supporting `time()` and `sleep()` methods
        like the standard `time` module; if not passed, uses the normal module.

    Returns:
      An `AsyncCallFuture` which will encapsulate the `grpc.Future`
      corresponding to the gRPC call which either completes successfully or
      represents the final try.
    """
def call_with_retries(api_method, request, clock: Incomplete | None = None):
    '''Call a gRPC stub API method, with automatic retry logic.

    This only supports unary-unary RPCs: i.e., no streaming on either end.
    Streamed RPCs will generally need application-level pagination support,
    because after a gRPC error one must retry the entire request; there is no
    "retry-resume" functionality.

    Retries are handled with jittered exponential backoff to spread out failures
    due to request spikes.

    Args:
      api_method: Callable for the API method to invoke.
      request: Request protocol buffer to pass to the API method.
      clock: an interface object supporting `time()` and `sleep()` methods
        like the standard `time` module; if not passed, uses the normal module.

    Returns:
      Response protocol buffer returned by the API method.

    Raises:
      grpc.RpcError: if a non-retryable error is returned, or if all retry
        attempts have been exhausted.
    '''
def version_metadata():
    """Creates gRPC invocation metadata encoding the TensorBoard version.

    Usage: `stub.MyRpc(request, metadata=version_metadata())`.

    Returns:
      A tuple of key-value pairs (themselves 2-tuples) to be passed as the
      `metadata` kwarg to gRPC stub API methods.
    """
def extract_version(metadata):
    """Extracts version from invocation metadata.

    The argument should be the result of a prior call to `metadata` or the
    result of combining such a result with other metadata.

    Returns:
      The TensorBoard version listed in this metadata, or `None` if none
      is listed.
    """

class ChannelCredsType(enum.Enum):
    LOCAL: str
    SSL: str
    SSL_DEV: str
    def channel_config(self):
        """Create channel credentials and options.

        Returns:
          A tuple `(channel_creds, channel_options)`, where `channel_creds`
          is a `grpc.ChannelCredentials` and `channel_options` is a
          (potentially empty) list of `(key, value)` tuples. Both results
          may be passed to `grpc.secure_channel`.
        """
    @classmethod
    def choices(cls): ...
