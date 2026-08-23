from optuna.logging import get_logger as get_logger
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from optuna.visualization._plotly_imports import go as go
from typing import Callable, Sequence

def plot_edf(study: Study | Sequence[Study], *, target: Callable[[FrozenTrial], float] | None = None, target_name: str = 'Objective Value') -> go.Figure:
    '''Plot the objective value EDF (empirical distribution function) of a study.

    Note that only the complete trials are considered when plotting the EDF.

    .. note::

        EDF is useful to analyze and improve search spaces.
        For instance, you can see a practical use case of EDF in the paper
        `Designing Network Design Spaces <https://arxiv.org/abs/2003.13678>`_.

    .. note::

        The plotted EDF assumes that the value of the objective function is in
        accordance with the uniform distribution over the objective space.

    Example:

        The following code snippet shows how to plot EDF.

        .. plotly::

            import math

            import optuna


            def ackley(x, y):
                a = 20 * math.exp(-0.2 * math.sqrt(0.5 * (x ** 2 + y ** 2)))
                b = math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)))
                return -a - b + math.e + 20


            def objective(trial, low, high):
                x = trial.suggest_float("x", low, high)
                y = trial.suggest_float("y", low, high)
                return ackley(x, y)


            sampler = optuna.samplers.RandomSampler(seed=10)

            # Widest search space.
            study0 = optuna.create_study(study_name="x=[0,5), y=[0,5)", sampler=sampler)
            study0.optimize(lambda t: objective(t, 0, 5), n_trials=500)

            # Narrower search space.
            study1 = optuna.create_study(study_name="x=[0,4), y=[0,4)", sampler=sampler)
            study1.optimize(lambda t: objective(t, 0, 4), n_trials=500)

            # Narrowest search space but it doesn\'t include the global optimum point.
            study2 = optuna.create_study(study_name="x=[1,3), y=[1,3)", sampler=sampler)
            study2.optimize(lambda t: objective(t, 1, 3), n_trials=500)

            fig = optuna.visualization.plot_edf([study0, study1, study2])
            fig.show()

    Args:
        study:
            A target :class:`~optuna.study.Study` object.
            You can pass multiple studies if you want to compare those EDFs.
        target:
            A function to specify the value to display. If it is :obj:`None` and ``study`` is being
            used for single-objective optimization, the objective values are plotted.

            .. note::
                Specify this argument if ``study`` is being used for multi-objective optimization.
        target_name:
            Target\'s name to display on the axis label.

    Returns:
        A :class:`plotly.graph_objs.Figure` object.

    Raises:
        :exc:`ValueError`:
            If ``target`` is :obj:`None` and ``study`` is being used for multi-objective
            optimization.
    '''
