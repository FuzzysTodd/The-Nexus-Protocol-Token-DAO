import optuna
from optuna._study_direction import StudyDirection as StudyDirection
from optuna.pruners._base import BasePruner as BasePruner
from optuna.trial._state import TrialState as TrialState

class SuccessiveHalvingPruner(BasePruner):
    '''Pruner using Asynchronous Successive Halving Algorithm.

    `Successive Halving <https://arxiv.org/abs/1502.07943>`_ is a bandit-based algorithm to
    identify the best one among multiple configurations. This class implements an asynchronous
    version of Successive Halving. Please refer to the paper of
    `Asynchronous Successive Halving <http://arxiv.org/abs/1810.05934>`_ for detailed descriptions.

    Note that, this class does not take care of the parameter for the maximum
    resource, referred to as :math:`R` in the paper. The maximum resource allocated to a trial is
    typically limited inside the objective function (e.g., ``step`` number in `simple_pruning.py
    <https://github.com/optuna/optuna-examples/blob/main/simple_pruning.py>`_,
    ``EPOCH`` number in `chainer_integration.py
    <https://github.com/optuna/optuna-examples/tree/main/chainer/chainer_integration.py#L77>`_).

    .. seealso::
        Please refer to :meth:`~optuna.trial.Trial.report`.

    Example:

        We minimize an objective function with ``SuccessiveHalvingPruner``.

        .. testcode::

            import numpy as np
            from sklearn.datasets import load_iris
            from sklearn.linear_model import SGDClassifier
            from sklearn.model_selection import train_test_split

            import optuna

            X, y = load_iris(return_X_y=True)
            X_train, X_valid, y_train, y_valid = train_test_split(X, y)
            classes = np.unique(y)


            def objective(trial):
                alpha = trial.suggest_float("alpha", 0.0, 1.0)
                clf = SGDClassifier(alpha=alpha)
                n_train_iter = 100

                for step in range(n_train_iter):
                    clf.partial_fit(X_train, y_train, classes=classes)

                    intermediate_value = clf.score(X_valid, y_valid)
                    trial.report(intermediate_value, step)

                    if trial.should_prune():
                        raise optuna.TrialPruned()

                return clf.score(X_valid, y_valid)


            study = optuna.create_study(
                direction="maximize", pruner=optuna.pruners.SuccessiveHalvingPruner()
            )
            study.optimize(objective, n_trials=20)

    Args:
        min_resource:
            A parameter for specifying the minimum resource allocated to a trial
            (in the `paper <http://arxiv.org/abs/1810.05934>`_ this parameter is
            referred to as :math:`r`).
            This parameter defaults to \'auto\' where the value is determined based on a heuristic
            that looks at the number of required steps for the first trial to complete.

            A trial is never pruned until it executes
            :math:`\\mathsf{min}\\_\\mathsf{resource} \\times
            \\mathsf{reduction}\\_\\mathsf{factor}^{
            \\mathsf{min}\\_\\mathsf{early}\\_\\mathsf{stopping}\\_\\mathsf{rate}}`
            steps (i.e., the completion point of the first rung). When the trial completes
            the first rung, it will be promoted to the next rung only
            if the value of the trial is placed in the top
            :math:`{1 \\over \\mathsf{reduction}\\_\\mathsf{factor}}` fraction of
            the all trials that already have reached the point (otherwise it will be pruned there).
            If the trial won the competition, it runs until the next completion point (i.e.,
            :math:`\\mathsf{min}\\_\\mathsf{resource} \\times
            \\mathsf{reduction}\\_\\mathsf{factor}^{
            (\\mathsf{min}\\_\\mathsf{early}\\_\\mathsf{stopping}\\_\\mathsf{rate}
            + \\mathsf{rung})}` steps)
            and repeats the same procedure.

            .. note::
                If the step of the last intermediate value may change with each trial, please
                manually specify the minimum possible step to ``min_resource``.
        reduction_factor:
            A parameter for specifying reduction factor of promotable trials
            (in the `paper <http://arxiv.org/abs/1810.05934>`_ this parameter is
            referred to as :math:`\\eta`).  At the completion point of each rung,
            about :math:`{1 \\over \\mathsf{reduction}\\_\\mathsf{factor}}`
            trials will be promoted.
        min_early_stopping_rate:
            A parameter for specifying the minimum early-stopping rate
            (in the `paper <http://arxiv.org/abs/1810.05934>`_ this parameter is
            referred to as :math:`s`).
        bootstrap_count:
            Minimum number of trials that need to complete a rung before any trial
            is considered for promotion into the next rung.
    '''
    def __init__(self, min_resource: str | int = 'auto', reduction_factor: int = 4, min_early_stopping_rate: int = 0, bootstrap_count: int = 0) -> None: ...
    def prune(self, study: optuna.study.Study, trial: optuna.trial.FrozenTrial) -> bool: ...
