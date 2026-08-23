from . import metrics as metrics, models as models
from .. import __version__ as __version__, datasets as datasets
from _typeshed import Incomplete
from collections.abc import Generator

regression_metrics: Incomplete
binary_classification_metrics: Incomplete
human_metrics: Incomplete
linear_regress_methods: Incomplete
linear_classify_methods: Incomplete
tree_regress_methods: Incomplete
rf_regress_methods: Incomplete
tree_classify_methods: Incomplete
deep_regress_methods: Incomplete
deep_classify_methods: Incomplete

def experiments(dataset: Incomplete | None = None, model: Incomplete | None = None, method: Incomplete | None = None, metric: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
def run_experiment(experiment, use_cache: bool = True, cache_dir: str = '/tmp'): ...
def run_experiments_helper(args): ...
def run_experiments(dataset: Incomplete | None = None, model: Incomplete | None = None, method: Incomplete | None = None, metric: Incomplete | None = None, cache_dir: str = '/tmp', nworkers: int = 1): ...

nexperiments: int
total_sent: int
total_done: int
total_failed: int
host_records: Incomplete
worker_lock: Incomplete
ssh_conn_per_min_limit: int

def run_remote_experiments(experiments, thread_hosts, rate_limit: int = 10) -> None:
    ''' Use ssh to run the experiments on remote machines in parallel.

    Parameters
    ----------
    experiments : iterable
        Output of shap.benchmark.experiments(...).

    thread_hosts : list of strings
        Each host has the format "host_name:path_to_python_binary" and can appear multiple times
        in the list (one for each parallel execution you want on that machine).

    rate_limit : int
        How many ssh connections we make per minute to each host (to avoid throttling issues).
    '''
