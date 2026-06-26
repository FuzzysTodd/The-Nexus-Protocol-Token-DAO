from .training_args import TrainingArguments as TrainingArguments
from .utils import add_start_docstrings as add_start_docstrings
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Optional

logger: Incomplete

@dataclass
class Seq2SeqTrainingArguments(TrainingArguments):
    """
    Args:
        sortish_sampler (`bool`, *optional*, defaults to `False`):
            Whether to use a *sortish sampler* or not. Only possible if the underlying datasets are *Seq2SeqDataset*
            for now but will become generally available in the near future.

            It sorts the inputs according to lengths in order to minimize the padding size, with a bit of randomness
            for the training set.
        predict_with_generate (`bool`, *optional*, defaults to `False`):
            Whether to use generate to calculate generative metrics (ROUGE, BLEU).
        generation_max_length (`int`, *optional*):
            The `max_length` to use on each evaluation loop when `predict_with_generate=True`. Will default to the
            `max_length` value of the model configuration.
        generation_num_beams (`int`, *optional*):
            The `num_beams` to use on each evaluation loop when `predict_with_generate=True`. Will default to the
            `num_beams` value of the model configuration.
    """
    sortish_sampler: bool = ...
    predict_with_generate: bool = ...
    generation_max_length: Optional[int] = ...
    generation_num_beams: Optional[int] = ...
    def __init__(self, output_dir, overwrite_output_dir, do_train, do_eval, do_predict, evaluation_strategy, prediction_loss_only, per_device_train_batch_size, per_device_eval_batch_size, per_gpu_train_batch_size, per_gpu_eval_batch_size, gradient_accumulation_steps, eval_accumulation_steps, eval_delay, learning_rate, weight_decay, adam_beta1, adam_beta2, adam_epsilon, max_grad_norm, num_train_epochs, max_steps, lr_scheduler_type, warmup_ratio, warmup_steps, log_level, log_level_replica, log_on_each_node, logging_dir, logging_strategy, logging_first_step, logging_steps, logging_nan_inf_filter, save_strategy, save_steps, save_total_limit, save_on_each_node, no_cuda, use_mps_device, seed, data_seed, jit_mode_eval, use_ipex, bf16, fp16, fp16_opt_level, half_precision_backend, bf16_full_eval, fp16_full_eval, tf32, local_rank, xpu_backend, tpu_num_cores, tpu_metrics_debug, debug, dataloader_drop_last, eval_steps, dataloader_num_workers, past_index, run_name, disable_tqdm, remove_unused_columns, label_names, load_best_model_at_end, metric_for_best_model, greater_is_better, ignore_data_skip, sharded_ddp, fsdp, fsdp_min_num_params, fsdp_transformer_layer_cls_to_wrap, deepspeed, label_smoothing_factor, optim, optim_args, adafactor, group_by_length, length_column_name, report_to, ddp_find_unused_parameters, ddp_bucket_cap_mb, dataloader_pin_memory, skip_memory_metrics, use_legacy_prediction_loop, push_to_hub, resume_from_checkpoint, hub_model_id, hub_strategy, hub_token, hub_private_repo, gradient_checkpointing, include_inputs_for_metrics, fp16_backend, push_to_hub_model_id, push_to_hub_organization, push_to_hub_token, mp_parameters, auto_find_batch_size, full_determinism, torchdynamo, ray_scope, ddp_timeout, torch_compile, torch_compile_backend, torch_compile_mode, sortish_sampler, predict_with_generate, generation_max_length, generation_num_beams) -> None: ...
