from _typeshed import Incomplete
from flaml.tune import Trial as Trial
from flaml.tune.scheduler import TrialScheduler as TrialScheduler

logger: Incomplete

class OnlineTrialRunner:
    """Class for the OnlineTrialRunner."""
    RANDOM_SEED: int
    WARMSTART_NUM: int
    def __init__(self, max_live_model_num: int, searcher: Incomplete | None = None, scheduler: Incomplete | None = None, champion_test_policy: str = 'loss_ucb', **kwargs) -> None:
        """Constructor.

        Args:
            max_live_model_num: The maximum number of 'live'/running models allowed.
            searcher: A class for generating Trial objects progressively.
                The ConfigOracle is implemented in the searcher.
            scheduler: A class for managing the 'live' trials and allocating the
                resources for the trials.
            champion_test_policy: A string to specify what test policy to test for
                champion. Currently can choose from ['loss_ucb', 'loss_avg', 'loss_lcb', None].
        """
    @property
    def champion_trial(self) -> Trial:
        """The champion trial."""
    @property
    def running_trials(self):
        """The running/'live' trials."""
    def step(self, data_sample: Incomplete | None = None, prediction_trial_tuple: Incomplete | None = None) -> None:
        """Schedule one trial to run each time it is called.

        Args:
            data_sample: One data example.
            prediction_trial_tuple: A list of information containing
                (prediction_made, prediction_trial).
        """
    def get_top_running_trials(self, top_ratio: Incomplete | None = None, top_metric: str = 'ucb') -> list:
        """Get a list of trial ids, whose performance is among the top running trials."""
    def get_trials(self) -> list:
        """Return the list of trials managed by this TrialRunner."""
    def add_trial(self, new_trial) -> None:
        """Add a new trial to this TrialRunner.
        Trials may be added at any time.

        Args:
            new_trial (Trial): Trial to queue.
        """
    def stop_trial(self, trial) -> None:
        """Stop a trial: set the status of a trial to be
        Trial.TERMINATED and perform other subsequent operations.
        """
    def pause_trial(self, trial) -> None:
        """Pause a trial: set the status of a trial to be Trial.PAUSED
        and perform other subsequent operations.
        """
    def run_trial(self, trial) -> None:
        """Run a trial: set the status of a trial to be Trial.RUNNING
        and perform other subsequent operations.
        """
