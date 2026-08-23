import abc
import ctypes
import numpy as np
import scipy.sparse
from .compat import pd_DataFrame, pd_Series
from _typeshed import Incomplete
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Set, Tuple

__all__ = ['Booster', 'Dataset', 'LGBMDeprecationWarning', 'LightGBMError', 'register_logger', 'Sequence']

class _MissingType(Enum):
    NONE: str
    NAN: str
    ZERO: str

class _DummyLogger:
    def info(self, msg: str) -> None: ...
    def warning(self, msg: str) -> None: ...

def register_logger(logger: Any, info_method_name: str = 'info', warning_method_name: str = 'warning') -> None:
    '''Register custom logger.

    Parameters
    ----------
    logger : Any
        Custom logger.
    info_method_name : str, optional (default="info")
        Method used to log info messages.
    warning_method_name : str, optional (default="warning")
        Method used to log warning messages.
    '''

class _TempFile:
    """Proxy class to workaround errors on Windows."""
    name: Incomplete
    path: Incomplete
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class LightGBMError(Exception):
    """Error thrown by LightGBM."""
class LGBMDeprecationWarning(UserWarning):
    """Custom deprecation warning."""

class _ConfigAliases:
    aliases: Incomplete
    @classmethod
    def get(cls, *args) -> Set[str]: ...
    @classmethod
    def get_sorted(cls, name: str) -> List[str]: ...
    @classmethod
    def get_by_alias(cls, *args) -> Set[str]: ...

class Sequence(abc.ABC, metaclass=abc.ABCMeta):
    """
    Generic data access interface.

    Object should support the following operations:

    .. code-block::

        # Get total row number.
        >>> len(seq)
        # Random access by row index. Used for data sampling.
        >>> seq[10]
        # Range data access. Used to read data in batch when constructing Dataset.
        >>> seq[0:100]
        # Optionally specify batch_size to control range data read size.
        >>> seq.batch_size

    - With random access, **data sampling does not need to go through all data**.
    - With range data access, there's **no need to read all data into memory thus reduce memory usage**.

    .. versionadded:: 3.3.0

    Attributes
    ----------
    batch_size : int
        Default size of a batch.
    """
    batch_size: int
    @abc.abstractmethod
    def __getitem__(self, idx: int | slice | List[int]) -> np.ndarray:
        '''Return data for given row index.

        A basic implementation should look like this:

        .. code-block:: python

            if isinstance(idx, numbers.Integral):
                return self._get_one_line(idx)
            elif isinstance(idx, slice):
                return np.stack([self._get_one_line(i) for i in range(idx.start, idx.stop)])
            elif isinstance(idx, list):
                # Only required if using ``Dataset.subset()``.
                return np.array([self._get_one_line(i) for i in idx])
            else:
                raise TypeError(f"Sequence index must be integer, slice or list, got {type(idx).__name__}")

        Parameters
        ----------
        idx : int, slice[int], list[int]
            Item index.

        Returns
        -------
        result : numpy 1-D array or numpy 2-D array
            1-D array if idx is int, 2-D array if idx is slice or list.
        '''
    @abc.abstractmethod
    def __len__(self) -> int:
        """Return row count of this sequence."""

class _InnerPredictor:
    """_InnerPredictor of LightGBM.

    Not exposed to user.
    Used only for prediction, usually used for continued training.

    .. note::

        Can be converted from Booster, but cannot be converted to Booster.
    """
    num_class: Incomplete
    num_total_iteration: Incomplete
    pandas_categorical: Incomplete
    pred_parameter: Incomplete
    def __init__(self, model_file: str | Path | None = None, booster_handle: ctypes.c_void_p | None = None, pred_parameter: Dict[str, Any] | None = None) -> None:
        """Initialize the _InnerPredictor.

        Parameters
        ----------
        model_file : str, pathlib.Path or None, optional (default=None)
            Path to the model file.
        booster_handle : object or None, optional (default=None)
            Handle of Booster.
        pred_parameter: dict or None, optional (default=None)
            Other parameters for the prediction.
        """
    def __del__(self) -> None: ...
    def predict(self, data: _LGBM_PredictDataType, start_iteration: int = 0, num_iteration: int = -1, raw_score: bool = False, pred_leaf: bool = False, pred_contrib: bool = False, data_has_header: bool = False, validate_features: bool = False) -> np.ndarray | scipy.sparse.spmatrix | List[scipy.sparse.spmatrix]:
        """Predict logic.

        Parameters
        ----------
        data : str, pathlib.Path, numpy array, pandas DataFrame, H2O DataTable's Frame or scipy.sparse
            Data source for prediction.
            If str or pathlib.Path, it represents the path to a text file (CSV, TSV, or LibSVM).
        start_iteration : int, optional (default=0)
            Start index of the iteration to predict.
        num_iteration : int, optional (default=-1)
            Iteration used for prediction.
        raw_score : bool, optional (default=False)
            Whether to predict raw scores.
        pred_leaf : bool, optional (default=False)
            Whether to predict leaf index.
        pred_contrib : bool, optional (default=False)
            Whether to predict feature contributions.
        data_has_header : bool, optional (default=False)
            Whether data has header.
            Used only for txt data.
        validate_features : bool, optional (default=False)
            If True, ensure that the features used to predict match the ones used to train.
            Used only if data is pandas DataFrame.

            .. versionadded:: 4.0.0

        Returns
        -------
        result : numpy array, scipy.sparse or list of scipy.sparse
            Prediction result.
            Can be sparse or a list of sparse objects (each element represents predictions for one class) for feature contributions (when ``pred_contrib=True``).
        """
    def current_iteration(self) -> int:
        """Get the index of the current iteration.

        Returns
        -------
        cur_iter : int
            The index of the current iteration.
        """

