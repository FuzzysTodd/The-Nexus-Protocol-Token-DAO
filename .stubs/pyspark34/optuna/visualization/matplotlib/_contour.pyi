from optuna._experimental import experimental as experimental
from optuna.logging import get_logger as get_logger
from optuna.study import Study as Study, StudyDirection as StudyDirection
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from optuna.visualization.matplotlib._matplotlib_imports import Axes as Axes, Colormap as Colormap, ContourSet as ContourSet, plt as plt
from typing import Callable, List

def plot_contour(study: Study, params: List[str] | None = None, *, target: Callable[[FrozenTrial], float] | None = None, target_name: str = 'Objective Value') -> Axes:
    '''Plot the parameter relationship as contour plot in a study with Matplotlib.

    Note that, if a parameter contains missing values, a trial with missing values is not plotted.

    .. seealso::
        Please refer to :func:`optuna.visualization.plot_contour` for an example.

    Warnings:
        Output figures of this Matplotlib-based
        :func:`~optuna.visualization.matplotlib.plot_contour` function would be different from
        those of the Plotly-based :func:`~optuna.visualization.plot_contour`.

    Example:

        The following code snippet shows how to plot the parameter relationship as contour plot.

        .. plot::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", -100, 100)
                y = trial.suggest_categorical("y", [-1, 0, 1])
                return x ** 2 + y


            sampler = optuna.samplers.TPESampler(seed=10)
            study = optuna.create_study(sampler=sampler)
            study.optimize(objective, n_trials=30)

            optuna.visualization.matplotlib.plot_contour(study, params=["x", "y"])

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
            Target\'s name to display on the color bar.

    Returns:
        A :class:`matplotlib.axes.Axes` object.

    Raises:
        :exc:`ValueError`:
            If ``target`` is :obj:`None` and ``study`` is being used for multi-objective
            optimization.
    '''
