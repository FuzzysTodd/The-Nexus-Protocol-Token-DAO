from .trial import Trial as Trial
from _typeshed import Incomplete

logger: Incomplete

class Nologger:
    """Logger without logging."""
    def on_result(self, result) -> None: ...

class SimpleTrial(Trial):
    """A simple trial class."""
    trial_id: Incomplete
    config: Incomplete
    status: Incomplete
    start_time: Incomplete
    last_result: Incomplete
    last_update_time: Incomplete
    custom_trial_name: Incomplete
    trainable_name: str
    experiment_tag: str
    verbose: bool
    result_logger: Incomplete
    metric_analysis: Incomplete
    n_steps: Incomplete
    metric_n_steps: Incomplete
    def __init__(self, config, trial_id: Incomplete | None = None) -> None: ...

class BaseTrialRunner:
    """Implementation of a simple trial runner.

    Note that the caller usually should not mutate trial state directly.
    """
    def __init__(self, search_alg: Incomplete | None = None, scheduler: Incomplete | None = None, metric: str | None = None, mode: str | None = 'min') -> None: ...
    def get_trials(self):
        """Returns the list of trials managed by this TrialRunner.

        Note that the caller usually should not mutate trial state directly.
        """
    def add_trial(self, trial) -> None:
        """Adds a new trial to this TrialRunner.

        Trials may be added at any time.

        Args:
            trial (Trial): Trial to queue.
        """
    def process_trial_result(self, trial, result) -> None: ...
    def stop_trial(self, trial) -> None:
        """Stops trial."""

class SequentialTrialRunner(BaseTrialRunner):
    """Implementation of the sequential trial runner."""
    running_trial: Incomplete
    def step(self) -> Trial:
        """Runs one step of the trial event loop.

        Callers should typically run this method repeatedly in a loop. They
        may inspect or modify the runner's state in between calls to step().

        Returns:
            a trial to run.
        """
    def stop_trial(self, trial) -> None: ...

class SparkTrialRunner(BaseTrialRunner):
    """Implementation of the spark trial runner."""
    running_trials: Incomplete
    def __init__(self, search_alg: Incomplete | None = None, scheduler: Incomplete | None = None, metric: str | None = None, mode: str | None = 'min') -> None: ...
    def step(self) -> Trial:
        """Runs one step of the trial event loop.

        Callers should typically run this method repeatedly in a loop. They
        may inspect or modify the runner's state in between calls to step().

        Returns:
            a trial to run.
        """
    def stop_trial(self, trial) -> None: ...
