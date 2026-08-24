from _typeshed import Incomplete
from mlflow.entities.dataset_input import DatasetInput
from typing import Any, Dict, List, NamedTuple

__all__ = ['MlflowAutologgingQueueingClient']

class _PendingCreateRun(NamedTuple):
    experiment_id: Incomplete
    start_time: Incomplete
    tags: Incomplete
    run_name: Incomplete

class _PendingSetTerminated(NamedTuple):
    status: Incomplete
    end_time: Incomplete

class PendingRunId:
    """
    Serves as a placeholder for the ID of a run that does not yet exist, enabling additional
    metadata (e.g. metrics, params, ...) to be enqueued for the run prior to its creation.
    """

class RunOperations:
    """
    Represents a collection of operations on one or more MLflow Runs, such as run creation
    or metric logging.
    """
    def __init__(self, operation_futures) -> None: ...
    def await_completion(self) -> None:
        """
        Blocks on completion of the MLflow Run operations.
        """

class MlflowAutologgingQueueingClient:
    """
    Efficiently implements a subset of MLflow Tracking's  `MlflowClient` and fluent APIs to provide
    automatic batching and async execution of run operations by way of queueing, as well as
    parameter / tag truncation for autologging use cases. Run operations defined by this client,
    such as `create_run` and `log_metrics`, enqueue data for future persistence to MLflow
    Tracking. Data is not persisted until the queue is flushed via the `flush()` method, which
    supports synchronous and asynchronous execution.

    MlflowAutologgingQueueingClient is not threadsafe; none of its APIs should be called
    concurrently.
    """
    def __init__(self, tracking_uri: Incomplete | None = None) -> None: ...
    def __enter__(self):
        """
        Enables `MlflowAutologgingQueueingClient` to be used as a context manager with
        synchronous flushing upon exit, removing the need to call `flush()` for use cases
        where logging completion can be waited upon synchronously.

        Run content is only flushed if the context exited without an exception.
        """
    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: types.TracebackType | None) -> None:
        """
        Enables `MlflowAutologgingQueueingClient` to be used as a context manager with
        synchronous flushing upon exit, removing the need to call `flush()` for use cases
        where logging completion can be waited upon synchronously.

        Run content is only flushed if the context exited without an exception.
        """
    def create_run(self, experiment_id: str, start_time: int | None = None, tags: Dict[str, Any] | None = None, run_name: str | None = None) -> PendingRunId:
        """
        Enqueues a CreateRun operation with the specified attributes, returning a `PendingRunId`
        instance that can be used as input to other client logging APIs (e.g. `log_metrics`,
        `log_params`, ...).

        :return: A `PendingRunId` that can be passed as the `run_id` parameter to other client
                 logging APIs, such as `log_params` and `log_metrics`.
        """
    def set_terminated(self, run_id: str | PendingRunId, status: str | None = None, end_time: int | None = None) -> None:
        """
        Enqueues an UpdateRun operation with the specified `status` and `end_time` attributes
        for the specified `run_id`.
        """
    def log_params(self, run_id: str | PendingRunId, params: Dict[str, Any]) -> None:
        """
        Enqueues a collection of Parameters to be logged to the run specified by `run_id`.
        """
    def log_inputs(self, run_id: str | PendingRunId, datasets: List[DatasetInput] | None) -> None:
        """
        Enqueues a collection of Dataset to be logged to the run specified by `run_id`.
        """
    def log_metrics(self, run_id: str | PendingRunId, metrics: Dict[str, float], step: int | None = None) -> None:
        """
        Enqueues a collection of Metrics to be logged to the run specified by `run_id` at the
        step specified by `step`.
        """
    def set_tags(self, run_id: str | PendingRunId, tags: Dict[str, Any]) -> None:
        """
        Enqueues a collection of Tags to be logged to the run specified by `run_id`.
        """
    def flush(self, synchronous: bool = True):
        """
        Flushes all queued run operations, resulting in the creation or mutation of runs
        and run data.

        :param synchronous: If `True`, run operations are performed synchronously, and a
                            `RunOperations` result object is only returned once all operations
                            are complete. If `False`, run operations are performed asynchronously,
                            and an `RunOperations` object is returned that represents the ongoing
                            run operations.
        :return: A `RunOperations` instance representing the flushed operations. These operations
                 are already complete if `synchronous` is `True`. If `synchronous` is `False`, these
                 operations may still be inflight. Operation completion can be synchronously waited
                 on via `RunOperations.await_completion()`.
        """

class _PendingRunOperations:
    """
    Represents a collection of queued / pending MLflow Run operations.
    """
    run_id: Incomplete
    create_run: Incomplete
    set_terminated: Incomplete
    params_queue: Incomplete
    tags_queue: Incomplete
    metrics_queue: Incomplete
    datasets_queue: Incomplete
    def __init__(self, run_id) -> None: ...
    def enqueue(self, params: Incomplete | None = None, tags: Incomplete | None = None, metrics: Incomplete | None = None, datasets: Incomplete | None = None, create_run: Incomplete | None = None, set_terminated: Incomplete | None = None) -> None:
        """
        Enqueues a new pending logging operation for the associated MLflow Run.
        """
