from .model_factory import CurveModel as CurveModel
from _typeshed import Incomplete
from nni import ClassArgsValidator as ClassArgsValidator
from nni.assessor import AssessResult as AssessResult, Assessor as Assessor
from nni.utils import extract_scalar_history as extract_scalar_history

logger: Incomplete

class CurvefittingClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...

class CurvefittingAssessor(Assessor):
    """
    CurvefittingAssessor uses learning curve fitting algorithm to predict the learning curve performance in the future.

    The intermediate result **must** be accuracy. Curve fitting does not support minimizing loss.

    Curve fitting assessor is an LPA (learning, predicting, assessing) algorithm.
    It stops a pending trial X at step S if the trial's forecast result at target step is convergence and lower than the
    best performance in the history.

    Paper: `Speeding up Automatic Hyperparameter Optimization of Deep Neural Networks by Extrapolation of Learning Curves
    <https://ml.informatik.uni-freiburg.de/wp-content/uploads/papers/15-IJCAI-Extrapolation_of_Learning_Curves.pdf>`__

    Examples
    --------

    .. code-block::

        config.assessor.name = 'Curvefitting'
        config.tuner.class_args = {
            'epoch_num': 20,
            'start_step': 6,
            'threshold': 9,
            'gap': 1,
        }

    Parameters
    ----------
    epoch_num : int
        The total number of epochs.

        We need to know the number of epochs to determine which points we need to predict.

    start_step : int
        A trial is determined to be stopped or not only after receiving start_step number of intermediate results.

    threshold : float
        The threshold that we use to decide to early stop the worst performance curve.

        For example: if threshold = 0.95, and the best performance in the history is 0.9,
        then we will stop the trial who's predicted value is lower than 0.95 * 0.9 = 0.855.

    gap : int
        The gap interval between assessor judgements.

        For example: if gap = 2, start_step = 6,
        then we will assess the result when we get 6, 8, 10, 12, ... intermediate results.
    """
    target_pos: Incomplete
    start_step: Incomplete
    threshold: Incomplete
    gap: Incomplete
    last_judgment_num: Incomplete
    set_best_performance: bool
    completed_best_performance: Incomplete
    trial_history: Incomplete
    def __init__(self, epoch_num: int = 20, start_step: int = 6, threshold: float = 0.95, gap: int = 1) -> None: ...
    def trial_end(self, trial_job_id, success) -> None: ...
    def assess_trial(self, trial_job_id, trial_history): ...
