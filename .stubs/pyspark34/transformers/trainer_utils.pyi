import numpy as np
from .utils import ExplicitEnum as ExplicitEnum, is_psutil_available as is_psutil_available, is_tf_available as is_tf_available, is_torch_available as is_torch_available, is_torch_cuda_available as is_torch_cuda_available, is_torch_tpu_available as is_torch_tpu_available, requires_backends as requires_backends
from _typeshed import Incomplete
from typing import Any, Dict, List, NamedTuple, Optional, Tuple, Union

def seed_worker(_) -> None:
    """
    Helper function to set worker seed during Dataloader initialization.
    """
def enable_full_determinism(seed: int):
    """
    Helper function for reproducible behavior during distributed training. See
    - https://pytorch.org/docs/stable/notes/randomness.html for pytorch
    - https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_op_determinism for tensorflow
    """
def set_seed(seed: int):
    """
    Helper function for reproducible behavior to set the seed in `random`, `numpy`, `torch` and/or `tf` (if installed).

    Args:
        seed (`int`): The seed to set.
    """

class EvalPrediction:
    """
    Evaluation output (always contains labels), to be used to compute metrics.

    Parameters:
        predictions (`np.ndarray`): Predictions of the model.
        label_ids (`np.ndarray`): Targets to be matched.
        inputs (`np.ndarray`, *optional*)
    """
    predictions: Incomplete
    label_ids: Incomplete
    inputs: Incomplete
    def __init__(self, predictions: Union[np.ndarray, Tuple[np.ndarray]], label_ids: Union[np.ndarray, Tuple[np.ndarray]], inputs: Optional[Union[np.ndarray, Tuple[np.ndarray]]] = None) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, idx): ...

class EvalLoopOutput(NamedTuple):
    predictions: Union[np.ndarray, Tuple[np.ndarray]]
    label_ids: Optional[Union[np.ndarray, Tuple[np.ndarray]]]
    metrics: Optional[Dict[str, float]]
    num_samples: Optional[int]

class PredictionOutput(NamedTuple):
    predictions: Union[np.ndarray, Tuple[np.ndarray]]
    label_ids: Optional[Union[np.ndarray, Tuple[np.ndarray]]]
    metrics: Optional[Dict[str, float]]

class TrainOutput(NamedTuple):
    global_step: int
    training_loss: float
    metrics: Dict[str, float]

PREFIX_CHECKPOINT_DIR: str

def get_last_checkpoint(folder): ...

class IntervalStrategy(ExplicitEnum):
    NO: str
    STEPS: str
    EPOCH: str

class EvaluationStrategy(ExplicitEnum):
    NO: str
    STEPS: str
    EPOCH: str

class HubStrategy(ExplicitEnum):
    END: str
    EVERY_SAVE: str
    CHECKPOINT: str
    ALL_CHECKPOINTS: str

class BestRun(NamedTuple):
    """
    The best run found by an hyperparameter search (see [`~Trainer.hyperparameter_search`]).

    Parameters:
        run_id (`str`):
            The id of the best run (if models were saved, the corresponding checkpoint will be in the folder ending
            with run-{run_id}).
        objective (`float`):
            The objective that was obtained for this run.
        hyperparameters (`Dict[str, Any]`):
            The hyperparameters picked to get this run.
    """
    run_id: str
    objective: float
    hyperparameters: Dict[str, Any]

def default_compute_objective(metrics: Dict[str, float]) -> float:
    """
    The default objective to maximize/minimize when doing an hyperparameter search. It is the evaluation loss if no
    metrics are provided to the [`Trainer`], the sum of all metrics otherwise.

    Args:
        metrics (`Dict[str, float]`): The metrics returned by the evaluate method.

    Return:
        `float`: The objective to minimize or maximize
    """
def default_hp_space_optuna(trial) -> Dict[str, float]: ...
def default_hp_space_ray(trial) -> Dict[str, float]: ...
def default_hp_space_sigopt(trial): ...
def default_hp_space_wandb(trial) -> Dict[str, float]: ...

class HPSearchBackend(ExplicitEnum):
    OPTUNA: str
    RAY: str
    SIGOPT: str
    WANDB: str

default_hp_space: Incomplete

def is_main_process(local_rank):
    """
    Whether or not the current process is the local process, based on `xm.get_ordinal()` (for TPUs) first, then on
    `local_rank`.
    """
def total_processes_number(local_rank):
    """
    Return the number of processes launched in parallel. Works with `torch.distributed` and TPUs.
    """
