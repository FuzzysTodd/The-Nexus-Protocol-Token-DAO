from .trainer_utils import IntervalStrategy as IntervalStrategy, has_length as has_length
from .training_args import TrainingArguments as TrainingArguments
from .utils import logging as logging
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, List, Optional, Union

logger: Incomplete

@dataclass
class TrainerState:
    """
    A class containing the [`Trainer`] inner state that will be saved along the model and optimizer when checkpointing
    and passed to the [`TrainerCallback`].

    <Tip>

    In all this class, one step is to be understood as one update step. When using gradient accumulation, one update
    step may require several forward and backward passes: if you use `gradient_accumulation_steps=n`, then one update
    step requires going through *n* batches.

    </Tip>

    Args:
        epoch (`float`, *optional*):
            Only set during training, will represent the epoch the training is at (the decimal part being the
            percentage of the current epoch completed).
        global_step (`int`, *optional*, defaults to 0):
            During training, represents the number of update steps completed.
        max_steps (`int`, *optional*, defaults to 0):
            The number of update steps to do during the current training.
        total_flos (`float`, *optional*, defaults to 0):
            The total number of floating operations done by the model since the beginning of training (stored as floats
            to avoid overflow).
        log_history (`List[Dict[str, float]]`, *optional*):
            The list of logs done since the beginning of training.
        best_metric (`float`, *optional*):
            When tracking the best model, the value of the best metric encountered so far.
        best_model_checkpoint (`str`, *optional*):
            When tracking the best model, the value of the name of the checkpoint for the best model encountered so
            far.
        is_local_process_zero (`bool`, *optional*, defaults to `True`):
            Whether or not this process is the local (e.g., on one machine if training in a distributed fashion on
            several machines) main process.
        is_world_process_zero (`bool`, *optional*, defaults to `True`):
            Whether or not this process is the global main process (when training in a distributed fashion on several
            machines, this is only going to be `True` for one process).
        is_hyper_param_search (`bool`, *optional*, defaults to `False`):
            Whether we are in the process of a hyper parameter search using Trainer.hyperparameter_search. This will
            impact the way data will be logged in TensorBoard.
    """
    epoch: Optional[float] = ...
    global_step: int = ...
    max_steps: int = ...
    num_train_epochs: int = ...
    total_flos: float = ...
    log_history: List[Dict[str, float]] = ...
    best_metric: Optional[float] = ...
    best_model_checkpoint: Optional[str] = ...
    is_local_process_zero: bool = ...
    is_world_process_zero: bool = ...
    is_hyper_param_search: bool = ...
    trial_name: str = ...
    trial_params: Dict[str, Union[str, float, int, bool]] = ...
    def __post_init__(self) -> None: ...
    def save_to_json(self, json_path: str):
        """Save the content of this instance in JSON format inside `json_path`."""
    @classmethod
    def load_from_json(cls, json_path: str):
        """Create an instance from the content of `json_path`."""
    def __init__(self, epoch, global_step, max_steps, num_train_epochs, total_flos, log_history, best_metric, best_model_checkpoint, is_local_process_zero, is_world_process_zero, is_hyper_param_search, trial_name, trial_params) -> None: ...

@dataclass
class TrainerControl:
    """
    A class that handles the [`Trainer`] control flow. This class is used by the [`TrainerCallback`] to activate some
    switches in the training loop.

    Args:
        should_training_stop (`bool`, *optional*, defaults to `False`):
            Whether or not the training should be interrupted.

            If `True`, this variable will not be set back to `False`. The training will just stop.
        should_epoch_stop (`bool`, *optional*, defaults to `False`):
            Whether or not the current epoch should be interrupted.

            If `True`, this variable will be set back to `False` at the beginning of the next epoch.
        should_save (`bool`, *optional*, defaults to `False`):
            Whether or not the model should be saved at this step.

            If `True`, this variable will be set back to `False` at the beginning of the next step.
        should_evaluate (`bool`, *optional*, defaults to `False`):
            Whether or not the model should be evaluated at this step.

            If `True`, this variable will be set back to `False` at the beginning of the next step.
        should_log (`bool`, *optional*, defaults to `False`):
            Whether or not the logs should be reported at this step.

            If `True`, this variable will be set back to `False` at the beginning of the next step.
    """
    should_training_stop: bool = ...
    should_epoch_stop: bool = ...
    should_save: bool = ...
    should_evaluate: bool = ...
    should_log: bool = ...
    def __init__(self, should_training_stop, should_epoch_stop, should_save, should_evaluate, should_log) -> None: ...

