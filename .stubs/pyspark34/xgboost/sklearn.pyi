import numpy as np
import os
from ._typing import ArrayLike as ArrayLike, FeatureNames as FeatureNames, FeatureTypes as FeatureTypes
from .callback import TrainingCallback as TrainingCallback
from .compat import SKLEARN_INSTALLED as SKLEARN_INSTALLED, XGBClassifierBase as XGBClassifierBase, XGBModelBase as XGBModelBase, XGBRegressorBase as XGBRegressorBase, XGBoostLabelEncoder as XGBoostLabelEncoder
from .config import config_context as config_context
from .core import Booster as Booster, DMatrix as DMatrix, Metric as Metric, QuantileDMatrix as QuantileDMatrix, XGBoostError as XGBoostError
from .training import train as train
from _typeshed import Incomplete
from typing import Any, Callable, Dict, List, Sequence, Tuple, Type, TypeVar

class XGBRankerMixIn:
    """MixIn for ranking, defines the _estimator_type usually defined in scikit-learn base
    classes."""

def xgboost_model_doc(header: str, items: List[str], extra_parameters: str | None = None, end_note: str | None = None) -> Callable[[Type], Type]:
    """Obtain documentation for Scikit-Learn wrappers

    Parameters
    ----------
    header: str
       An introducion to the class.
    items : list
       A list of common doc items.  Available items are:
         - estimators: the meaning of n_estimators
         - model: All the other parameters
         - objective: note for customized objective
    extra_parameters: str
       Document for class specific parameters, placed at the head.
    end_note: str
       Extra notes put to the end."""

