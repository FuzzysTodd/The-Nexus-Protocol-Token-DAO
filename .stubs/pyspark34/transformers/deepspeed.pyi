from .dependency_versions_check import dep_version_check as dep_version_check
from .utils import is_accelerate_available as is_accelerate_available, is_torch_available as is_torch_available, logging as logging
from _typeshed import Incomplete

logger: Incomplete

def is_deepspeed_available(): ...

class HfDeepSpeedConfig:
    '''
    This object contains a DeepSpeed configuration dictionary and can be quickly queried for things like zero stage.

    A `weakref` of this object is stored in the module\'s globals to be able to access the config from areas where
    things like the Trainer object is not available (e.g. `from_pretrained` and `_get_resized_embeddings`). Therefore
    it\'s important that this object remains alive while the program is still running.

    [`Trainer`] uses the `HfTrainerDeepSpeedConfig` subclass instead. That subclass has logic to sync the configuration
    with values of [`TrainingArguments`] by replacing special placeholder values: `"auto"`. Without this special logic
    the DeepSpeed configuration is not modified in any way.

    Args:
        config_file_or_dict (`Union[str, Dict]`): path to DeepSpeed config file or dict.

    '''
    def __init__(self, config_file_or_dict) -> None: ...

class HfTrainerDeepSpeedConfig(HfDeepSpeedConfig):
    """
    The `HfTrainerDeepSpeedConfig` object is meant to be created during `TrainingArguments` object creation and has the
    same lifespan as the latter.
    """
    mismatches: Incomplete
    def __init__(self, config_file_or_dict) -> None: ...
    def dtype(self): ...
    def fill_match(self, ds_key_long, hf_val, hf_key: Incomplete | None = None, must_match: bool = True) -> None:
        '''
        A utility method that massages the config file and can optionally verify that the values match.

        1. Replace "auto" values with `TrainingArguments` value.

        2. If it wasn\'t "auto" and `must_match` is true, then check that DS config matches Trainer
        config values and if mismatched add the entry to `self.mismatched` - will assert during
        `trainer_config_finalize` for one or more mismatches.

        '''
    fill_only: Incomplete
    def trainer_config_process(self, args) -> None:
        """
        Adjust the config with `TrainingArguments` values. This stage is run during `TrainingArguments` object
        creation.
        """
    def trainer_config_finalize(self, args, model, num_training_steps) -> None:
        """
        This stage is run after we have the model and know num_training_steps.

        Now we can complete the configuration process.
        """

def set_hf_deepspeed_config(hf_deepspeed_config_obj) -> None: ...
def unset_hf_deepspeed_config() -> None: ...
def is_deepspeed_zero3_enabled(): ...
def deepspeed_config(): ...
def deepspeed_optim_sched(trainer, hf_deepspeed_config, args, num_training_steps):
    """
    A convenience wrapper that deals with optimizer and lr scheduler configuration.
    """
def deepspeed_init(trainer, num_training_steps, resume_from_checkpoint: Incomplete | None = None, inference: bool = False):
    """
    Init DeepSpeed, after updating the DeepSpeed configuration with any relevant Trainer's args.

    If `resume_from_checkpoint` was passed then an attempt to resume from a previously saved checkpoint will be made.

    Args:
        trainer: Trainer object
        num_training_steps: per single gpu
        resume_from_checkpoint: path to a checkpoint if to resume from after normal DeepSpeedEngine load
        inference: launch in inference mode (no optimizer and no lr scheduler)

    Returns: model, optimizer, lr_scheduler

    We may use `deepspeed_init` more than once during the life of Trainer, when we do - it's a temp hack based on:
    https://github.com/microsoft/DeepSpeed/issues/1394#issuecomment-937405374 until Deepspeed fixes a bug where it
    can't resume from a checkpoint after it did some stepping https://github.com/microsoft/DeepSpeed/issues/1612

    """
