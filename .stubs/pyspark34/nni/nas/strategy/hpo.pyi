from .base import BaseStrategy as BaseStrategy
from _typeshed import Incomplete
from nni.nas import Sampler as Sampler, budget_exhausted as budget_exhausted, is_stopped_exec as is_stopped_exec, query_available_resources as query_available_resources, submit_models as submit_models

class TPESampler(Sampler):
    tpe_tuner: Incomplete
    cur_sample: Incomplete
    index: Incomplete
    total_parameters: Incomplete
    def __init__(self, optimize_mode: str = 'minimize') -> None: ...
    def update_sample_space(self, sample_space) -> None: ...
    def generate_samples(self, model_id) -> None: ...
    def receive_result(self, model_id, result) -> None: ...
    def choice(self, candidates, mutator, model, index): ...

class TPE(BaseStrategy):
    """
    The Tree-structured Parzen Estimator (TPE) is a sequential model-based optimization (SMBO) approach.

    Find the details in
    `Algorithms for Hyper-Parameter Optimization <https://papers.nips.cc/paper/2011/file/86e8f7ab32cfd12577bc2619bc635690-Paper.pdf>`__.

    SMBO methods sequentially construct models to approximate the performance of hyperparameters based on historical measurements,
    and then subsequently choose new hyperparameters to test based on this model.
    """
    tpe_sampler: Incomplete
    model_id: int
    running_models: Incomplete
    def __init__(self) -> None: ...
    def run(self, base_model, applied_mutators) -> None: ...
TPEStrategy = TPE
