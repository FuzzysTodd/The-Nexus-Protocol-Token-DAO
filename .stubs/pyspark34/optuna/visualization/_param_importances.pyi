from _typeshed import Incomplete
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.importance._base import BaseImportanceEvaluator as BaseImportanceEvaluator
from optuna.logging import get_logger as get_logger
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from optuna.visualization._plotly_imports import go as go
from typing import Callable, List

logger: Incomplete

def plot_param_importances(study: Study, evaluator: BaseImportanceEvaluator | None = None, params: List[str] | None = None, *, target: Callable[[FrozenTrial], float] | None = None, target_name: str = 'Objective Value') -> go.Figure:
    '''Plot hyperparameter importances.

    Example:

        The following code snippet shows how to plot hyperparameter importances.

        .. plotly::

            import optuna


            def objective(trial):
                x = trial.suggest_int("x", 0, 2)
                y = trial.suggest_float("y", -1.0, 1.0)
                z = trial.suggest_float("z", 0.0, 1.5)
                return x ** 2 + y ** 3 - z ** 4


            sampler = optuna.samplers.RandomSampler(seed=10)
            study = optuna.create_study(sampler=sampler)
            study.optimize(objective, n_trials=100)

            fig = optuna.visualization.plot_param_importances(study)
            fig.show()

    .. seealso::

        This function visualizes the results of :func:`optuna.importance.get_param_importances`.

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
        A :class:`plotly.graph_objs.Figure` object.

    Raises:
        :exc:`ValueError`:
            If ``target`` is :obj:`None` and ``study`` is being used for multi-objective
            optimization.
    '''
