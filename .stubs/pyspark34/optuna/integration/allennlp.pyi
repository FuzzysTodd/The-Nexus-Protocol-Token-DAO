import optuna
from allennlp.training import GradientDescentTrainer as GradientDescentTrainer, TrainerCallback
from optuna import Trial as Trial, load_study as load_study
from optuna._experimental import experimental as experimental
from optuna._imports import try_import as try_import
from typing import Any, Callable, Dict, List

class TrainerCallback:
    """Stub for TrainerCallback."""
    @classmethod
    def register(cls, *args: Any, **kwargs: Any) -> Callable:
        """Stub method for `TrainerCallback.register`.

            This method has the same signature as
            `Registrable.register <https://docs.allennlp.org/master/
            api/common/registrable/#registrable>`_ in AllenNLP.

            """

def dump_best_config(input_config_file: str, output_config_file: str, study: optuna.Study) -> None:
    """Save JSON config file with environment variables and best performing hyperparameters.

    Args:
        input_config_file:
            Input Jsonnet config file used with
            :class:`~optuna.integration.AllenNLPExecutor`.
        output_config_file:
            Output JSON config file.
        study:
            Instance of :class:`~optuna.study.Study`.
            Note that :func:`~optuna.study.Study.optimize` must have been called.

    """

class AllenNLPExecutor:
    """AllenNLP extension to use optuna with Jsonnet config file.

    This feature is experimental since AllenNLP major release will come soon.
    The interface may change without prior notice to correspond to the update.

    See the examples of `objective function <https://github.com/optuna/optuna-examples/tree/
    main/allennlp/allennlp_jsonnet.py>`_.

    You can also see the tutorial of our AllenNLP integration on
    `AllenNLP Guide <https://guide.allennlp.org/hyperparameter-optimization>`_.

    .. note::
        From Optuna v2.1.0, users have to cast their parameters by using methods in Jsonnet.
        Call ``std.parseInt`` for integer, or ``std.parseJson`` for floating point.
        Please see the `example configuration <https://github.com/optuna/optuna-examples/tree/main/
        allennlp/classifier.jsonnet>`_.

    .. note::
        In :class:`~optuna.integration.AllenNLPExecutor`,
        you can pass parameters to AllenNLP by either defining a search space using
        Optuna suggest methods or setting environment variables just like AllenNLP CLI.
        If a value is set in both a search space in Optuna and the environment variables,
        the executor will use the value specified in the search space in Optuna.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current evaluation
            of the objective function.
        config_file:
            Config file for AllenNLP.
            Hyperparameters should be masked with ``std.extVar``.
            Please refer to `the config example <https://github.com/allenai/allentune/blob/
            master/examples/classifier.jsonnet>`_.
        serialization_dir:
            A path which model weights and logs are saved.
        metrics:
            An evaluation metric for the result of ``objective``.
        force:
            If :obj:`True`, an executor overwrites the output directory if it exists.
        file_friendly_logging:
            If :obj:`True`, tqdm status is printed on separate lines and slows tqdm refresh rate.
        include_package:
            Additional packages to include.
            For more information, please see
            `AllenNLP documentation <https://docs.allennlp.org/master/api/commands/train/>`_.

    """
    def __init__(self, trial: optuna.Trial, config_file: str, serialization_dir: str, metrics: str = 'best_validation_accuracy', *, include_package: str | List[str] | None = None, force: bool = False, file_friendly_logging: bool = False) -> None: ...
    def run(self) -> float:
        """Train a model using AllenNLP."""

class AllenNLPPruningCallback(TrainerCallback):
    """AllenNLP callback to prune unpromising trials.

    See `the example <https://github.com/optuna/optuna-examples/tree/main/
    allennlp/allennlp_simple.py>`__
    if you want to add a pruning callback which observes a metric.

    You can also see the tutorial of our AllenNLP integration on
    `AllenNLP Guide <https://guide.allennlp.org/hyperparameter-optimization>`_.

    .. note::
        When :class:`~optuna.integration.AllenNLPPruningCallback` is instantiated in Python script,
        trial and monitor are mandatory.

        On the other hand, when :class:`~optuna.integration.AllenNLPPruningCallback` is used with
        :class:`~optuna.integration.AllenNLPExecutor`, ``trial`` and ``monitor``
        would be ``None``. :class:`~optuna.integration.AllenNLPExecutor` sets
        environment variables for a study name, trial id, monitor, and storage.
        Then :class:`~optuna.integration.AllenNLPPruningCallback`
        loads them to restore ``trial`` and ``monitor``.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` corresponding to the current evaluation of the
            objective function.
        monitor:
            An evaluation metric for pruning, e.g. ``validation_loss`` or
            ``validation_accuracy``.

    """
    def __init__(self, trial: optuna.trial.Trial | None = None, monitor: str | None = None) -> None: ...
    def on_epoch(self, trainer: GradientDescentTrainer, metrics: Dict[str, Any], epoch: int, is_primary: bool = True, **kwargs: Any) -> None:
        """Check if a training reaches saturation.

        Args:
            trainer:
                AllenNLP's trainer
            metrics:
                Dictionary of metrics.
            epoch:
                Number of current epoch.
            is_primary:
                A flag for AllenNLP internal.

        """
