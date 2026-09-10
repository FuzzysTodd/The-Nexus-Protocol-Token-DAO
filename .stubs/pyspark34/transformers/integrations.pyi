from .trainer_callback import ProgressCallback as ProgressCallback, TrainerCallback as TrainerCallback
from .trainer_utils import BestRun as BestRun, IntervalStrategy as IntervalStrategy, PREFIX_CHECKPOINT_DIR as PREFIX_CHECKPOINT_DIR
from .training_args import ParallelMode as ParallelMode
from .utils import ENV_VARS_TRUE_VALUES as ENV_VARS_TRUE_VALUES, flatten_dict as flatten_dict, is_datasets_available as is_datasets_available, is_torch_available as is_torch_available, is_torch_tpu_available as is_torch_tpu_available, logging as logging
from _typeshed import Incomplete
from neptune.new.metadata_containers.run import Run
from typing import Dict, Optional

logger: Incomplete

def is_wandb_available(): ...
def is_clearml_available(): ...
def is_comet_available(): ...
def is_tensorboard_available(): ...
def is_optuna_available(): ...
def is_ray_available(): ...
def is_ray_tune_available(): ...
def is_sigopt_available(): ...
def is_azureml_available(): ...
def is_mlflow_available(): ...
def is_fairscale_available(): ...
def is_neptune_available(): ...
def is_codecarbon_available(): ...
def hp_params(trial): ...
def default_hp_search_backend(): ...
def run_hp_search_optuna(trainer, n_trials: int, direction: str, **kwargs) -> BestRun: ...
def run_hp_search_ray(trainer, n_trials: int, direction: str, **kwargs) -> BestRun: ...
def run_hp_search_sigopt(trainer, n_trials: int, direction: str, **kwargs) -> BestRun: ...
def run_hp_search_wandb(trainer, n_trials: int, direction: str, **kwargs) -> BestRun: ...
def get_available_reporting_integrations(): ...
def rewrite_logs(d): ...

class TensorBoardCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that sends the logs to [TensorBoard](https://www.tensorflow.org/tensorboard).

    Args:
        tb_writer (`SummaryWriter`, *optional*):
            The writer to use. Will instantiate one if not set.
    """
    tb_writer: Incomplete
    def __init__(self, tb_writer: Incomplete | None = None) -> None: ...
    def on_train_begin(self, args, state, control, **kwargs) -> None: ...
    def on_log(self, args, state, control, logs: Incomplete | None = None, **kwargs) -> None: ...
    def on_train_end(self, args, state, control, **kwargs) -> None: ...

class WandbCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that logs metrics, media, model checkpoints to [Weight and Biases](https://www.wandb.com/).
    """
    def __init__(self) -> None: ...
    def setup(self, args, state, model, **kwargs) -> None:
        '''
        Setup the optional Weights & Biases (*wandb*) integration.

        One can subclass and override this method to customize the setup if needed. Find more information
        [here](https://docs.wandb.ai/guides/integrations/huggingface). You can also override the following environment
        variables:

        Environment:
        - **WANDB_LOG_MODEL** (`str`, *optional*, defaults to `"false"`):
            Whether to log model and checkpoints during training. Can be `"end"`, `"checkpoint"` or `"false"`. If set
            to `"end"`, the model will be uploaded at the end of training. If set to `"checkpoint"`, the checkpoint
            will be uploaded every `args.save_steps` . If set to `"false"`, the model will not be uploaded. Use along
            with [`~transformers.TrainingArguments.load_best_model_at_end`] to upload best model.

            <Deprecated version="5.0">

            Setting `WANDB_LOG_MODEL` as `bool` will be deprecated in version 5 of 🤗 Transformers.

            </Deprecated>
        - **WANDB_WATCH** (`str`, *optional* defaults to `"false"`):
            Can be `"gradients"`, `"all"`, `"parameters"`, or `"false"`. Set to `"all"` to log gradients and
            parameters.
        - **WANDB_PROJECT** (`str`, *optional*, defaults to `"huggingface"`):
            Set this to a custom string to store results in a different project.
        - **WANDB_DISABLED** (`bool`, *optional*, defaults to `False`):
            Whether to disable wandb entirely. Set `WANDB_DISABLED=true` to disable.
        '''
    def on_train_begin(self, args, state, control, model: Incomplete | None = None, **kwargs) -> None: ...
    def on_train_end(self, args, state, control, model: Incomplete | None = None, tokenizer: Incomplete | None = None, **kwargs) -> None: ...
    def on_log(self, args, state, control, model: Incomplete | None = None, logs: Incomplete | None = None, **kwargs) -> None: ...
    def on_save(self, args, state, control, **kwargs) -> None: ...

class CometCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that sends the logs to [Comet ML](https://www.comet.ml/site/).
    """
    def __init__(self) -> None: ...
    def setup(self, args, state, model) -> None:
        """
        Setup the optional Comet.ml integration.

        Environment:
        - **COMET_MODE** (`str`, *optional*, defaults to `ONLINE`):
            Whether to create an online, offline experiment or disable Comet logging. Can be `OFFLINE`, `ONLINE`, or
            `DISABLED`.
        - **COMET_PROJECT_NAME** (`str`, *optional*):
            Comet project name for experiments.
        - **COMET_OFFLINE_DIRECTORY** (`str`, *optional*):
            Folder to use for saving offline experiments when `COMET_MODE` is `OFFLINE`.
        - **COMET_LOG_ASSETS** (`str`, *optional*, defaults to `TRUE`):
            Whether or not to log training assets (tf event logs, checkpoints, etc), to Comet. Can be `TRUE`, or
            `FALSE`.

        For a number of configurable items in the environment, see
        [here](https://www.comet.ml/docs/python-sdk/advanced/#comet-configuration-variables).
        """
    def on_train_begin(self, args, state, control, model: Incomplete | None = None, **kwargs) -> None: ...
    def on_log(self, args, state, control, model: Incomplete | None = None, logs: Incomplete | None = None, **kwargs) -> None: ...
    def on_train_end(self, args, state, control, **kwargs) -> None: ...

class AzureMLCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that sends the logs to [AzureML](https://pypi.org/project/azureml-sdk/).
    """
    azureml_run: Incomplete
    def __init__(self, azureml_run: Incomplete | None = None) -> None: ...
    def on_init_end(self, args, state, control, **kwargs) -> None: ...
    def on_log(self, args, state, control, logs: Incomplete | None = None, **kwargs) -> None: ...

class MLflowCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that sends the logs to [MLflow](https://www.mlflow.org/). Can be disabled by setting
    environment variable `DISABLE_MLFLOW_INTEGRATION = TRUE`.
    """
    def __init__(self) -> None: ...
    def setup(self, args, state, model) -> None:
        '''
        Setup the optional MLflow integration.

        Environment:
        - **HF_MLFLOW_LOG_ARTIFACTS** (`str`, *optional*):
            Whether to use MLflow `.log_artifact()` facility to log artifacts. This only makes sense if logging to a
            remote server, e.g. s3 or GCS. If set to `True` or *1*, will copy each saved checkpoint on each save in
            [`TrainingArguments`]\'s `output_dir` to the local or remote artifact storage. Using it without a remote
            storage will just copy the files to your artifact location.
        - **MLFLOW_EXPERIMENT_NAME** (`str`, *optional*, defaults to `None`):
            Whether to use an MLflow experiment_name under which to launch the run. Default to `None` which will point
            to the `Default` experiment in MLflow. Otherwise, it is a case sensitive name of the experiment to be
            activated. If an experiment with this name does not exist, a new experiment with this name is created.
        - **MLFLOW_TAGS** (`str`, *optional*):
            A string dump of a dictionary of key/value pair to be added to the MLflow run as tags. Example:
            `os.environ[\'MLFLOW_TAGS\']=\'{"release.candidate": "RC1", "release.version": "2.2.0"}\'`.
        - **MLFLOW_NESTED_RUN** (`str`, *optional*):
            Whether to use MLflow nested runs. If set to `True` or *1*, will create a nested run inside the current
            run.
        - **MLFLOW_RUN_ID** (`str`, *optional*):
            Allow to reattach to an existing run which can be usefull when resuming training from a checkpoint. When
            `MLFLOW_RUN_ID` environment variable is set, `start_run` attempts to resume a run with the specified run ID
            and other parameters are ignored.
        - **MLFLOW_FLATTEN_PARAMS** (`str`, *optional*, defaults to `False`):
            Whether to flatten the parameters dictionary before logging.
        '''
    def on_train_begin(self, args, state, control, model: Incomplete | None = None, **kwargs) -> None: ...
    def on_log(self, args, state, control, logs, model: Incomplete | None = None, **kwargs) -> None: ...
    def on_train_end(self, args, state, control, **kwargs) -> None: ...
    def on_save(self, args, state, control, **kwargs) -> None: ...
    def __del__(self) -> None: ...

class NeptuneMissingConfiguration(Exception):
    def __init__(self) -> None: ...

class NeptuneCallback(TrainerCallback):
    '''TrainerCallback that sends the logs to [Neptune](https://neptune.ai).

    Args:
        api_token (`str`, optional):
            Neptune API token obtained upon registration. You can leave this argument out if you have saved your token
            to the `NEPTUNE_API_TOKEN` environment variable (strongly recommended). See full setup instructions in the
            [docs](https://docs.neptune.ai/getting-started/installation).
        project (`str`, optional):
            Name of an existing Neptune project, in the form: "workspace-name/project-name". You can find and copy the
            name from the project Settings -> Properties in Neptune. If None (default), the value of the
            `NEPTUNE_PROJECT` environment variable will be used.
        name (`str`, optional): Custom name for the run.
        base_namespace (`str`, optional, defaults to "finetuning"): In the Neptune run, the root namespace
            that will contain all of the logged metadata.
        log_parameters (`bool`, optional, defaults to True):
            If True, logs all Trainer arguments and model parameters provided by the Trainer.
        log_checkpoints (`str`, optional, defaults to None):
            If "same", uploads checkpoints whenever they are saved by the Trainer. If "last", uploads only the most
            recently saved checkpoint. If "best", uploads the best checkpoint (among the ones saved by the Trainer). If
            None, does not upload checkpoints.
        run (`Run`, optional):
            Pass a Neptune run object if you want to continue logging to an existing run. Read more about resuming runs
            in the [docs](https://docs.neptune.ai/how-to-guides/neptune-api/resume-run).
        **neptune_run_kwargs (optional):
            Additional keyword arguments to be passed directly to the
            [neptune.init_run()](https://docs.neptune.ai/api-reference/neptune#.init_run) function when a new run is
            created.
    '''
    integration_version_key: str
    model_parameters_key: str
    trial_name_key: str
    trial_params_key: str
    trainer_parameters_key: str
    flat_metrics: Incomplete
    def __init__(self, *, api_token: Optional[str] = None, project: Optional[str] = None, name: Optional[str] = None, base_namespace: str = 'finetuning', run: Optional['Run'] = None, log_parameters: bool = True, log_checkpoints: Optional[str] = None, **neptune_run_kwargs) -> None: ...
    @property
    def run(self): ...
    def on_init_end(self, args, state, control, **kwargs) -> None: ...
    def on_train_begin(self, args, state, control, model: Incomplete | None = None, **kwargs) -> None: ...
    def on_train_end(self, args, state, control, **kwargs) -> None: ...
    def __del__(self) -> None: ...
    def on_save(self, args, state, control, **kwargs) -> None: ...
    def on_evaluate(self, args, state, control, metrics: Incomplete | None = None, **kwargs) -> None: ...
    @classmethod
    def get_run(cls, trainer): ...
    def on_log(self, args, state, control, logs: Optional[Dict[str, float]] = None, **kwargs): ...

class CodeCarbonCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that tracks the CO2 emission of training.
    """
    tracker: Incomplete
    def __init__(self) -> None: ...
    def on_init_end(self, args, state, control, **kwargs) -> None: ...
    def on_train_begin(self, args, state, control, model: Incomplete | None = None, **kwargs) -> None: ...
    def on_train_end(self, args, state, control, **kwargs) -> None: ...

class ClearMLCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that sends the logs to [ClearML](https://clear.ml/).

    Environment:
    - **CLEARML_PROJECT** (`str`, *optional*, defaults to `HuggingFace Transformers`):
        ClearML project name.
    - **CLEARML_TASK** (`str`, *optional*, defaults to `Trainer`):
        ClearML task name.
    - **CLEARML_LOG_MODEL** (`bool`, *optional*, defaults to `False`):
        Whether to log models as artifacts during training.
    """
    def __init__(self) -> None: ...
    def setup(self, args, state, model, tokenizer, **kwargs) -> None: ...
    def on_train_begin(self, args, state, control, model: Incomplete | None = None, tokenizer: Incomplete | None = None, **kwargs) -> None: ...
    def on_train_end(self, args, state, control, model: Incomplete | None = None, tokenizer: Incomplete | None = None, metrics: Incomplete | None = None, logs: Incomplete | None = None, **kwargs) -> None: ...
    def on_log(self, args, state, control, model: Incomplete | None = None, tokenizer: Incomplete | None = None, logs: Incomplete | None = None, **kwargs) -> None: ...
    def on_save(self, args, state, control, **kwargs) -> None: ...

INTEGRATION_TO_CALLBACK: Incomplete

def get_reporting_integration_callbacks(report_to): ...
