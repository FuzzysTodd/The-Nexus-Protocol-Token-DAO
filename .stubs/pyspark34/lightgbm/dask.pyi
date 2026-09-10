import numpy as np
from .compat import Client, dask_Array
from .sklearn import LGBMClassifier, LGBMRanker, LGBMRegressor, _LGBM_ScikitCustomObjectiveFunction, _LGBM_ScikitEvalMetricType
from _typeshed import Incomplete
from enum import Enum
from typing import Any, List, Tuple

__all__ = ['DaskLGBMClassifier', 'DaskLGBMRanker', 'DaskLGBMRegressor']

class _RemoteSocket:
    socket: Incomplete
    def acquire(self) -> int: ...
    def release(self) -> None: ...

class _DatasetNames(Enum):
    """Placeholder names used by lightgbm.dask internals to say 'also evaluate the training data'.

    Avoid duplicating the training data when the validation set refers to elements of training data.
    """
    TRAINSET: Incomplete
    SAMPLE_WEIGHT: Incomplete
    INIT_SCORE: Incomplete
    GROUP: Incomplete

class _DaskLGBMModel:
    @property
    def client_(self) -> Client:
        """:obj:`dask.distributed.Client`: Dask client.

        This property can be passed in the constructor or updated
        with ``model.set_params(client=client)``.
        """

class DaskLGBMClassifier(LGBMClassifier, _DaskLGBMModel):
    """Distributed version of lightgbm.LGBMClassifier."""
    client: Incomplete
    def __init__(self, boosting_type: str = 'gbdt', num_leaves: int = 31, max_depth: int = -1, learning_rate: float = 0.1, n_estimators: int = 100, subsample_for_bin: int = 200000, objective: str | _LGBM_ScikitCustomObjectiveFunction | None = None, class_weight: dict | str | None = None, min_split_gain: float = 0.0, min_child_weight: float = 0.001, min_child_samples: int = 20, subsample: float = 1.0, subsample_freq: int = 0, colsample_bytree: float = 1.0, reg_alpha: float = 0.0, reg_lambda: float = 0.0, random_state: int | np.random.RandomState | None = None, n_jobs: int | None = None, importance_type: str = 'split', client: Client | None = None, **kwargs: Any) -> None:
        """Docstring is inherited from the lightgbm.LGBMClassifier.__init__."""
    def fit(self, X: _DaskMatrixLike, y: _DaskCollection, sample_weight: _DaskVectorLike | None = None, init_score: _DaskCollection | None = None, eval_set: List[Tuple[_DaskMatrixLike, _DaskCollection]] | None = None, eval_names: List[str] | None = None, eval_sample_weight: List[_DaskVectorLike] | None = None, eval_class_weight: List[dict | str] | None = None, eval_init_score: List[_DaskCollection] | None = None, eval_metric: _LGBM_ScikitEvalMetricType | None = None, **kwargs: Any) -> DaskLGBMClassifier:
        """Docstring is inherited from the lightgbm.LGBMClassifier.fit."""
    def predict(self, X: _DaskMatrixLike, raw_score: bool = False, start_iteration: int = 0, num_iteration: int | None = None, pred_leaf: bool = False, pred_contrib: bool = False, validate_features: bool = False, **kwargs: Any) -> dask_Array:
        """Docstring is inherited from the lightgbm.LGBMClassifier.predict."""
    def predict_proba(self, X: _DaskMatrixLike, raw_score: bool = False, start_iteration: int = 0, num_iteration: int | None = None, pred_leaf: bool = False, pred_contrib: bool = False, validate_features: bool = False, **kwargs: Any) -> dask_Array:
        """Docstring is inherited from the lightgbm.LGBMClassifier.predict_proba."""
    def to_local(self) -> LGBMClassifier:
        """Create regular version of lightgbm.LGBMClassifier from the distributed version.

        Returns
        -------
        model : lightgbm.LGBMClassifier
            Local underlying model.
        """