class XGBModel(XGBModelBase):
    n_estimators: Incomplete
    objective: Incomplete
    max_depth: Incomplete
    max_leaves: Incomplete
    max_bin: Incomplete
    grow_policy: Incomplete
    learning_rate: Incomplete
    verbosity: Incomplete
    booster: Incomplete
    tree_method: Incomplete
    gamma: Incomplete
    min_child_weight: Incomplete
    max_delta_step: Incomplete
    subsample: Incomplete
    sampling_method: Incomplete
    colsample_bytree: Incomplete
    colsample_bylevel: Incomplete
    colsample_bynode: Incomplete
    reg_alpha: Incomplete
    reg_lambda: Incomplete
    scale_pos_weight: Incomplete
    base_score: Incomplete
    missing: Incomplete
    num_parallel_tree: Incomplete
    random_state: Incomplete
    n_jobs: Incomplete
    monotone_constraints: Incomplete
    interaction_constraints: Incomplete
    importance_type: Incomplete
    gpu_id: Incomplete
    validate_parameters: Incomplete
    predictor: Incomplete
    enable_categorical: Incomplete
    feature_types: Incomplete
    max_cat_to_onehot: Incomplete
    max_cat_threshold: Incomplete
    eval_metric: Incomplete
    early_stopping_rounds: Incomplete
    callbacks: Incomplete
    kwargs: Incomplete
    def __init__(self, max_depth: int | None = None, max_leaves: int | None = None, max_bin: int | None = None, grow_policy: str | None = None, learning_rate: float | None = None, n_estimators: int = 100, verbosity: int | None = None, objective: _SklObjective = None, booster: str | None = None, tree_method: str | None = None, n_jobs: int | None = None, gamma: float | None = None, min_child_weight: float | None = None, max_delta_step: float | None = None, subsample: float | None = None, sampling_method: str | None = None, colsample_bytree: float | None = None, colsample_bylevel: float | None = None, colsample_bynode: float | None = None, reg_alpha: float | None = None, reg_lambda: float | None = None, scale_pos_weight: float | None = None, base_score: float | None = None, random_state: np.random.RandomState | int | None = None, missing: float = ..., num_parallel_tree: int | None = None, monotone_constraints: Dict[str, int] | str | None = None, interaction_constraints: str | Sequence[Sequence[str]] | None = None, importance_type: str | None = None, gpu_id: int | None = None, validate_parameters: bool | None = None, predictor: str | None = None, enable_categorical: bool = False, feature_types: FeatureTypes = None, max_cat_to_onehot: int | None = None, max_cat_threshold: int | None = None, eval_metric: str | List[str] | Callable | None = None, early_stopping_rounds: int | None = None, callbacks: List[TrainingCallback] | None = None, **kwargs: Any) -> None: ...
    def __sklearn_is_fitted__(self) -> bool: ...
    def get_booster(self) -> Booster:
        """Get the underlying xgboost Booster of this model.

        This will raise an exception when fit was not called

        Returns
        -------
        booster : a xgboost booster of underlying model
        """
    def set_params(self, **params: Any) -> XGBModel:
        """Set the parameters of this estimator.  Modification of the sklearn method to
        allow unknown kwargs. This allows using the full range of xgboost
        parameters that are not defined as member variables in sklearn grid
        search.

        Returns
        -------
        self

        """
    def get_params(self, deep: bool = True) -> Dict[str, Any]:
        """Get parameters."""
    def get_xgb_params(self) -> Dict[str, Any]:
        """Get xgboost specific parameters."""
    def get_num_boosting_rounds(self) -> int:
        """Gets the number of xgboost boosting rounds."""
    def save_model(self, fname: str | os.PathLike) -> None: ...
    classes_: Incomplete
    def load_model(self, fname: str | bytearray | os.PathLike) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike, *, sample_weight: ArrayLike | None = None, base_margin: ArrayLike | None = None, eval_set: Sequence[Tuple[ArrayLike, ArrayLike]] | None = None, eval_metric: str | Sequence[str] | Metric | None = None, early_stopping_rounds: int | None = None, verbose: bool | int | None = True, xgb_model: Booster | str | XGBModel | None = None, sample_weight_eval_set: Sequence[ArrayLike] | None = None, base_margin_eval_set: Sequence[ArrayLike] | None = None, feature_weights: ArrayLike | None = None, callbacks: Sequence[TrainingCallback] | None = None) -> XGBModel:
        """Fit gradient boosting model.

        Note that calling ``fit()`` multiple times will cause the model object to be
        re-fit from scratch. To resume training from a previous checkpoint, explicitly
        pass ``xgb_model`` argument.

        Parameters
        ----------
        X :
            Feature matrix
        y :
            Labels
        sample_weight :
            instance weights
        base_margin :
            global bias for each instance.
        eval_set :
            A list of (X, y) tuple pairs to use as validation sets, for which
            metrics will be computed.
            Validation metrics will help us track the performance of the model.

        eval_metric : str, list of str, or callable, optional
            .. deprecated:: 1.6.0
                Use `eval_metric` in :py:meth:`__init__` or :py:meth:`set_params` instead.

        early_stopping_rounds : int
            .. deprecated:: 1.6.0
                Use `early_stopping_rounds` in :py:meth:`__init__` or
                :py:meth:`set_params` instead.
        verbose :
            If `verbose` is True and an evaluation set is used, the evaluation metric
            measured on the validation set is printed to stdout at each boosting stage.
            If `verbose` is an integer, the evaluation metric is printed at each `verbose`
            boosting stage. The last boosting stage / the boosting stage found by using
            `early_stopping_rounds` is also printed.
        xgb_model :
            file name of stored XGBoost model or 'Booster' instance XGBoost model to be
            loaded before training (allows training continuation).
        sample_weight_eval_set :
            A list of the form [L_1, L_2, ..., L_n], where each L_i is an array like
            object storing instance weights for the i-th validation set.
        base_margin_eval_set :
            A list of the form [M_1, M_2, ..., M_n], where each M_i is an array like
            object storing base margin for the i-th validation set.
        feature_weights :
            Weight for each feature, defines the probability of each feature being
            selected when colsample is being used.  All values must be greater than 0,
            otherwise a `ValueError` is thrown.

        callbacks :
            .. deprecated:: 1.6.0
                Use `callbacks` in :py:meth:`__init__` or :py:meth:`set_params` instead.
        """
    def predict(self, X: ArrayLike, output_margin: bool = False, ntree_limit: int | None = None, validate_features: bool = True, base_margin: ArrayLike | None = None, iteration_range: Tuple[int, int] | None = None) -> np.ndarray:
        """Predict with `X`.  If the model is trained with early stopping, then `best_iteration`
        is used automatically.  For tree models, when data is on GPU, like cupy array or
        cuDF dataframe and `predictor` is not specified, the prediction is run on GPU
        automatically, otherwise it will run on CPU.

        .. note:: This function is only thread safe for `gbtree` and `dart`.

        Parameters
        ----------
        X :
            Data to predict with.
        output_margin :
            Whether to output the raw untransformed margin value.
        ntree_limit :
            Deprecated, use `iteration_range` instead.
        validate_features :
            When this is True, validate that the Booster's and data's feature_names are
            identical.  Otherwise, it is assumed that the feature_names are the same.
        base_margin :
            Margin added to prediction.
        iteration_range :
            Specifies which layer of trees are used in prediction.  For example, if a
            random forest is trained with 100 rounds.  Specifying ``iteration_range=(10,
            20)``, then only the forests built during [10, 20) (half open set) rounds
            are used in this prediction.

            .. versionadded:: 1.4.0

        Returns
        -------
        prediction

        """
    def apply(self, X: ArrayLike, ntree_limit: int = 0, iteration_range: Tuple[int, int] | None = None) -> np.ndarray:
        """Return the predicted leaf every tree for each sample. If the model is trained with
        early stopping, then `best_iteration` is used automatically.

        Parameters
        ----------
        X : array_like, shape=[n_samples, n_features]
            Input features matrix.

        iteration_range :
            See :py:meth:`predict`.

        ntree_limit :
            Deprecated, use ``iteration_range`` instead.

        Returns
        -------
        X_leaves : array_like, shape=[n_samples, n_trees]
            For each datapoint x in X and for each tree, return the index of the
            leaf x ends up in. Leaves are numbered within
            ``[0; 2**(self.max_depth+1))``, possibly with gaps in the numbering.

        """
    def evals_result(self) -> Dict[str, Dict[str, List[float]]]:
        """Return the evaluation results.

        If **eval_set** is passed to the :py:meth:`fit` function, you can call
        ``evals_result()`` to get evaluation results for all passed **eval_sets**.  When
        **eval_metric** is also passed to the :py:meth:`fit` function, the
        **evals_result** will contain the **eval_metrics** passed to the :py:meth:`fit`
        function.

        The returned evaluation result is a dictionary:

        .. code-block:: python

            {'validation_0': {'logloss': ['0.604835', '0.531479']},
             'validation_1': {'logloss': ['0.41965', '0.17686']}}

        Returns
        -------
        evals_result

        """
    @property
    def n_features_in_(self) -> int:
        """Number of features seen during :py:meth:`fit`."""
    @property
    def feature_names_in_(self) -> np.ndarray:
        """Names of features seen during :py:meth:`fit`.  Defined only when `X` has feature
        names that are all strings."""
    @property
    def best_score(self) -> float:
        """The best score obtained by early stopping."""
    @property
    def best_iteration(self) -> int:
        """The best iteration obtained by early stopping.  This attribute is 0-based,
        for instance if the best iteration is the first round, then best_iteration is 0.

        """
    @property
    def best_ntree_limit(self) -> int: ...
    @property
    def feature_importances_(self) -> np.ndarray:
        '''Feature importances property, return depends on `importance_type`
        parameter. When model trained with multi-class/multi-label/multi-target dataset,
        the feature importance is "averaged" over all targets. The "average" is defined
        based on the importance type. For instance, if the importance type is
        "total_gain", then the score is sum of loss change for each split from all
        trees.

        Returns
        -------
        feature_importances_ : array of shape ``[n_features]`` except for multi-class
        linear model, which returns an array with shape `(n_features, n_classes)`

        '''
    @property
    def coef_(self) -> np.ndarray:
        """
        Coefficients property

        .. note:: Coefficients are defined only for linear learners

            Coefficients are only defined when the linear model is chosen as
            base learner (`booster=gblinear`). It is not defined for other base
            learner types, such as tree learners (`booster=gbtree`).

        Returns
        -------
        coef_ : array of shape ``[n_features]`` or ``[n_classes, n_features]``
        """
    @property
    def intercept_(self) -> np.ndarray:
        """
        Intercept (bias) property

        .. note:: Intercept is defined only for linear learners

            Intercept (bias) is only defined when the linear model is chosen as base
            learner (`booster=gblinear`). It is not defined for other base learner types,
            such as tree learners (`booster=gbtree`).

        Returns
        -------
        intercept_ : array of shape ``(1,)`` or ``[n_classes]``
        """
