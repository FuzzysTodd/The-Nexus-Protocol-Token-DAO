import abc
import ctypes
import numpy as np
import os
import scipy.sparse
from ._typing import ArrayLike as ArrayLike, BoosterParam as BoosterParam, CFloatPtr as CFloatPtr, CNumeric as CNumeric, CNumericPtr as CNumericPtr, CStrPptr as CStrPptr, CStrPtr as CStrPtr, CTypeT as CTypeT, CupyT as CupyT, DataType as DataType, FeatureInfo as FeatureInfo, FeatureNames as FeatureNames, FeatureTypes as FeatureTypes, NumpyOrCupy as NumpyOrCupy, _T, c_bst_ulong as c_bst_ulong
from .compat import DataFrame as DataFrame, PANDAS_INSTALLED as PANDAS_INSTALLED, py_str as py_str
from .libpath import find_lib_path as find_lib_path
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Iterable, List, Sequence, Tuple, Type, TypeVar, overload

class XGBoostError(ValueError):
    """Error thrown by xgboost trainer."""

@overload
def from_pystr_to_cstr(data: str) -> bytes: ...
@overload
def from_pystr_to_cstr(data: List[str]) -> ctypes.Array: ...
def from_cstr_to_pystr(data: CStrPptr, length: c_bst_ulong) -> List[str]:
    """Revert C pointer to Python str

    Parameters
    ----------
    data : ctypes pointer
        pointer to data
    length : ctypes pointer
        pointer to length of data
    """
def make_jcargs(**kwargs: Any) -> bytes:
    """Make JSON-based arguments for C functions."""
IterRange = TypeVar('IterRange', Tuple[int, int] | None, Tuple[int, int])

def build_info() -> dict:
    """Build information of XGBoost.  The returned value format is not stable. Also, please
    note that build time dependency is not the same as runtime dependency. For instance,
    it's possible to build XGBoost with older CUDA version but run it with the lastest
    one.

      .. versionadded:: 1.6.0

    """
def ctypes2numpy(cptr: CNumericPtr, length: int, dtype: Type[np.number]) -> np.ndarray:
    """Convert a ctypes pointer array to a numpy array."""
def ctypes2cupy(cptr: CNumericPtr, length: int, dtype: Type[np.number]) -> CupyT:
    """Convert a ctypes pointer array to a cupy array."""
def ctypes2buffer(cptr: CStrPtr, length: int) -> bytearray:
    """Convert ctypes pointer to buffer type."""
def c_str(string: str) -> ctypes.c_char_p:
    """Convert a python string to cstring."""
def c_array(ctype: Type[CTypeT], values: ArrayLike) -> ctypes.Array | ctypes._Pointer:
    """Convert a python array to c array."""

class DataIter(ABC, metaclass=abc.ABCMeta):
    """The interface for user defined data iterator.

    Parameters
    ----------
    cache_prefix:
        Prefix to the cache files, only used in external memory.  It can be either an
        URI or a file path.

    """
    cache_prefix: Incomplete
    def __init__(self, cache_prefix: str | None = None) -> None: ...
    def get_callbacks(self, allow_host: bool, enable_categorical: bool) -> Tuple[Callable, Callable]:
        """Get callback functions for iterating in C."""
    @property
    def proxy(self) -> _ProxyDMatrix:
        """Handle of DMatrix proxy."""
    def reraise(self) -> None:
        """Reraise the exception thrown during iteration."""
    def __del__(self) -> None: ...
    @abstractmethod
    def reset(self) -> None:
        """Reset the data iterator.  Prototype for user defined function."""
    @abstractmethod
    def next(self, input_data: Callable) -> int:
        """Set the next batch of data.

        Parameters
        ----------

        input_data:
            A function with same data fields like `data`, `label` with
            `xgboost.DMatrix`.

        Returns
        -------
        0 if there's no more batch, otherwise 1.

        """

