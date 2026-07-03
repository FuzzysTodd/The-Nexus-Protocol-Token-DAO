from _typeshed import Incomplete
from nni import ClassArgsValidator
from nni.tuner import Tuner

__all__ = ['RandomTuner']

class RandomTuner(Tuner):
    """
    A naive tuner that generates fully random hyperparameters.

    Examples
    --------

    .. code-block::

        config.tuner.name = 'Random'
        config.tuner.class_args = {
            'seed': 100
        }

    Parameters
    ----------
    seed
        The random seed.
    """
    space: Incomplete
    rng: Incomplete
    dedup: Incomplete
    def __init__(self, seed: int | None = None, optimize_mode: str | None = None) -> None: ...
    def update_search_space(self, space) -> None: ...
    def generate_parameters(self, *args, **kwargs): ...
    def receive_trial_result(self, *args, **kwargs) -> None: ...

class RandomClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...
