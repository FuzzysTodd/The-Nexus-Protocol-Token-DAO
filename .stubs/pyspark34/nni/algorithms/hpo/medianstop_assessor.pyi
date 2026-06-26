from _typeshed import Incomplete
from nni import ClassArgsValidator as ClassArgsValidator
from nni.assessor import AssessResult as AssessResult, Assessor as Assessor
from nni.utils import extract_scalar_history as extract_scalar_history
from typing_extensions import Literal

logger: Incomplete

class MedianstopClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...

class MedianstopAssessor(Assessor):
    """
    The median stopping rule stops a pending trial X at step S
    if the trial’s best objective value by step S is strictly worse than the median value
    of the running averages of all completed trials’ objectives reported up to step S

    Paper: `Google Vizer: A Service for Black-Box Optimization
    <https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46180.pdf>`__

    Examples
    --------

    .. code-block::

        config.assessor.name = 'Medianstop'
        config.tuner.class_args = {
            'optimize_mode': 'maximize',
            'start_step': 5
        }

    Parameters
    ----------
    optimize_mode
        Whether optimize to minimize or maximize trial result.
    start_step
        A trial is determined to be stopped or not
        only after receiving start_step number of reported intermediate results.
    """
    def __init__(self, optimize_mode: Literal['minimize', 'maximize'] = 'maximize', start_step: int = 0) -> None: ...
    def trial_end(self, trial_job_id, success) -> None: ...
    def assess_trial(self, trial_job_id, trial_history): ...
