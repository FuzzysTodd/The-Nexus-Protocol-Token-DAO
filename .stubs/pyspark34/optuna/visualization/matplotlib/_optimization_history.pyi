from optuna._experimental import experimental as experimental
from optuna.logging import get_logger as get_logger
from optuna.study import Study as Study, StudyDirection as StudyDirection
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from optuna.visualization.matplotlib._matplotlib_imports import Axes as Axes, plt as plt
from typing import Callable

def plot_optimization_history(study: Study, *, target: Callable[[FrozenTrial], float] | None = None, target_name: str = 'Objective Value') -> Axes:
    '''Plot optimization history of all trials in a study with Matplotlib.

    .. seealso::
        Please refer to :func:`optuna.visualization.plot_optimization_history` for an example.

    Example:

        The following code snippet shows how to plot optimization history.

        .. plot::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", -100, 100)
                y = trial.suggest_categorical("y", [-1, 0, 1])
                return x ** 2 + y

            sampler = optuna.samplers.TPESampler(seed=10)
            study = optuna.create_study(sampler=sampler)
            study.optimize(objective, n_trials=10)

            optuna.visualization.matplotlib.plot_optimization_history(study)

    Args:
        study:
            A :class:`~optuna.study.Study` object whose trials are plotted for their target values.
        target:
            A function to specify the value to display. If it is :obj:`None` and ``study`` is being
            used for single-objective optimization, the objective values are plotted.

            .. note::
                Specify this argument if ``study`` is being used for multi-objective optimization.
        target_name:
            Target\'s name to display on the axis label and the legend.

    Returns:
        A :class:`matplotlib.axes.Axes` object.

    Raises:
        :exc:`ValueError`:
            If ``target`` is :obj:`None` and ``study`` is being used for multi-objective
            optimization.
    '''
