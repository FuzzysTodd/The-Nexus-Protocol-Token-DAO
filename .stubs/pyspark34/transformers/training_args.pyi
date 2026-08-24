import torch
from .debug_utils import DebugOption as DebugOption
from .trainer_utils import EvaluationStrategy as EvaluationStrategy, FSDPOption as FSDPOption, HubStrategy as HubStrategy, IntervalStrategy as IntervalStrategy, SchedulerType as SchedulerType, ShardedDDPOption as ShardedDDPOption
from .utils import ExplicitEnum as ExplicitEnum, cached_property as cached_property, ccl_version as ccl_version, get_full_repo_name as get_full_repo_name, is_accelerate_available as is_accelerate_available, is_psutil_available as is_psutil_available, is_sagemaker_dp_enabled as is_sagemaker_dp_enabled, is_sagemaker_mp_enabled as is_sagemaker_mp_enabled, is_torch_available as is_torch_available, is_torch_bf16_cpu_available as is_torch_bf16_cpu_available, is_torch_bf16_gpu_available as is_torch_bf16_gpu_available, is_torch_neuroncore_available as is_torch_neuroncore_available, is_torch_tf32_available as is_torch_tf32_available, is_torch_tpu_available as is_torch_tpu_available, logging as logging, requires_backends as requires_backends
from _typeshed import Incomplete
from collections.abc import Generator
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, Dict, List, Optional, Union

logger: Incomplete
log_levels: Incomplete
trainer_log_levels: Incomplete
TORCH_COMPILE_BACKENDS: Incomplete

def default_logdir() -> str:
    """
    Same default as PyTorch
    """
def get_int_from_env(env_keys, default):
    """Returns the first positive env value found in the `env_keys` list or the default."""
def get_xla_device_type(device: torch.device) -> Optional[str]:
    """
    Returns the xla device type (CPU|GPU|TPU) or None if the device is a non-xla device.
    """

class OptimizerNames(ExplicitEnum):
    """
    Stores the acceptable string identifiers for optimizers.
    """
    ADAMW_HF: str
    ADAMW_TORCH: str
    ADAMW_TORCH_XLA: str
    ADAMW_APEX_FUSED: str
    ADAFACTOR: str
    ADAMW_BNB: str
    ADAMW_ANYPRECISION: str
    SGD: str
    ADAGRAD: str

