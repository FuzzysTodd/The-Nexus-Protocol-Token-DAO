from optuna._experimental import experimental as experimental
from optuna.importance._base import BaseImportanceEvaluator as BaseImportanceEvaluator
from optuna.logging import get_logger as get_logger
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from optuna.visualization.matplotlib._matplotlib_imports import Axes as Axes, cm as cm, plt as plt
from typing import Callable, List

def plot_param_importances(study: Study, evaluator: BaseImportanceEvaluator | None = None, params: List[str] | None = None, *, target: Callable[[FrozenTrial], float] | None = None, target_name: str = 'Objective Value') -> Axes:
    '''Plot hyperparameter importances with Matplotlib.

    .. seealso::
        Please refer to :func:`optuna.visualization.plot_param_importances` for an example.

    Example:

        The following code snippet shows how to plot hyperparameter importances.

        .. plot::

            import optuna


            def objective(trial):
                x = trial.suggest_int("x", 0, 2)
                y = trial.suggest_float("y", -1.0, 1.0)
                z = trial.suggest_float("z", 0.0, 1.5)
                return x ** 2 + y ** 3 - z ** 4


            sampler = optuna.samplers.RandomSampler(seed=10)
            study = optuna.create_study(sampler=sampler)
            study.optimize(objective, n_trials=100)

            optuna.visualization.matplotlib.plot_param_importances(study)

    Args:
        study:
            An optimized study.
        evaluator:
            An importance evaluator object that specifies which algorithm to base the importance
            assessment on.
            Defaults to
            :class:`~optuna.importance.FanovaImportanceEvaluator`.
        params:
            A list of names of parameters to assess.
            If :obj:`None`, all parameters that are present in all of the completed trials are
            assessed.
        target:
            A function to specify the value to display. If it is :obj:`None` and ``study`` is being
            used for single-objective optimization, the objective values are plotted.

            .. note::
                Specify this argument if ``study`` is being used for multi-objective
                optimization. For example, to get the hyperparameter importance of the first
                objective, use ``target=lambda t: t.values[0]`` for the target parameter.
        target_name:
            Target\'s name to display on the axis label.

    Returns:
        A :class:`matplotlib.axes.Axes` object.

    Raises:
        :exc:`ValueError`:
            If ``target`` is :obj:`None` and ``study`` is being used for multi-objective
            optimization.
    '''
