from _typeshed import Incomplete
from optuna import _study_summary, exceptions as exceptions, trial as trial
from optuna._deprecated import deprecated as deprecated

StudyDirection: Incomplete
TrialState: Incomplete

class FrozenTrial(trial.FrozenTrial): ...
class StudySummary(_study_summary.StudySummary): ...
class TrialPruned(exceptions.TrialPruned):
    """Exception for pruned trials."""
