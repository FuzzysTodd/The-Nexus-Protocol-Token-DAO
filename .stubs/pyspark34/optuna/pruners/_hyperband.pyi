import optuna
from optuna import logging as logging
from optuna.pruners._base import BasePruner as BasePruner
from optuna.pruners._successive_halving import SuccessiveHalvingPruner as SuccessiveHalvingPruner
from optuna.trial._state import TrialState as TrialState

class HyperbandPruner(BasePruner):
    '''Pruner using Hyperband.

    As SuccessiveHalving (SHA) requires the number of configurations
    :math:`n` as its hyperparameter.  For a given finite budget :math:`B`,
    all the configurations have the resources of :math:`B \\over n` on average.
    As you can see, there will be a trade-off of :math:`B` and :math:`B \\over n`.
    `Hyperband <http://www.jmlr.org/papers/volume18/16-558/16-558.pdf>`_ attacks this trade-off
    by trying different :math:`n` values for a fixed budget.

    .. note::
        * In the Hyperband paper, the counterpart of :class:`~optuna.samplers.RandomSampler`
          is used.
        * Optuna uses :class:`~optuna.samplers.TPESampler` by default.
        * `The benchmark result
          <https://github.com/optuna/optuna/pull/828#issuecomment-575457360>`_
          shows that :class:`optuna.pruners.HyperbandPruner` supports both samplers.

    .. note::
        If you use ``HyperbandPruner`` with :class:`~optuna.samplers.TPESampler`,
        it\'s recommended to consider to set larger ``n_trials`` or ``timeout`` to make full use of
        the characteristics of :class:`~optuna.samplers.TPESampler`
        because :class:`~optuna.samplers.TPESampler` uses some (by default, :math:`10`)
        :class:`~optuna.trial.Trial`\\ s for its startup.

        As Hyperband runs multiple :class:`~optuna.pruners.SuccessiveHalvingPruner` and collect
        trials based on the current :class:`~optuna.trial.Trial`\\ \'s bracket ID, each bracket
        needs to observe more than :math:`10` :class:`~optuna.trial.Trial`\\ s
        for :class:`~optuna.samplers.TPESampler` to adapt its search space.

        Thus, for example, if ``HyperbandPruner`` has :math:`4` pruners in it,
        at least :math:`4 \\times 10` trials are consumed for startup.

    .. note::
        Hyperband has several :class:`~optuna.pruners.SuccessiveHalvingPruner`. Each
        :class:`~optuna.pruners.SuccessiveHalvingPruner` is referred as "bracket" in the original
        paper. The number of brackets is an important factor to control the early stopping behavior
        of Hyperband and is automatically determined by ``min_resource``, ``max_resource`` and
        ``reduction_factor`` as
        `The number of brackets = floor(log_{reduction_factor}(max_resource / min_resource)) + 1`.
        Please set ``reduction_factor`` so that the number of brackets is not too large (about 4 ~
        6 in most use cases). Please see Section 3.6 of the `original paper
        <http://www.jmlr.org/papers/volume18/16-558/16-558.pdf>`_ for the detail.

    .. seealso::
        Please refer to :meth:`~optuna.trial.Trial.report`.

    Example:

        We minimize an objective function with Hyperband pruning algorithm.

        .. testcode::

            import numpy as np
            from sklearn.datasets import load_iris
            from sklearn.linear_model import SGDClassifier
            from sklearn.model_selection import train_test_split

            import optuna

            X, y = load_iris(return_X_y=True)
            X_train, X_valid, y_train, y_valid = train_test_split(X, y)
            classes = np.unique(y)
            n_train_iter = 100


            def objective(trial):
                alpha = trial.suggest_float("alpha", 0.0, 1.0)
                clf = SGDClassifier(alpha=alpha)

                for step in range(n_train_iter):
                    clf.partial_fit(X_train, y_train, classes=classes)

                    intermediate_value = clf.score(X_valid, y_valid)
                    trial.report(intermediate_value, step)

                    if trial.should_prune():
                        raise optuna.TrialPruned()

                return clf.score(X_valid, y_valid)


            study = optuna.create_study(
                direction="maximize",
                pruner=optuna.pruners.HyperbandPruner(
                    min_resource=1, max_resource=n_train_iter, reduction_factor=3
                ),
            )
            study.optimize(objective, n_trials=20)

    Args:
        min_resource:
            A parameter for specifying the minimum resource allocated to a trial noted as :math:`r`
            in the paper. A smaller :math:`r` will give a result faster, but a larger
            :math:`r` will give a better guarantee of successful judging between configurations.
            See the details for :class:`~optuna.pruners.SuccessiveHalvingPruner`.
        max_resource:
            A parameter for specifying the maximum resource allocated to a trial. :math:`R` in the
            paper corresponds to ``max_resource / min_resource``. This value represents and should
            match the maximum iteration steps (e.g., the number of epochs for neural networks).
            When this argument is "auto", the maximum resource is estimated according to the
            completed trials. The default value of this argument is "auto".

            .. note::
                With "auto", the maximum resource will be the largest step reported by
                :meth:`~optuna.trial.Trial.report` in the first, or one of the first if trained in
                parallel, completed trial. No trials will be pruned until the maximum resource is
                determined.

            .. note::
                If the step of the last intermediate value may change with each trial, please
                manually specify the maximum possible step to ``max_resource``.
        reduction_factor:
            A parameter for specifying reduction factor of promotable trials noted as
            :math:`\\eta` in the paper.
            See the details for :class:`~optuna.pruners.SuccessiveHalvingPruner`.
        bootstrap_count:
            Parameter specifying the number of trials required in a rung before any trial can be
            promoted. Incompatible with ``max_resouce`` is ``"auto"``.
            See the details for :class:`~optuna.pruners.SuccessiveHalvingPruner`.
    '''
    def __init__(self, min_resource: int = 1, max_resource: str | int = 'auto', reduction_factor: int = 3, bootstrap_count: int = 0) -> None: ...
    def prune(self, study: optuna.study.Study, trial: optuna.trial.FrozenTrial) -> bool: ...