class Dataset:
    """Dataset in LightGBM."""
    data: Incomplete
    label: Incomplete
    reference: Incomplete
    weight: Incomplete
    group: Incomplete
    init_score: Incomplete
    feature_name: Incomplete
    categorical_feature: Incomplete
    params: Incomplete
    free_raw_data: Incomplete
    used_indices: Incomplete
    pandas_categorical: Incomplete
    version: int
    def __init__(self, data: _LGBM_TrainDataType, label: _LGBM_LabelType | None = None, reference: Dataset | None = None, weight: _LGBM_WeightType | None = None, group: _LGBM_GroupType | None = None, init_score: _LGBM_InitScoreType | None = None, feature_name: _LGBM_FeatureNameConfiguration = 'auto', categorical_feature: _LGBM_CategoricalFeatureConfiguration = 'auto', params: Dict[str, Any] | None = None, free_raw_data: bool = True) -> None:
        '''Initialize Dataset.

        Parameters
        ----------
        data : str, pathlib.Path, numpy array, pandas DataFrame, H2O DataTable\'s Frame, scipy.sparse, Sequence, list of Sequence or list of numpy array
            Data source of Dataset.
            If str or pathlib.Path, it represents the path to a text file (CSV, TSV, or LibSVM) or a LightGBM Dataset binary file.
        label : list, numpy 1-D array, pandas Series / one-column DataFrame or None, optional (default=None)
            Label of the data.
        reference : Dataset or None, optional (default=None)
            If this is Dataset for validation, training data should be used as reference.
        weight : list, numpy 1-D array, pandas Series or None, optional (default=None)
            Weight for each instance. Weights should be non-negative.
        group : list, numpy 1-D array, pandas Series or None, optional (default=None)
            Group/query data.
            Only used in the learning-to-rank task.
            sum(group) = n_samples.
            For example, if you have a 100-document dataset with ``group = [10, 20, 40, 10, 10, 10]``, that means that you have 6 groups,
            where the first 10 records are in the first group, records 11-30 are in the second group, records 31-70 are in the third group, etc.
        init_score : list, list of lists (for multi-class task), numpy array, pandas Series, pandas DataFrame (for multi-class task), or None, optional (default=None)
            Init score for Dataset.
        feature_name : list of str, or \'auto\', optional (default="auto")
            Feature names.
            If \'auto\' and data is pandas DataFrame, data columns names are used.
        categorical_feature : list of str or int, or \'auto\', optional (default="auto")
            Categorical features.
            If list of int, interpreted as indices.
            If list of str, interpreted as feature names (need to specify ``feature_name`` as well).
            If \'auto\' and data is pandas DataFrame, pandas unordered categorical columns are used.
            All values in categorical features will be cast to int32 and thus should be less than int32 max value (2147483647).
            Large values could be memory consuming. Consider using consecutive integers starting from zero.
            All negative values in categorical features will be treated as missing values.
            The output cannot be monotonically constrained with respect to a categorical feature.
            Floating point numbers in categorical features will be rounded towards 0.
        params : dict or None, optional (default=None)
            Other parameters for Dataset.
        free_raw_data : bool, optional (default=True)
            If True, raw data is freed after constructing inner Dataset.
        '''
    def __del__(self) -> None: ...
    def get_params(self) -> Dict[str, Any]:
        """Get the used parameters in the Dataset.

        Returns
        -------
        params : dict
            The used parameters in this Dataset object.
        """
    def construct(self) -> Dataset:
        """Lazy init.

        Returns
        -------
        self : Dataset
            Constructed Dataset object.
        """
    def create_valid(self, data: _LGBM_TrainDataType, label: _LGBM_LabelType | None = None, weight: _LGBM_WeightType | None = None, group: _LGBM_GroupType | None = None, init_score: _LGBM_InitScoreType | None = None, params: Dict[str, Any] | None = None) -> Dataset:
        """Create validation data align with current Dataset.

        Parameters
        ----------
        data : str, pathlib.Path, numpy array, pandas DataFrame, H2O DataTable's Frame, scipy.sparse, Sequence, list of Sequence or list of numpy array
            Data source of Dataset.
            If str or pathlib.Path, it represents the path to a text file (CSV, TSV, or LibSVM) or a LightGBM Dataset binary file.
        label : list, numpy 1-D array, pandas Series / one-column DataFrame or None, optional (default=None)
            Label of the data.
        weight : list, numpy 1-D array, pandas Series or None, optional (default=None)
            Weight for each instance. Weights should be non-negative.
        group : list, numpy 1-D array, pandas Series or None, optional (default=None)
            Group/query data.
            Only used in the learning-to-rank task.
            sum(group) = n_samples.
            For example, if you have a 100-document dataset with ``group = [10, 20, 40, 10, 10, 10]``, that means that you have 6 groups,
            where the first 10 records are in the first group, records 11-30 are in the second group, records 31-70 are in the third group, etc.
        init_score : list, list of lists (for multi-class task), numpy array, pandas Series, pandas DataFrame (for multi-class task), or None, optional (default=None)
            Init score for Dataset.
        params : dict or None, optional (default=None)
            Other parameters for validation Dataset.

        Returns
        -------
        valid : Dataset
            Validation Dataset with reference to self.
        """
    def subset(self, used_indices: List[int], params: Dict[str, Any] | None = None) -> Dataset:
        """Get subset of current Dataset.

        Parameters
        ----------
        used_indices : list of int
            Indices used to create the subset.
        params : dict or None, optional (default=None)
            These parameters will be passed to Dataset constructor.

        Returns
        -------
        subset : Dataset
            Subset of the current Dataset.
        """
    def save_binary(self, filename: str | Path) -> Dataset:
        """Save Dataset to a binary file.

        .. note::

            Please note that `init_score` is not saved in binary file.
            If you need it, please set it again after loading Dataset.

        Parameters
        ----------
        filename : str or pathlib.Path
            Name of the output file.

        Returns
        -------
        self : Dataset
            Returns self.
        """
    def set_field(self, field_name: str, data: List[List[float]] | List[List[int]] | List[float] | List[int] | np.ndarray | pd_Series | pd_DataFrame | None) -> Dataset:
        """Set property into the Dataset.

        Parameters
        ----------
        field_name : str
            The field name of the information.
        data : list, list of lists (for multi-class task), numpy array, pandas Series, pandas DataFrame (for multi-class task), or None
            The data to be set.

        Returns
        -------
        self : Dataset
            Dataset with set property.
        """
    def get_field(self, field_name: str) -> np.ndarray | None:
        """Get property from the Dataset.

        Parameters
        ----------
        field_name : str
            The field name of the information.

        Returns
        -------
        info : numpy array or None
            A numpy array with information from the Dataset.
        """
    def set_categorical_feature(self, categorical_feature: _LGBM_CategoricalFeatureConfiguration) -> Dataset:
        """Set categorical features.

        Parameters
        ----------
        categorical_feature : list of str or int, or 'auto'
            Names or indices of categorical features.

        Returns
        -------
        self : Dataset
            Dataset with set categorical features.
        """
    def set_reference(self, reference: Dataset) -> Dataset:
        """Set reference Dataset.

        Parameters
        ----------
        reference : Dataset
            Reference that is used as a template to construct the current Dataset.

        Returns
        -------
        self : Dataset
            Dataset with set reference.
        """
    def set_feature_name(self, feature_name: _LGBM_FeatureNameConfiguration) -> Dataset:
        """Set feature name.

        Parameters
        ----------
        feature_name : list of str
            Feature names.

        Returns
        -------
        self : Dataset
            Dataset with set feature name.
        """
    def set_label(self, label: _LGBM_LabelType | None) -> Dataset:
        """Set label of Dataset.

        Parameters
        ----------
        label : list, numpy 1-D array, pandas Series / one-column DataFrame or None
            The label information to be set into Dataset.

        Returns
        -------
        self : Dataset
            Dataset with set label.
        """
    def set_weight(self, weight: _LGBM_WeightType | None) -> Dataset:
        """Set weight of each instance.

        Parameters
        ----------
        weight : list, numpy 1-D array, pandas Series or None
            Weight to be set for each data point. Weights should be non-negative.

        Returns
        -------
        self : Dataset
            Dataset with set weight.
        """
    def set_init_score(self, init_score: _LGBM_InitScoreType | None) -> Dataset:
        """Set init score of Booster to start from.

        Parameters
        ----------
        init_score : list, list of lists (for multi-class task), numpy array, pandas Series, pandas DataFrame (for multi-class task), or None
            Init score for Booster.

        Returns
        -------
        self : Dataset
            Dataset with set init score.
        """
    def set_group(self, group: _LGBM_GroupType | None) -> Dataset:
        """Set group size of Dataset (used for ranking).

        Parameters
        ----------
        group : list, numpy 1-D array, pandas Series or None
            Group/query data.
            Only used in the learning-to-rank task.
            sum(group) = n_samples.
            For example, if you have a 100-document dataset with ``group = [10, 20, 40, 10, 10, 10]``, that means that you have 6 groups,
            where the first 10 records are in the first group, records 11-30 are in the second group, records 31-70 are in the third group, etc.

        Returns
        -------
        self : Dataset
            Dataset with set group.
        """
    def get_feature_name(self) -> List[str]:
        """Get the names of columns (features) in the Dataset.

        Returns
        -------
        feature_names : list of str
            The names of columns (features) in the Dataset.
        """
    def get_label(self) -> np.ndarray | None:
        """Get the label of the Dataset.

        Returns
        -------
        label : numpy array or None
            The label information from the Dataset.
        """
    def get_weight(self) -> np.ndarray | None:
        """Get the weight of the Dataset.

        Returns
        -------
        weight : numpy array or None
            Weight for each data point from the Dataset. Weights should be non-negative.
        """
    def get_init_score(self) -> np.ndarray | None:
        """Get the initial score of the Dataset.

        Returns
        -------
        init_score : numpy array or None
            Init score of Booster.
        """
    def get_data(self) -> _LGBM_TrainDataType | None:
        """Get the raw data of the Dataset.

        Returns
        -------
        data : str, pathlib.Path, numpy array, pandas DataFrame, H2O DataTable's Frame, scipy.sparse, Sequence, list of Sequence or list of numpy array or None
            Raw data used in the Dataset construction.
        """
    def get_group(self) -> np.ndarray | None:
        """Get the group of the Dataset.

        Returns
        -------
        group : numpy array or None
            Group/query data.
            Only used in the learning-to-rank task.
            sum(group) = n_samples.
            For example, if you have a 100-document dataset with ``group = [10, 20, 40, 10, 10, 10]``, that means that you have 6 groups,
            where the first 10 records are in the first group, records 11-30 are in the second group, records 31-70 are in the third group, etc.
        """
    def num_data(self) -> int:
        """Get the number of rows in the Dataset.

        Returns
        -------
        number_of_rows : int
            The number of rows in the Dataset.
        """
    def num_feature(self) -> int:
        """Get the number of columns (features) in the Dataset.

        Returns
        -------
        number_of_columns : int
            The number of columns (features) in the Dataset.
        """
    def feature_num_bin(self, feature: int | str) -> int:
        """Get the number of bins for a feature.

        .. versionadded:: 4.0.0

        Parameters
        ----------
        feature : int or str
            Index or name of the feature.

        Returns
        -------
        number_of_bins : int
            The number of constructed bins for the feature in the Dataset.
        """
    def get_ref_chain(self, ref_limit: int = 100) -> Set['Dataset']:
        """Get a chain of Dataset objects.

        Starts with r, then goes to r.reference (if exists),
        then to r.reference.reference, etc.
        until we hit ``ref_limit`` or a reference loop.

        Parameters
        ----------
        ref_limit : int, optional (default=100)
            The limit number of references.

        Returns
        -------
        ref_chain : set of Dataset
            Chain of references of the Datasets.
        """
    def add_features_from(self, other: Dataset) -> Dataset:
        """Add features from other Dataset to the current Dataset.

        Both Datasets must be constructed before calling this method.

        Parameters
        ----------
        other : Dataset
            The Dataset to take features from.

        Returns
        -------
        self : Dataset
            Dataset with the new features added.
        """

