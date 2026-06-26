from flaml.tune import trial_runner as trial_runner
from flaml.tune.trial import Trial as Trial

class TrialScheduler:
    """Interface for implementing a Trial Scheduler class."""
    CONTINUE: str
    PAUSE: str
    STOP: str
    def on_trial_add(self, trial_runner: trial_runner.TrialRunner, trial: Trial): ...
    def on_trial_remove(self, trial_runner: trial_runner.TrialRunner, trial: Trial): ...
