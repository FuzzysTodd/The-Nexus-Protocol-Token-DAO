from . import launcher as launcher, management as management, rest as rest
from ..tools.nnictl.command_utils import kill_command as kill_command
from .config import ExperimentConfig as ExperimentConfig
from .data import TrialJob as TrialJob, TrialMetricData as TrialMetricData, TrialResult as TrialResult
from _typeshed import Incomplete
from enum import Enum
from nni.runtime.log import start_experiment_logging as start_experiment_logging, stop_experiment_logging as stop_experiment_logging

class RunMode(Enum):
    """
    Config lifecycle and ouput redirection of NNI manager process.

    - Background: stop NNI manager when Python script exits; do not print NNI manager log. (default)
    - Foreground: stop NNI manager when Python script exits; print NNI manager log to stdout.
    - Detach: do not stop NNI manager when Python script exits.

    NOTE: This API is non-stable and is likely to get refactored in upcoming release.
    """
    Background: str
    Foreground: str
    Detach: str

class Experiment:
    """
    Manage NNI experiment.

    You can either specify an :class:`ExperimentConfig` object, or a training service name.
    If a platform name is used, a blank config template for that training service will be generated.

    When configuration is completed, use :meth:`Experiment.run` to launch the experiment.

    Example
    -------
    .. code-block::

        experiment = Experiment('remote')
        experiment.config.trial_command = 'python3 trial.py'
        experiment.config.machines.append(RemoteMachineConfig(ip=..., user_name=...))
        ...
        experiment.run(8080)

    Attributes
    ----------
    config
        Experiment configuration.
    id
        Experiment ID.
    port
        Web portal port. Or ``None`` if the experiment is not running.
    """
    config: Incomplete
    id: Incomplete
    port: Incomplete
    url_prefix: Incomplete
    def __init__(self, config_or_platform: ExperimentConfig | str | list[str] | None) -> None: ...
    def start(self, port: int = 8080, debug: bool = False, run_mode: RunMode = ...) -> None:
        """
        Start the experiment in background.

        This method will raise exception on failure.
        If it returns, the experiment should have been successfully started.

        Parameters
        ----------
        port
            The port of web UI.
        debug
            Whether to start in debug mode.
        run_mode
            Running the experiment in foreground or background
        """
    def stop(self) -> None:
        """
        Stop the experiment.
        """
    def run(self, port: int = 8080, wait_completion: bool = True, debug: bool = False) -> bool | None:
        """
        Run the experiment.

        If ``wait_completion`` is ``True``, this function will block until experiment finish or error.

        Return ``True`` when experiment done; or return ``False`` when experiment failed.

        Else if ``wait_completion`` is ``False``, this function will non-block and return None immediately.
        """
    @classmethod
    def connect(cls, port: int):
        """
        Connect to an existing experiment.

        Parameters
        ----------
        port
            The port of web UI.
        """
    @staticmethod
    def resume(experiment_id: str, port: int = 8080, wait_completion: bool = True, debug: bool = False):
        """
        Resume a stopped experiment.

        Parameters
        ----------
        experiment_id
            The stopped experiment id.
        port
            The port of web UI.
        wait_completion
            If true, run in the foreground. If false, run in the background.
        debug
            Whether to start in debug mode.
        """
    @staticmethod
    def view(experiment_id: str, port: int = 8080, non_blocking: bool = False):
        """
        View a stopped experiment.

        Parameters
        ----------
        experiment_id
            The stopped experiment id.
        port
            The port of web UI.
        non_blocking
            If false, run in the foreground. If true, run in the background.
        """
    def get_status(self) -> str:
        """
        Return experiment status as a str.

        Returns
        -------
        str
            Experiment status.
        """
    def get_trial_job(self, trial_job_id: str):
        """
        Return a trial job.

        Parameters
        ----------
        trial_job_id: str
            Trial job id.

        Returns
        -------
        TrialJob
            A `TrialJob` instance corresponding to `trial_job_id`.
        """
    def list_trial_jobs(self):
        """
        Return information for all trial jobs as a list.

        Returns
        -------
        list
            List of `TrialJob`.
        """
    def get_job_statistics(self):
        """
        Return trial job statistics information as a dict.

        Returns
        -------
        dict
            Job statistics information.
        """
    def get_job_metrics(self, trial_job_id: Incomplete | None = None):
        """
        Return trial job metrics.

        Parameters
        ----------
        trial_job_id: str
            trial job id. if this parameter is None, all trail jobs' metrics will be returned.

        Returns
        -------
        dict
            Each key is a trialJobId, the corresponding value is a list of `TrialMetricData`.
        """
    def get_experiment_profile(self):
        """
        Return experiment profile as a dict.

        Returns
        -------
        dict
            The profile of the experiment.
        """
    def get_experiment_metadata(self, exp_id: str):
        """
        Return experiment metadata with specified exp_id as a dict.

        Returns
        -------
        dict
            The specified experiment metadata.
        """
    def get_all_experiments_metadata(self):
        """
        Return all experiments metadata as a list.

        Returns
        -------
        list
            The experiments metadata.
        """
    def export_data(self):
        """
        Return exported information for all trial jobs.

        Returns
        -------
        list
            List of `TrialResult`.
        """
    def update_trial_concurrency(self, value: int):
        """
        Update an experiment's trial_concurrency

        Parameters
        ----------
        value: int
            New trial_concurrency value.
        """
    def update_max_experiment_duration(self, value: str):
        """
        Update an experiment's max_experiment_duration

        Parameters
        ----------
        value: str
            Strings like '1m' for one minute or '2h' for two hours.
            SUFFIX may be 's' for seconds, 'm' for minutes, 'h' for hours or 'd' for days.
        """
    def update_search_space(self, value: dict):
        """
        Update the experiment's search_space.
        TODO: support searchspace file.

        Parameters
        ----------
        value: dict
            New search_space.
        """
    def update_max_trial_number(self, value: int):
        """
        Update an experiment's max_trial_number

        Parameters
        ----------
        value: int
            New max_trial_number value.
        """
