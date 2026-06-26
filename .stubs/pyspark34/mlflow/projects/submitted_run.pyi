import abc
from _typeshed import Incomplete
from abc import abstractmethod
from mlflow.entities import RunStatus as RunStatus
from mlflow.utils.annotations import developer_stable as developer_stable

class SubmittedRun(metaclass=abc.ABCMeta):
    """
    Wrapper around an MLflow project run (e.g. a subprocess running an entry point
    command or a Databricks job run) and exposing methods for waiting on and cancelling the run.
    This class defines the interface that the MLflow project runner uses to manage the lifecycle
    of runs launched in different environments (e.g. runs launched locally or on Databricks).

    ``SubmittedRun`` is not thread-safe. That is, concurrent calls to wait() / cancel()
    from multiple threads may inadvertently kill resources (e.g. local processes) unrelated to the
    run.

    NOTE:

        Subclasses of ``SubmittedRun`` must expose a ``run_id`` member containing the
        run's MLflow run ID.
    """
    @abstractmethod
    def wait(self):
        """
        Wait for the run to finish, returning True if the run succeeded and false otherwise. Note
        that in some cases (e.g. remote execution on Databricks), we may wait until the remote job
        completes rather than until the MLflow run completes.
        """
    @abstractmethod
    def get_status(self):
        """
        Get status of the run.
        """
    @abstractmethod
    def cancel(self):
        """
        Cancel the run (interrupts the command subprocess, cancels the Databricks run, etc) and
        waits for it to terminate. The MLflow run status may not be set correctly
        upon run cancellation.
        """
    @property
    @abstractmethod
    def run_id(self): ...

class LocalSubmittedRun(SubmittedRun):
    """
    Instance of ``SubmittedRun`` corresponding to a subprocess launched to run an entry point
    command locally.
    """
    command_proc: Incomplete
    def __init__(self, run_id, command_proc) -> None: ...
    @property
    def run_id(self): ...
    def wait(self): ...
    def cancel(self) -> None: ...
    def get_status(self): ...
