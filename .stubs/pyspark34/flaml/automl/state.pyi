from _typeshed import Incomplete
from flaml import tune as tune
from flaml.automl.logger import logger as logger
from flaml.automl.ml import compute_estimator as compute_estimator, train_estimator as train_estimator
from flaml.automl.spark import DataFrame as DataFrame, Series as Series, psDataFrame as psDataFrame, psSeries as psSeries
from flaml.automl.time_series.ts_data import TimeSeriesDataset as TimeSeriesDataset
from flaml.internal._autofe import parse_autofe_config as parse_autofe_config

class SearchState:
    @property
    def search_space(self): ...
    @property
    def estimated_cost4improvement(self): ...
    def valid_starting_point_one_dim(self, value_one_dim, domain_one_dim): ...
    def valid_starting_point(self, starting_point, search_space): ...
    init_eci: Incomplete
    init_config: Incomplete
    low_cost_partial_config: Incomplete
    cat_hp_cost: Incomplete
    ls_ever_converged: bool
    learner_class: Incomplete
    data_size: Incomplete
    search_alg: Incomplete
    best_config: Incomplete
    best_result: Incomplete
    best_loss: Incomplete
    total_time_used: int
    total_iter: int
    base_eci: Incomplete
    time_best_found: int
    time2eval_best: int
    time2eval_best_old: int
    trained_estimator: Incomplete
    sample_size: Incomplete
    trial_time: int
    def __init__(self, learner_class, data, task, starting_point: Incomplete | None = None, period: Incomplete | None = None, custom_hp: Incomplete | None = None, max_iter: Incomplete | None = None, budget: Incomplete | None = None, featurization: str = 'auto') -> None: ...
    best_loss_old: Incomplete
    time_best_found_old: Incomplete
    iter_best_found: Incomplete
    best_config_sample_size: Incomplete
    best_config_train_time: Incomplete
    metric_for_logging: Incomplete
    def update(self, result, time_used) -> None: ...
    def get_hist_config_sig(self, sample_size, config): ...
    def est_retrain_time(self, retrain_sample_size): ...

class AutoMLState:
    def prepare_sample_train_data(self, sample_size: int): ...
    @classmethod
    def sanitize(cls, config: dict) -> dict:
        """Make a config ready for passing to estimator."""
