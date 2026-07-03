import tensorflow as tf
from .training_args import TrainingArguments as TrainingArguments
from .utils import cached_property as cached_property, is_tf_available as is_tf_available, logging as logging, requires_backends as requires_backends
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Optional

logger: Incomplete

@dataclass
class TFTrainingArguments(TrainingArguments):
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

        per_device_train_batch_size (`int`, *optional*, defaults to 8):
            The batch size per GPU/TPU core/CPU for training.
        per_device_eval_batch_size (`int`, *optional*, defaults to 8):
            The batch size per GPU/TPU core/CPU for evaluation.
        gradient_accumulation_steps: (`int`, *optional*, defaults to 1):
            Number of updates steps to accumulate the gradients for, before performing a backward/update pass.

            <Tip warning={true}>

            When using gradient accumulation, one step is counted as one step with backward pass. Therefore, logging,
            evaluation, save will be conducted every `gradient_accumulation_steps * xxx_step` training examples.

            </Tip>

        learning_rate (`float`, *optional*, defaults to 5e-5):
            The initial learning rate for Adam.
        weight_decay (`float`, *optional*, defaults to 0):
            The weight decay to apply (if not zero).
        adam_beta1 (`float`, *optional*, defaults to 0.9):
            The beta1 hyperparameter for the Adam optimizer.
        adam_beta2 (`float`, *optional*, defaults to 0.999):
            The beta2 hyperparameter for the Adam optimizer.
        adam_epsilon (`float`, *optional*, defaults to 1e-8):
            The epsilon hyperparameter for the Adam optimizer.
        max_grad_norm (`float`, *optional*, defaults to 1.0):
            Maximum gradient norm (for gradient clipping).
        num_train_epochs(`float`, *optional*, defaults to 3.0):
            Total number of training epochs to perform.
        max_steps (`int`, *optional*, defaults to -1):
            If set to a positive number, the total number of training steps to perform. Overrides `num_train_epochs`.
        warmup_ratio (`float`, *optional*, defaults to 0.0):
            Ratio of total training steps used for a linear warmup from 0 to `learning_rate`.
        warmup_steps (`int`, *optional*, defaults to 0):
            Number of steps used for a linear warmup from 0 to `learning_rate`. Overrides any effect of `warmup_ratio`.
        logging_dir (`str`, *optional*):
            [TensorBoard](https://www.tensorflow.org/tensorboard) log directory. Will default to
            *runs/**CURRENT_DATETIME_HOSTNAME***.
        logging_strategy (`str` or [`~trainer_utils.IntervalStrategy`], *optional*, defaults to `"steps"`):
            The logging strategy to adopt during training. Possible values are:

                - `"no"`: No logging is done during training.
                - `"epoch"`: Logging is done at the end of each epoch.
                - `"steps"`: Logging is done every `logging_steps`.

        logging_first_step (`bool`, *optional*, defaults to `False`):
            Whether to log and evaluate the first `global_step` or not.
        logging_steps (`int`, *optional*, defaults to 500):
            Number of update steps between two logs if `logging_strategy="steps"`.
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
        no_cuda (`bool`, *optional*, defaults to `False`):
            Whether to not use CUDA even when it is available or not.
        seed (`int`, *optional*, defaults to 42):
            Random seed that will be set at the beginning of training.
        fp16 (`bool`, *optional*, defaults to `False`):
            Whether to use 16-bit (mixed) precision training (through NVIDIA Apex) instead of 32-bit training.
        fp16_opt_level (`str`, *optional*, defaults to \'O1\'):
            For `fp16` training, Apex AMP optimization level selected in [\'O0\', \'O1\', \'O2\', and \'O3\']. See details on
            the [Apex documentation](https://nvidia.github.io/apex/amp).
        local_rank (`int`, *optional*, defaults to -1):
            During distributed training, the rank of the process.
        tpu_num_cores (`int`, *optional*):
            When training on TPU, the number of TPU cores (automatically passed by launcher script).
        debug (`bool`, *optional*, defaults to `False`):
            Whether to activate the trace to record computation graphs and profiling information or not.
        dataloader_drop_last (`bool`, *optional*, defaults to `False`):
            Whether to drop the last incomplete batch (if the length of the dataset is not divisible by the batch size)
            or not.
        eval_steps (`int`, *optional*, defaults to 1000):
            Number of update steps before two evaluations.
        past_index (`int`, *optional*, defaults to -1):
            Some models like [TransformerXL](../model_doc/transformerxl) or :doc*XLNet <../model_doc/xlnet>* can make
            use of the past hidden states for their predictions. If this argument is set to a positive int, the
            `Trainer` will use the corresponding output (usually index 2) as the past state and feed it to the model at
            the next training step under the keyword argument `mems`.
        tpu_name (`str`, *optional*):
            The name of the TPU the process is running on.
        tpu_zone (`str`, *optional*):
            The zone of the TPU the process is running on. If not specified, we will attempt to automatically detect
            from metadata.
        gcp_project (`str`, *optional*):
            Google Cloud Project name for the Cloud TPU-enabled project. If not specified, we will attempt to
            automatically detect from metadata.
        run_name (`str`, *optional*):
            A descriptor for the run. Notably used for wandb logging.
        xla (`bool`, *optional*):
            Whether to activate the XLA compilation or not.
    '''
    framework = ...
    tpu_name: Optional[str] = ...
    tpu_zone: Optional[str] = ...
    gcp_project: Optional[str] = ...
    poly_power: float = ...
    xla: bool = ...
    @property
    def strategy(self) -> tf.distribute.Strategy:
        """
        The strategy used for distributed training.
        """
    @property
    def n_replicas(self) -> int:
        """
        The number of replicas (CPUs, GPUs or TPU cores) used in this training.
        """
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
    def n_gpu(self) -> int:
        """
        The number of replicas (CPUs, GPUs or TPU cores) used in this training.
        """
    def __init__(self, output_dir, overwrite_output_dir, do_train, do_eval, do_predict, evaluation_strategy, prediction_loss_only, per_device_train_batch_size, per_device_eval_batch_size, per_gpu_train_batch_size, per_gpu_eval_batch_size, gradient_accumulation_steps, eval_accumulation_steps, eval_delay, learning_rate, weight_decay, adam_beta1, adam_beta2, adam_epsilon, max_grad_norm, num_train_epochs, max_steps, lr_scheduler_type, warmup_ratio, warmup_steps, log_level, log_level_replica, log_on_each_node, logging_dir, logging_strategy, logging_first_step, logging_steps, logging_nan_inf_filter, save_strategy, save_steps, save_total_limit, save_on_each_node, no_cuda, use_mps_device, seed, data_seed, jit_mode_eval, use_ipex, bf16, fp16, fp16_opt_level, half_precision_backend, bf16_full_eval, fp16_full_eval, tf32, local_rank, xpu_backend, tpu_num_cores, tpu_metrics_debug, debug, dataloader_drop_last, eval_steps, dataloader_num_workers, past_index, run_name, disable_tqdm, remove_unused_columns, label_names, load_best_model_at_end, metric_for_best_model, greater_is_better, ignore_data_skip, sharded_ddp, fsdp, fsdp_min_num_params, fsdp_transformer_layer_cls_to_wrap, deepspeed, label_smoothing_factor, optim, optim_args, adafactor, group_by_length, length_column_name, report_to, ddp_find_unused_parameters, ddp_bucket_cap_mb, dataloader_pin_memory, skip_memory_metrics, use_legacy_prediction_loop, push_to_hub, resume_from_checkpoint, hub_model_id, hub_strategy, hub_token, hub_private_repo, gradient_checkpointing, include_inputs_for_metrics, fp16_backend, push_to_hub_model_id, push_to_hub_organization, push_to_hub_token, mp_parameters, auto_find_batch_size, full_determinism, torchdynamo, ray_scope, ddp_timeout, torch_compile, torch_compile_backend, torch_compile_mode, tpu_name, tpu_zone, gcp_project, poly_power, xla) -> None: ...
