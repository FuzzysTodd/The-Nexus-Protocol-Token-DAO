import numpy as np
from .basic import Booster, Dataset, _LGBM_BoosterBestScoreType, _LGBM_CategoricalFeatureConfiguration, _LGBM_EvalFunctionResultType, _LGBM_FeatureNameConfiguration, _LGBM_GroupType, _LGBM_InitScoreType, _LGBM_LabelType, _LGBM_WeightType
from .callback import _EvalResultDict
from .compat import _LGBMClassifierBase, _LGBMModelBase, _LGBMRegressorBase
from _typeshed import Incomplete
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple

__all__ = ['LGBMClassifier', 'LGBMModel', 'LGBMRanker', 'LGBMRegressor']

class _ObjectiveFunctionWrapper:
    """Proxy class for objective function."""
    func: Incomplete
    def __init__(self, func: _LGBM_ScikitCustomObjectiveFunction) -> None:
        """Construct a proxy class.

        This class transforms objective function to match objective function with signature ``new_func(preds, dataset)``
        as expected by ``lightgbm.engine.train``.

        Parameters
        ----------
        func : callable
            Expects a callable with following signatures:
            ``func(y_true, y_pred)``,
            ``func(y_true, y_pred, weight)``
            or ``func(y_true, y_pred, weight, group)``
            and returns (grad, hess):

                y_true : numpy 1-D array of shape = [n_samples]
                    The target values.
                y_pred : numpy 1-D array of shape = [n_samples] or numpy 2-D array of shape = [n_samples, n_classes] (for multi-class task)
                    The predicted values.
                    Predicted values are returned before any transformation,
                    e.g. they are raw margin instead of probability of positive class for binary task.
                weight : numpy 1-D array of shape = [n_samples]
                    The weight of samples. Weights should be non-negative.
                group : numpy 1-D array
                    Group/query data.
                    Only used in the learning-to-rank task.
                    sum(group) = n_samples.
                    For example, if you have a 100-document dataset with ``group = [10, 20, 40, 10, 10, 10]``, that means that you have 6 groups,
                    where the first 10 records are in the first group, records 11-30 are in the second group, records 31-70 are in the third group, etc.
                grad : numpy 1-D array of shape = [n_samples] or numpy 2-D array of shape [n_samples, n_classes] (for multi-class task)
                    The value of the first order derivative (gradient) of the loss
                    with respect to the elements of y_pred for each sample point.
                hess : numpy 1-D array of shape = [n_samples] or numpy 2-D array of shape = [n_samples, n_classes] (for multi-class task)
                    The value of the second order derivative (Hessian) of the loss
                    with respect to the elements of y_pred for each sample point.

        .. note::

            For multi-class task, y_pred is a numpy 2-D array of shape = [n_samples, n_classes],
            and grad and hess should be returned in the same format.
        """
    def __call__(self, preds: np.ndarray, dataset: Dataset) -> Tuple[np.ndarray, np.ndarray]:
        """Call passed function with appropriate arguments.

        Parameters
        ----------
        preds : numpy 1-D array of shape = [n_samples] or numpy 2-D array of shape = [n_samples, n_classes] (for multi-class task)
            The predicted values.
        dataset : Dataset
            The training dataset.

        Returns
        -------
        grad : numpy 1-D array of shape = [n_samples] or numpy 2-D array of shape = [n_samples, n_classes] (for multi-class task)
            The value of the first order derivative (gradient) of the loss
            with respect to the elements of preds for each sample point.
        hess : numpy 1-D array of shape = [n_samples] or numpy 2-D array of shape = [n_samples, n_classes] (for multi-class task)
            The value of the second order derivative (Hessian) of the loss
            with respect to the elements of preds for each sample point.
        """

