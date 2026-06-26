import distributed
from . import collective
from ._typing import FeatureNames, FeatureTypes
from .callback import TrainingCallback
from .core import Booster, DMatrix, DataIter, Metric, Objective
from .sklearn import XGBClassifierBase, XGBModel, XGBRankerMixIn, XGBRegressorBase
from _typeshed import Incomplete
from typing import Any, Awaitable, Callable, Dict, Generator, List, Sequence, Tuple
from typing_extensions import TypedDict

__all__ = ['CommunicatorContext', 'DaskDMatrix', 'DaskDeviceQuantileDMatrix', 'DaskXGBRegressor', 'DaskXGBClassifier', 'DaskXGBRanker', 'DaskXGBRFRegressor', 'DaskXGBRFClassifier', 'train', 'predict', 'inplace_predict']

class TrainReturnT(TypedDict):
    booster: Booster
    history: Dict

class CommunicatorContext(collective.CommunicatorContext):
    """A context controlling collective communicator initialization and finalization."""
    def __init__(self, **args: Any) -> None: ...

class DaskDMatrix:
    """DMatrix holding on references to Dask DataFrame or Dask Array.  Constructing a
    `DaskDMatrix` forces all lazy computation to be carried out.  Wait for the input
    data explicitly if you want to see actual computation of constructing `DaskDMatrix`.

    See doc for :py:obj:`xgboost.DMatrix` constructor for other parameters.  DaskDMatrix
    accepts only dask collection.

    .. note::

        DaskDMatrix does not repartition or move data between workers.  It's
        the caller's responsibility to balance the data.

    .. versionadded:: 1.0.0

    Parameters
    ----------
    client :
        Specify the dask client used for training.  Use default client returned from
        dask if it's set to None.

    """
    feature_names: Incomplete
    feature_types: Incomplete
    missing: Incomplete
    enable_categorical: Incomplete
    worker_map: Incomplete
    is_quantile: bool
    def __init__(self, client: distributed.Client, data: _DataT, label: _DaskCollection | None = None, *, weight: _DaskCollection | None = None, base_margin: _DaskCollection | None = None, missing: float = None, silent: bool = False, feature_names: FeatureNames | None = None, feature_types: FeatureTypes = None, group: _DaskCollection | None = None, qid: _DaskCollection | None = None, label_lower_bound: _DaskCollection | None = None, label_upper_bound: _DaskCollection | None = None, feature_weights: _DaskCollection | None = None, enable_categorical: bool = False) -> None: ...
    def __await__(self) -> Generator: ...
    def num_col(self) -> int:
        """Get the number of columns (features) in the DMatrix.

        Returns
        -------
        number of columns
        """

class DaskPartitionIter(DataIter):
    """A data iterator for `DaskDeviceQuantileDMatrix`."""
    def __init__(self, data: List[Any], label: List[Any] | None = None, weight: List[Any] | None = None, base_margin: List[Any] | None = None, qid: List[Any] | None = None, label_lower_bound: List[Any] | None = None, label_upper_bound: List[Any] | None = None, feature_names: FeatureNames | None = None, feature_types: Any | List[Any] | None = None, feature_weights: Any | None = None) -> None: ...
    def data(self) -> Any:
        """Utility function for obtaining current batch of data."""
    def reset(self) -> None:
        """Reset the iterator"""
    def next(self, input_data: Callable) -> int:
        """Yield next batch of data"""

class DaskQuantileDMatrix(DaskDMatrix):
    max_bin: Incomplete
    is_quantile: bool
    def __init__(self, client: distributed.Client, data: _DataT, label: _DaskCollection | None = None, *, weight: _DaskCollection | None = None, base_margin: _DaskCollection | None = None, missing: float = None, silent: bool = False, feature_names: FeatureNames | None = None, feature_types: Any | List[Any] | None = None, max_bin: int | None = None, ref: DMatrix | None = None, group: _DaskCollection | None = None, qid: _DaskCollection | None = None, label_lower_bound: _DaskCollection | None = None, label_upper_bound: _DaskCollection | None = None, feature_weights: _DaskCollection | None = None, enable_categorical: bool = False) -> None: ...

class DaskDeviceQuantileDMatrix(DaskQuantileDMatrix):
    """Use `DaskQuantileDMatrix` instead.

    .. deprecated:: 1.7.0

    .. versionadded:: 1.2.0

    """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

