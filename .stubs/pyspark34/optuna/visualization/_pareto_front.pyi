from optuna._experimental import experimental as experimental
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from optuna.visualization._plotly_imports import go as go
from typing import List

def plot_pareto_front(study: Study, *, target_names: List[str] | None = None, include_dominated_trials: bool = True, axis_order: List[int] | None = None) -> go.Figure:
    '''Plot the Pareto front of a study.

    Example:

        The following code snippet shows how to plot the Pareto front of a study.

        .. plotly::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", 0, 5)
                y = trial.suggest_float("y", 0, 3)

                v0 = 4 * x ** 2 + 4 * y ** 2
                v1 = (x - 5) ** 2 + (y - 5) ** 2
                return v0, v1


            study = optuna.create_study(directions=["minimize", "minimize"])
            study.optimize(objective, n_trials=50)

            fig = optuna.visualization.plot_pareto_front(study)
            fig.show()

    Args:
        study:
            A :class:`~optuna.study.Study` object whose trials are plotted for their objective
            values.
        target_names:
            Objective name list used as the axis titles. If :obj:`None` is specified,
            "Objective {objective_index}" is used instead.
        include_dominated_trials:
            A flag to include all dominated trial\'s objective values.
        axis_order:
            A list of indices indicating the axis order. If :obj:`None` is specified,
            default order is used.

    Returns:
        A :class:`plotly.graph_objs.Figure` object.

    Raises:
        :exc:`ValueError`:
            If the number of objectives of ``study`` isn\'t 2 or 3.
    '''