class _EvalFunctionWrapper:
    """Proxy class for evaluation function."""
    func: Incomplete
    def __init__(self, func: _LGBM_ScikitCustomEvalFunction) -> None:
        """Construct a proxy class.

        This class transforms evaluation function to match evaluation function with signature ``new_func(preds, dataset)``
        as expected by ``lightgbm.engine.train``.

        Parameters
        ----------
        func : callable
            Expects a callable with following signatures:
            ``func(y_true, y_pred)``,
            ``func(y_true, y_pred, weight)``
            or ``func(y_true, y_pred, weight, group)``
            and returns (eval_name, eval_result, is_higher_better) or
            list of (eval_name, eval_result, is_higher_better):

                y_true : numpy 1-D array of shape = [n_samples]
                    The target values.
                y_pred : numpy 1-D array of shape = [n_samples] or numpy 2-D array shape = [n_samples, n_classes] (for multi-class task)
                    The predicted values.
                    In case of custom ``objective``, predicted values are returned before any transformation,
                    e.g. they are raw margin instead of probability of positive class for binary task in this case.
                weight : numpy 1-D array of shape = [n_samples]
                    The weight of samples. Weights should be non-negative.
                group : numpy 1-D array
                    Group/query data.
                    Only used in the learning-to-rank task.
                    sum(group) = n_samples.
                    For example, if you have a 100-document dataset with ``group = [10, 20, 40, 10, 10, 10]``, that means that you have 6 groups,
                    where the first 10 records are in the first group, records 11-30 are in the second group, records 31-70 are in the third group, etc.
                eval_name : str
                    The name of evaluation function (without whitespace).
                eval_result : float
                    The eval result.
                is_higher_better : bool
                    Is eval result higher better, e.g. AUC is ``is_higher_better``.
        """
    def __call__(self, preds: np.ndarray, dataset: Dataset) -> _LGBM_EvalFunctionResultType | List[_LGBM_EvalFunctionResultType]:
        """Call passed function with appropriate arguments.

        Parameters
        ----------
        preds : numpy 1-D array of shape = [n_samples] or numpy 2-D array of shape = [n_samples, n_classes] (for multi-class task)
            The predicted values.
        dataset : Dataset
            The training dataset.

        Returns
        -------
        eval_name : str
            The name of evaluation function (without whitespace).
        eval_result : float
            The eval result.
        is_higher_better : bool
            Is eval result higher better, e.g. AUC is ``is_higher_better``.
        """

