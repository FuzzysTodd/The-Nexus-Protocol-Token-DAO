from _typeshed import Incomplete
from tensorboard.backend import process_graph as process_graph
from tensorboard.backend.event_processing import directory_loader as directory_loader, event_file_loader as event_file_loader, io_wrapper as io_wrapper
from tensorboard.compat.proto import graph_pb2 as graph_pb2, summary_pb2 as summary_pb2, types_pb2 as types_pb2
from tensorboard.uploader import logdir_loader as logdir_loader, upload_tracker as upload_tracker, util as util
from tensorboard.uploader.proto import write_service_pb2 as write_service_pb2
from tensorboard.util import grpc_util as grpc_util, tb_logging as tb_logging, tensor_util as tensor_util

logger: Incomplete

class TensorBoardUploader:
    """Uploads a TensorBoard logdir to TensorBoard.dev."""
    def __init__(self, writer_client, logdir, allowed_plugins, upload_limits, logdir_poll_rate_limiter: Incomplete | None = None, rpc_rate_limiter: Incomplete | None = None, tensor_rpc_rate_limiter: Incomplete | None = None, blob_rpc_rate_limiter: Incomplete | None = None, name: Incomplete | None = None, description: Incomplete | None = None, verbosity: Incomplete | None = None, one_shot: Incomplete | None = None) -> None:
        """Constructs a TensorBoardUploader.

        Args:
          writer_client: a TensorBoardWriterService stub instance
          logdir: path of the log directory to upload
          allowed_plugins: collection of string plugin names; events will only
            be uploaded if their time series's metadata specifies one of these
            plugin names
          upload_limits: instance of tensorboard.service.UploadLimits proto.
          logdir_poll_rate_limiter: a `RateLimiter` to use to limit logdir
            polling frequency, to avoid thrashing disks, especially on networked
            file systems
          rpc_rate_limiter: a `RateLimiter` to use to limit write RPC frequency.
            Note this limit applies at the level of single RPCs in the Scalar
            and Tensor case, but at the level of an entire blob upload in the
            Blob case-- which may require a few preparatory RPCs and a stream
            of chunks.  Note the chunk stream is internally rate-limited by
            backpressure from the server, so it is not a concern that we do not
            explicitly rate-limit within the stream here.
          name: String name to assign to the experiment.
          description: String description to assign to the experiment.
          verbosity: Level of verbosity, an integer. Supported value:
              0 - No upload statistics is printed.
              1 - Print upload statistics while uploading data (default).
         one_shot: Once uploading starts, upload only the existing data in
            the logdir and then return immediately, instead of the default
            behavior of continuing to listen for new data in the logdir and
            upload them when it appears.
        """
    def has_data(self) -> bool:
        """Returns this object's upload tracker."""
    @property
    def experiment_id(self) -> str:
        """Returns the experiment_id associated with this uploader.

        May be none if no experiment is set, for instance, if
        `create_experiment` has not been called.
        """
    def create_experiment(self):
        """Creates an Experiment for this upload session and returns the ID."""
    def start_uploading(self) -> None:
        """Uploads data from the logdir.

        This will continuously scan the logdir, uploading as data is added
        unless the uploader was built with the _one_shot option, in which
        case it will terminate after the first scan.

        Raises:
          RuntimeError: If `create_experiment` has not yet been called.
          ExperimentNotFoundError: If the experiment is deleted during the
            course of the upload.
        """

def update_experiment_metadata(writer_client, experiment_id, name: Incomplete | None = None, description: Incomplete | None = None) -> None:
    """Modifies user data associated with an experiment.

    Args:
      writer_client: a TensorBoardWriterService stub instance
      experiment_id: string ID of the experiment to modify
      name: If provided, modifies name of experiment to this value.
      description: If provided, modifies the description of the experiment to
         this value

    Raises:
      ExperimentNotFoundError: If no such experiment exists.
      PermissionDeniedError: If the user is not authorized to modify this
        experiment.
      InvalidArgumentError: If the server rejected the name or description, if,
        for instance, the size limits have changed on the server.
    """
def delete_experiment(writer_client, experiment_id) -> None:
    """Permanently deletes an experiment and all of its contents.

    Args:
      writer_client: a TensorBoardWriterService stub instance
      experiment_id: string ID of the experiment to delete

    Raises:
      ExperimentNotFoundError: If no such experiment exists.
      PermissionDeniedError: If the user is not authorized to delete this
        experiment.
      RuntimeError: On unexpected failure.
    """

class InvalidArgumentError(RuntimeError): ...
class ExperimentNotFoundError(RuntimeError): ...
class PermissionDeniedError(RuntimeError): ...
class _OutOfSpaceError(Exception):
    """Action could not proceed without overflowing request budget.

    This is a signaling exception (like `StopIteration`) used internally
    by `_*RequestSender`; it does not mean that anything has gone wrong.
    """

