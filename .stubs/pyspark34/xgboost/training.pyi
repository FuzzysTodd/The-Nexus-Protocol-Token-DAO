import numpy as np
import os
from ._typing import BoosterParam as BoosterParam, Callable as Callable, FPreProcCallable as FPreProcCallable
from .callback import CallbackContainer as CallbackContainer, EarlyStopping as EarlyStopping, EvaluationMonitor as EvaluationMonitor, TrainingCallback as TrainingCallback
from .compat import DataFrame as DataFrame, SKLEARN_INSTALLED as SKLEARN_INSTALLED, XGBStratifiedKFold as XGBStratifiedKFold
from .core import Booster as Booster, DMatrix as DMatrix, Metric as Metric, Objective as Objective, XGBoostError as XGBoostError
from _typeshed import Incomplete
from typing import Any, Dict, Iterable, List, Sequence, Tuple

def train(params: Dict[str, Any], dtrain: DMatrix, num_boost_round: int = 10, *, evals: Sequence[Tuple[DMatrix, str]] | None = None, obj: Objective | None = None, feval: Metric | None = None, maximize: bool | None = None, early_stopping_rounds: int | None = None, evals_result: TrainingCallback.EvalsLog = None, verbose_eval: bool | int | None = True, xgb_model: str | os.PathLike | Booster | bytearray | None = None, callbacks: Sequence[TrainingCallback] | None = None, custom_metric: Metric | None = None) -> Booster:
    """Train a booster with given parameters.

    Parameters
    ----------
    params :
        Booster params.
    dtrain :
        Data to be trained.
    num_boost_round :
        Number of boosting iterations.
    evals :
        List of validation sets for which metrics will evaluated during training.
        Validation metrics will help us track the performance of the model.
    obj
        Custom objective function.  See :doc:`Custom Objective
        </tutorials/custom_metric_obj>` for details.
    feval :
        .. deprecated:: 1.6.0
            Use `custom_metric` instead.
    maximize : bool
        Whether to maximize feval.
    early_stopping_rounds :
        Activates early stopping. Validation metric needs to improve at least once in
        every **early_stopping_rounds** round(s) to continue training.
        Requires at least one item in **evals**.
        The method returns the model from the last iteration (not the best one).  Use
        custom callback or model slicing if the best model is desired.
        If there's more than one item in **evals**, the last entry will be used for early
        stopping.
        If there's more than one metric in the **eval_metric** parameter given in
        **params**, the last metric will be used for early stopping.
        If early stopping occurs, the model will have two additional fields:
        ``bst.best_score``, ``bst.best_iteration``.
    evals_result :
        This dictionary stores the evaluation results of all the items in watchlist.

        Example: with a watchlist containing
        ``[(dtest,'eval'), (dtrain,'train')]`` and
        a parameter containing ``('eval_metric': 'logloss')``,
        the **evals_result** returns

        .. code-block:: python

            {'train': {'logloss': ['0.48253', '0.35953']},
             'eval': {'logloss': ['0.480385', '0.357756']}}

    verbose_eval :
        Requires at least one item in **evals**.
        If **verbose_eval** is True then the evaluation metric on the validation set is
        printed at each boosting stage.
        If **verbose_eval** is an integer then the evaluation metric on the validation set
        is printed at every given **verbose_eval** boosting stage. The last boosting stage
        / the boosting stage found by using **early_stopping_rounds** is also printed.
        Example: with ``verbose_eval=4`` and at least one item in **evals**, an evaluation metric
        is printed every 4 boosting stages, instead of every boosting stage.
    xgb_model :
        Xgb model to be loaded before training (allows training continuation).
    callbacks :
        List of callback functions that are applied at end of each iteration.
        It is possible to use predefined callbacks by using
        :ref:`Callback API <callback_api>`.

        .. note::

           States in callback are not preserved during training, which means callback
           objects can not be reused for multiple training sessions without
           reinitialization or deepcopy.

        .. code-block:: python

            for params in parameters_grid:
                # be sure to (re)initialize the callbacks before each run
                callbacks = [xgb.callback.LearningRateScheduler(custom_rates)]
                xgboost.train(params, Xy, callbacks=callbacks)

    custom_metric:

        .. versionadded 1.6.0

        Custom metric function.  See :doc:`Custom Metric </tutorials/custom_metric_obj>`
        for details.

    Returns
    -------
    Booster : a trained booster model
    """

class CVPack:
    '''"Auxiliary datastruct to hold one fold of CV.'''
    dtrain: Incomplete
    dtest: Incomplete
    watchlist: Incomplete
    bst: Incomplete
    def __init__(self, dtrain: DMatrix, dtest: DMatrix, param: Dict | List | None) -> None:
        '''"Initialize the CVPack'''
    def __getattr__(self, name: str) -> Callable: ...
    def update(self, iteration: int, fobj: Objective | None) -> None:
        '''"Update the boosters for one iteration'''
    def eval(self, iteration: int, feval: Metric | None, output_margin: bool) -> str:
        '''"Evaluate the CVPack for one iteration.'''