class LGBMModel(_LGBMModelBase):
    """Implementation of the scikit-learn API for LightGBM."""
    boosting_type: Incomplete
    objective: Incomplete
    num_leaves: Incomplete
    max_depth: Incomplete
    learning_rate: Incomplete
    n_estimators: Incomplete
    subsample_for_bin: Incomplete
    min_split_gain: Incomplete
    min_child_weight: Incomplete
    min_child_samples: Incomplete
    subsample: Incomplete
    subsample_freq: Incomplete
    colsample_bytree: Incomplete
    reg_alpha: Incomplete
    reg_lambda: Incomplete
    random_state: Incomplete
    n_jobs: Incomplete
    importance_type: Incomplete
    class_weight: Incomplete
    def __init__(self, boosting_type: str = 'gbdt', num_leaves: int = 31, max_depth: int = -1, learning_rate: float = 0.1, n_estimators: int = 100, subsample_for_bin: int = 200000, objective: str | _LGBM_ScikitCustomObjectiveFunction | None = None, class_weight: Dict | str | None = None, min_split_gain: float = 0.0, min_child_weight: float = 0.001, min_child_samples: int = 20, subsample: float = 1.0, subsample_freq: int = 0, colsample_bytree: float = 1.0, reg_alpha: float = 0.0, reg_lambda: float = 0.0, random_state: int | np.random.RandomState | None = None, n_jobs: int | None = None, importance_type: str = 'split', **kwargs) -> None:
        """Construct a gradient boosting model.

        Parameters
        ----------
        boosting_type : str, optional (default='gbdt')
            'gbdt', traditional Gradient Boosting Decision Tree.
            'dart', Dropouts meet Multiple Additive Regression Trees.
            'rf', Random Forest.
        num_leaves : int, optional (default=31)
            Maximum tree leaves for base learners.
        max_depth : int, optional (default=-1)
            Maximum tree depth for base learners, <=0 means no limit.
        learning_rate : float, optional (default=0.1)
            Boosting learning rate.
            You can use ``callbacks`` parameter of ``fit`` method to shrink/adapt learning rate
            in training using ``reset_parameter`` callback.
            Note, that this will ignore the ``learning_rate`` argument in training.
        n_estimators : int, optional (default=100)
            Number of boosted trees to fit.
        subsample_for_bin : int, optional (default=200000)
            Number of samples for constructing bins.
        objective : str, callable or None, optional (default=None)
            Specify the learning task and the corresponding learning objective or
            a custom objective function to be used (see note below).
            Default: 'regression' for LGBMRegressor, 'binary' or 'multiclass' for LGBMClassifier, 'lambdarank' for LGBMRanker.
        class_weight : dict, 'balanced' or None, optional (default=None)
            Weights associated with classes in the form ``{class_label: weight}``.
            Use this parameter only for multi-class classification task;
            for binary classification task you may use ``is_unbalance`` or ``scale_pos_weight`` parameters.
            Note, that the usage of all these parameters will result in poor estimates of the individual class probabilities.
            You may want to consider performing probability calibration
            (https://scikit-learn.org/stable/modules/calibration.html) of your model.
            The 'balanced' mode uses the values of y to automatically adjust weights
            inversely proportional to class frequencies in the input data as ``n_samples / (n_classes * np.bincount(y))``.
            If None, all classes are supposed to have weight one.
            Note, that these weights will be multiplied with ``sample_weight`` (passed through the ``fit`` method)
            if ``sample_weight`` is specified.
        min_split_gain : float, optional (default=0.)
            Minimum loss reduction required to make a further partition on a leaf node of the tree.
        min_child_weight : float, optional (default=1e-3)
            Minimum sum of instance weight (Hessian) needed in a child (leaf).
        min_child_samples : int, optional (default=20)
            Minimum number of data needed in a child (leaf).
        subsample : float, optional (default=1.)
            Subsample ratio of the training instance.
        subsample_freq : int, optional (default=0)
            Frequency of subsample, <=0 means no enable.
        colsample_bytree : float, optional (default=1.)
            Subsample ratio of columns when constructing each tree.
        reg_alpha : float, optional (default=0.)
            L1 regularization term on weights.
        reg_lambda : float, optional (default=0.)
            L2 regularization term on weights.
        random_state : int, RandomState object or None, optional (default=None)
            Random number seed.
            If int, this number is used to seed the C++ code.
            If RandomState object (numpy), a random integer is picked based on its state to seed the C++ code.
            If None, default seeds in C++ code are used.
        n_jobs : int or None, optional (default=None)
            Number of parallel threads to use for training (can be changed at prediction time by
            passing it as an extra keyword argument).

            For better performance, it is recommended to set this to the number of physical cores
            in the CPU.

            Negative integers are interpreted as following joblib's formula (n_cpus + 1 + n_jobs), just like
            scikit-learn (so e.g. -1 means using all threads). A value of zero corresponds the default number of
            threads configured for OpenMP in the system. A value of ``None`` (the default) corresponds
            to using the number of physical cores in the system (its correct detection requires
            either the ``joblib`` or the ``psutil`` util libraries to be installed).

            .. versionchanged:: 4.0.0

        importance_type : str, optional (default='split')
            The type of feature importance to be filled into ``feature_importances_``.
            If 'split', result contains numbers of times the feature is used in a model.
            If 'gain', result contains total gains of splits which use the feature.
        **kwargs
            Other parameters for the model.
            Check http://lightgbm.readthedocs.io/en/latest/Parameters.html for more parameters.

            .. warning::

                \\*\\*kwargs is not supported in sklearn, it may cause unexpected issues.

        Note
        ----
        A custom objective function can be provided for the ``objective`` parameter.
        In this case, it should have the signature
        ``objective(y_true, y_pred) -> grad, hess``,
        ``objective(y_true, y_pred, weight) -> grad, hess``
        or ``objective(y_true, y_pred, weight, group) -> grad, hess``:

            y_true : numpy 1-D array of shape = [n_samples]
                The target values.
            y_pred : numpy 1-D array of shape = [n_samples] or numpy 2-D array of shape = [n_samples, n_classes] (for multi-class task)
                The predicted values.
                Predicted values are returned before any transformation,
                e.g. they are raw margin instead of probability of positive class for binary task.
            weight : numpy 1-D array of shape = [n_samples]
                The weight of samples. Weights should be non-negative.
            group : numpy 1-D array
                Group/query data.
                Only used in the learning-to-rank task.
                sum(group) = n_samples.
                For example, if you have a 100-document dataset with ``group = [10, 20, 40, 10, 10, 10]``, that means that you have 6 groups,
                where the first 10 records are in the first group, records 11-30 are in the second group, records 31-70 are in the third group, etc.
            grad : numpy 1-D array of shape = [n_samples] or numpy 2-D array of shape = [n_samples, n_classes] (for multi-class task)
                The value of the first order derivative (gradient) of the loss
                with respect to the elements of y_pred for each sample point.
            hess : numpy 1-D array of shape = [n_samples] or numpy 2-D array of shape = [n_samples, n_classes] (for multi-class task)
                The value of the second order derivative (Hessian) of the loss
                with respect to the elements of y_pred for each sample point.

        For multi-class task, y_pred is a numpy 2-D array of shape = [n_samples, n_classes],
        and grad and hess should be returned in the same format.
        """
    def __sklearn_is_fitted__(self) -> bool: ...
    def get_params(self, deep: bool = True) -> Dict[str, Any]:
        """Get parameters for this estimator.

        Parameters
        ----------
        deep : bool, optional (default=True)
            If True, will return the parameters for this estimator and
            contained subobjects that are estimators.

        Returns
        -------
        params : dict
            Parameter names mapped to their values.
        """
    def set_params(self, **params: Any) -> LGBMModel:
        """Set the parameters of this estimator.

        Parameters
        ----------
        **params
            Parameter names with their new values.

        Returns
        -------
        self : object
            Returns self.
        """
    fitted_: bool
    def fit(self, X: _LGBM_ScikitMatrixLike, y: _LGBM_LabelType, sample_weight: _LGBM_WeightType | None = None, init_score: _LGBM_InitScoreType | None = None, group: _LGBM_GroupType | None = None, eval_set: List[_LGBM_ScikitValidSet] | None = None, eval_names: List[str] | None = None, eval_sample_weight: List[_LGBM_WeightType] | None = None, eval_class_weight: List[float] | None = None, eval_init_score: List[_LGBM_InitScoreType] | None = None, eval_group: List[_LGBM_GroupType] | None = None, eval_metric: _LGBM_ScikitEvalMetricType | None = None, feature_name: _LGBM_FeatureNameConfiguration = 'auto', categorical_feature: _LGBM_CategoricalFeatureConfiguration = 'auto', callbacks: List[Callable] | None = None, init_model: str | Path | Booster | LGBMModel | None = None) -> LGBMModel:
        """Docstring is set after definition, using a template."""
    def predict(self, X: _LGBM_ScikitMatrixLike, raw_score: bool = False, start_iteration: int = 0, num_iteration: int | None = None, pred_leaf: bool = False, pred_contrib: bool = False, validate_features: bool = False, **kwargs: Any):
        """Docstring is set after definition, using a template."""
    @property
    def n_features_(self) -> int:
        """:obj:`int`: The number of features of fitted model."""
    @property
    def n_features_in_(self) -> int:
        """:obj:`int`: The number of features of fitted model."""
    @property
    def best_score_(self) -> _LGBM_BoosterBestScoreType:
        """:obj:`dict`: The best score of fitted model."""
    @property
    def best_iteration_(self) -> int:
        """:obj:`int`: The best iteration of fitted model if ``early_stopping()`` callback has been specified."""
    @property
    def objective_(self) -> str | _LGBM_ScikitCustomObjectiveFunction:
        """:obj:`str` or :obj:`callable`: The concrete objective used while fitting this model."""
    @property
    def n_estimators_(self) -> int:
        """:obj:`int`: True number of boosting iterations performed.

        This might be less than parameter ``n_estimators`` if early stopping was enabled or
        if boosting stopped early due to limits on complexity like ``min_gain_to_split``.
        
        .. versionadded:: 4.0.0
        """
    @property
    def n_iter_(self) -> int:
        """:obj:`int`: True number of boosting iterations performed.

        This might be less than parameter ``n_estimators`` if early stopping was enabled or
        if boosting stopped early due to limits on complexity like ``min_gain_to_split``.
        
        .. versionadded:: 4.0.0
        """
    @property
    def booster_(self) -> Booster:
        """Booster: The underlying Booster of this model."""
    @property
    def evals_result_(self) -> _EvalResultDict:
        """:obj:`dict`: The evaluation results if validation sets have been specified."""
    @property
    def feature_importances_(self) -> np.ndarray:
        """:obj:`array` of shape = [n_features]: The feature importances (the higher, the more important).

        .. note::

            ``importance_type`` attribute is passed to the function
            to configure the type of importance values to be extracted.
        """
    @property
    def feature_name_(self) -> List[str]:
        """:obj:`list` of shape = [n_features]: The names of features."""