class Booster:
    """Booster in LightGBM."""
    best_iteration: int
    best_score: Incomplete
    train_set: Incomplete
    valid_sets: Incomplete
    name_valid_sets: Incomplete
    pandas_categorical: Incomplete
    train_set_version: Incomplete
    params: Incomplete
    def __init__(self, params: Dict[str, Any] | None = None, train_set: Dataset | None = None, model_file: str | Path | None = None, model_str: str | None = None) -> None:
        """Initialize the Booster.

        Parameters
        ----------
        params : dict or None, optional (default=None)
            Parameters for Booster.
        train_set : Dataset or None, optional (default=None)
            Training dataset.
        model_file : str, pathlib.Path or None, optional (default=None)
            Path to the model file.
        model_str : str or None, optional (default=None)
            Model will be loaded from this string.
        """
    def __del__(self) -> None: ...
    def __copy__(self) -> Booster: ...
    def __deepcopy__(self, _) -> Booster: ...
    def free_dataset(self) -> Booster:
        """Free Booster's Datasets.

        Returns
        -------
        self : Booster
            Booster without Datasets.
        """
    def set_network(self, machines: List[str] | Set[str] | str, local_listen_port: int = 12400, listen_time_out: int = 120, num_machines: int = 1) -> Booster:
        """Set the network configuration.

        Parameters
        ----------
        machines : list, set or str
            Names of machines.
        local_listen_port : int, optional (default=12400)
            TCP listen port for local machines.
        listen_time_out : int, optional (default=120)
            Socket time-out in minutes.
        num_machines : int, optional (default=1)
            The number of machines for distributed learning application.

        Returns
        -------
        self : Booster
            Booster with set network.
        """
    def free_network(self) -> Booster:
        """Free Booster's network.

        Returns
        -------
        self : Booster
            Booster with freed network.
        """
    def trees_to_dataframe(self) -> pd_DataFrame:
        '''Parse the fitted model and return in an easy-to-read pandas DataFrame.

        The returned DataFrame has the following columns.

            - ``tree_index`` : int64, which tree a node belongs to. 0-based, so a value of ``6``, for example, means "this node is in the 7th tree".
            - ``node_depth`` : int64, how far a node is from the root of the tree. The root node has a value of ``1``, its direct children are ``2``, etc.
            - ``node_index`` : str, unique identifier for a node.
            - ``left_child`` : str, ``node_index`` of the child node to the left of a split. ``None`` for leaf nodes.
            - ``right_child`` : str, ``node_index`` of the child node to the right of a split. ``None`` for leaf nodes.
            - ``parent_index`` : str, ``node_index`` of this node\'s parent. ``None`` for the root node.
            - ``split_feature`` : str, name of the feature used for splitting. ``None`` for leaf nodes.
            - ``split_gain`` : float64, gain from adding this split to the tree. ``NaN`` for leaf nodes.
            - ``threshold`` : float64, value of the feature used to decide which side of the split a record will go down. ``NaN`` for leaf nodes.
            - ``decision_type`` : str, logical operator describing how to compare a value to ``threshold``.
              For example, ``split_feature = "Column_10", threshold = 15, decision_type = "<="`` means that
              records where ``Column_10 <= 15`` follow the left side of the split, otherwise follows the right side of the split. ``None`` for leaf nodes.
            - ``missing_direction`` : str, split direction that missing values should go to. ``None`` for leaf nodes.
            - ``missing_type`` : str, describes what types of values are treated as missing.
            - ``value`` : float64, predicted value for this leaf node, multiplied by the learning rate.
            - ``weight`` : float64 or int64, sum of Hessian (second-order derivative of objective), summed over observations that fall in this node.
            - ``count`` : int64, number of records in the training data that fall into this node.

        Returns
        -------
        result : pandas DataFrame
            Returns a pandas DataFrame of the parsed model.
        '''
    def set_train_data_name(self, name: str) -> Booster:
        """Set the name to the training Dataset.

        Parameters
        ----------
        name : str
            Name for the training Dataset.

        Returns
        -------
        self : Booster
            Booster with set training Dataset name.
        """
    def add_valid(self, data: Dataset, name: str) -> Booster:
        """Add validation data.

        Parameters
        ----------
        data : Dataset
            Validation data.
        name : str
            Name of validation data.

        Returns
        -------
        self : Booster
            Booster with set validation data.
        """
    def reset_parameter(self, params: Dict[str, Any]) -> Booster:
        """Reset parameters of Booster.

        Parameters
        ----------
        params : dict
            New parameters for Booster.

        Returns
        -------
        self : Booster
            Booster with new parameters.
        """
    def update(self, train_set: Dataset | None = None, fobj: _LGBM_CustomObjectiveFunction | None = None) -> bool:
        """Update Booster for one iteration.

        Parameters
        ----------
        train_set : Dataset or None, optional (default=None)
            Training data.
            If None, last training data is used.
        fobj : callable or None, optional (default=None)
            Customized objective function.
            Should accept two parameters: preds, train_data,
            and return (grad, hess).

                preds : numpy 1-D array or numpy 2-D array (for multi-class task)
                    The predicted values.
                    Predicted values are returned before any transformation,
                    e.g. they are raw margin instead of probability of positive class for binary task.
                train_data : Dataset
                    The training dataset.
                grad : numpy 1-D array or numpy 2-D array (for multi-class task)
                    The value of the first order derivative (gradient) of the loss
                    with respect to the elements of preds for each sample point.
                hess : numpy 1-D array or numpy 2-D array (for multi-class task)
                    The value of the second order derivative (Hessian) of the loss
                    with respect to the elements of preds for each sample point.

            For multi-class task, preds are numpy 2-D array of shape = [n_samples, n_classes],
            and grad and hess should be returned in the same format.

        Returns
        -------
        is_finished : bool
            Whether the update was successfully finished.
        """
    def rollback_one_iter(self) -> Booster:
        """Rollback one iteration.

        Returns
        -------
        self : Booster
            Booster with rolled back one iteration.
        """
    def current_iteration(self) -> int:
        """Get the index of the current iteration.

        Returns
        -------
        cur_iter : int
            The index of the current iteration.
        """
    def num_model_per_iteration(self) -> int:
        """Get number of models per iteration.

        Returns
        -------
        model_per_iter : int
            The number of models per iteration.
        """
    def num_trees(self) -> int:
        """Get number of weak sub-models.

        Returns
        -------
        num_trees : int
            The number of weak sub-models.
        """
    def upper_bound(self) -> float:
        """Get upper bound value of a model.

        Returns
        -------
        upper_bound : float
            Upper bound value of the model.
        """
    def lower_bound(self) -> float:
        """Get lower bound value of a model.

        Returns
        -------
        lower_bound : float
            Lower bound value of the model.
        """
    def eval(self, data: Dataset, name: str, feval: _LGBM_CustomEvalFunction | List[_LGBM_CustomEvalFunction] | None = None) -> List[_LGBM_BoosterEvalMethodResultType]:
        """Evaluate for data.

        Parameters
        ----------
        data : Dataset
            Data for the evaluating.
        name : str
            Name of the data.
        feval : callable, list of callable, or None, optional (default=None)
            Customized evaluation function.
            Each evaluation function should accept two parameters: preds, eval_data,
            and return (eval_name, eval_result, is_higher_better) or list of such tuples.

                preds : numpy 1-D array or numpy 2-D array (for multi-class task)
                    The predicted values.
                    For multi-class task, preds are numpy 2-D array of shape = [n_samples, n_classes].
                    If custom objective function is used, predicted values are returned before any transformation,
                    e.g. they are raw margin instead of probability of positive class for binary task in this case.
                eval_data : Dataset
                    A ``Dataset`` to evaluate.
                eval_name : str
                    The name of evaluation function (without whitespace).
                eval_result : float
                    The eval result.
                is_higher_better : bool
                    Is eval result higher better, e.g. AUC is ``is_higher_better``.

        Returns
        -------
        result : list
            List with (dataset_name, eval_name, eval_result, is_higher_better) tuples.
        """
    def eval_train(self, feval: _LGBM_CustomEvalFunction | List[_LGBM_CustomEvalFunction] | None = None) -> List[_LGBM_BoosterEvalMethodResultType]:
        """Evaluate for training data.

        Parameters
        ----------
        feval : callable, list of callable, or None, optional (default=None)
            Customized evaluation function.
            Each evaluation function should accept two parameters: preds, eval_data,
            and return (eval_name, eval_result, is_higher_better) or list of such tuples.

                preds : numpy 1-D array or numpy 2-D array (for multi-class task)
                    The predicted values.
                    For multi-class task, preds are numpy 2-D array of shape = [n_samples, n_classes].
                    If custom objective function is used, predicted values are returned before any transformation,
                    e.g. they are raw margin instead of probability of positive class for binary task in this case.
                eval_data : Dataset
                    The training dataset.
                eval_name : str
                    The name of evaluation function (without whitespace).
                eval_result : float
                    The eval result.
                is_higher_better : bool
                    Is eval result higher better, e.g. AUC is ``is_higher_better``.

        Returns
        -------
        result : list
            List with (train_dataset_name, eval_name, eval_result, is_higher_better) tuples.
        """
    def eval_valid(self, feval: _LGBM_CustomEvalFunction | List[_LGBM_CustomEvalFunction] | None = None) -> List[_LGBM_BoosterEvalMethodResultType]:
        """Evaluate for validation data.

        Parameters
        ----------
        feval : callable, list of callable, or None, optional (default=None)
            Customized evaluation function.
            Each evaluation function should accept two parameters: preds, eval_data,
            and return (eval_name, eval_result, is_higher_better) or list of such tuples.

                preds : numpy 1-D array or numpy 2-D array (for multi-class task)
                    The predicted values.
                    For multi-class task, preds are numpy 2-D array of shape = [n_samples, n_classes].
                    If custom objective function is used, predicted values are returned before any transformation,
                    e.g. they are raw margin instead of probability of positive class for binary task in this case.
                eval_data : Dataset
                    The validation dataset.
                eval_name : str
                    The name of evaluation function (without whitespace).
                eval_result : float
                    The eval result.
                is_higher_better : bool
                    Is eval result higher better, e.g. AUC is ``is_higher_better``.

        Returns
        -------
        result : list
            List with (validation_dataset_name, eval_name, eval_result, is_higher_better) tuples.
        """
    def save_model(self, filename: str | Path, num_iteration: int | None = None, start_iteration: int = 0, importance_type: str = 'split') -> Booster:
        '''Save Booster to file.

        Parameters
        ----------
        filename : str or pathlib.Path
            Filename to save Booster.
        num_iteration : int or None, optional (default=None)
            Index of the iteration that should be saved.
            If None, if the best iteration exists, it is saved; otherwise, all iterations are saved.
            If <= 0, all iterations are saved.
        start_iteration : int, optional (default=0)
            Start index of the iteration that should be saved.
        importance_type : str, optional (default="split")
            What type of feature importance should be saved.
            If "split", result contains numbers of times the feature is used in a model.
            If "gain", result contains total gains of splits which use the feature.

        Returns
        -------
        self : Booster
            Returns self.
        '''
    def shuffle_models(self, start_iteration: int = 0, end_iteration: int = -1) -> Booster:
        """Shuffle models.

        Parameters
        ----------
        start_iteration : int, optional (default=0)
            The first iteration that will be shuffled.
        end_iteration : int, optional (default=-1)
            The last iteration that will be shuffled.
            If <= 0, means the last available iteration.

        Returns
        -------
        self : Booster
            Booster with shuffled models.
        """
    def model_from_string(self, model_str: str) -> Booster:
        """Load Booster from a string.

        Parameters
        ----------
        model_str : str
            Model will be loaded from this string.

        Returns
        -------
        self : Booster
            Loaded Booster object.
        """
    def model_to_string(self, num_iteration: int | None = None, start_iteration: int = 0, importance_type: str = 'split') -> str:
        '''Save Booster to string.

        Parameters
        ----------
        num_iteration : int or None, optional (default=None)
            Index of the iteration that should be saved.
            If None, if the best iteration exists, it is saved; otherwise, all iterations are saved.
            If <= 0, all iterations are saved.
        start_iteration : int, optional (default=0)
            Start index of the iteration that should be saved.
        importance_type : str, optional (default="split")
            What type of feature importance should be saved.
            If "split", result contains numbers of times the feature is used in a model.
            If "gain", result contains total gains of splits which use the feature.

        Returns
        -------
        str_repr : str
            String representation of Booster.
        '''
    def dump_model(self, num_iteration: int | None = None, start_iteration: int = 0, importance_type: str = 'split', object_hook: Callable[[Dict[str, Any]], Dict[str, Any]] | None = None) -> Dict[str, Any]:
        '''Dump Booster to JSON format.

        Parameters
        ----------
        num_iteration : int or None, optional (default=None)
            Index of the iteration that should be dumped.
            If None, if the best iteration exists, it is dumped; otherwise, all iterations are dumped.
            If <= 0, all iterations are dumped.
        start_iteration : int, optional (default=0)
            Start index of the iteration that should be dumped.
        importance_type : str, optional (default="split")
            What type of feature importance should be dumped.
            If "split", result contains numbers of times the feature is used in a model.
            If "gain", result contains total gains of splits which use the feature.
        object_hook : callable or None, optional (default=None)
            If not None, ``object_hook`` is a function called while parsing the json
            string returned by the C API. It may be used to alter the json, to store
            specific values while building the json structure. It avoids
            walking through the structure again. It saves a significant amount
            of time if the number of trees is huge.
            Signature is ``def object_hook(node: dict) -> dict``.
            None is equivalent to ``lambda node: node``.
            See documentation of ``json.loads()`` for further details.

        Returns
        -------
        json_repr : dict
            JSON format of Booster.
        '''
    def predict(self, data: _LGBM_PredictDataType, start_iteration: int = 0, num_iteration: int | None = None, raw_score: bool = False, pred_leaf: bool = False, pred_contrib: bool = False, data_has_header: bool = False, validate_features: bool = False, **kwargs: Any) -> np.ndarray | scipy.sparse.spmatrix | List[scipy.sparse.spmatrix]:
        """Make a prediction.

        Parameters
        ----------
        data : str, pathlib.Path, numpy array, pandas DataFrame, H2O DataTable's Frame or scipy.sparse
            Data source for prediction.
            If str or pathlib.Path, it represents the path to a text file (CSV, TSV, or LibSVM).
        start_iteration : int, optional (default=0)
            Start index of the iteration to predict.
            If <= 0, starts from the first iteration.
        num_iteration : int or None, optional (default=None)
            Total number of iterations used in the prediction.
            If None, if the best iteration exists and start_iteration <= 0, the best iteration is used;
            otherwise, all iterations from ``start_iteration`` are used (no limits).
            If <= 0, all iterations from ``start_iteration`` are used (no limits).
        raw_score : bool, optional (default=False)
            Whether to predict raw scores.
        pred_leaf : bool, optional (default=False)
            Whether to predict leaf index.
        pred_contrib : bool, optional (default=False)
            Whether to predict feature contributions.

            .. note::

                If you want to get more explanations for your model's predictions using SHAP values,
                like SHAP interaction values,
                you can install the shap package (https://github.com/slundberg/shap).
                Note that unlike the shap package, with ``pred_contrib`` we return a matrix with an extra
                column, where the last column is the expected value.

        data_has_header : bool, optional (default=False)
            Whether the data has header.
            Used only if data is str.
        validate_features : bool, optional (default=False)
            If True, ensure that the features used to predict match the ones used to train.
            Used only if data is pandas DataFrame.
        **kwargs
            Other parameters for the prediction.

        Returns
        -------
        result : numpy array, scipy.sparse or list of scipy.sparse
            Prediction result.
            Can be sparse or a list of sparse objects (each element represents predictions for one class) for feature contributions (when ``pred_contrib=True``).
        """
    def refit(self, data: _LGBM_TrainDataType, label: _LGBM_LabelType, decay_rate: float = 0.9, reference: Dataset | None = None, weight: _LGBM_WeightType | None = None, group: _LGBM_GroupType | None = None, init_score: _LGBM_InitScoreType | None = None, feature_name: _LGBM_FeatureNameConfiguration = 'auto', categorical_feature: _LGBM_CategoricalFeatureConfiguration = 'auto', dataset_params: Dict[str, Any] | None = None, free_raw_data: bool = True, validate_features: bool = False, **kwargs) -> Booster:
        '''Refit the existing Booster by new data.

        Parameters
        ----------
        data : str, pathlib.Path, numpy array, pandas DataFrame, H2O DataTable\'s Frame, scipy.sparse, Sequence, list of Sequence or list of numpy array
            Data source for refit.
            If str or pathlib.Path, it represents the path to a text file (CSV, TSV, or LibSVM).
        label : list, numpy 1-D array or pandas Series / one-column DataFrame
            Label for refit.
        decay_rate : float, optional (default=0.9)
            Decay rate of refit,
            will use ``leaf_output = decay_rate * old_leaf_output + (1.0 - decay_rate) * new_leaf_output`` to refit trees.
        reference : Dataset or None, optional (default=None)
            Reference for ``data``.

            .. versionadded:: 4.0.0

        weight : list, numpy 1-D array, pandas Series or None, optional (default=None)
            Weight for each ``data`` instance. Weights should be non-negative.

            .. versionadded:: 4.0.0

        group : list, numpy 1-D array, pandas Series or None, optional (default=None)
            Group/query size for ``data``.
            Only used in the learning-to-rank task.
            sum(group) = n_samples.
            For example, if you have a 100-document dataset with ``group = [10, 20, 40, 10, 10, 10]``, that means that you have 6 groups,
            where the first 10 records are in the first group, records 11-30 are in the second group, records 31-70 are in the third group, etc.

            .. versionadded:: 4.0.0

        init_score : list, list of lists (for multi-class task), numpy array, pandas Series, pandas DataFrame (for multi-class task), or None, optional (default=None)
            Init score for ``data``.

            .. versionadded:: 4.0.0

        feature_name : list of str, or \'auto\', optional (default="auto")
            Feature names for ``data``.
            If \'auto\' and data is pandas DataFrame, data columns names are used.

            .. versionadded:: 4.0.0

        categorical_feature : list of str or int, or \'auto\', optional (default="auto")
            Categorical features for ``data``.
            If list of int, interpreted as indices.
            If list of str, interpreted as feature names (need to specify ``feature_name`` as well).
            If \'auto\' and data is pandas DataFrame, pandas unordered categorical columns are used.
            All values in categorical features will be cast to int32 and thus should be less than int32 max value (2147483647).
            Large values could be memory consuming. Consider using consecutive integers starting from zero.
            All negative values in categorical features will be treated as missing values.
            The output cannot be monotonically constrained with respect to a categorical feature.
            Floating point numbers in categorical features will be rounded towards 0.

            .. versionadded:: 4.0.0

        dataset_params : dict or None, optional (default=None)
            Other parameters for Dataset ``data``.

            .. versionadded:: 4.0.0

        free_raw_data : bool, optional (default=True)
            If True, raw data is freed after constructing inner Dataset for ``data``.

            .. versionadded:: 4.0.0

        validate_features : bool, optional (default=False)
            If True, ensure that the features used to refit the model match the original ones.
            Used only if data is pandas DataFrame.

            .. versionadded:: 4.0.0

        **kwargs
            Other parameters for refit.
            These parameters will be passed to ``predict`` method.

        Returns
        -------
        result : Booster
            Refitted Booster.
        '''
    def get_leaf_output(self, tree_id: int, leaf_id: int) -> float:
        """Get the output of a leaf.

        Parameters
        ----------
        tree_id : int
            The index of the tree.
        leaf_id : int
            The index of the leaf in the tree.

        Returns
        -------
        result : float
            The output of the leaf.
        """
    def set_leaf_output(self, tree_id: int, leaf_id: int, value: float) -> Booster:
        """Set the output of a leaf.

        .. versionadded:: 4.0.0

        Parameters
        ----------
        tree_id : int
            The index of the tree.
        leaf_id : int
            The index of the leaf in the tree.
        value : float
            Value to set as the output of the leaf.

        Returns
        -------
        self : Booster
            Booster with the leaf output set.
        """
    def num_feature(self) -> int:
        """Get number of features.

        Returns
        -------
        num_feature : int
            The number of features.
        """
    def feature_name(self) -> List[str]:
        """Get names of features.

        Returns
        -------
        result : list of str
            List with names of features.
        """
    def feature_importance(self, importance_type: str = 'split', iteration: int | None = None) -> np.ndarray:
        '''Get feature importances.

        Parameters
        ----------
        importance_type : str, optional (default="split")
            How the importance is calculated.
            If "split", result contains numbers of times the feature is used in a model.
            If "gain", result contains total gains of splits which use the feature.
        iteration : int or None, optional (default=None)
            Limit number of iterations in the feature importance calculation.
            If None, if the best iteration exists, it is used; otherwise, all trees are used.
            If <= 0, all trees are used (no limits).

        Returns
        -------
        result : numpy array
            Array with feature importances.
        '''
    def get_split_value_histogram(self, feature: int | str, bins: int | str | None = None, xgboost_style: bool = False) -> Tuple[np.ndarray, np.ndarray] | np.ndarray | pd_DataFrame:
        """Get split value histogram for the specified feature.

        Parameters
        ----------
        feature : int or str
            The feature name or index the histogram is calculated for.
            If int, interpreted as index.
            If str, interpreted as name.

            .. warning::

                Categorical features are not supported.

        bins : int, str or None, optional (default=None)
            The maximum number of bins.
            If None, or int and > number of unique split values and ``xgboost_style=True``,
            the number of bins equals number of unique split values.
            If str, it should be one from the list of the supported values by ``numpy.histogram()`` function.
        xgboost_style : bool, optional (default=False)
            Whether the returned result should be in the same form as it is in XGBoost.
            If False, the returned value is tuple of 2 numpy arrays as it is in ``numpy.histogram()`` function.
            If True, the returned value is matrix, in which the first column is the right edges of non-empty bins
            and the second one is the histogram values.

        Returns
        -------
        result_tuple : tuple of 2 numpy arrays
            If ``xgboost_style=False``, the values of the histogram of used splitting values for the specified feature
            and the bin edges.
        result_array_like : numpy array or pandas DataFrame (if pandas is installed)
            If ``xgboost_style=True``, the histogram of used splitting values for the specified feature.
        """