class TrainerCallback:
    '''
    A class for objects that will inspect the state of the training loop at some events and take some decisions. At
    each of those events the following arguments are available:

    Args:
        args ([`TrainingArguments`]):
            The training arguments used to instantiate the [`Trainer`].
        state ([`TrainerState`]):
            The current state of the [`Trainer`].
        control ([`TrainerControl`]):
            The object that is returned to the [`Trainer`] and can be used to make some decisions.
        model ([`PreTrainedModel`] or `torch.nn.Module`):
            The model being trained.
        tokenizer ([`PreTrainedTokenizer`]):
            The tokenizer used for encoding the data.
        optimizer (`torch.optim.Optimizer`):
            The optimizer used for the training steps.
        lr_scheduler (`torch.optim.lr_scheduler.LambdaLR`):
            The scheduler used for setting the learning rate.
        train_dataloader (`torch.utils.data.DataLoader`, *optional*):
            The current dataloader used for training.
        eval_dataloader (`torch.utils.data.DataLoader`, *optional*):
            The current dataloader used for training.
        metrics (`Dict[str, float]`):
            The metrics computed by the last evaluation phase.

            Those are only accessible in the event `on_evaluate`.
        logs  (`Dict[str, float]`):
            The values to log.

            Those are only accessible in the event `on_log`.

    The `control` object is the only one that can be changed by the callback, in which case the event that changes it
    should return the modified version.

    The argument `args`, `state` and `control` are positionals for all events, all the others are grouped in `kwargs`.
    You can unpack the ones you need in the signature of the event using them. As an example, see the code of the
    simple [`~transformer.PrinterCallback`].

    Example:

    ```python
    class PrinterCallback(TrainerCallback):
        def on_log(self, args, state, control, logs=None, **kwargs):
            _ = logs.pop("total_flos", None)
            if state.is_local_process_zero:
                print(logs)
    ```'''
    def on_init_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called at the end of the initialization of the [`Trainer`].
        """
    def on_train_begin(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called at the beginning of training.
        """
    def on_train_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called at the end of training.
        """
    def on_epoch_begin(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called at the beginning of an epoch.
        """
    def on_epoch_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called at the end of an epoch.
        """
    def on_step_begin(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called at the beginning of a training step. If using gradient accumulation, one training step might take
        several inputs.
        """
    def on_substep_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called at the end of an substep during gradient accumulation.
        """
    def on_step_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called at the end of a training step. If using gradient accumulation, one training step might take
        several inputs.
        """
    def on_evaluate(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called after an evaluation phase.
        """
    def on_predict(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, metrics, **kwargs):
        """
        Event called after a successful prediction.
        """
    def on_save(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called after a checkpoint save.
        """
    def on_log(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called after logging the last logs.
        """
    def on_prediction_step(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        """
        Event called after a prediction step.
        """

class CallbackHandler(TrainerCallback):
    """Internal class that just calls the list of callbacks in order."""
    callbacks: Incomplete
    model: Incomplete
    tokenizer: Incomplete
    optimizer: Incomplete
    lr_scheduler: Incomplete
    train_dataloader: Incomplete
    eval_dataloader: Incomplete
    def __init__(self, callbacks, model, tokenizer, optimizer, lr_scheduler) -> None: ...
    def add_callback(self, callback) -> None: ...
    def pop_callback(self, callback): ...
    def remove_callback(self, callback) -> None: ...
    @property
    def callback_list(self): ...
    def on_init_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl): ...
    def on_train_begin(self, args: TrainingArguments, state: TrainerState, control: TrainerControl): ...
    def on_train_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl): ...
    def on_epoch_begin(self, args: TrainingArguments, state: TrainerState, control: TrainerControl): ...
    def on_epoch_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl): ...
    def on_step_begin(self, args: TrainingArguments, state: TrainerState, control: TrainerControl): ...
    def on_substep_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl): ...
    def on_step_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl): ...
    def on_evaluate(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, metrics): ...
    def on_predict(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, metrics): ...
    def on_save(self, args: TrainingArguments, state: TrainerState, control: TrainerControl): ...
    def on_log(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, logs): ...
    def on_prediction_step(self, args: TrainingArguments, state: TrainerState, control: TrainerControl): ...
    def call_event(self, event, args, state, control, **kwargs): ...

class DefaultFlowCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that handles the default flow of the training loop for logs, evaluation and checkpoints.
    """
    def on_step_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs): ...
    def on_epoch_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs): ...

class ProgressCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that displays the progress of training or evaluation.
    """
    training_bar: Incomplete
    prediction_bar: Incomplete
    def __init__(self) -> None: ...
    current_step: int
    def on_train_begin(self, args, state, control, **kwargs) -> None: ...
    def on_step_end(self, args, state, control, **kwargs) -> None: ...
    def on_prediction_step(self, args, state, control, eval_dataloader: Incomplete | None = None, **kwargs) -> None: ...
    def on_evaluate(self, args, state, control, **kwargs) -> None: ...
    def on_predict(self, args, state, control, **kwargs) -> None: ...
    def on_log(self, args, state, control, logs: Incomplete | None = None, **kwargs) -> None: ...
    def on_train_end(self, args, state, control, **kwargs) -> None: ...

class PrinterCallback(TrainerCallback):
    """
    A bare [`TrainerCallback`] that just prints the logs.
    """
    def on_log(self, args, state, control, logs: Incomplete | None = None, **kwargs) -> None: ...

class EarlyStoppingCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that handles early stopping.

    Args:
       early_stopping_patience (`int`):
            Use with `metric_for_best_model` to stop training when the specified metric worsens for
            `early_stopping_patience` evaluation calls.
       early_stopping_threshold(`float`, *optional*):
            Use with TrainingArguments `metric_for_best_model` and `early_stopping_patience` to denote how much the
            specified metric must improve to satisfy early stopping conditions. `

    This callback depends on [`TrainingArguments`] argument *load_best_model_at_end* functionality to set best_metric
    in [`TrainerState`].
    """
    early_stopping_patience: Incomplete
    early_stopping_threshold: Incomplete
    early_stopping_patience_counter: int
    def __init__(self, early_stopping_patience: int = 1, early_stopping_threshold: Optional[float] = 0.0) -> None: ...
    def check_metric_value(self, args, state, control, metric_value) -> None: ...
    def on_train_begin(self, args, state, control, **kwargs) -> None: ...
    def on_evaluate(self, args, state, control, metrics, **kwargs) -> None: ...