PredtT = TypeVar('PredtT', bound=np.ndarray)

class XGBClassifier(XGBModel, XGBClassifierBase):
    use_label_encoder: Incomplete
    def __init__(self, *, objective: _SklObjective = 'binary:logistic', use_label_encoder: bool | None = None, **kwargs: Any) -> None: ...
    classes_: Incomplete
    n_classes_: Incomplete
    objective: Incomplete
    def fit(self, X: ArrayLike, y: ArrayLike, *, sample_weight: ArrayLike | None = None, base_margin: ArrayLike | None = None, eval_set: Sequence[Tuple[ArrayLike, ArrayLike]] | None = None, eval_metric: str | Sequence[str] | Metric | None = None, early_stopping_rounds: int | None = None, verbose: bool | int | None = True, xgb_model: Booster | str | XGBModel | None = None, sample_weight_eval_set: Sequence[ArrayLike] | None = None, base_margin_eval_set: Sequence[ArrayLike] | None = None, feature_weights: ArrayLike | None = None, callbacks: Sequence[TrainingCallback] | None = None) -> XGBClassifier: ...
    def predict(self, X: ArrayLike, output_margin: bool = False, ntree_limit: int | None = None, validate_features: bool = True, base_margin: ArrayLike | None = None, iteration_range: Tuple[int, int] | None = None) -> np.ndarray: ...
    def predict_proba(self, X: ArrayLike, ntree_limit: int | None = None, validate_features: bool = True, base_margin: ArrayLike | None = None, iteration_range: Tuple[int, int] | None = None) -> np.ndarray:
        """Predict the probability of each `X` example being of a given class.

        .. note:: This function is only thread safe for `gbtree` and `dart`.

        Parameters
        ----------
        X : array_like
            Feature matrix.
        ntree_limit : int
            Deprecated, use `iteration_range` instead.
        validate_features : bool
            When this is True, validate that the Booster's and data's feature_names are
            identical.  Otherwise, it is assumed that the feature_names are the same.
        base_margin : array_like
            Margin added to prediction.
        iteration_range :
            Specifies which layer of trees are used in prediction.  For example, if a
            random forest is trained with 100 rounds.  Specifying `iteration_range=(10,
            20)`, then only the forests built during [10, 20) (half open set) rounds are
            used in this prediction.

        Returns
        -------
        prediction :
            a numpy array of shape array-like of shape (n_samples, n_classes) with the
            probability of each data example being of a given class.
        """

