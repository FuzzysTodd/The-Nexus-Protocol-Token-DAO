import chainer
import optuna
from chainer.training.extension import Extension
from chainer.training.triggers import IntervalTrigger, ManualScheduleTrigger
from typing import Tuple

Extension = object

class ChainerPruningExtension(Extension):
    """Chainer extension to prune unpromising trials.

    See `the example <https://github.com/optuna/optuna-examples/blob/main/
    chainer/chainer_integration.py>`__
    if you want to add a pruning extension which observes validation
    accuracy of a `Chainer Trainer <https://docs.chainer.org/en/stable/
    reference/generated/chainer.training.Trainer.html>`_.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current evaluation of the
            objective function.
        observation_key:
            An evaluation metric for pruning, e.g., ``main/loss`` and
            ``validation/main/accuracy``. Please refer to
            `chainer.Reporter reference <https://docs.chainer.org/en/stable/reference/
            util/generated/chainer.Reporter.html>`_ for further details.
        pruner_trigger:
            A trigger to execute pruning. ``pruner_trigger`` is an instance of
            `IntervalTrigger <https://docs.chainer.org/en/stable/reference/generated/
            chainer.training.triggers.IntervalTrigger.html>`_ or
            `ManualScheduleTrigger <https://docs.chainer.org/en/stable/reference/generated/
            chainer.training.triggers.ManualScheduleTrigger.html>`_. `IntervalTrigger <https://
            docs.chainer.org/en/stable/reference/generated/chainer.training.triggers.
            IntervalTrigger.html>`_ can be specified by a tuple of the interval length and its
            unit like ``(1, 'epoch')``.
    """
    def __init__(self, trial: optuna.trial.Trial, observation_key: str, pruner_trigger: Tuple[int, str] | IntervalTrigger | ManualScheduleTrigger) -> None: ...
    def __call__(self, trainer: chainer.training.Trainer) -> None: ...
