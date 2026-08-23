from _typeshed import Incomplete
from flaml import tune as tune
from flaml.automl.data import add_time_idx_col as add_time_idx_col
from flaml.automl.time_series.ts_data import TimeSeriesDataset as TimeSeriesDataset
from flaml.automl.time_series.ts_model import TimeSeriesEstimator as TimeSeriesEstimator
from pandas import to_datetime as to_datetime

class PD: ...

class TemporalFusionTransformerEstimator(TimeSeriesEstimator):
    """The class for tuning Temporal Fusion Transformer"""
    @classmethod
    def search_space(cls, data, task, pred_horizon, **params): ...
    data: Incomplete
    max_encoder_length: Incomplete
    group_ids: Incomplete
    def transform_ds(self, X_train: TimeSeriesDataset, y_train, **kwargs): ...
    def fit(self, X_train, y_train, budget: Incomplete | None = None, **kwargs): ...
    def predict(self, X): ...
