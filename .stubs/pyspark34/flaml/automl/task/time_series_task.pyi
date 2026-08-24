from _typeshed import Incomplete
from flaml.automl.ml import default_cv_score_agg_func as default_cv_score_agg_func, get_val_loss as get_val_loss
from flaml.automl.task.task import TS_FORECAST as TS_FORECAST, TS_FORECASTPANEL as TS_FORECASTPANEL, Task as Task, get_classification_objective as get_classification_objective
from flaml.automl.time_series.ts_data import DataTransformerTS as DataTransformerTS, TimeSeriesDataset as TimeSeriesDataset, normalize_ts_data as normalize_ts_data
from typing import List

logger: Incomplete

class TimeSeriesTask(Task):
    @property
    def estimators(self): ...
    time_col: Incomplete
    target_names: Incomplete
    def validate_data(self, automl, state, X_train_all, y_train_all, dataframe, label, X_val: Incomplete | None = None, y_val: Incomplete | None = None, groups_val: Incomplete | None = None, groups: Incomplete | None = None) -> None: ...
    def prepare_data(self, state, X_train_all, y_train_all, auto_argument, eval_method, split_type, split_ratio, n_splits, data_is_df, sample_weight_full, time_col: Incomplete | None = None): ...
    name: Incomplete
    def decide_split_type(self, split_type, y_train_all, fit_kwargs, groups: Incomplete | None = None) -> str: ...
    def preprocess(self, X, transformer: Incomplete | None = None): ...
    def evaluate_model_CV(self, config, estimator, X_train_all, y_train_all, budget, kf, eval_metric, best_val_loss, cv_score_agg_func: Incomplete | None = None, log_training_metric: bool = False, fit_kwargs={}, free_mem_ratio: int = 0): ...
    def default_estimator_list(self, estimator_list: List[str], is_spark_dataframe: bool) -> List[str]: ...
    def default_metric(self, metric: str) -> str: ...
    @staticmethod
    def prepare_sample_train_data(automlstate, sample_size): ...

def remove_ts_duplicates(X, time_col):
    """
    Assumes the targets are included
    @param X:
    @param time_col:
    @param y:
    @return:
    """