class _PackedBooster:
    cvfolds: Incomplete
    def __init__(self, cvfolds: _CVFolds) -> None: ...
    def update(self, iteration: int, obj: Objective | None) -> None:
        """Iterate through folds for update"""
    def eval(self, iteration: int, feval: Metric | None, output_margin: bool) -> List[str]:
        """Iterate through folds for eval"""
    def set_attr(self, **kwargs: str | None) -> Any:
        """Iterate through folds for setting attributes"""
    def attr(self, key: str) -> str | None:
        """Redirect to booster attr."""
    def set_param(self, params: Dict | Iterable[Tuple[str, Any]] | str, value: str | None = None) -> None:
        """Iterate through folds for set_param"""
    def num_boosted_rounds(self) -> int:
        """Number of boosted rounds."""
    @property
    def best_iteration(self) -> int:
        """Get best_iteration"""
    @property
    def best_score(self) -> float:
        """Get best_score."""

def groups_to_rows(groups: List[np.ndarray], boundaries: np.ndarray) -> np.ndarray:
    """
    Given group row boundaries, convert ground indexes to row indexes
    :param groups: list of groups for testing
    :param boundaries: rows index limits of each group
    :return: row in group
    """
def mkgroupfold(dall: DMatrix, nfold: int, param: BoosterParam, evals: Sequence[str] = (), fpreproc: FPreProcCallable = None, shuffle: bool = True) -> List[CVPack]:
    """
    Make n folds for cross-validation maintaining groups
    :return: cross-validation folds
    """
def mknfold(dall: DMatrix, nfold: int, param: BoosterParam, seed: int, evals: Sequence[str] = (), fpreproc: FPreProcCallable = None, stratified: bool = False, folds: XGBStratifiedKFold = None, shuffle: bool = True) -> List[CVPack]:
    """
    Make an n-fold list of CVPack from random indices.
    """
def cv(params: BoosterParam, dtrain: DMatrix, num_boost_round: int = 10, nfold: int = 3, stratified: bool = False, folds: XGBStratifiedKFold = None, metrics: Sequence[str] = (), obj: Objective | None = None, feval: Metric | None = None, maximize: bool = None, early_stopping_rounds: int = None, fpreproc: FPreProcCallable = None, as_pandas: bool = True, verbose_eval: int | bool | None = None, show_stdv: bool = True, seed: int = 0, callbacks: Sequence[TrainingCallback] = None, shuffle: bool = True, custom_metric: Metric | None = None) -> Dict[str, float] | DataFrame:
    """Cross-validation with given parameters.

    Parameters
    ----------
    params : dict
        Booster params.
    dtrain : DMatrix
        Data to be trained.
    num_boost_round : int
        Number of boosting iterations.
    nfold : int
        Number of folds in CV.
    stratified : bool
        Perform stratified sampling.
    folds : a KFold or StratifiedKFold instance or list of fold indices
        Sklearn KFolds or StratifiedKFolds object.
        Alternatively may explicitly pass sample indices for each fold.
        For ``n`` folds, **folds** should be a length ``n`` list of tuples.
        Each tuple is ``(in,out)`` where ``in`` is a list of indices to be used
        as the training samples for the ``n`` th fold and ``out`` is a list of
        indices to be used as the testing samples for the ``n`` th fold.
    metrics : string or list of strings
        Evaluation metrics to be watched in CV.
    obj :

        Custom objective function.  See :doc:`Custom Objective
        </tutorials/custom_metric_obj>` for details.

    feval : function
        .. deprecated:: 1.6.0
            Use `custom_metric` instead.
    maximize : bool
        Whether to maximize feval.
    early_stopping_rounds: int
        Activates early stopping. Cross-Validation metric (average of validation
        metric computed over CV folds) needs to improve at least once in
        every **early_stopping_rounds** round(s) to continue training.
        The last entry in the evaluation history will represent the best iteration.
        If there's more than one metric in the **eval_metric** parameter given in
        **params**, the last metric will be used for early stopping.
    fpreproc : function
        Preprocessing function that takes (dtrain, dtest, param) and returns
        transformed versions of those.
    as_pandas : bool, default True
        Return pd.DataFrame when pandas is installed.
        If False or pandas is not installed, return np.ndarray
    verbose_eval : bool, int, or None, default None
        Whether to display the progress. If None, progress will be displayed
        when np.ndarray is returned. If True, progress will be displayed at
        boosting stage. If an integer is given, progress will be displayed
        at every given `verbose_eval` boosting stage.
    show_stdv : bool, default True
        Whether to display the standard deviation in progress.
        Results are not affected, and always contains std.
    seed : int
        Seed used to generate the folds (passed to numpy.random.seed).
    callbacks :
        List of callback functions that are applied at end of each iteration.
        It is possible to use predefined callbacks by using
        :ref:`Callback API <callback_api>`.

        .. note::

           States in callback are not preserved during training, which means callback
           objects can not be reused for multiple training sessions without
           reinitialization or deepcopy.

        .. code-block:: python

            for params in parameters_grid:
                # be sure to (re)initialize the callbacks before each run
                callbacks = [xgb.callback.LearningRateScheduler(custom_rates)]
                xgboost.train(params, Xy, callbacks=callbacks)

    shuffle : bool
        Shuffle data before creating folds.
    custom_metric :

        .. versionadded 1.6.0

        Custom metric function.  See :doc:`Custom Metric </tutorials/custom_metric_obj>`
        for details.

    Returns
    -------
    evaluation history : list(string)
    """
