from _typeshed import Incomplete
from flaml.automl.logger import logger as logger
from flaml.version import __version__ as __version__
from typing import MutableMapping

SEARCH_MAX_RESULTS: int

def flatten_dict(d: MutableMapping, sep: str = '.') -> MutableMapping: ...
def is_autolog_enabled(): ...

class MLflowIntegration:
    driver_mlflow_env_config: Incomplete
    autolog: bool
    manual_log: bool
    parent_run_id: Incomplete
    parent_run_name: Incomplete
    log_type: str
    resume_params: Incomplete
    train_func: Incomplete
    best_iteration: Incomplete
    best_run_id: Incomplete
    child_counter: int
    infos: Incomplete
    manual_run_ids: Incomplete
    has_summary: bool
    has_model: bool
    only_history: bool
    extra_tag: Incomplete
    start_time: Incomplete
    mlflow_client: Incomplete
    experiment_id: Incomplete
    experiment_name: Incomplete
    experiment_type: Incomplete
    def __init__(self, experiment_type: str = 'automl', mlflow_exp_name: Incomplete | None = None, extra_tag: Incomplete | None = None) -> None: ...
    def set_mlflow_config(self) -> None: ...
    def wrap_evaluation_function(self, evaluation_function): ...
    def set_best_iter(self, result) -> None: ...
    def update_autolog_state(self) -> None: ...
    def copy_mlflow_run(self, src_id, target_id, components=['param', 'metric', 'tag']) -> None: ...
    def record_trial(self, result, trial, metric) -> None: ...
    def log_tune(self, analysis, metric) -> None: ...
    def log_model(self, model, estimator) -> None: ...
    def pickle_and_log_automl_artifacts(self, automl, model) -> None:
        """log automl artifacts to mlflow
        load back with `automl = mlflow.pyfunc.load_model(model_run_id_or_uri)`, then do prediction with `automl.predict(X)`
        """
    def record_state(self, automl, search_state, estimator) -> None: ...
    def log_automl(self, automl) -> None: ...
    def resume_mlflow(self) -> None: ...
    def adopt_children(self, result: Incomplete | None = None) -> None:
        '''
        Set autologging child runs to nested by fetching them after all child runs are completed.
        Note that this may cause disorder when concurrently starting multiple AutoML processes
        with the same experiment name if the MLflow version is less than or equal to "2.5.0".
        '''
    def retrain(self, train_func, config) -> None:
        """retrain with given config, added for logging the best config and model to parent run.
        No more needed after v2.0.2post2 as we no longer log best config and model to parent run.
        """
    def __del__(self) -> None: ...

def register_automl_pipeline(automl, model_name: Incomplete | None = None): ...