def speed_metrics(split, start_time, num_samples: Incomplete | None = None, num_steps: Incomplete | None = None):
    """
    Measure and return speed performance metrics.

    This function requires a time snapshot `start_time` before the operation to be measured starts and this function
    should be run immediately after the operation to be measured has completed.

    Args:
    - split: name to prefix metric (like train, eval, test...)
    - start_time: operation start time
    - num_samples: number of samples processed
    """

class SchedulerType(ExplicitEnum):
    LINEAR: str
    COSINE: str
    COSINE_WITH_RESTARTS: str
    POLYNOMIAL: str
    CONSTANT: str
    CONSTANT_WITH_WARMUP: str

class TrainerMemoryTracker:
    '''
    A helper class that tracks cpu and gpu memory.

    This class will silently skip unless `psutil` is available. Install with `pip install psutil`.

    When a stage completes, it can pass metrics dict to update with the memory metrics gathered during this stage.

    Example :

    ```python
    self._memory_tracker = TrainerMemoryTracker(self.args.skip_memory_metrics)
    self._memory_tracker.start()
    # code ...
    metrics = {"train_runtime": 10.5}
    self._memory_tracker.stop_and_update_metrics(metrics)
    ```

    At the moment GPU tracking is only for `pytorch`, but can be extended to support `tensorflow`.

    To understand this class\' intricacies please read the documentation of [`~Trainer.log_metrics`].
    '''
    stages: Incomplete
    skip_memory_metrics: Incomplete
    torch: Incomplete
    gpu: Incomplete
    process: Incomplete
    cur_stage: Incomplete
    cpu: Incomplete
    init_reported: bool
    def __init__(self, skip_memory_metrics: bool = False) -> None: ...
    def derive_stage(self):
        """derives the stage/caller name automatically"""
    def cpu_mem_used(self):
        """get resident set size memory for the current process"""
    cpu_mem_used_peak: int
    def peak_monitor_func(self) -> None: ...
    gpu_mem_used_at_start: Incomplete
    cpu_mem_used_at_start: Incomplete
    peak_monitoring: bool
    def start(self) -> None:
        """start tracking for the caller's stage"""
    gpu_mem_used_now: Incomplete
    gpu_mem_used_peak: Incomplete
    cpu_mem_used_now: Incomplete
    def stop(self, stage) -> None:
        """stop tracking for the passed stage"""
    def update_metrics(self, stage, metrics) -> None:
        """updates the metrics"""
    def stop_and_update_metrics(self, metrics: Incomplete | None = None) -> None:
        """combine stop and metrics update in one call for simpler code"""

def has_length(dataset):
    """
    Checks if the dataset implements __len__() and it doesn't raise an error
    """
def denumpify_detensorize(metrics):
    """
    Recursively calls `.item()` on the element of the dictionary passed
    """
def number_of_arguments(func):
    """
    Return the number of arguments of the passed function, even if it's a partial function.
    """

class ShardedDDPOption(ExplicitEnum):
    SIMPLE: str
    ZERO_DP_2: str
    ZERO_DP_3: str
    OFFLOAD: str
    AUTO_WRAP: str

def find_executable_batch_size(function: callable = None, starting_batch_size: int = 128, auto_find_batch_size: bool = False):
    """
    Args:
    A basic decorator that will try to execute `function`. If it fails from exceptions related to out-of-memory or
    CUDNN, the batch size is cut in half and passed to `function` `function` must take in a `batch_size` parameter as
    its first argument.
        function (`callable`, *optional*)
            A function to wrap
        starting_batch_size (`int`, *optional*)
            The batch size to try and fit into memory
        auto_find_batch_size (`bool`, *optional*)
            If False, will just execute `function`
    """

class FSDPOption(ExplicitEnum):
    FULL_SHARD: str
    SHARD_GRAD_OP: str
    NO_SHARD: str
    OFFLOAD: str
    AUTO_WRAP: str

class RemoveColumnsCollator:
    """Wrap the data collator to remove unused columns before they are passed to the collator."""
    data_collator: Incomplete
    signature_columns: Incomplete
    logger: Incomplete
    description: Incomplete
    model_name: Incomplete
    message_logged: bool
    def __init__(self, data_collator, signature_columns, logger: Incomplete | None = None, model_name: Optional[str] = None, description: Optional[str] = None) -> None: ...
    def __call__(self, features: List[dict]): ...