def require_keyword_args(error: bool) -> Callable[[Callable[..., _T]], Callable[..., _T]]:
    """Decorator for methods that issues warnings for positional arguments

    Using the keyword-only argument syntax in pep 3102, arguments after the
    * will issue a warning or error when passed as a positional argument.

    Modified from sklearn utils.validation.

    Parameters
    ----------
    error :
        Whether to throw an error or raise a warning.
    """

class DMatrix:
    """Data Matrix used in XGBoost.

    DMatrix is an internal data structure that is used by XGBoost,
    which is optimized for both memory efficiency and training speed.
    You can construct DMatrix from multiple different sources of data.
    """
    missing: Incomplete
    nthread: Incomplete
    silent: Incomplete
    handle: Incomplete
    def __init__(self, data: DataType, label: ArrayLike | None = None, *, weight: ArrayLike | None = None, base_margin: ArrayLike | None = None, missing: float | None = None, silent: bool = False, feature_names: FeatureNames | None = None, feature_types: FeatureTypes | None = None, nthread: int | None = None, group: ArrayLike | None = None, qid: ArrayLike | None = None, label_lower_bound: ArrayLike | None = None, label_upper_bound: ArrayLike | None = None, feature_weights: ArrayLike | None = None, enable_categorical: bool = False) -> None:
        '''Parameters
        ----------
        data : os.PathLike/string/numpy.array/scipy.sparse/pd.DataFrame/
               dt.Frame/cudf.DataFrame/cupy.array/dlpack/arrow.Table

            Data source of DMatrix.

            When data is string or os.PathLike type, it represents the path libsvm
            format txt file, csv file (by specifying uri parameter
            \'path_to_csv?format=csv\'), or binary file that xgboost can read from.

        label : array_like
            Label of the training data.
        weight : array_like
            Weight for each instance.

            .. note:: For ranking task, weights are per-group.

                In ranking task, one weight is assigned to each group (not each
                data point). This is because we only care about the relative
                ordering of data points within each group, so it doesn\'t make
                sense to assign weights to individual data points.

        base_margin: array_like
            Base margin used for boosting from existing model.
        missing : float, optional
            Value in the input data which needs to be present as a missing
            value. If None, defaults to np.nan.
        silent : boolean, optional
            Whether print messages during construction
        feature_names : list, optional
            Set names for features.
        feature_types : FeatureTypes

            Set types for features.  When `enable_categorical` is set to `True`, string
            "c" represents categorical data type while "q" represents numerical feature
            type. For categorical features, the input is assumed to be preprocessed and
            encoded by the users. The encoding can be done via
            :py:class:`sklearn.preprocessing.OrdinalEncoder` or pandas dataframe
            `.cat.codes` method. This is useful when users want to specify categorical
            features without having to construct a dataframe as input.

        nthread : integer, optional
            Number of threads to use for loading data when parallelization is
            applicable. If -1, uses maximum threads available on the system.
        group : array_like
            Group size for all ranking group.
        qid : array_like
            Query ID for data samples, used for ranking.
        label_lower_bound : array_like
            Lower bound for survival training.
        label_upper_bound : array_like
            Upper bound for survival training.
        feature_weights : array_like, optional
            Set feature weights for column sampling.
        enable_categorical: boolean, optional

            .. versionadded:: 1.3.0

            .. note:: This parameter is experimental

            Experimental support of specializing for categorical features.  Do not set
            to True unless you are interested in development. Also, JSON/UBJSON
            serialization format is required.

        '''
    def __del__(self) -> None: ...
    def set_info(self, *, label: ArrayLike | None = None, weight: ArrayLike | None = None, base_margin: ArrayLike | None = None, group: ArrayLike | None = None, qid: ArrayLike | None = None, label_lower_bound: ArrayLike | None = None, label_upper_bound: ArrayLike | None = None, feature_names: FeatureNames | None = None, feature_types: FeatureTypes | None = None, feature_weights: ArrayLike | None = None) -> None:
        """Set meta info for DMatrix.  See doc string for :py:obj:`xgboost.DMatrix`."""
    def get_float_info(self, field: str) -> np.ndarray:
        """Get float property from the DMatrix.

        Parameters
        ----------
        field: str
            The field name of the information

        Returns
        -------
        info : array
            a numpy array of float information of the data
        """
    def get_uint_info(self, field: str) -> np.ndarray:
        """Get unsigned integer property from the DMatrix.

        Parameters
        ----------
        field: str
            The field name of the information

        Returns
        -------
        info : array
            a numpy array of unsigned integer information of the data
        """
    def set_float_info(self, field: str, data: ArrayLike) -> None:
        """Set float type property into the DMatrix.

        Parameters
        ----------
        field: str
            The field name of the information

        data: numpy array
            The array of data to be set
        """
    def set_float_info_npy2d(self, field: str, data: ArrayLike) -> None:
        """Set float type property into the DMatrix
           for numpy 2d array input

        Parameters
        ----------
        field: str
            The field name of the information

        data: numpy array
            The array of data to be set
        """
    def set_uint_info(self, field: str, data: ArrayLike) -> None:
        """Set uint type property into the DMatrix.

        Parameters
        ----------
        field: str
            The field name of the information

        data: numpy array
            The array of data to be set
        """
    def save_binary(self, fname: str | os.PathLike, silent: bool = True) -> None:
        """Save DMatrix to an XGBoost buffer.  Saved binary can be later loaded
        by providing the path to :py:func:`xgboost.DMatrix` as input.

        Parameters
        ----------
        fname : string or os.PathLike
            Name of the output buffer file.
        silent : bool (optional; default: True)
            If set, the output is suppressed.
        """
    def set_label(self, label: ArrayLike) -> None:
        """Set label of dmatrix

        Parameters
        ----------
        label: array like
            The label information to be set into DMatrix
        """
    def set_weight(self, weight: ArrayLike) -> None:
        """Set weight of each instance.

        Parameters
        ----------
        weight : array like
            Weight for each data point

            .. note:: For ranking task, weights are per-group.

                In ranking task, one weight is assigned to each group (not each
                data point). This is because we only care about the relative
                ordering of data points within each group, so it doesn't make
                sense to assign weights to individual data points.

        """
    def set_base_margin(self, margin: ArrayLike) -> None:
        """Set base margin of booster to start from.

        This can be used to specify a prediction value of existing model to be
        base_margin However, remember margin is needed, instead of transformed
        prediction e.g. for logistic regression: need to put in value before
        logistic transformation see also example/demo.py

        Parameters
        ----------
        margin: array like
            Prediction margin of each datapoint

        """
    def set_group(self, group: ArrayLike) -> None:
        """Set group size of DMatrix (used for ranking).

        Parameters
        ----------
        group : array like
            Group size of each group
        """
    def get_label(self) -> np.ndarray:
        """Get the label of the DMatrix.

        Returns
        -------
        label : array
        """
    def get_weight(self) -> np.ndarray:
        """Get the weight of the DMatrix.

        Returns
        -------
        weight : array
        """
    def get_base_margin(self) -> np.ndarray:
        """Get the base margin of the DMatrix.

        Returns
        -------
        base_margin
        """
    def get_group(self) -> np.ndarray:
        """Get the group of the DMatrix.

        Returns
        -------
        group
        """
    def get_data(self) -> scipy.sparse.csr_matrix:
        """Get the predictors from DMatrix as a CSR matrix. This getter is mostly for
        testing purposes. If this is a quantized DMatrix then quantized values are
        returned instead of input values.

            .. versionadded:: 1.7.0

        """
    def num_row(self) -> int:
        """Get the number of rows in the DMatrix."""
    def num_col(self) -> int:
        """Get the number of columns (features) in the DMatrix."""
    def num_nonmissing(self) -> int:
        """Get the number of non-missing values in the DMatrix."""
    def slice(self, rindex: List[int] | np.ndarray, allow_groups: bool = False) -> DMatrix:
        """Slice the DMatrix and return a new DMatrix that only contains `rindex`.

        Parameters
        ----------
        rindex
            List of indices to be selected.
        allow_groups
            Allow slicing of a matrix with a groups attribute

        Returns
        -------
        res
            A new DMatrix containing only selected indices.
        """
    @property
    def feature_names(self) -> FeatureNames | None:
        """Get feature names (column labels).

        Returns
        -------
        feature_names : list or None
        """
    @feature_names.setter
    def feature_names(self, feature_names: FeatureNames | None) -> None:
        """Set feature names (column labels).

        Parameters
        ----------
        feature_names : list or None
            Labels for features. None will reset existing feature names
        """
    @property
    def feature_types(self) -> FeatureTypes | None:
        """Get feature types (column types).

        Returns
        -------
        feature_types : list or None
        """
    @feature_types.setter
    def feature_types(self, feature_types: List[str] | str | None) -> None:
        """Set feature types (column types).

        This is for displaying the results and categorical data support. See
        :py:class:`DMatrix` for details.

        Parameters
        ----------
        feature_types :
            Labels for features. None will reset existing feature names

        """

