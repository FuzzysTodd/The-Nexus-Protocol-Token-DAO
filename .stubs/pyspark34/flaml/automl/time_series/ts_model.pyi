import pandas as pd
from _typeshed import Incomplete
from flaml import tune as tune
from flaml.automl.data import TS_TIMESTAMP_COL as TS_TIMESTAMP_COL, TS_VALUE_COL as TS_VALUE_COL
from flaml.automl.model import CatBoostEstimator as CatBoostEstimator, ExtraTreesEstimator as ExtraTreesEstimator, LGBMEstimator as LGBMEstimator, LassoLarsEstimator as LassoLarsEstimator, RandomForestEstimator as RandomForestEstimator, SKLearnEstimator as SKLearnEstimator, XGBoostLimitDepthEstimator as XGBoostLimitDepthEstimator, XGBoostSklearnEstimator as XGBoostSklearnEstimator, logger as logger, suppress_stdout_stderr as suppress_stdout_stderr
from flaml.automl.task import Task as Task
from flaml.automl.time_series.ts_data import TimeSeriesDataset as TimeSeriesDataset, create_forward_frame as create_forward_frame, enrich_dataframe as enrich_dataframe, enrich_dataset as enrich_dataset, normalize_ts_data as normalize_ts_data
from pandas import DataFrame, Series

class PD: ...

class TimeSeriesEstimator(SKLearnEstimator):
    time_col: Incomplete
    target_names: Incomplete
    frequency: Incomplete
    end_date: Incomplete
    regressors: Incomplete
    def __init__(self, task: str = 'ts_forecast', n_jobs: int = 1, **params) -> None: ...
    def enrich(self, X: int | TimeSeriesDataset | DataFrame, remove_constants: bool = False): ...
    @classmethod
    def search_space(cls, data: TimeSeriesDataset, task: Task, pred_horizon: int): ...
    @staticmethod
    def adjust_scale(scale: int, data_len: int, pred_horizon: int): ...
    @classmethod
    def top_search_space(cls): ...
    @classmethod
    def top_level_params(cls): ...
    X_train: Incomplete
    def fit(self, X_train: TimeSeriesDataset, y_train: Incomplete | None = None, budget: Incomplete | None = None, **kwargs): ...
    def score(self, X_val: DataFrame, y_val: Series, **kwargs): ...

class Orbit(TimeSeriesEstimator):
    logger: Incomplete
    def fit(self, X_train: TimeSeriesDataset, y_train: Incomplete | None = None, budget: Incomplete | None = None, **kwargs): ...
    def predict(self, X: TimeSeriesDataset | DataFrame, **kwargs): ...

class Prophet(TimeSeriesEstimator):
    """The class for tuning Prophet."""
    def fit(self, X_train, y_train: Incomplete | None = None, budget: Incomplete | None = None, **kwargs): ...
    def predict(self, X, **kwargs): ...

class StatsModelsEstimator(TimeSeriesEstimator):
    def predict(self, X, **kwargs) -> pd.Series: ...

class ARIMA(StatsModelsEstimator):
    """The class for tuning ARIMA."""
    def __init__(self, **kwargs) -> None: ...
    regressors: Incomplete
    time_col: Incomplete
    target_names: Incomplete
    def fit(self, X_train, y_train: Incomplete | None = None, budget: Incomplete | None = None, **kwargs): ...

class SARIMAX(StatsModelsEstimator):
    """The class for tuning SARIMA."""
    regressors: Incomplete
    def fit(self, X_train, y_train: Incomplete | None = None, budget: Incomplete | None = None, **kwargs): ...

class HoltWinters(StatsModelsEstimator):
    """
    The class for tuning Holt Winters model, aka 'Triple Exponential Smoothing'.
    """
    regressors: Incomplete
    def fit(self, X_train, y_train, budget: Incomplete | None = None, free_mem_ratio: int = 0, **kwargs): ...

class SimpleForecaster(StatsModelsEstimator):
    """Base class for Naive Forecaster like Seasonal Naive, Naive, Seasonal Average, Average"""
    regressors: Incomplete
    time_col: Incomplete
    target_names: Incomplete
    def joint_preprocess(self, X_train, y_train: Incomplete | None = None): ...
    season: Incomplete
    def fit(self, X_train, y_train: Incomplete | None = None, budget: Incomplete | None = None, **kwargs): ...

class SeasonalNaive(SimpleForecaster):
    smoothing_level: float
    def predict(self, X, **kwargs): ...

class Naive(SimpleForecaster):
    smoothing_level: float
    def predict(self, X, **kwargs): ...

class SeasonalAverage(SimpleForecaster):
    season: Incomplete
    def fit(self, X_train, y_train: Incomplete | None = None, budget: Incomplete | None = None, **kwargs): ...

class Average(SimpleForecaster):
    def fit(self, X_train, y_train: Incomplete | None = None, budget: Incomplete | None = None, **kwargs): ...

class TS_SKLearn(TimeSeriesEstimator):
    """The class for tuning SKLearn Regressors for time-series forecasting"""
    base_class = SKLearnEstimator
    ts_task: Incomplete
    def __init__(self, task: str = 'ts_forecast', **params) -> None: ...
    regressors: Incomplete
    time_col: Incomplete
    target_names: Incomplete
    def fit(self, X_train, y_train: Incomplete | None = None, budget: Incomplete | None = None, **kwargs): ...
    def predict(self, X, **kwargs): ...

class LGBM_TS(TS_SKLearn):
    """The class for tuning LGBM Regressor for time-series forecasting"""
    base_class = LGBMEstimator

class XGBoost_TS(TS_SKLearn):
    """The class for tuning XGBoost Regressor for time-series forecasting"""
    base_class = XGBoostSklearnEstimator

class RF_TS(TS_SKLearn):
    """The class for tuning Random Forest Regressor for time-series forecasting"""
    base_class = RandomForestEstimator

class ExtraTrees_TS(TS_SKLearn):
    """The class for tuning Extra Trees Regressor for time-series forecasting"""
    base_class = ExtraTreesEstimator

class XGBoostLimitDepth_TS(TS_SKLearn):
    """The class for tuning XGBoost Regressor with unlimited depth for time-series forecasting"""
    base_class = XGBoostLimitDepthEstimator

class CatBoost_TS(TS_SKLearn):
    base_class = CatBoostEstimator

class LassoLars_TS(TS_SKLearn):
    base_class = LassoLarsEstimator
