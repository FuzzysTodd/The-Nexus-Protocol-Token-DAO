import optuna
from _typeshed import Incomplete
from fastai.callback.tracker import TrackerCallback
from optuna._imports import try_import as try_import

TrackerCallback = object

class FastAIV2PruningCallback(TrackerCallback):
    '''FastAI callback to prune unpromising trials for fastai.

    .. note::
        This callback is for fastai>=2.0.

    See `the example <https://github.com/optuna/optuna-examples/blob/main/
    fastai/fastaiv2_simple.py>`__
    if you want to add a pruning callback which monitors validation loss of a ``Learner``.

    Example:

        Register a pruning callback to ``learn.fit`` and ``learn.fit_one_cycle``.

        .. code::

            learn = cnn_learner(dls, resnet18, metrics=[error_rate])
            learn.fit(n_epochs, cbs=[FastAIPruningCallback(trial)])  # Monitor "valid_loss"
            learn.fit_one_cycle(
                n_epochs,
                lr_max,
                cbs=[FastAIPruningCallback(trial, monitor="error_rate")],  # Monitor "error_rate"
            )


    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current
            evaluation of the objective function.
        monitor:
            An evaluation metric for pruning, e.g. ``valid_loss`` or ``accuracy``.
            Please refer to `fastai.callback.TrackerCallback reference
            <https://docs.fast.ai/callback.tracker#TrackerCallback>`_ for further
            details.
    '''
    trial: Incomplete
    def __init__(self, trial: optuna.Trial, monitor: str = 'valid_loss') -> None: ...
    def after_epoch(self) -> None: ...
    def after_fit(self) -> None: ...
FastAIPruningCallback = FastAIV2PruningCallback