class _ProxyDMatrix(DMatrix):
    """A placeholder class when DMatrix cannot be constructed (QuantileDMatrix,
    inplace_predict).

    """
    handle: Incomplete
    def __init__(self) -> None: ...

class QuantileDMatrix(DMatrix):
    """A DMatrix variant that generates quantilized data directly from input for
    ``hist`` and ``gpu_hist`` tree methods. This DMatrix is primarily designed to save
    memory in training by avoiding intermediate storage. Set ``max_bin`` to control the
    number of bins during quantisation, which should be consistent with the training
    parameter ``max_bin``. When ``QuantileDMatrix`` is used for validation/test dataset,
    ``ref`` should be another ``QuantileDMatrix``(or ``DMatrix``, but not recommended as
    it defeats the purpose of saving memory) constructed from training dataset.  See
    :py:obj:`xgboost.DMatrix` for documents on meta info.

    .. note::

        Do not use ``QuantileDMatrix`` as validation/test dataset without supplying a
        reference (the training dataset) ``QuantileDMatrix`` using ``ref`` as some
        information may be lost in quantisation.

    .. versionadded:: 1.7.0

    Parameters
    ----------
    max_bin :
        The number of histogram bin, should be consistent with the training parameter
        ``max_bin``.

    ref :
        The training dataset that provides quantile information, needed when creating
        validation/test dataset with ``QuantileDMatrix``. Supplying the training DMatrix
        as a reference means that the same quantisation applied to the training data is
        applied to the validation/test data

    """
    max_bin: Incomplete
    missing: Incomplete
    nthread: Incomplete
    handle: Incomplete
    def __init__(self, data: DataType, label: ArrayLike | None = None, *, weight: ArrayLike | None = None, base_margin: ArrayLike | None = None, missing: float | None = None, silent: bool = False, feature_names: FeatureNames | None = None, feature_types: FeatureTypes | None = None, nthread: int | None = None, max_bin: int | None = None, ref: DMatrix | None = None, group: ArrayLike | None = None, qid: ArrayLike | None = None, label_lower_bound: ArrayLike | None = None, label_upper_bound: ArrayLike | None = None, feature_weights: ArrayLike | None = None, enable_categorical: bool = False) -> None: ...