class _BatchedRequestSender:
    """Helper class for building requests that fit under a size limit.

    This class maintains stateful request builders for each of the possible
    request types (scalars, tensors, and blobs).  These accumulate batches
    independently, each maintaining its own byte budget and emitting a request
    when the batch becomes full.  As a consequence, events of different types
    will likely be sent to the backend out of order.  E.g., in the extreme case,
    a single tensor-flavored request may be sent only when the event stream is
    exhausted, even though many more recent scalar events were sent earlier.

    This class is not threadsafe. Use external synchronization if
    calling its methods concurrently.
    """
    def __init__(self, experiment_id, api, allowed_plugins, upload_limits, rpc_rate_limiter, tensor_rpc_rate_limiter, blob_rpc_rate_limiter, tracker) -> None: ...
    def send_requests(self, run_to_events) -> None:
        """Accepts a stream of TF events and sends batched write RPCs.

        Each sent request will be batched, the size of each batch depending on
        the type of data (Scalar vs Tensor vs Blob) being sent.

        Args:
          run_to_events: Mapping from run name to generator of `tf.Event`
            values, as returned by `LogdirLoader.get_run_events`.

        Raises:
          RuntimeError: If no progress can be made because even a single
          point is too large (say, due to a gigabyte-long tag name).
        """

class _ScalarBatchedRequestSender:
    """Helper class for building requests that fit under a size limit.

    This class accumulates a current request.  `add_event(...)` may or may not
    send the request (and start a new one).  After all `add_event(...)` calls
    are complete, a final call to `flush()` is needed to send the final request.

    This class is not threadsafe. Use external synchronization if calling its
    methods concurrently.
    """
    def __init__(self, experiment_id, api, rpc_rate_limiter, max_request_size, tracker) -> None: ...
    def add_event(self, run_name, event, value, metadata) -> None:
        """Attempts to add the given event to the current request.

        If the event cannot be added to the current request because the byte
        budget is exhausted, the request is flushed, and the event is added
        to the next request.
        """
    def flush(self) -> None:
        """Sends the active request after removing empty runs and tags.

        Starts a new, empty active request.
        """

class _TensorBatchedRequestSender:
    """Helper class for building WriteTensor() requests that fit under a size limit.

    This class accumulates a current request.  `add_event(...)` may or may not
    send the request (and start a new one).  After all `add_event(...)` calls
    are complete, a final call to `flush()` is needed to send the final request.

    This class is not threadsafe. Use external synchronization if calling its
    methods concurrently.
    """
    def __init__(self, experiment_id, api, rpc_rate_limiter, max_request_size, max_tensor_point_size, tracker) -> None: ...
    def add_event(self, run_name, event, value, metadata) -> None:
        """Attempts to add the given event to the current request.

        If the event cannot be added to the current request because the byte
        budget is exhausted, the request is flushed, and the event is added
        to the next request.
        """
    def flush(self) -> None:
        """Sends the active request after removing empty runs and tags.

        Starts a new, empty active request.
        """

class _ByteBudgetManager:
    """Helper class for managing the request byte budget for certain RPCs.

    This should be used for RPCs that organize data by Runs, Tags, and Points,
    specifically WriteScalar and WriteTensor.

    Any call to add_run(), add_tag(), or add_point() may raise an
    _OutOfSpaceError, which is non-fatal. It signals to the caller that they
    should flush the current request and begin a new one.

    For more information on the protocol buffer encoding and how byte cost
    can be calculated, visit:

    https://developers.google.com/protocol-buffers/docs/encoding
    """
    def __init__(self, max_bytes) -> None: ...
    def reset(self, base_request) -> None:
        """Resets the byte budget and calculates the cost of the base request.

        Args:
          base_request: Base request.

        Raises:
          _OutOfSpaceError: If the size of the request exceeds the entire
            request byte budget.
        """
    def add_run(self, run_proto) -> None:
        """Integrates the cost of a run proto into the byte budget.

        Args:
          run_proto: The proto representing a run.

        Raises:
          _OutOfSpaceError: If adding the run would exceed the remaining request
            budget.
        """
    def add_tag(self, tag_proto) -> None:
        """Integrates the cost of a tag proto into the byte budget.

        Args:
          tag_proto: The proto representing a tag.

        Raises:
          _OutOfSpaceError: If adding the tag would exceed the remaining request
           budget.
        """
    def add_point(self, point_proto) -> None:
        """Integrates the cost of a point proto into the byte budget.

        Args:
          point_proto: The proto representing a point.

        Raises:
          _OutOfSpaceError: If adding the point would exceed the remaining request
           budget.
        """

class _BlobRequestSender:
    """Uploader for blob-type event data.

    Unlike the other types, this class does not accumulate events in batches;
    every blob is sent individually and immediately.  Nonetheless we retain
    the `add_event()`/`flush()` structure for symmetry.

    This class is not threadsafe. Use external synchronization if calling its
    methods concurrently.
    """
    def __init__(self, experiment_id, api, rpc_rate_limiter, max_blob_request_size, max_blob_size, tracker) -> None: ...
    def add_event(self, run_name, event, value, metadata) -> None:
        """Attempts to add the given event to the current request.

        If the event cannot be added to the current request because the byte
        budget is exhausted, the request is flushed, and the event is added
        to the next request.
        """
    def flush(self) -> None:
        """Sends the current blob sequence fully, and clears it to make way for the next."""
