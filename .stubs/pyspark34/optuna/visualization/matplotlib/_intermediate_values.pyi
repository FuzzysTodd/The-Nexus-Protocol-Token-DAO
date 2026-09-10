from optuna._experimental import experimental as experimental
from optuna.logging import get_logger as get_logger
from optuna.study import Study as Study
from optuna.trial import TrialState as TrialState
from optuna.visualization.matplotlib._matplotlib_imports import Axes as Axes, plt as plt

def plot_intermediate_values(study: Study) -> Axes:
    '''Plot intermediate values of all trials in a study with Matplotlib.

    .. note::
        Please refer to `matplotlib.pyplot.legend
        <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html>`_
        to adjust the style of the generated legend.

    Example:

        The following code snippet shows how to plot intermediate values.

        .. plot::

            import optuna


            def f(x):
                return (x - 2) ** 2


            def df(x):
                return 2 * x - 4


            def objective(trial):
                lr = trial.suggest_float("lr", 1e-5, 1e-1, log=True)

                x = 3
                for step in range(128):
                    y = f(x)

                    trial.report(y, step=step)
                    if trial.should_prune():
                        raise optuna.TrialPruned()

                    gy = df(x)
                    x -= gy * lr

                return y


            sampler = optuna.samplers.TPESampler(seed=10)
            study = optuna.create_study(sampler=sampler)
            study.optimize(objective, n_trials=16)

            optuna.visualization.matplotlib.plot_intermediate_values(study)

    .. seealso::
        Please refer to :func:`optuna.visualization.plot_intermediate_values` for an example.

    Args:
        study:
            A :class:`~optuna.study.Study` object whose trials are plotted for their intermediate
            values.

    Returns:
        A :class:`matplotlib.axes.Axes` object.
    '''