class DaskLGBMRegressor(LGBMRegressor, _DaskLGBMModel):
    """Distributed version of lightgbm.LGBMRegressor."""
    client: Incomplete
    def __init__(self, boosting_type: str = 'gbdt', num_leaves: int = 31, max_depth: int = -1, learning_rate: float = 0.1, n_estimators: int = 100, subsample_for_bin: int = 200000, objective: str | _LGBM_ScikitCustomObjectiveFunction | None = None, class_weight: dict | str | None = None, min_split_gain: float = 0.0, min_child_weight: float = 0.001, min_child_samples: int = 20, subsample: float = 1.0, subsample_freq: int = 0, colsample_bytree: float = 1.0, reg_alpha: float = 0.0, reg_lambda: float = 0.0, random_state: int | np.random.RandomState | None = None, n_jobs: int | None = None, importance_type: str = 'split', client: Client | None = None, **kwargs: Any) -> None:
        """Docstring is inherited from the lightgbm.LGBMRegressor.__init__."""
    def fit(self, X: _DaskMatrixLike, y: _DaskCollection, sample_weight: _DaskVectorLike | None = None, init_score: _DaskVectorLike | None = None, eval_set: List[Tuple[_DaskMatrixLike, _DaskCollection]] | None = None, eval_names: List[str] | None = None, eval_sample_weight: List[_DaskVectorLike] | None = None, eval_init_score: List[_DaskVectorLike] | None = None, eval_metric: _LGBM_ScikitEvalMetricType | None = None, **kwargs: Any) -> DaskLGBMRegressor:
        """Docstring is inherited from the lightgbm.LGBMRegressor.fit."""
    def predict(self, X: _DaskMatrixLike, raw_score: bool = False, start_iteration: int = 0, num_iteration: int | None = None, pred_leaf: bool = False, pred_contrib: bool = False, validate_features: bool = False, **kwargs: Any) -> dask_Array:
        """Docstring is inherited from the lightgbm.LGBMRegressor.predict."""
    def to_local(self) -> LGBMRegressor:
        """Create regular version of lightgbm.LGBMRegressor from the distributed version.

        Returns
        -------
        model : lightgbm.LGBMRegressor
            Local underlying model.
        """

class DaskLGBMRanker(LGBMRanker, _DaskLGBMModel):
    """Distributed version of lightgbm.LGBMRanker."""
    client: Incomplete
    def __init__(self, boosting_type: str = 'gbdt', num_leaves: int = 31, max_depth: int = -1, learning_rate: float = 0.1, n_estimators: int = 100, subsample_for_bin: int = 200000, objective: str | _LGBM_ScikitCustomObjectiveFunction | None = None, class_weight: dict | str | None = None, min_split_gain: float = 0.0, min_child_weight: float = 0.001, min_child_samples: int = 20, subsample: float = 1.0, subsample_freq: int = 0, colsample_bytree: float = 1.0, reg_alpha: float = 0.0, reg_lambda: float = 0.0, random_state: int | np.random.RandomState | None = None, n_jobs: int | None = None, importance_type: str = 'split', client: Client | None = None, **kwargs: Any) -> None:
        """Docstring is inherited from the lightgbm.LGBMRanker.__init__."""
    def fit(self, X: _DaskMatrixLike, y: _DaskCollection, sample_weight: _DaskVectorLike | None = None, init_score: _DaskVectorLike | None = None, group: _DaskVectorLike | None = None, eval_set: List[Tuple[_DaskMatrixLike, _DaskCollection]] | None = None, eval_names: List[str] | None = None, eval_sample_weight: List[_DaskVectorLike] | None = None, eval_init_score: List[_DaskVectorLike] | None = None, eval_group: List[_DaskVectorLike] | None = None, eval_metric: _LGBM_ScikitEvalMetricType | None = None, eval_at: List[int] | Tuple[int, ...] = (1, 2, 3, 4, 5), **kwargs: Any) -> DaskLGBMRanker:
        """Docstring is inherited from the lightgbm.LGBMRanker.fit."""
    def predict(self, X: _DaskMatrixLike, raw_score: bool = False, start_iteration: int = 0, num_iteration: int | None = None, pred_leaf: bool = False, pred_contrib: bool = False, validate_features: bool = False, **kwargs: Any) -> dask_Array:
        """Docstring is inherited from the lightgbm.LGBMRanker.predict."""
    def to_local(self) -> LGBMRanker:
        """Create regular version of lightgbm.LGBMRanker from the distributed version.

        Returns
        -------
        model : lightgbm.LGBMRanker
            Local underlying model.
        """
