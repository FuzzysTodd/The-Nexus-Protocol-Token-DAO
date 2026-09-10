from ignite.engine import Engine as Engine
from optuna.trial import Trial as Trial

class PyTorchIgnitePruningHandler:
    """PyTorch Ignite handler to prune unpromising trials.

    See `the example <https://github.com/optuna/optuna-examples/blob/main/
    pytorch/pytorch_ignite_simple.py>`__
    if you want to add a pruning handler which observes validation accuracy.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current evaluation of the
            objective function.
        metric:
            A name of metric for pruning, e.g., ``accuracy`` and ``loss``.
        trainer:
            A trainer engine of PyTorch Ignite. Please refer to `ignite.engine.Engine reference
            <https://pytorch.org/ignite/engine.html#ignite.engine.Engine>`_ for further details.
    """
    def __init__(self, trial: Trial, metric: str, trainer: Engine) -> None: ...
    def __call__(self, engine: Engine) -> None: ...