class LGBMRegressor(_LGBMRegressorBase, LGBMModel):
    """LightGBM regressor."""
    def fit(self, X: _LGBM_ScikitMatrixLike, y: _LGBM_LabelType, sample_weight: _LGBM_WeightType | None = None, init_score: _LGBM_InitScoreType | None = None, eval_set: List[_LGBM_ScikitValidSet] | None = None, eval_names: List[str] | None = None, eval_sample_weight: List[_LGBM_WeightType] | None = None, eval_init_score: List[_LGBM_InitScoreType] | None = None, eval_metric: _LGBM_ScikitEvalMetricType | None = None, feature_name: _LGBM_FeatureNameConfiguration = 'auto', categorical_feature: _LGBM_CategoricalFeatureConfiguration = 'auto', callbacks: List[Callable] | None = None, init_model: str | Path | Booster | LGBMModel | None = None) -> LGBMRegressor:
        """Docstring is inherited from the LGBMModel."""

class LGBMClassifier(_LGBMClassifierBase, LGBMModel):
    """LightGBM classifier."""
    def fit(self, X: _LGBM_ScikitMatrixLike, y: _LGBM_LabelType, sample_weight: _LGBM_WeightType | None = None, init_score: _LGBM_InitScoreType | None = None, eval_set: List[_LGBM_ScikitValidSet] | None = None, eval_names: List[str] | None = None, eval_sample_weight: List[_LGBM_WeightType] | None = None, eval_class_weight: List[float] | None = None, eval_init_score: List[_LGBM_InitScoreType] | None = None, eval_metric: _LGBM_ScikitEvalMetricType | None = None, feature_name: _LGBM_FeatureNameConfiguration = 'auto', categorical_feature: _LGBM_CategoricalFeatureConfiguration = 'auto', callbacks: List[Callable] | None = None, init_model: str | Path | Booster | LGBMModel | None = None) -> LGBMClassifier:
        """Docstring is inherited from the LGBMModel."""
    def predict(self, X: _LGBM_ScikitMatrixLike, raw_score: bool = False, start_iteration: int = 0, num_iteration: int | None = None, pred_leaf: bool = False, pred_contrib: bool = False, validate_features: bool = False, **kwargs: Any):
        """Docstring is inherited from the LGBMModel."""
    def predict_proba(self, X: _LGBM_ScikitMatrixLike, raw_score: bool = False, start_iteration: int = 0, num_iteration: int | None = None, pred_leaf: bool = False, pred_contrib: bool = False, validate_features: bool = False, **kwargs: Any):
        """Docstring is set after definition, using a template."""
    @property
    def classes_(self) -> np.ndarray:
        """:obj:`array` of shape = [n_classes]: The class label array."""
    @property
    def n_classes_(self) -> int:
        """:obj:`int`: The number of classes."""