@dataclass
class TrainingArguments:
    '''
    TrainingArguments is the subset of the arguments we use in our example scripts **which relate to the training loop
    itself**.

    Using [`HfArgumentParser`] we can turn this class into
    [argparse](https://docs.python.org/3/library/argparse#module-argparse) arguments that can be specified on the
    command line.

    Parameters:
        output_dir (`str`):
            The output directory where the model predictions and checkpoints will be written.
        overwrite_output_dir (`bool`, *optional*, defaults to `False`):
            If `True`, overwrite the content of the output directory. Use this to continue training if `output_dir`
            points to a checkpoint directory.
        do_train (`bool`, *optional*, defaults to `False`):
            Whether to run training or not. This argument is not directly used by [`Trainer`], it\'s intended to be used
            by your training/evaluation scripts instead. See the [example
            scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
        do_eval (`bool`, *optional*):
            Whether to run evaluation on the validation set or not. Will be set to `True` if `evaluation_strategy` is
            different from `"no"`. This argument is not directly used by [`Trainer`], it\'s intended to be used by your
            training/evaluation scripts instead. See the [example
            scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
        do_predict (`bool`, *optional*, defaults to `False`):
            Whether to run predictions on the test set or not. This argument is not directly used by [`Trainer`], it\'s
            intended to be used by your training/evaluation scripts instead. See the [example
            scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
        evaluation_strategy (`str` or [`~trainer_utils.IntervalStrategy`], *optional*, defaults to `"no"`):
            The evaluation strategy to adopt during training. Possible values are:

                - `"no"`: No evaluation is done during training.
                - `"steps"`: Evaluation is done (and logged) every `eval_steps`.
                - `"epoch"`: Evaluation is done at the end of each epoch.

        prediction_loss_only (`bool`, *optional*, defaults to `False`):
            When performing evaluation and generating predictions, only returns the loss.
        per_device_train_batch_size (`int`, *optional*, defaults to 8):
            The batch size per GPU/TPU core/CPU for training.
        per_device_eval_batch_size (`int`, *optional*, defaults to 8):
            The batch size per GPU/TPU core/CPU for evaluation.
        gradient_accumulation_steps (`int`, *optional*, defaults to 1):
            Number of updates steps to accumulate the gradients for, before performing a backward/update pass.

            <Tip warning={true}>

            When using gradient accumulation, one step is counted as one step with backward pass. Therefore, logging,
            evaluation, save will be conducted every `gradient_accumulation_steps * xxx_step` training examples.

            </Tip>

        eval_accumulation_steps (`int`, *optional*):
            Number of predictions steps to accumulate the output tensors for, before moving the results to the CPU. If
            left unset, the whole predictions are accumulated on GPU/TPU before being moved to the CPU (faster but
            requires more memory).
        eval_delay (`float`, *optional*):
            Number of epochs or steps to wait for before the first evaluation can be performed, depending on the
            evaluation_strategy.
        learning_rate (`float`, *optional*, defaults to 5e-5):
            The initial learning rate for [`AdamW`] optimizer.
        weight_decay (`float`, *optional*, defaults to 0):
            The weight decay to apply (if not zero) to all layers except all bias and LayerNorm weights in [`AdamW`]
            optimizer.
        adam_beta1 (`float`, *optional*, defaults to 0.9):
            The beta1 hyperparameter for the [`AdamW`] optimizer.
        adam_beta2 (`float`, *optional*, defaults to 0.999):
            The beta2 hyperparameter for the [`AdamW`] optimizer.
        adam_epsilon (`float`, *optional*, defaults to 1e-8):
            The epsilon hyperparameter for the [`AdamW`] optimizer.
        max_grad_norm (`float`, *optional*, defaults to 1.0):
            Maximum gradient norm (for gradient clipping).
        num_train_epochs(`float`, *optional*, defaults to 3.0):
            Total number of training epochs to perform (if not an integer, will perform the decimal part percents of
            the last epoch before stopping training).
        max_steps (`int`, *optional*, defaults to -1):
            If set to a positive number, the total number of training steps to perform. Overrides `num_train_epochs`.
            In case of using a finite iterable dataset the training may stop before reaching the set number of steps
            when all data is exhausted
        lr_scheduler_type (`str` or [`SchedulerType`], *optional*, defaults to `"linear"`):
            The scheduler type to use. See the documentation of [`SchedulerType`] for all possible values.
        warmup_ratio (`float`, *optional*, defaults to 0.0):
            Ratio of total training steps used for a linear warmup from 0 to `learning_rate`.
        warmup_steps (`int`, *optional*, defaults to 0):
            Number of steps used for a linear warmup from 0 to `learning_rate`. Overrides any effect of `warmup_ratio`.
        log_level (`str`, *optional*, defaults to `passive`):
            Logger log level to use on the main process. Possible choices are the log levels as strings: \'debug\',
            \'info\', \'warning\', \'error\' and \'critical\', plus a \'passive\' level which doesn\'t set anything and lets the
            application set the level.
        log_level_replica (`str`, *optional*, defaults to `passive`):
            Logger log level to use on replicas. Same choices as `log_level`"
        log_on_each_node (`bool`, *optional*, defaults to `True`):
            In multinode distributed training, whether to log using `log_level` once per node, or only on the main
            node.
        logging_dir (`str`, *optional*):
            [TensorBoard](https://www.tensorflow.org/tensorboard) log directory. Will default to
            *output_dir/runs/**CURRENT_DATETIME_HOSTNAME***.
        logging_strategy (`str` or [`~trainer_utils.IntervalStrategy`], *optional*, defaults to `"steps"`):
            The logging strategy to adopt during training. Possible values are:

                - `"no"`: No logging is done during training.
                - `"epoch"`: Logging is done at the end of each epoch.
                - `"steps"`: Logging is done every `logging_steps`.

        logging_first_step (`bool`, *optional*, defaults to `False`):
            Whether to log and evaluate the first `global_step` or not.
        logging_steps (`int`, *optional*, defaults to 500):
            Number of update steps between two logs if `logging_strategy="steps"`.
        logging_nan_inf_filter (`bool`, *optional*, defaults to `True`):
            Whether to filter `nan` and `inf` losses for logging. If set to `True` the loss of every step that is `nan`
            or `inf` is filtered and the average loss of the current logging window is taken instead.

            <Tip>

            `logging_nan_inf_filter` only influences the logging of loss values, it does not change the behavior the
            gradient is computed or applied to the model.

            </Tip>

        save_strategy (`str` or [`~trainer_utils.IntervalStrategy`], *optional*, defaults to `"steps"`):
            The checkpoint save strategy to adopt during training. Possible values are:

                - `"no"`: No save is done during training.
                - `"epoch"`: Save is done at the end of each epoch.
                - `"steps"`: Save is done every `save_steps`.
        save_steps (`int`, *optional*, defaults to 500):
            Number of updates steps before two checkpoint saves if `save_strategy="steps"`.
        save_total_limit (`int`, *optional*):
            If a value is passed, will limit the total amount of checkpoints. Deletes the older checkpoints in
            `output_dir`.
        save_on_each_node (`bool`, *optional*, defaults to `False`):
            When doing multi-node distributed training, whether to save models and checkpoints on each node, or only on
            the main one.

            This should not be activated when the different nodes use the same storage as the files will be saved with
            the same names for each node.
        no_cuda (`bool`, *optional*, defaults to `False`):
            Whether to not use CUDA even when it is available or not.
        seed (`int`, *optional*, defaults to 42):
            Random seed that will be set at the beginning of training. To ensure reproducibility across runs, use the
            [`~Trainer.model_init`] function to instantiate the model if it has some randomly initialized parameters.
        data_seed (`int`, *optional*):
            Random seed to be used with data samplers. If not set, random generators for data sampling will use the
            same seed as `seed`. This can be used to ensure reproducibility of data sampling, independent of the model
            seed.
        jit_mode_eval (`bool`, *optional*, defaults to `False`):
            Whether or not to use PyTorch jit trace for inference.
        use_ipex (`bool`, *optional*, defaults to `False`):
            Use Intel extension for PyTorch when it is available. [IPEX
            installation](https://github.com/intel/intel-extension-for-pytorch).
        bf16 (`bool`, *optional*, defaults to `False`):
            Whether to use bf16 16-bit (mixed) precision training instead of 32-bit training. Requires Ampere or higher
            NVIDIA architecture or using CPU (no_cuda). This is an experimental API and it may change.
        fp16 (`bool`, *optional*, defaults to `False`):
            Whether to use fp16 16-bit (mixed) precision training instead of 32-bit training.
        fp16_opt_level (`str`, *optional*, defaults to \'O1\'):
            For `fp16` training, Apex AMP optimization level selected in [\'O0\', \'O1\', \'O2\', and \'O3\']. See details on
            the [Apex documentation](https://nvidia.github.io/apex/amp).
        fp16_backend (`str`, *optional*, defaults to `"auto"`):
            This argument is deprecated. Use `half_precision_backend` instead.
        half_precision_backend (`str`, *optional*, defaults to `"auto"`):
            The backend to use for mixed precision training. Must be one of `"auto", "cuda_amp", "apex", "cpu_amp"`.
            `"auto"` will use CPU/CUDA AMP or APEX depending on the PyTorch version detected, while the other choices
            will force the requested backend.
        bf16_full_eval (`bool`, *optional*, defaults to `False`):
            Whether to use full bfloat16 evaluation instead of 32-bit. This will be faster and save memory but can harm
            metric values. This is an experimental API and it may change.
        fp16_full_eval (`bool`, *optional*, defaults to `False`):
            Whether to use full float16 evaluation instead of 32-bit. This will be faster and save memory but can harm
            metric values.
        tf32 (`bool`, *optional*):
            Whether to enable the TF32 mode, available in Ampere and newer GPU architectures. The default value depends
            on PyTorch\'s version default of `torch.backends.cuda.matmul.allow_tf32`. For more details please refer to
            the [TF32](https://huggingface.co/docs/transformers/performance#tf32) documentation. This is an
            experimental API and it may change.
        local_rank (`int`, *optional*, defaults to -1):
            Rank of the process during distributed training.
        xpu_backend (`str`, *optional*):
            The backend to use for xpu distributed training. Must be one of `"mpi"` or `"ccl"` or `"gloo"`.
        tpu_num_cores (`int`, *optional*):
            When training on TPU, the number of TPU cores (automatically passed by launcher script).
        dataloader_drop_last (`bool`, *optional*, defaults to `False`):
            Whether to drop the last incomplete batch (if the length of the dataset is not divisible by the batch size)
            or not.
        eval_steps (`int`, *optional*):
            Number of update steps between two evaluations if `evaluation_strategy="steps"`. Will default to the same
            value as `logging_steps` if not set.
        dataloader_num_workers (`int`, *optional*, defaults to 0):
            Number of subprocesses to use for data loading (PyTorch only). 0 means that the data will be loaded in the
            main process.
        past_index (`int`, *optional*, defaults to -1):
            Some models like [TransformerXL](../model_doc/transformerxl) or [XLNet](../model_doc/xlnet) can make use of
            the past hidden states for their predictions. If this argument is set to a positive int, the `Trainer` will
            use the corresponding output (usually index 2) as the past state and feed it to the model at the next
            training step under the keyword argument `mems`.
        run_name (`str`, *optional*):
            A descriptor for the run. Typically used for [wandb](https://www.wandb.com/) and
            [mlflow](https://www.mlflow.org/) logging.
        disable_tqdm (`bool`, *optional*):
            Whether or not to disable the tqdm progress bars and table of metrics produced by
            [`~notebook.NotebookTrainingTracker`] in Jupyter Notebooks. Will default to `True` if the logging level is
            set to warn or lower (default), `False` otherwise.
        remove_unused_columns (`bool`, *optional*, defaults to `True`):
            Whether or not to automatically remove the columns unused by the model forward method.

            (Note that this behavior is not implemented for [`TFTrainer`] yet.)
        label_names (`List[str]`, *optional*):
            The list of keys in your dictionary of inputs that correspond to the labels.

            Will eventually default to `["labels"]` except if the model used is one of the `XxxForQuestionAnswering` in
            which case it will default to `["start_positions", "end_positions"]`.
        load_best_model_at_end (`bool`, *optional*, defaults to `False`):
            Whether or not to load the best model found during training at the end of training.

            <Tip>

            When set to `True`, the parameters `save_strategy` needs to be the same as `evaluation_strategy`, and in
            the case it is "steps", `save_steps` must be a round multiple of `eval_steps`.

            </Tip>

        metric_for_best_model (`str`, *optional*):
            Use in conjunction with `load_best_model_at_end` to specify the metric to use to compare two different
            models. Must be the name of a metric returned by the evaluation with or without the prefix `"eval_"`. Will
            default to `"loss"` if unspecified and `load_best_model_at_end=True` (to use the evaluation loss).

            If you set this value, `greater_is_better` will default to `True`. Don\'t forget to set it to `False` if
            your metric is better when lower.
        greater_is_better (`bool`, *optional*):
            Use in conjunction with `load_best_model_at_end` and `metric_for_best_model` to specify if better models
            should have a greater metric or not. Will default to:

            - `True` if `metric_for_best_model` is set to a value that isn\'t `"loss"` or `"eval_loss"`.
            - `False` if `metric_for_best_model` is not set, or set to `"loss"` or `"eval_loss"`.
        ignore_data_skip (`bool`, *optional*, defaults to `False`):
            When resuming training, whether or not to skip the epochs and batches to get the data loading at the same
            stage as in the previous training. If set to `True`, the training will begin faster (as that skipping step
            can take a long time) but will not yield the same results as the interrupted training would have.
        sharded_ddp (`bool`, `str` or list of [`~trainer_utils.ShardedDDPOption`], *optional*, defaults to `False`):
            Use Sharded DDP training from [FairScale](https://github.com/facebookresearch/fairscale) (in distributed
            training only). This is an experimental feature.

            A list of options along the following:

            - `"simple"`: to use first instance of sharded DDP released by fairscale (`ShardedDDP`) similar to ZeRO-2.
            - `"zero_dp_2"`: to use the second instance of sharded DPP released by fairscale (`FullyShardedDDP`) in
              Zero-2 mode (with `reshard_after_forward=False`).
            - `"zero_dp_3"`: to use the second instance of sharded DPP released by fairscale (`FullyShardedDDP`) in
              Zero-3 mode (with `reshard_after_forward=True`).
            - `"offload"`: to add ZeRO-offload (only compatible with `"zero_dp_2"` and `"zero_dp_3"`).

            If a string is passed, it will be split on space. If a bool is passed, it will be converted to an empty
            list for `False` and `["simple"]` for `True`.
        fsdp (`bool`, `str` or list of [`~trainer_utils.FSDPOption`], *optional*, defaults to `False`):
            Use PyTorch Distributed Parallel Training (in distributed training only).

            A list of options along the following:

            - `"full_shard"`: Shard parameters, gradients and optimizer states.
            - `"shard_grad_op"`: Shard optimizer states and gradients.
            - `"offload"`: Offload parameters and gradients to CPUs (only compatible with `"full_shard"` and
              `"shard_grad_op"`).
            - `"auto_wrap"`: Automatically recursively wrap layers with FSDP using `default_auto_wrap_policy`.
        fsdp_min_num_params (`int`, *optional*, defaults to `0`):
            FSDP\'s minimum number of parameters for Default Auto Wrapping. (useful only when `fsdp` field is passed).
        deepspeed (`str` or `dict`, *optional*):
            Use [Deepspeed](https://github.com/microsoft/deepspeed). This is an experimental feature and its API may
            evolve in the future. The value is either the location of DeepSpeed json config file (e.g.,
            `ds_config.json`) or an already loaded json file as a `dict`"
        label_smoothing_factor (`float`, *optional*, defaults to 0.0):
            The label smoothing factor to use. Zero means no label smoothing, otherwise the underlying onehot-encoded
            labels are changed from 0s and 1s to `label_smoothing_factor/num_labels` and `1 - label_smoothing_factor +
            label_smoothing_factor/num_labels` respectively.
        debug (`str` or list of [`~debug_utils.DebugOption`], *optional*, defaults to `""`):
            Enable one or more debug features. This is an experimental feature.

            Possible options are:

            - `"underflow_overflow"`: detects overflow in model\'s input/outputs and reports the last frames that led to
              the event
            - `"tpu_metrics_debug"`: print debug metrics on TPU

            The options should be separated by whitespaces.
        optim (`str` or [`training_args.OptimizerNames`], *optional*, defaults to `"adamw_hf"`):
            The optimizer to use: adamw_hf, adamw_torch, adamw_apex_fused, adamw_anyprecision or adafactor.
        optim_args (`str`, *optional*):
            Optional arguments that are supplied to AnyPrecisionAdamW.
        adafactor (`bool`, *optional*, defaults to `False`):
            This argument is deprecated. Use `--optim adafactor` instead.
        group_by_length (`bool`, *optional*, defaults to `False`):
            Whether or not to group together samples of roughly the same length in the training dataset (to minimize
            padding applied and be more efficient). Only useful if applying dynamic padding.
        length_column_name (`str`, *optional*, defaults to `"length"`):
            Column name for precomputed lengths. If the column exists, grouping by length will use these values rather
            than computing them on train startup. Ignored unless `group_by_length` is `True` and the dataset is an
            instance of `Dataset`.
        report_to (`str` or `List[str]`, *optional*, defaults to `"all"`):
            The list of integrations to report the results and logs to. Supported platforms are `"azure_ml"`,
            `"comet_ml"`, `"mlflow"`, `"neptune"`, `"tensorboard"`,`"clearml"` and `"wandb"`. Use `"all"` to report to
            all integrations installed, `"none"` for no integrations.
        ddp_find_unused_parameters (`bool`, *optional*):
            When using distributed training, the value of the flag `find_unused_parameters` passed to
            `DistributedDataParallel`. Will default to `False` if gradient checkpointing is used, `True` otherwise.
        ddp_bucket_cap_mb (`int`, *optional*):
            When using distributed training, the value of the flag `bucket_cap_mb` passed to `DistributedDataParallel`.
        dataloader_pin_memory (`bool`, *optional*, defaults to `True`):
            Whether you want to pin memory in data loaders or not. Will default to `True`.
        skip_memory_metrics (`bool`, *optional*, defaults to `True`):
            Whether to skip adding of memory profiler reports to metrics. This is skipped by default because it slows
            down the training and evaluation speed.
        push_to_hub (`bool`, *optional*, defaults to `False`):
            Whether or not to push the model to the Hub every time the model is saved. If this is activated,
            `output_dir` will begin a git directory synced with the repo (determined by `hub_model_id`) and the content
            will be pushed each time a save is triggered (depending on your `save_strategy`). Calling
            [`~Trainer.save_model`] will also trigger a push.

            <Tip warning={true}>

            If `output_dir` exists, it needs to be a local clone of the repository to which the [`Trainer`] will be
            pushed.

            </Tip>

        resume_from_checkpoint (`str`, *optional*):
            The path to a folder with a valid checkpoint for your model. This argument is not directly used by
            [`Trainer`], it\'s intended to be used by your training/evaluation scripts instead. See the [example
            scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
        hub_model_id (`str`, *optional*):
            The name of the repository to keep in sync with the local *output_dir*. It can be a simple model ID in
            which case the model will be pushed in your namespace. Otherwise it should be the whole repository name,
            for instance `"user_name/model"`, which allows you to push to an organization you are a member of with
            `"organization_name/model"`. Will default to `user_name/output_dir_name` with *output_dir_name* being the
            name of `output_dir`.

            Will default to the name of `output_dir`.
        hub_strategy (`str` or [`~trainer_utils.HubStrategy`], *optional*, defaults to `"every_save"`):
            Defines the scope of what is pushed to the Hub and when. Possible values are:

            - `"end"`: push the model, its configuration, the tokenizer (if passed along to the [`Trainer`]) and a
              draft of a model card when the [`~Trainer.save_model`] method is called.
            - `"every_save"`: push the model, its configuration, the tokenizer (if passed along to the [`Trainer`]) and
              a draft of a model card each time there is a model save. The pushes are asynchronous to not block
              training, and in case the save are very frequent, a new push is only attempted if the previous one is
              finished. A last push is made with the final model at the end of training.
            - `"checkpoint"`: like `"every_save"` but the latest checkpoint is also pushed in a subfolder named
              last-checkpoint, allowing you to resume training easily with
              `trainer.train(resume_from_checkpoint="last-checkpoint")`.
            - `"all_checkpoints"`: like `"checkpoint"` but all checkpoints are pushed like they appear in the output
              folder (so you will get one checkpoint folder per folder in your final repository)

        hub_token (`str`, *optional*):
            The token to use to push the model to the Hub. Will default to the token in the cache folder obtained with
            `huggingface-cli login`.
        hub_private_repo (`bool`, *optional*, defaults to `False`):
            If True, the Hub repo will be set to private.
        gradient_checkpointing (`bool`, *optional*, defaults to `False`):
            If True, use gradient checkpointing to save memory at the expense of slower backward pass.
        include_inputs_for_metrics (`bool`, *optional*, defaults to `False`):
            Whether or not the inputs will be passed to the `compute_metrics` function. This is intended for metrics
            that need inputs, predictions and references for scoring calculation in Metric class.
        auto_find_batch_size (`bool`, *optional*, defaults to `False`)
            Whether to find a batch size that will fit into memory automatically through exponential decay, avoiding
            CUDA Out-of-Memory errors. Requires accelerate to be installed (`pip install accelerate`)
        full_determinism (`bool`, *optional*, defaults to `False`)
            If `True`, [`enable_full_determinism`] is called instead of [`set_seed`] to ensure reproducible results in
            distributed training
        torchdynamo (`str`, *optional*):
            If set, the backend compiler for TorchDynamo. Possible choices are `"eager"`, `"aot_eager"`, `"inductor"`,
            `"nvfuser"`, `"aot_nvfuser"`, `"aot_cudagraphs"`, `"ofi"`, `"fx2trt"`, `"onnxrt"` and `"ipex"`.
        ray_scope (`str`, *optional*, defaults to `"last"`):
            The scope to use when doing hyperparameter search with Ray. By default, `"last"` will be used. Ray will
            then use the last checkpoint of all trials, compare those, and select the best one. However, other options
            are also available. See the [Ray documentation](
            https://docs.ray.io/en/latest/tune/api_docs/analysis.html#ray.tune.ExperimentAnalysis.get_best_trial) for
            more options.
        ddp_timeout (`int`, *optional*, defaults to 1800):
            The timeout for `torch.distributed.init_process_group` calls, used to avoid GPU socket timeouts when
            performing slow operations in distributed runnings. Please refer the [PyTorch documentation]
            (https://pytorch.org/docs/stable/distributed.html#torch.distributed.init_process_group) for more
            information.
        use_mps_device (`bool`, *optional*, defaults to `False`):
            Whether to use Apple Silicon chip based `mps` device.
        torch_compile (`bool`, *optional*, defaults to `False`):
            Whether or not to compile the model using PyTorch 2.0
            [`torch.compile`](https://pytorch.org/get-started/pytorch-2.0/) (requires a nighlty install of PyTorch).

            If set, the backend will default to `"inductor"` (can be customized with `torch_compile_backend`) and the
            mode will default to `"default"` (can be customized with `torch_compile_mode`).
        torch_compile_backend (`str`, *optional*):
            The backend to use in `torch.compile`. If set to any value, `torch_compile` will be set to `True`.

            Possible choices are `"eager"`, `"aot_eager"`, `"inductor"`, `"nvfuser"`, `"aot_nvfuser"`,
            `"aot_cudagraphs"`, `"ofi"`, `"fx2trt"`, `"onnxrt"` and `"ipex"`.
        torch_compile_mode (`str`, *optional*):
            The mode to use in `torch.compile`. If set to any value, `torch_compile` will be set to `True`.

            Possible choices are `"default"`, `"reduce-overhead"` and `"max-autotune"`.
    '''
    framework = ...
    output_dir: str = ...
    overwrite_output_dir: bool = ...
    do_train: bool = ...
    do_eval: bool = ...
    do_predict: bool = ...
    evaluation_strategy: Union[IntervalStrategy, str] = ...
    prediction_loss_only: bool = ...
    per_device_train_batch_size: int = ...
    per_device_eval_batch_size: int = ...
    per_gpu_train_batch_size: Optional[int] = ...
    per_gpu_eval_batch_size: Optional[int] = ...
    gradient_accumulation_steps: int = ...
    eval_accumulation_steps: Optional[int] = ...
    eval_delay: Optional[float] = ...
    learning_rate: float = ...
    weight_decay: float = ...
    adam_beta1: float = ...
    adam_beta2: float = ...
    adam_epsilon: float = ...
    max_grad_norm: float = ...
    num_train_epochs: float = ...
    max_steps: int = ...
    lr_scheduler_type: Union[SchedulerType, str] = ...
    warmup_ratio: float = ...
    warmup_steps: int = ...
    log_level: Optional[str] = ...
    log_level_replica: Optional[str] = ...
    log_on_each_node: bool = ...
    logging_dir: Optional[str] = ...
    logging_strategy: Union[IntervalStrategy, str] = ...
    logging_first_step: bool = ...
    logging_steps: int = ...
    logging_nan_inf_filter: bool = ...
    save_strategy: Union[IntervalStrategy, str] = ...
    save_steps: int = ...
    save_total_limit: Optional[int] = ...
    save_on_each_node: bool = ...
    no_cuda: bool = ...
    use_mps_device: bool = ...
    seed: int = ...
    data_seed: Optional[int] = ...
    jit_mode_eval: bool = ...
    use_ipex: bool = ...
    bf16: bool = ...
    fp16: bool = ...
    fp16_opt_level: str = ...
    half_precision_backend: str = ...
    bf16_full_eval: bool = ...
    fp16_full_eval: bool = ...
    tf32: Optional[bool] = ...
    local_rank: int = ...
    xpu_backend: Optional[str] = ...
    tpu_num_cores: Optional[int] = ...
    tpu_metrics_debug: bool = ...
    debug: str = ...
    dataloader_drop_last: bool = ...
    eval_steps: Optional[int] = ...
    dataloader_num_workers: int = ...
    past_index: int = ...
    run_name: Optional[str] = ...
    disable_tqdm: Optional[bool] = ...
    remove_unused_columns: Optional[bool] = ...
    label_names: Optional[List[str]] = ...
    load_best_model_at_end: Optional[bool] = ...
    metric_for_best_model: Optional[str] = ...
    greater_is_better: Optional[bool] = ...
    ignore_data_skip: bool = ...
    sharded_ddp: str = ...
    fsdp: str = ...
    fsdp_min_num_params: int = ...
    fsdp_transformer_layer_cls_to_wrap: Optional[str] = ...
    deepspeed: Optional[str] = ...
    label_smoothing_factor: float = ...
    optim: Union[OptimizerNames, str] = ...
    optim_args: Optional[str] = ...
    adafactor: bool = ...
    group_by_length: bool = ...
    length_column_name: Optional[str] = ...
    report_to: Optional[List[str]] = ...
    ddp_find_unused_parameters: Optional[bool] = ...
    ddp_bucket_cap_mb: Optional[int] = ...
    dataloader_pin_memory: bool = ...
    skip_memory_metrics: bool = ...
    use_legacy_prediction_loop: bool = ...
    push_to_hub: bool = ...
    resume_from_checkpoint: Optional[str] = ...
    hub_model_id: Optional[str] = ...
    hub_strategy: Union[HubStrategy, str] = ...
    hub_token: Optional[str] = ...
    hub_private_repo: bool = ...
    gradient_checkpointing: bool = ...
    include_inputs_for_metrics: bool = ...
    fp16_backend: str = ...
    push_to_hub_model_id: Optional[str] = ...
    push_to_hub_organization: Optional[str] = ...
    push_to_hub_token: Optional[str] = ...
    mp_parameters: str = ...
    auto_find_batch_size: bool = ...
    full_determinism: bool = ...
    torchdynamo: Optional[str] = ...
    ray_scope: Optional[str] = ...
    ddp_timeout: Optional[int] = ...
    torch_compile: bool = ...
    torch_compile_backend: Optional[str] = ...
    torch_compile_mode: Optional[str] = ...
    hf_deepspeed_config = ...
    def __post_init__(self) -> None: ...
    @property
    def train_batch_size(self) -> int:
        """
        The actual batch size for training (may differ from `per_gpu_train_batch_size` in distributed training).
        """
    @property
    def eval_batch_size(self) -> int:
        """
        The actual batch size for evaluation (may differ from `per_gpu_eval_batch_size` in distributed training).
        """
    @property
    def ddp_timeout_delta(self) -> timedelta:
        """
        The actual timeout for torch.distributed.init_process_group since it expects a timedelta variable.
        """
    @property
    def device(self) -> torch.device:
        """
        The device used by this process.
        """
    @property
    def n_gpu(self):
        """
        The number of GPUs used by this process.

        Note:
            This will only be greater than one when you have multiple GPUs available but are not using distributed
            training. For distributed training, it will always be 1.
        """
    @property
    def parallel_mode(self):
        """
        The current mode used for parallelism if multiple GPUs/TPU cores are available. One of:

        - `ParallelMode.NOT_PARALLEL`: no parallelism (CPU or one GPU).
        - `ParallelMode.NOT_DISTRIBUTED`: several GPUs in one single process (uses `torch.nn.DataParallel`).
        - `ParallelMode.DISTRIBUTED`: several GPUs, each having its own process (uses
          `torch.nn.DistributedDataParallel`).
        - `ParallelMode.TPU`: several TPU cores.
        """
    @property
    def world_size(self):
        """
        The number of processes used in parallel.
        """
    @property
    def process_index(self):
        """
        The index of the current process used.
        """
    @property
    def local_process_index(self):
        """
        The index of the local process used.
        """
    @property
    def should_log(self):
        """
        Whether or not the current process should produce log.
        """
    @property
    def should_save(self):
        """
        Whether or not the current process should write to disk, e.g., to save models and checkpoints.
        """
    def get_process_log_level(self):
        """
        Returns the log level to be used depending on whether this process is the main process of node 0, main process
        of node non-0, or a non-main process.

        For the main process the log level defaults to `logging.INFO` unless overridden by `log_level` argument.

        For the replica processes the log level defaults to `logging.WARNING` unless overridden by `log_level_replica`
        argument.

        The choice between the main and replica process settings is made according to the return value of `should_log`.
        """
    @property
    def place_model_on_device(self):
        """
        Can be subclassed and overridden for some specific integrations.
        """
    def main_process_first(self, local: bool = True, desc: str = 'work') -> Generator[None, None, None]:
        '''
        A context manager for torch distributed environment where on needs to do something on the main process, while
        blocking replicas, and when it\'s finished releasing the replicas.

        One such use is for `datasets`\'s `map` feature which to be efficient should be run once on the main process,
        which upon completion saves a cached version of results and which then automatically gets loaded by the
        replicas.

        Args:
            local (`bool`, *optional*, defaults to `True`):
                if `True` first means process of rank 0 of each node if `False` first means process of rank 0 of node
                rank 0 In multi-node environment with a shared filesystem you most likely will want to use
                `local=False` so that only the main process of the first node will do the processing. If however, the
                filesystem is not shared, then the main process of each node will need to do the processing, which is
                the default behavior.
            desc (`str`, *optional*, defaults to `"work"`):
                a work description to be used in debug logs

        '''
    def get_warmup_steps(self, num_training_steps: int):
        """
        Get number of steps used for a linear warmup.
        """
    def to_dict(self):
        """
        Serializes this instance while replace `Enum` by their values (for JSON serialization support). It obfuscates
        the token values by removing their value.
        """
    def to_json_string(self):
        """
        Serializes this instance to a JSON string.
        """
    def to_sanitized_dict(self) -> Dict[str, Any]:
        """
        Sanitized serialization to use with TensorBoard’s hparams
        """
    def __init__(self, output_dir, overwrite_output_dir, do_train, do_eval, do_predict, evaluation_strategy, prediction_loss_only, per_device_train_batch_size, per_device_eval_batch_size, per_gpu_train_batch_size, per_gpu_eval_batch_size, gradient_accumulation_steps, eval_accumulation_steps, eval_delay, learning_rate, weight_decay, adam_beta1, adam_beta2, adam_epsilon, max_grad_norm, num_train_epochs, max_steps, lr_scheduler_type, warmup_ratio, warmup_steps, log_level, log_level_replica, log_on_each_node, logging_dir, logging_strategy, logging_first_step, logging_steps, logging_nan_inf_filter, save_strategy, save_steps, save_total_limit, save_on_each_node, no_cuda, use_mps_device, seed, data_seed, jit_mode_eval, use_ipex, bf16, fp16, fp16_opt_level, half_precision_backend, bf16_full_eval, fp16_full_eval, tf32, local_rank, xpu_backend, tpu_num_cores, tpu_metrics_debug, debug, dataloader_drop_last, eval_steps, dataloader_num_workers, past_index, run_name, disable_tqdm, remove_unused_columns, label_names, load_best_model_at_end, metric_for_best_model, greater_is_better, ignore_data_skip, sharded_ddp, fsdp, fsdp_min_num_params, fsdp_transformer_layer_cls_to_wrap, deepspeed, label_smoothing_factor, optim, optim_args, adafactor, group_by_length, length_column_name, report_to, ddp_find_unused_parameters, ddp_bucket_cap_mb, dataloader_pin_memory, skip_memory_metrics, use_legacy_prediction_loop, push_to_hub, resume_from_checkpoint, hub_model_id, hub_strategy, hub_token, hub_private_repo, gradient_checkpointing, include_inputs_for_metrics, fp16_backend, push_to_hub_model_id, push_to_hub_organization, push_to_hub_token, mp_parameters, auto_find_batch_size, full_determinism, torchdynamo, ray_scope, ddp_timeout, torch_compile, torch_compile_backend, torch_compile_mode) -> None: ...

class ParallelMode(Enum):
    NOT_PARALLEL: str
    NOT_DISTRIBUTED: str
    DISTRIBUTED: str
    SAGEMAKER_MODEL_PARALLEL: str
    SAGEMAKER_DATA_PARALLEL: str
    TPU: str