def train(client: distributed.Client, params: Dict[str, Any], dtrain: DaskDMatrix, num_boost_round: int = 10, *, evals: Sequence[Tuple[DaskDMatrix, str]] | None = None, obj: Objective | None = None, feval: Metric | None = None, early_stopping_rounds: int | None = None, xgb_model: Booster | None = None, verbose_eval: int | bool = True, callbacks: Sequence[TrainingCallback] | None = None, custom_metric: Metric | None = None) -> Any:
    """Train XGBoost model.

    .. versionadded:: 1.0.0

    .. note::

        Other parameters are the same as :py:func:`xgboost.train` except for
        `evals_result`, which is returned as part of function return value instead of
        argument.

    Parameters
    ----------
    client :
        Specify the dask client used for training.  Use default client returned from
        dask if it's set to None.

    Returns
    -------
    results: dict
        A dictionary containing trained booster and evaluation history.  `history` field
        is the same as `eval_result` from `xgboost.train`.

        .. code-block:: python

            {'booster': xgboost.Booster,
             'history': {'train': {'logloss': ['0.48253', '0.35953']},
                         'eval': {'logloss': ['0.480385', '0.357756']}}}

    """
def predict(client: distributed.Client | None, model: TrainReturnT | Booster | distributed.Future, data: DaskDMatrix | _DataT, output_margin: bool = False, missing: float = ..., pred_leaf: bool = False, pred_contribs: bool = False, approx_contribs: bool = False, pred_interactions: bool = False, validate_features: bool = True, iteration_range: Tuple[int, int] = (0, 0), strict_shape: bool = False) -> Any:
    """Run prediction with a trained booster.

    .. note::

        Using ``inplace_predict`` might be faster when some features are not needed.
        See :py:meth:`xgboost.Booster.predict` for details on various parameters.  When
        output has more than 2 dimensions (shap value, leaf with strict_shape), input
        should be ``da.Array`` or ``DaskDMatrix``.

    .. versionadded:: 1.0.0

    Parameters
    ----------
    client:
        Specify the dask client used for training.  Use default client
        returned from dask if it's set to None.
    model:
        The trained model.  It can be a distributed.Future so user can
        pre-scatter it onto all workers.
    data:
        Input data used for prediction.  When input is a dataframe object,
        prediction output is a series.
    missing:
        Used when input data is not DaskDMatrix.  Specify the value
        considered as missing.

    Returns
    -------
    prediction: dask.array.Array/dask.dataframe.Series
        When input data is ``dask.array.Array`` or ``DaskDMatrix``, the return value is
        an array, when input data is ``dask.dataframe.DataFrame``, return value can be
        ``dask.dataframe.Series``, ``dask.dataframe.DataFrame``, depending on the output
        shape.

    """
def inplace_predict(client: distributed.Client | None, model: TrainReturnT | Booster | distributed.Future, data: _DataT, iteration_range: Tuple[int, int] = (0, 0), predict_type: str = 'value', missing: float = ..., validate_features: bool = True, base_margin: _DaskCollection | None = None, strict_shape: bool = False) -> Any:
    """Inplace prediction. See doc in :py:meth:`xgboost.Booster.inplace_predict` for
    details.

    .. versionadded:: 1.1.0

    Parameters
    ----------
    client:
        Specify the dask client used for training.  Use default client
        returned from dask if it's set to None.
    model:
        See :py:func:`xgboost.dask.predict` for details.
    data :
        dask collection.
    iteration_range:
        See :py:meth:`xgboost.Booster.predict` for details.
    predict_type:
        See :py:meth:`xgboost.Booster.inplace_predict` for details.
    missing:
        Value in the input data which needs to be present as a missing
        value. If None, defaults to np.nan.
    base_margin:
        See :py:obj:`xgboost.DMatrix` for details.

        .. versionadded:: 1.4.0

    strict_shape:
        See :py:meth:`xgboost.Booster.predict` for details.

        .. versionadded:: 1.4.0

    Returns
    -------
    prediction :
        When input data is ``dask.array.Array``, the return value is an array, when
        input data is ``dask.dataframe.DataFrame``, return value can be
        ``dask.dataframe.Series``, ``dask.dataframe.DataFrame``, depending on the output
        shape.

    """

class DaskScikitLearnBase(XGBModel):
    """Base class for implementing scikit-learn interface with Dask"""
    def predict(self, X: _DataT, output_margin: bool = False, ntree_limit: int | None = None, validate_features: bool = True, base_margin: _DaskCollection | None = None, iteration_range: Tuple[int, int] | None = None) -> Any: ...
    def apply(self, X: _DataT, ntree_limit: int | None = None, iteration_range: Tuple[int, int] | None = None) -> Any: ...
    def __await__(self) -> Awaitable[Any]: ...
    @property
    def client(self) -> distributed.Client:
        """The dask client used in this model.  The `Client` object can not be serialized for
        transmission, so if task is launched from a worker instead of directly from the
        client process, this attribute needs to be set at that worker.

        """
    @client.setter
    def client(self, clt: distributed.Client) -> None: ...

