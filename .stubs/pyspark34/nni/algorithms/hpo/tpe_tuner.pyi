from _typeshed import Incomplete
from nni.tuner import Tuner
from typing import Any, NamedTuple
from typing_extensions import Literal

__all__ = ['TpeTuner', 'TpeArguments']

class TpeArguments(NamedTuple):
    '''
    Hyperparameters of TPE algorithm itself.

    To avoid confusing with trials\' hyperparameters to be tuned, these are called "arguments" here.

    Parameters
    ----------
    constant_liar_type
        TPE algorithm itself does not support parallel tuning.
        This parameter specifies how to optimize for trial_concurrency > 1.

        None (or "null" in YAML) means do not optimize. This is the default behavior in legacy version.

        How each liar works is explained in paper\'s section 6.1.
        In general "best" suit for small trial number and "worst" suit for large trial number.
        (:doc:`experiment result </sharings/parallelizing_tpe_search>`)

    n_startup_jobs
        The first N hyperparameters are generated fully randomly for warming up.
        If the search space is large, you can increase this value.
        Or if max_trial_number is small, you may want to decrease it.

    n_ei_candidates
        For each iteration TPE samples EI for N sets of parameters and choose the best one. (loosely speaking)

    linear_forgetting
        TPE will lower the weights of old trials.
        This controls how many iterations it takes for a trial to start decay.

    prior_weight
        TPE treats user provided search space as prior.
        When generating new trials, it also incorporates the prior in trial history by transforming the search space to
        one trial configuration (i.e., each parameter of this configuration chooses the mean of its candidate range).
        Here, prior_weight determines the weight of this trial configuration in the history trial configurations.

        With prior weight 1.0, the search space is treated as one good trial.
        For example, "normal(0, 1)" effectly equals to a trial with x = 0 which has yielded good result.

    gamma
        Controls how many trials are considered "good".
        The number is calculated as "min(gamma * sqrt(N), linear_forgetting)".
    '''
    constant_liar_type: Literal['best', 'worst', 'mean'] | None = ...
    n_startup_jobs: int = ...
    n_ei_candidates: int = ...
    linear_forgetting: int = ...
    prior_weight: float = ...
    gamma: float = ...

class TpeTuner(Tuner):
    """
    Tree-structured Parzen Estimator (TPE) tuner.

    TPE is a lightweight tuner that has no extra dependency and supports all search space types,
    designed to be the default tuner.

    It has the drawback that TPE cannot discover relationship between different hyperparameters.

    **Implementation**

    TPE is an SMBO algorithm.
    It models P(x|y) and P(y) where x represents hyperparameters and y the evaluation result.
    P(x|y) is modeled by transforming the generative process of hyperparameters,
    replacing the distributions of the configuration prior with non-parametric densities.

    Paper: `Algorithms for Hyper-Parameter Optimization
    <https://proceedings.neurips.cc/paper/2011/file/86e8f7ab32cfd12577bc2619bc635690-Paper.pdf>`__

    Examples
    --------

    .. code-block::

        ## minimal config ##

        config.tuner.name = 'TPE'
        config.tuner.class_args = {
            'optimize_mode': 'maximize'
        }

    .. code-block::

        ## advanced config ##

        config.tuner.name = 'TPE'
        config.tuner.class_args = {
            'optimize_mode': maximize,
            'seed': 12345,
            'tpe_args': {
                'constant_liar_type': 'mean',
                'n_startup_jobs': 10,
                'n_ei_candidates': 20,
                'linear_forgetting': 100,
                'prior_weight': 0,
                'gamma': 0.5
            }
        }

    Parameters
    ----------
    optimze_mode: Literal['minimize', 'maximize']
        Whether optimize to minimize or maximize trial result.
    seed
        The random seed.
    tpe_args
        Advanced users can use this to customize TPE tuner.
        See :class:`TpeArguments` for details.
    """
    optimize_mode: Incomplete
    args: Incomplete
    space: Incomplete
    liar: Incomplete
    dedup: Incomplete
    rng: Incomplete
    def __init__(self, optimize_mode: Literal['minimize', 'maximize'] = 'minimize', seed: int | None = None, tpe_args: dict[str, Any] | None = None) -> None: ...
    def update_search_space(self, space) -> None: ...
    def generate_parameters(self, parameter_id, **kwargs): ...
    def receive_trial_result(self, parameter_id, _parameters, value, **kwargs) -> None: ...
    def trial_end(self, parameter_id, _success, **kwargs) -> None: ...
    def import_data(self, data) -> None: ...

class Record(NamedTuple):
    param: int | float
    loss: float

class BestLiar:
    def __init__(self) -> None: ...
    def update(self, loss) -> None: ...
    def lie(self): ...

class WorstLiar:
    def __init__(self) -> None: ...
    def update(self, loss) -> None: ...
    def lie(self): ...

class MeanLiar:
    def __init__(self) -> None: ...
    def update(self, loss) -> None: ...
    def lie(self): ...