class LGBMRanker(LGBMModel):
    """LightGBM ranker.

    .. warning::

        scikit-learn doesn't support ranking applications yet,
        therefore this class is not really compatible with the sklearn ecosystem.
        Please use this class mainly for training and applying ranking models in common sklearnish way.
    """
    def fit(self, X: _LGBM_ScikitMatrixLike, y: _LGBM_LabelType, sample_weight: _LGBM_WeightType | None = None, init_score: _LGBM_InitScoreType | None = None, group: _LGBM_GroupType | None = None, eval_set: List[_LGBM_ScikitValidSet] | None = None, eval_names: List[str] | None = None, eval_sample_weight: List[_LGBM_WeightType] | None = None, eval_init_score: List[_LGBM_InitScoreType] | None = None, eval_group: List[_LGBM_GroupType] | None = None, eval_metric: _LGBM_ScikitEvalMetricType | None = None, eval_at: List[int] | Tuple[int, ...] = (1, 2, 3, 4, 5), feature_name: _LGBM_FeatureNameConfiguration = 'auto', categorical_feature: _LGBM_CategoricalFeatureConfiguration = 'auto', callbacks: List[Callable] | None = None, init_model: str | Path | Booster | LGBMModel | None = None) -> LGBMRanker:
        """Docstring is inherited from the LGBMModel."""