class XGBRFClassifier(XGBClassifier):
    def __init__(self, *, learning_rate: float = 1.0, subsample: float = 0.8, colsample_bynode: float = 0.8, reg_lambda: float = 1e-05, **kwargs: Any) -> None: ...
    def get_xgb_params(self) -> Dict[str, Any]: ...
    def get_num_boosting_rounds(self) -> int: ...
    def fit(self, X: ArrayLike, y: ArrayLike, *, sample_weight: ArrayLike | None = None, base_margin: ArrayLike | None = None, eval_set: Sequence[Tuple[ArrayLike, ArrayLike]] | None = None, eval_metric: str | Sequence[str] | Metric | None = None, early_stopping_rounds: int | None = None, verbose: bool | int | None = True, xgb_model: Booster | str | XGBModel | None = None, sample_weight_eval_set: Sequence[ArrayLike] | None = None, base_margin_eval_set: Sequence[ArrayLike] | None = None, feature_weights: ArrayLike | None = None, callbacks: Sequence[TrainingCallback] | None = None) -> XGBRFClassifier: ...

class XGBRegressor(XGBModel, XGBRegressorBase):
    def __init__(self, *, objective: _SklObjective = 'reg:squarederror', **kwargs: Any) -> None: ...

class XGBRFRegressor(XGBRegressor):
    def __init__(self, *, learning_rate: float = 1.0, subsample: float = 0.8, colsample_bynode: float = 0.8, reg_lambda: float = 1e-05, **kwargs: Any) -> None: ...
    def get_xgb_params(self) -> Dict[str, Any]: ...
    def get_num_boosting_rounds(self) -> int: ...
    def fit(self, X: ArrayLike, y: ArrayLike, *, sample_weight: ArrayLike | None = None, base_margin: ArrayLike | None = None, eval_set: Sequence[Tuple[ArrayLike, ArrayLike]] | None = None, eval_metric: str | Sequence[str] | Metric | None = None, early_stopping_rounds: int | None = None, verbose: bool | int | None = True, xgb_model: Booster | str | XGBModel | None = None, sample_weight_eval_set: Sequence[ArrayLike] | None = None, base_margin_eval_set: Sequence[ArrayLike] | None = None, feature_weights: ArrayLike | None = None, callbacks: Sequence[TrainingCallback] | None = None) -> XGBRFRegressor: ...

