from optuna._experimental import experimental as experimental
from optuna._study_direction import StudyDirection as StudyDirection
from optuna.logging import get_logger as get_logger
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from optuna.visualization.matplotlib._matplotlib_imports import Axes as Axes, LineCollection as LineCollection, plt as plt
from typing import Callable, List

def plot_parallel_coordinate(study: Study, params: List[str] | None = None, *, target: Callable[[FrozenTrial], float] | None = None, target_name: str = 'Objective Value') -> Axes:
    '''Plot the high-dimensional parameter relationships in a study with Matplotlib.

    .. seealso::
        Please refer to :func:`optuna.visualization.plot_parallel_coordinate` for an example.

    Example:

        The following code snippet shows how to plot the high-dimensional parameter relationships.

        .. plot::

            import optuna

            def objective(trial):
                x = trial.suggest_float("x", -100, 100)
                y = trial.suggest_categorical("y", [-1, 0, 1])
                return x ** 2 + y


            sampler = optuna.samplers.TPESampler(seed=10)
            study = optuna.create_study(sampler=sampler)
            study.optimize(objective, n_trials=10)

            optuna.visualization.matplotlib.plot_parallel_coordinate(study, params=["x", "y"])

    Args:
        study:
            A :class:`~optuna.study.Study` object whose trials are plotted for their target values.
        params:
            Parameter list to visualize. The default is all parameters.
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
