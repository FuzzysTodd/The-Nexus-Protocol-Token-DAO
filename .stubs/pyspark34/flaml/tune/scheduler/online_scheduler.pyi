from _typeshed import Incomplete
from flaml.tune import Trial as Trial
from flaml.tune.scheduler import TrialScheduler as TrialScheduler
from typing import Dict

logger: Incomplete

class OnlineScheduler(TrialScheduler):
    """Class for the most basic OnlineScheduler."""
    def on_trial_result(self, trial_runner, trial: Trial, result: Dict):
        """Report result and return a decision on the trial's status."""
    def choose_trial_to_run(self, trial_runner) -> Trial:
        """Decide which trial to run next."""

class OnlineSuccessiveDoublingScheduler(OnlineScheduler):
    """class for the OnlineSuccessiveDoublingScheduler algorithm."""
    def __init__(self, increase_factor: float = 2.0) -> None:
        """Constructor.

        Args:
            increase_factor: A float of multiplicative factor
                used to increase resource lease. Default is 2.0.
        """
    def on_trial_result(self, trial_runner, trial: Trial, result: Dict):
        """Report result and return a decision on the trial's status."""

class ChaChaScheduler(OnlineSuccessiveDoublingScheduler):
    """class for the ChaChaScheduler algorithm."""
    def __init__(self, increase_factor: float = 2.0, **kwargs) -> None:
        """Constructor.

        Args:
            increase_factor: A float of multiplicative factor
                used to increase resource lease. Default is 2.0.
        """
    def on_trial_result(self, trial_runner, trial: Trial, result: Dict):
        """Report result and return a decision on the trial's status."""