class XGBRanker(XGBModel, XGBRankerMixIn):
    def __init__(self, *, objective: str = 'rank:pairwise', **kwargs: Any) -> None: ...
    objective: Incomplete
    def fit(self, X: ArrayLike, y: ArrayLike, *, group: ArrayLike | None = None, qid: ArrayLike | None = None, sample_weight: ArrayLike | None = None, base_margin: ArrayLike | None = None, eval_set: Sequence[Tuple[ArrayLike, ArrayLike]] | None = None, eval_group: Sequence[ArrayLike] | None = None, eval_qid: Sequence[ArrayLike] | None = None, eval_metric: str | Sequence[str] | Metric | None = None, early_stopping_rounds: int | None = None, verbose: bool | int | None = False, xgb_model: Booster | str | XGBModel | None = None, sample_weight_eval_set: Sequence[ArrayLike] | None = None, base_margin_eval_set: Sequence[ArrayLike] | None = None, feature_weights: ArrayLike | None = None, callbacks: Sequence[TrainingCallback] | None = None) -> XGBRanker:
        """Fit gradient boosting ranker

        Note that calling ``fit()`` multiple times will cause the model object to be
        re-fit from scratch. To resume training from a previous checkpoint, explicitly
        pass ``xgb_model`` argument.

        Parameters
        ----------
        X :
            Feature matrix
        y :
            Labels
        group :
            Size of each query group of training data. Should have as many elements as the
            query groups in the training data.  If this is set to None, then user must
            provide qid.
        qid :
            Query ID for each training sample.  Should have the size of n_samples.  If
            this is set to None, then user must provide group.
        sample_weight :
            Query group weights

            .. note:: Weights are per-group for ranking tasks

                In ranking task, one weight is assigned to each query group/id (not each
                data point). This is because we only care about the relative ordering of
                data points within each group, so it doesn't make sense to assign weights
                to individual data points.
        base_margin :
            Global bias for each instance.
        eval_set :
            A list of (X, y) tuple pairs to use as validation sets, for which
            metrics will be computed.
            Validation metrics will help us track the performance of the model.
        eval_group :
            A list in which ``eval_group[i]`` is the list containing the sizes of all
            query groups in the ``i``-th pair in **eval_set**.
        eval_qid :
            A list in which ``eval_qid[i]`` is the array containing query ID of ``i``-th
            pair in **eval_set**.

        eval_metric : str, list of str, optional
            .. deprecated:: 1.6.0
                use `eval_metric` in :py:meth:`__init__` or :py:meth:`set_params` instead.

        early_stopping_rounds : int
            .. deprecated:: 1.6.0
                use `early_stopping_rounds` in :py:meth:`__init__` or
                :py:meth:`set_params` instead.

        verbose :
            If `verbose` is True and an evaluation set is used, the evaluation metric
            measured on the validation set is printed to stdout at each boosting stage.
            If `verbose` is an integer, the evaluation metric is printed at each `verbose`
            boosting stage. The last boosting stage / the boosting stage found by using
            `early_stopping_rounds` is also printed.
        xgb_model :
            file name of stored XGBoost model or 'Booster' instance XGBoost model to be
            loaded before training (allows training continuation).
        sample_weight_eval_set :
            A list of the form [L_1, L_2, ..., L_n], where each L_i is a list of
            group weights on the i-th validation set.

            .. note:: Weights are per-group for ranking tasks

                In ranking task, one weight is assigned to each query group (not each
                data point). This is because we only care about the relative ordering of
                data points within each group, so it doesn't make sense to assign
                weights to individual data points.
        base_margin_eval_set :
            A list of the form [M_1, M_2, ..., M_n], where each M_i is an array like
            object storing base margin for the i-th validation set.
        feature_weights :
            Weight for each feature, defines the probability of each feature being
            selected when colsample is being used.  All values must be greater than 0,
            otherwise a `ValueError` is thrown.

        callbacks :
            .. deprecated:: 1.6.0
                Use `callbacks` in :py:meth:`__init__` or :py:meth:`set_params` instead.
        """