class DeviceQuantileDMatrix(QuantileDMatrix):
    """ Use `QuantileDMatrix` instead.

    .. deprecated:: 1.7.0

    .. versionadded:: 1.1.0

    """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
Objective = Callable[[np.ndarray, DMatrix], Tuple[np.ndarray, np.ndarray]]
Metric = Callable[[np.ndarray, DMatrix], Tuple[str, float]]

class Booster:
    """A Booster of XGBoost.

    Booster is the model of xgboost, that contains low level routines for
    training, prediction and evaluation.
    """
    handle: Incomplete
    def __init__(self, params: BoosterParam | None = None, cache: Sequence[DMatrix] | None = None, model_file: Booster | bytearray | os.PathLike | str | None = None) -> None:
        """
        Parameters
        ----------
        params : dict
            Parameters for boosters.
        cache : list
            List of cache items.
        model_file : string/os.PathLike/Booster/bytearray
            Path to the model file if it's string or PathLike.
        """
    def __del__(self) -> None: ...
    def __getitem__(self, val: int | tuple | slice) -> Booster: ...
    def save_config(self) -> str:
        """Output internal parameter configuration of Booster as a JSON
        string.

        .. versionadded:: 1.0.0
        """
    def load_config(self, config: str) -> None:
        """Load configuration returned by `save_config`.

        .. versionadded:: 1.0.0
        """
    def __copy__(self) -> Booster: ...
    def __deepcopy__(self, _: Any) -> Booster:
        """Return a copy of booster."""
    def copy(self) -> Booster:
        """Copy the booster object.

        Returns
        -------
        booster: `Booster`
            a copied booster model
        """
    def attr(self, key: str) -> str | None:
        """Get attribute string from the Booster.

        Parameters
        ----------
        key : str
            The key to get attribute from.

        Returns
        -------
        value : str
            The attribute value of the key, returns None if attribute do not exist.
        """
    def attributes(self) -> Dict[str, str | None]:
        """Get attributes stored in the Booster as a dictionary.

        Returns
        -------
        result : dictionary of  attribute_name: attribute_value pairs of strings.
            Returns an empty dict if there's no attributes.
        """
    def set_attr(self, **kwargs: str | None) -> None:
        """Set the attribute of the Booster.

        Parameters
        ----------
        **kwargs
            The attributes to set. Setting a value to None deletes an attribute.
        """
    @property
    def feature_types(self) -> FeatureTypes | None:
        """Feature types for this booster.  Can be directly set by input data or by
        assignment.  See :py:class:`DMatrix` for details.

        """
    @feature_types.setter
    def feature_types(self, features: FeatureTypes | None) -> None: ...
    @property
    def feature_names(self) -> FeatureNames | None:
        """Feature names for this booster.  Can be directly set by input data or by
        assignment.

        """
    @feature_names.setter
    def feature_names(self, features: FeatureNames | None) -> None: ...
    def set_param(self, params: Dict | Iterable[Tuple[str, Any]] | str, value: str | None = None) -> None:
        """Set parameters into the Booster.

        Parameters
        ----------
        params: dict/list/str
           list of key,value pairs, dict of key to value or simply str key
        value: optional
           value of the specified parameter, when params is str key
        """
    def update(self, dtrain: DMatrix, iteration: int, fobj: Objective | None = None) -> None:
        """Update for one iteration, with objective function calculated
        internally.  This function should not be called directly by users.

        Parameters
        ----------
        dtrain : DMatrix
            Training data.
        iteration : int
            Current iteration number.
        fobj : function
            Customized objective function.

        """
    def boost(self, dtrain: DMatrix, grad: np.ndarray, hess: np.ndarray) -> None:
        """Boost the booster for one iteration, with customized gradient
        statistics.  Like :py:func:`xgboost.Booster.update`, this
        function should not be called directly by users.

        Parameters
        ----------
        dtrain :
            The training DMatrix.
        grad :
            The first order of gradient.
        hess :
            The second order of gradient.

        """
    def eval_set(self, evals: Sequence[Tuple[DMatrix, str]], iteration: int = 0, feval: Metric | None = None, output_margin: bool = True) -> str:
        """Evaluate a set of data.

        Parameters
        ----------
        evals :
            List of items to be evaluated.
        iteration :
            Current iteration.
        feval :
            Custom evaluation function.

        Returns
        -------
        result: str
            Evaluation result string.
        """
    def eval(self, data: DMatrix, name: str = 'eval', iteration: int = 0) -> str:
        """Evaluate the model on mat.

        Parameters
        ----------
        data :
            The dmatrix storing the input.

        name :
            The name of the dataset.

        iteration :
            The current iteration number.

        Returns
        -------
        result: str
            Evaluation result string.
        """
    def predict(self, data: DMatrix, output_margin: bool = False, ntree_limit: int = 0, pred_leaf: bool = False, pred_contribs: bool = False, approx_contribs: bool = False, pred_interactions: bool = False, validate_features: bool = True, training: bool = False, iteration_range: Tuple[int, int] = (0, 0), strict_shape: bool = False) -> np.ndarray:
        """Predict with data.  The full model will be used unless `iteration_range` is specified,
        meaning user have to either slice the model or use the ``best_iteration``
        attribute to get prediction from best model returned from early stopping.

        .. note::

            See :doc:`Prediction </prediction>` for issues like thread safety and a
            summary of outputs from this function.

        Parameters
        ----------
        data :
            The dmatrix storing the input.

        output_margin :
            Whether to output the raw untransformed margin value.

        ntree_limit :
            Deprecated, use `iteration_range` instead.

        pred_leaf :
            When this option is on, the output will be a matrix of (nsample,
            ntrees) with each record indicating the predicted leaf index of
            each sample in each tree.  Note that the leaf index of a tree is
            unique per tree, so you may find leaf 1 in both tree 1 and tree 0.

        pred_contribs :
            When this is True the output will be a matrix of size (nsample,
            nfeats + 1) with each record indicating the feature contributions
            (SHAP values) for that prediction. The sum of all feature
            contributions is equal to the raw untransformed margin value of the
            prediction. Note the final column is the bias term.

        approx_contribs :
            Approximate the contributions of each feature.  Used when ``pred_contribs`` or
            ``pred_interactions`` is set to True.  Changing the default of this parameter
            (False) is not recommended.

        pred_interactions :
            When this is True the output will be a matrix of size (nsample,
            nfeats + 1, nfeats + 1) indicating the SHAP interaction values for
            each pair of features. The sum of each row (or column) of the
            interaction values equals the corresponding SHAP value (from
            pred_contribs), and the sum of the entire matrix equals the raw
            untransformed margin value of the prediction. Note the last row and
            column correspond to the bias term.

        validate_features :
            When this is True, validate that the Booster's and data's
            feature_names are identical.  Otherwise, it is assumed that the
            feature_names are the same.

        training :
            Whether the prediction value is used for training.  This can effect `dart`
            booster, which performs dropouts during training iterations but use all trees
            for inference. If you want to obtain result with dropouts, set this parameter
            to `True`.  Also, the parameter is set to true when obtaining prediction for
            custom objective function.

            .. versionadded:: 1.0.0

        iteration_range :
            Specifies which layer of trees are used in prediction.  For example, if a
            random forest is trained with 100 rounds.  Specifying `iteration_range=(10,
            20)`, then only the forests built during [10, 20) (half open set) rounds are
            used in this prediction.

            .. versionadded:: 1.4.0

        strict_shape :
            When set to True, output shape is invariant to whether classification is used.
            For both value and margin prediction, the output shape is (n_samples,
            n_groups), n_groups == 1 when multi-class is not used.  Default to False, in
            which case the output shape can be (n_samples, ) if multi-class is not used.

            .. versionadded:: 1.4.0

        Returns
        -------
        prediction : numpy array

        """
    def inplace_predict(self, data: DataType, iteration_range: Tuple[int, int] = (0, 0), predict_type: str = 'value', missing: float = ..., validate_features: bool = True, base_margin: Any = None, strict_shape: bool = False) -> NumpyOrCupy:
        '''Run prediction in-place, Unlike :py:meth:`predict` method, inplace prediction
        does not cache the prediction result.

        Calling only ``inplace_predict`` in multiple threads is safe and lock
        free.  But the safety does not hold when used in conjunction with other
        methods. E.g. you can\'t train the booster in one thread and perform
        prediction in the other.

        .. code-block:: python

            booster.set_param({"predictor": "gpu_predictor"})
            booster.inplace_predict(cupy_array)

            booster.set_param({"predictor": "cpu_predictor"})
            booster.inplace_predict(numpy_array)

        .. versionadded:: 1.1.0

        Parameters
        ----------
        data : numpy.ndarray/scipy.sparse.csr_matrix/cupy.ndarray/
               cudf.DataFrame/pd.DataFrame
            The input data, must not be a view for numpy array.  Set
            ``predictor`` to ``gpu_predictor`` for running prediction on CuPy
            array or CuDF DataFrame.
        iteration_range :
            See :py:meth:`predict` for details.
        predict_type :
            * `value` Output model prediction values.
            * `margin` Output the raw untransformed margin value.
        missing :
            See :py:obj:`xgboost.DMatrix` for details.
        validate_features:
            See :py:meth:`xgboost.Booster.predict` for details.
        base_margin:
            See :py:obj:`xgboost.DMatrix` for details.

            .. versionadded:: 1.4.0

        strict_shape:
            See :py:meth:`xgboost.Booster.predict` for details.

            .. versionadded:: 1.4.0

        Returns
        -------
        prediction : numpy.ndarray/cupy.ndarray
            The prediction result.  When input data is on GPU, prediction
            result is stored in a cupy array.

        '''
    def save_model(self, fname: str | os.PathLike) -> None:
        '''Save the model to a file.

        The model is saved in an XGBoost internal format which is universal among the
        various XGBoost interfaces. Auxiliary attributes of the Python Booster object
        (such as feature_names) will not be saved when using binary format.  To save
        those attributes, use JSON/UBJ instead. See :doc:`Model IO
        </tutorials/saving_model>` for more info.

        .. code-block:: python

          model.save_model("model.json")
          # or
          model.save_model("model.ubj")

        Parameters
        ----------
        fname : string or os.PathLike
            Output file name

        '''
    def save_raw(self, raw_format: str = 'deprecated') -> bytearray:
        """Save the model to a in memory buffer representation instead of file.

        Parameters
        ----------
        raw_format :
            Format of output buffer. Can be `json`, `ubj` or `deprecated`.  Right now
            the default is `deprecated` but it will be changed to `ubj` (univeral binary
            json) in the future.

        Returns
        -------
        An in memory buffer representation of the model
        """
    best_iteration: Incomplete
    best_score: Incomplete
    best_ntree_limit: Incomplete
    def load_model(self, fname: str | bytearray | os.PathLike) -> None:
        '''Load the model from a file or bytearray. Path to file can be local
        or as an URI.

        The model is loaded from XGBoost format which is universal among the various
        XGBoost interfaces. Auxiliary attributes of the Python Booster object (such as
        feature_names) will not be loaded when using binary format.  To save those
        attributes, use JSON/UBJ instead.  See :doc:`Model IO </tutorials/saving_model>`
        for more info.

        .. code-block:: python

          model.load_model("model.json")
          # or
          model.load_model("model.ubj")

        Parameters
        ----------
        fname :
            Input file name or memory buffer(see also save_raw)

        '''
    def num_boosted_rounds(self) -> int:
        """Get number of boosted rounds.  For gblinear this is reset to 0 after
        serializing the model.

        """
    def num_features(self) -> int:
        """Number of features in booster."""
    def dump_model(self, fout: str | os.PathLike, fmap: str | os.PathLike = '', with_stats: bool = False, dump_format: str = 'text') -> None:
        """Dump model into a text or JSON file.  Unlike :py:meth:`save_model`, the
        output format is primarily used for visualization or interpretation,
        hence it's more human readable but cannot be loaded back to XGBoost.

        Parameters
        ----------
        fout : string or os.PathLike
            Output file name.
        fmap : string or os.PathLike, optional
            Name of the file containing feature map names.
        with_stats : bool, optional
            Controls whether the split statistics are output.
        dump_format : string, optional
            Format of model dump file. Can be 'text' or 'json'.
        """
    def get_dump(self, fmap: str | os.PathLike = '', with_stats: bool = False, dump_format: str = 'text') -> List[str]:
        """Returns the model dump as a list of strings.  Unlike :py:meth:`save_model`, the output
        format is primarily used for visualization or interpretation, hence it's more
        human readable but cannot be loaded back to XGBoost.

        Parameters
        ----------
        fmap :
            Name of the file containing feature map names.
        with_stats :
            Controls whether the split statistics are output.
        dump_format :
            Format of model dump. Can be 'text', 'json' or 'dot'.

        """
    def get_fscore(self, fmap: str | os.PathLike = '') -> Dict[str, float | List[float]]:
        """Get feature importance of each feature.

        .. note:: Zero-importance features will not be included

           Keep in mind that this function does not include zero-importance feature, i.e.
           those features that have not been used in any split conditions.

        Parameters
        ----------
        fmap :
           The name of feature map file
        """
    def get_score(self, fmap: str | os.PathLike = '', importance_type: str = 'weight') -> Dict[str, float | List[float]]:
        '''Get feature importance of each feature.
        For tree model Importance type can be defined as:

        * \'weight\': the number of times a feature is used to split the data across all trees.
        * \'gain\': the average gain across all splits the feature is used in.
        * \'cover\': the average coverage across all splits the feature is used in.
        * \'total_gain\': the total gain across all splits the feature is used in.
        * \'total_cover\': the total coverage across all splits the feature is used in.

        .. note::

           For linear model, only "weight" is defined and it\'s the normalized coefficients
           without bias.

        .. note:: Zero-importance features will not be included

           Keep in mind that this function does not include zero-importance feature, i.e.
           those features that have not been used in any split conditions.

        Parameters
        ----------
        fmap:
           The name of feature map file.
        importance_type:
            One of the importance types defined above.

        Returns
        -------
        A map between feature names and their scores.  When `gblinear` is used for
        multi-class classification the scores for each feature is a list with length
        `n_classes`, otherwise they\'re scalars.
        '''
    def trees_to_dataframe(self, fmap: str | os.PathLike = '') -> DataFrame:
        """Parse a boosted tree model text dump into a pandas DataFrame structure.

        This feature is only defined when the decision tree model is chosen as base
        learner (`booster in {gbtree, dart}`). It is not defined for other base learner
        types, such as linear learners (`booster=gblinear`).

        Parameters
        ----------
        fmap: str or os.PathLike (optional)
           The name of feature map file.
        """
    def get_split_value_histogram(self, feature: str, fmap: os.PathLike | str = '', bins: int | None = None, as_pandas: bool = True) -> np.ndarray | DataFrame:
        """Get split value histogram of a feature

        Parameters
        ----------
        feature: str
            The name of the feature.
        fmap: str or os.PathLike (optional)
            The name of feature map file.
        bin: int, default None
            The maximum number of bins.
            Number of bins equals number of unique split values n_unique,
            if bins == None or bins > n_unique.
        as_pandas: bool, default True
            Return pd.DataFrame when pandas is installed.
            If False or pandas is not installed, return numpy ndarray.

        Returns
        -------
        a histogram of used splitting values for the specified feature
        either as numpy array or pandas DataFrame.
        """