class DaskXGBRegressor(DaskScikitLearnBase, XGBRegressorBase):
    """dummy doc string to workaround pylint, replaced by the decorator."""
    def fit(self, X: _DataT, y: _DaskCollection, *, sample_weight: _DaskCollection | None = None, base_margin: _DaskCollection | None = None, eval_set: Sequence[Tuple[_DaskCollection, _DaskCollection]] | None = None, eval_metric: str | Sequence[str] | Callable | None = None, early_stopping_rounds: int | None = None, verbose: int | bool = True, xgb_model: Booster | XGBModel | None = None, sample_weight_eval_set: Sequence[_DaskCollection] | None = None, base_margin_eval_set: Sequence[_DaskCollection] | None = None, feature_weights: _DaskCollection | None = None, callbacks: Sequence[TrainingCallback] | None = None) -> DaskXGBRegressor: ...

class DaskXGBClassifier(DaskScikitLearnBase, XGBClassifierBase):
    def fit(self, X: _DataT, y: _DaskCollection, *, sample_weight: _DaskCollection | None = None, base_margin: _DaskCollection | None = None, eval_set: Sequence[Tuple[_DaskCollection, _DaskCollection]] | None = None, eval_metric: str | Sequence[str] | Callable | None = None, early_stopping_rounds: int | None = None, verbose: int | bool = True, xgb_model: Booster | XGBModel | None = None, sample_weight_eval_set: Sequence[_DaskCollection] | None = None, base_margin_eval_set: Sequence[_DaskCollection] | None = None, feature_weights: _DaskCollection | None = None, callbacks: Sequence[TrainingCallback] | None = None) -> DaskXGBClassifier: ...
    def predict_proba(self, X: _DaskCollection, ntree_limit: int | None = None, validate_features: bool = True, base_margin: _DaskCollection | None = None, iteration_range: Tuple[int, int] | None = None) -> Any: ...

class DaskXGBRanker(DaskScikitLearnBase, XGBRankerMixIn):
    def __init__(self, *, objective: str = 'rank:pairwise', **kwargs: Any) -> None: ...
    def fit(self, X: _DataT, y: _DaskCollection, *, group: _DaskCollection | None = None, qid: _DaskCollection | None = None, sample_weight: _DaskCollection | None = None, base_margin: _DaskCollection | None = None, eval_set: Sequence[Tuple[_DaskCollection, _DaskCollection]] | None = None, eval_group: Sequence[_DaskCollection] | None = None, eval_qid: Sequence[_DaskCollection] | None = None, eval_metric: str | Sequence[str] | Callable | None = None, early_stopping_rounds: int = None, verbose: int | bool = False, xgb_model: XGBModel | Booster | None = None, sample_weight_eval_set: Sequence[_DaskCollection] | None = None, base_margin_eval_set: Sequence[_DaskCollection] | None = None, feature_weights: _DaskCollection | None = None, callbacks: Sequence[TrainingCallback] | None = None) -> DaskXGBRanker: ...

class DaskXGBRFRegressor(DaskXGBRegressor):
    def __init__(self, *, learning_rate: float | None = 1, subsample: float | None = 0.8, colsample_bynode: float | None = 0.8, reg_lambda: float | None = 1e-05, **kwargs: Any) -> None: ...
    def get_xgb_params(self) -> Dict[str, Any]: ...
    def get_num_boosting_rounds(self) -> int: ...
    def fit(self, X: _DataT, y: _DaskCollection, *, sample_weight: _DaskCollection | None = None, base_margin: _DaskCollection | None = None, eval_set: Sequence[Tuple[_DaskCollection, _DaskCollection]] | None = None, eval_metric: str | Sequence[str] | Callable | None = None, early_stopping_rounds: int | None = None, verbose: int | bool = True, xgb_model: Booster | XGBModel | None = None, sample_weight_eval_set: Sequence[_DaskCollection] | None = None, base_margin_eval_set: Sequence[_DaskCollection] | None = None, feature_weights: _DaskCollection | None = None, callbacks: Sequence[TrainingCallback] | None = None) -> DaskXGBRFRegressor: ...

class DaskXGBRFClassifier(DaskXGBClassifier):
    def __init__(self, *, learning_rate: float | None = 1, subsample: float | None = 0.8, colsample_bynode: float | None = 0.8, reg_lambda: float | None = 1e-05, **kwargs: Any) -> None: ...
    def get_xgb_params(self) -> Dict[str, Any]: ...
    def get_num_boosting_rounds(self) -> int: ...
    def fit(self, X: _DataT, y: _DaskCollection, *, sample_weight: _DaskCollection | None = None, base_margin: _DaskCollection | None = None, eval_set: Sequence[Tuple[_DaskCollection, _DaskCollection]] | None = None, eval_metric: str | Sequence[str] | Callable | None = None, early_stopping_rounds: int | None = None, verbose: int | bool = True, xgb_model: Booster | XGBModel | None = None, sample_weight_eval_set: Sequence[_DaskCollection] | None = None, base_margin_eval_set: Sequence[_DaskCollection] | None = None, feature_weights: _DaskCollection | None = None, callbacks: Sequence[TrainingCallback] | None = None) -> DaskXGBRFClassifier: ...
