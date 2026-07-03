import optuna
from fastai.basic_train import Learner as Learner
from fastai.callbacks import TrackerCallback
from optuna._deprecated import deprecated as deprecated
from optuna._imports import try_import as try_import
from typing import Any

TrackerCallback = object

class FastAIV1PruningCallback(TrackerCallback):
    '''FastAI callback to prune unpromising trials for fastai.

    .. note::
        This callback is for fastai<2.0.

    See `the example <https://github.com/optuna/optuna-examples/blob/main/
    fastai/fastaiv1_simple.py>`__
    if you want to add a pruning callback which monitors validation loss of a ``Learner``.

    Example:

        Register a pruning callback to ``learn.fit`` and ``learn.fit_one_cycle``.

        .. code::

            learn.fit(n_epochs, callbacks=[FastAIPruningCallback(learn, trial, "valid_loss")])
            learn.fit_one_cycle(
                n_epochs,
                cyc_len,
                max_lr,
                callbacks=[FastAIPruningCallback(learn, trial, "valid_loss")],
            )


    Args:
        learn:
            `fastai.basic_train.Learner <https://docs.fast.ai/basic_train.html#Learner>`_.
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current
            evaluation of the objective function.
        monitor:
            An evaluation metric for pruning, e.g. ``valid_loss`` and ``Accuracy``.
            Please refer to `fastai.callbacks.TrackerCallback reference
            <https://fastai1.fast.ai/callbacks.tracker.html#TrackerCallback>`_ for further
            details.
    '''
    def __init__(self, learn: Learner, trial: optuna.trial.Trial, monitor: str) -> None: ...
    def on_epoch_end(self, epoch: int, **kwargs: Any) -> None: ...
