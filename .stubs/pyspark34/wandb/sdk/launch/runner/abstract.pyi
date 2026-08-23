import abc
from .._project_spec import LaunchProject as LaunchProject
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import Any, Dict
from wandb.apis.internal import Api as Api
from wandb.sdk.lib import runid as runid

State: Incomplete

class Status:
    state: Incomplete
    data: Incomplete
    def __init__(self, state: State = 'unknown', data: Incomplete | None = None) -> None: ...

class AbstractRun(ABC, metaclass=abc.ABCMeta):
    """Wrapper around a W&B launch run.

    A launched run is a subprocess running an entry point
    command, that exposes methods for waiting on and cancelling the run.
    This class defines the interface that the W&B launch runner uses to manage the lifecycle
    of runs launched in different environments (e.g. runs launched locally or in a cluster).
    ``AbstractRun`` is not thread-safe. That is, concurrent calls to wait() / cancel()
    from multiple threads may inadvertently kill resources (e.g. local processes) unrelated to the
    run.
    """
    def __init__(self) -> None: ...
    @property
    def status(self) -> Status: ...
    @abstractmethod
    def get_logs(self) -> str | None:
        """Return the logs associated with the run."""
    @abstractmethod
    def wait(self) -> bool:
        """Wait for the run to finish, returning True if the run succeeded and false otherwise.

        Note that in some cases, we may wait until the remote job completes rather than until the W&B run completes.
        """
    @abstractmethod
    def get_status(self) -> Status:
        """Get status of the run."""
    @abstractmethod
    def cancel(self) -> None:
        """Cancel the run (interrupts the command subprocess, cancels the run, etc).

        Cancels the run and waits for it to terminate. The W&B run status may not be
        set correctly upon run cancellation.
        """
    @property
    @abstractmethod
    def id(self) -> str | None: ...

class AbstractRunner(ABC, metaclass=abc.ABCMeta):
    """Abstract plugin class defining the interface needed to execute W&B Launches.

    You can define subclasses of ``AbstractRunner`` and expose them as third-party
    plugins to enable running W&B projects against custom execution backends
    (e.g. to run projects against your team's in-house cluster or job scheduler).
    """
    backend_config: Incomplete
    def __init__(self, api: Api, backend_config: Dict[str, Any]) -> None: ...
    def find_executable(self, cmd: str) -> Any:
        """Cross platform utility for checking if a program is available."""
    @property
    def api_key(self) -> Any: ...
    def verify(self) -> bool:
        """This is called on first boot to verify the needed commands, and permissions are available.

        For now just call `wandb.termerror` and `sys.exit(1)`
        """
    @abstractmethod
    def run(self, launch_project: LaunchProject, image_uri: str) -> AbstractRun | None:
        """Submit an LaunchProject to be run.

        Returns a SubmittedRun object to track the execution
        Arguments:
        launch_project: Object of _project_spec.LaunchProject class representing a wandb launch project

        Returns:
            A :py:class:`wandb.sdk.launch.runners.SubmittedRun`. This function is expected to run
            the project asynchronously, i.e. it should trigger project execution and then
            immediately return a `SubmittedRun` to track execution status.
        """
