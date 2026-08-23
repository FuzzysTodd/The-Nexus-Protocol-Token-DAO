import torch.nn as nn
from .config import RetiariiExeConfig as RetiariiExeConfig
from _typeshed import Incomplete
from nni.experiment import Experiment
from nni.nas.evaluator import Evaluator
from nni.nas.mutable import Mutator
from nni.nas.strategy import BaseStrategy
from typing import Any, List

__all__ = ['RetiariiExeConfig', 'RetiariiExperiment', 'preprocess_model', 'debug_mutated_model']

def preprocess_model(base_model, evaluator, applied_mutators, full_ir: bool = True, dummy_input: Incomplete | None = None, oneshot: bool = False): ...
def debug_mutated_model(base_model, evaluator, applied_mutators) -> None:
    """
    Locally run only one trial without launching an experiment for debug purpose, then exit.
    For example, it can be used to quickly check shape mismatch.

    Specifically, it applies mutators (default to choose the first candidate for the choices)
    to generate a new model, then run this model locally.

    The model will be parsed with graph execution engine.

    Parameters
    ----------
    base_model : nni.retiarii.nn.pytorch.nn.Module
        the base model
    evaluator : nni.retiarii.graph.Evaluator
        the training class of the generated models
    applied_mutators : list
        a list of mutators that will be applied on the base model for generating a new model
    """

class RetiariiExperiment(Experiment):
    """
    The entry for a NAS experiment.
    Users can use this class to start/stop or inspect an experiment, like exporting the results.

    Experiment is a sub-class of :class:`nni.experiment.Experiment`, there are many similarities such as
    configurable training service to distributed running the experiment on remote server.
    But unlike :class:`nni.experiment.Experiment`, RetiariiExperiment doesn't support configure:

    - ``trial_code_directory``, which can only be current working directory.
    - ``search_space``, which is auto-generated in NAS.
    - ``trial_command``, which must be ``python -m nni.retiarii.trial_entry`` to launch the modulized trial code.

    RetiariiExperiment also doesn't have tuner/assessor/advisor, because they are also implemented in strategy.

    Also, unlike :class:`nni.experiment.Experiment` which is bounded to a node server,
    RetiariiExperiment optionally starts a node server to schedule the trials, when the strategy is a multi-trial strategy.
    When the strategy is one-shot, the step of launching node server is omitted, and the experiment is run locally by default.

    Configurations of experiments, such as execution engine, number of GPUs allocated,
    should be put into a :class:`RetiariiExeConfig` and used as an argument of :meth:`RetiariiExperiment.run`.

    Parameters
    ----------
    base_model : nn.Module
        The model defining the search space / base skeleton without mutation.
        It should be wrapped by decorator ``nni.retiarii.model_wrapper``.
    evaluator : nni.retiarii.Evaluator, default = None
        Evaluator for the experiment.
        If you are using a one-shot trainer, it should be placed here, although this usage is deprecated.
    applied_mutators : list of nni.retiarii.Mutator, default = None
        Mutators os mutate the base model. If none, mutators are skipped.
        Note that when ``base_model`` uses inline mutations (e.g., LayerChoice), ``applied_mutators`` must be empty / none.
    strategy : nni.retiarii.strategy.BaseStrategy, default = None
        Exploration strategy. Can be multi-trial or one-shot.
    trainer : BaseOneShotTrainer
        Kept for compatibility purposes.

    Examples
    --------
    Multi-trial NAS:

    >>> base_model = Net()
    >>> search_strategy = strategy.Random()
    >>> model_evaluator = FunctionalEvaluator(evaluate_model)
    >>> exp = RetiariiExperiment(base_model, model_evaluator, [], search_strategy)
    >>> exp_config = RetiariiExeConfig('local')
    >>> exp_config.trial_concurrency = 2
    >>> exp_config.max_trial_number = 20
    >>> exp_config.training_service.use_active_gpu = False
    >>> exp.run(exp_config, 8081)

    One-shot NAS:

    >>> base_model = Net()
    >>> search_strategy = strategy.DARTS()
    >>> evaluator = pl.Classification(train_dataloader=train_loader, val_dataloaders=valid_loader)
    >>> exp = RetiariiExperiment(base_model, evaluator, [], search_strategy)
    >>> exp_config = RetiariiExeConfig()
    >>> exp_config.execution_engine = 'oneshot'  # must be set of one-shot strategy
    >>> exp.run(exp_config)

    Export top models:

    >>> for model_dict in exp.export_top_models(formatter='dict'):
    ...     print(model_dict)
    >>> with nni.retarii.fixed_arch(model_dict):
    ...     final_model = Net()
    """
    config: Incomplete
    base_model: Incomplete
    evaluator: Incomplete
    applied_mutators: Incomplete
    strategy: Incomplete
    def __init__(self, base_model: nn.Module = ..., evaluator: Evaluator = ..., applied_mutators: List[Mutator] = ..., strategy: BaseStrategy = ..., trainer: Any = None) -> None: ...
    def start(self, *args, **kwargs) -> None:
        """
        By design, the only different between `start` and `run` is that `start` is asynchronous,
        while `run` waits the experiment to complete. RetiariiExperiment always waits the experiment
        to complete as strategy runs in foreground.
        """
    def run(self, config: RetiariiExeConfig | None = None, port: int = 8080, debug: bool = False) -> None:
        """
        Run the experiment.
        This function will block until experiment finish or error.
        """
    def stop(self) -> None:
        """
        Stop background experiment.
        """
    def export_top_models(self, top_k: int = 1, optimize_mode: str = 'maximize', formatter: str = 'dict') -> Any:
        """
        Export several top performing models.

        For one-shot algorithms, only top-1 is supported. For others, ``optimize_mode`` and ``formatter`` are
        available for customization.

        The concrete behavior of export depends on each strategy.
        See the documentation of each strategy for detailed specifications.

        Parameters
        ----------
        top_k : int
            How many models are intended to be exported.
        optimize_mode : str
            ``maximize`` or ``minimize``. Not supported by one-shot algorithms.
            ``optimize_mode`` is likely to be removed and defined in strategy in future.
        formatter : str
            Support ``code`` and ``dict``. Not supported by one-shot algorithms.
            If ``code``, the python code of model will be returned.
            If ``dict``, the mutation history will be returned.
        """
    @staticmethod
    def view(experiment_id: str, port: int = 8080, non_blocking: bool = False) -> RetiariiExperiment | None:
        """
        View a stopped experiment.

        Parameters
        ----------
        experiment_id
            The stopped experiment id.
        port
            The port of web UI.
        non_blocking
            If false, run in the foreground. If true, run in the background.
        """
    @staticmethod
    def resume(experiment_id: str, port: int = 8080, debug: bool = False) -> RetiariiExperiment:
        """
        Resume a stopped experiment.

        Parameters
        ----------
        experiment_id
            The stopped experiment id.
        port
            The port of web UI.
        debug
            Whether to start in debug mode.
        """
