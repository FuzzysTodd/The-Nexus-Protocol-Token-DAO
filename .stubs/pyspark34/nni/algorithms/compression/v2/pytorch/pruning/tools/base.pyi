from ...base import LayerInfo as LayerInfo, Pruner as Pruner, Task as Task, TaskResult as TaskResult
from ...utils import Evaluator as Evaluator, Hook as Hook, OptimizerConstructHelper as OptimizerConstructHelper, Scaling as Scaling
from _typeshed import Incomplete
from pathlib import Path
from torch import Tensor
from torch.nn import Module
from torch.optim import Optimizer
from typing import Callable, Dict, List, Tuple
from typing_extensions import Literal

class DataCollector:
    """
    An abstract class for collect the data needed by the compressor.

    Parameters
    ----------
    compressor
        The compressor binded with this DataCollector.
    """
    compressor: Incomplete
    def __init__(self, compressor: Pruner) -> None: ...
    def reset(self, *args, **kwargs) -> None:
        """
        Reset the `DataCollector`.
        """
    def collect(self) -> Dict:
        """
        Collect the compressor needed data, i.e., module weight, the output of activation function.

        Returns
        -------
        Dict
            Usually has format like {module_name: tensor_type_data}.
        """
COLLECTOR_TYPE = Callable[[List, Tensor], Callable[[Tensor], None]] | Callable[[List], Callable[[Module, Tensor, Tensor], None]]

class HookCollectorInfo:
    targets: Incomplete
    hook_type: Incomplete
    collector: Incomplete
    def __init__(self, targets: Dict[str, Tensor] | List[LayerInfo], hook_type: str, collector: COLLECTOR_TYPE) -> None:
        """
        This class used to aggregate the information of what kind of hook is placed on which layers.

        Parameters
        ----------
        targets
            List of LayerInfo or Dict of {layer_name: weight_tensor}, the hook targets.
        hook_type
            'forward' or 'backward'.
        collector
            A hook function generator, the input is a buffer (empty list) or a buffer (empty list) and tensor,
            the output is a hook function. The buffer is used to store the data wanted to hook.
        """

class TrainerBasedDataCollector(DataCollector):
    """
    This class includes some trainer based util functions, i.e., patch optimizer or criterion, add hooks.
    """
    trainer: Incomplete
    training_epochs: Incomplete
    optimizer_helper: Incomplete
    def __init__(self, compressor: Pruner, trainer: Callable[[Module, Optimizer, Callable], None], optimizer_helper: OptimizerConstructHelper, criterion: Callable[[Tensor, Tensor], Tensor], training_epochs: int, opt_before_tasks: List = [], opt_after_tasks: List = [], collector_infos: List[HookCollectorInfo] = [], criterion_patch: Callable[[Callable], Callable] | None = None) -> None:
        '''
        Parameters
        ----------
        compressor
            The compressor binded with this DataCollector.
        trainer
            A callable function used to train model or just inference. Take model, optimizer, criterion as input.
            The model will be trained or inferenced `training_epochs` epochs.

            Example::

                def trainer(model: Module, optimizer: Optimizer, criterion: Callable[[Tensor, Tensor], Tensor]):
                    training = model.training
                    model.train(mode=True)
                    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
                    for batch_idx, (data, target) in enumerate(train_loader):
                        data, target = data.to(device), target.to(device)
                        optimizer.zero_grad()
                        output = model(data)
                        loss = criterion(output, target)
                        loss.backward()
                        # If you don\'t want to update the model, you can skip `optimizer.step()`, and set train mode False.
                        optimizer.step()
                    model.train(mode=training)
        optimizer
            The optimizer instance used in trainer. Note that this optimizer might be patched during collect data,
            so do not use this optimizer in other places.
        criterion
            The criterion function used in trainer. Take model output and target value as input, and return the loss.
        training_epochs
            The total number of calling trainer.
        opt_before_tasks
            A list of function that will be called one by one before origin `optimizer.step()`.
            Note that these functions will be patched into `optimizer.step()`.
        opt_after_tasks
            A list of function that will be called one by one after origin `optimizer.step()`.
            Note that these functions will be patched into `optimizer.step()`.
        collector_infos
            A list of `HookCollectorInfo` instance. And the hooks will be registered in `__init__`.
        criterion_patch
            A callable function used to patch the criterion. Take a criterion function as input and return a new one.

            Example::

                def criterion_patch(criterion: Callable[[Tensor, Tensor], Tensor]) -> Callable[[Tensor, Tensor], Tensor]:
                    weight = ...
                    def patched_criterion(output, target):
                        return criterion(output, target) + torch.norm(weight)
                    return patched_criterion
        '''
    criterion: Incomplete
    def reset(self, collector_infos: List[HookCollectorInfo] = []): ...

class EvaluatorBasedDataCollector(DataCollector):
    """
    This data collector is the base class for the data collectors that want to use ``Evaluator`` to train or inference.
    Three main usages are supported in this data collector:

    1. Doing something before ``optimzer.step()`` and after ``optimzer.step()``. ``before_opt_step_tasks`` is a list of task functions
       that will execute before ``optimzer.step()``. ``after_opt_step_tasks`` is a list of task functions that will execute after
       ``optimzer.step()``. All the task functions in the list should not have input arguments, function return value is allowed,
       but ``Evaluator`` will not catch it.
    2. Patch or modify the training loss. ``loss_patch`` is a function with input is the original loss and the output is the modified loss.
    3. Add hooks on ``torch.nn.Module`` or ``Parameter`` or ``Buffer``. Three kinds of hook are supported, ``TensorHook``, ``ForwardHook``
       and ``BackwardHook``. For initializing a ``Hook``, a hook function factory is needed, the factory function's input is an empty list,
       and the output is a hook function defined by Pytorch.
       Please refer `register_hook <https://pytorch.org/docs/stable/generated/torch.Tensor.register_hook.html>`_,
       `register_forward_hook <https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_forward_hook>`_,
       `register_backward_hook <https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_backward_hook>`_.
    """
    evaluator: Incomplete
    max_steps: Incomplete
    max_epochs: Incomplete
    def __init__(self, compressor: Pruner, evaluator: Evaluator, before_opt_step_tasks: List[Callable] | None = None, after_opt_step_tasks: List[Callable] | None = None, loss_patch: Callable[[Tensor], Tensor] | None = None, hooks: Dict[str, Dict[str, Hook]] | None = None, max_steps: int | None = None, max_epochs: int | None = None) -> None: ...
    def reset(self, before_opt_step_tasks: List[Callable] | None = None, after_opt_step_tasks: List[Callable] | None = None, loss_patch: Callable[[Tensor], Tensor] | None = None, hooks: Dict[str, Dict[str, Hook]] | None = None): ...

class MetricsCalculator:
    """
    An abstract class for calculate a kind of metrics of the given data.

    Parameters
    ----------
    scalers
        Scaler is used to scale the metrics' size. It scaling metric to the same size as the shrinked mask in the sparsity allocator.
        If you want to use different scalers for different pruning targets in different modules,
        please use a dict `{module_name: {target_name: scaler}}`.
        If allocator meets an unspecified module name, it will try to use `scalers['_default'][target_name]` to scale its mask.
        If allocator meets an unspecified target name, it will try to use `scalers[module_name]['_default']` to scale its mask.
        Passing in a scaler instead of a `dict` of scalers will be treated as passed in `{'_default': {'_default': scalers}}`.
        Passing in `None` means no need to scale.
    """
    scalers: Incomplete
    def __init__(self, scalers: Dict[str, Dict[str, Scaling]] | Scaling | None = None) -> None: ...
    def calculate_metrics(self, data: Dict) -> Dict[str, Tensor]:
        """
        Parameters
        ----------
        data
            A dict handle the data used to calculate metrics. Usually has format like {module_name: tensor_type_data}.

        Returns
        -------
        Dict[str, Tensor]
            The key is the layer_name, value is the metric.
            Note that the metric has the same size with the data size on `dim`.
        """

class SparsityAllocator:
    """
    A base class for allocating mask based on metrics.

    Parameters
    ----------
    pruner
        The pruner that binded with this `SparsityAllocator`.
    scalers
        Scaler is used to scale the masks' size. It shrinks the mask of the same size as the pruning target to the same size as the metric,
        or expands the mask of the same size as the metric to the same size as the pruning target.
        If you want to use different scalers for different pruning targets in different modules,
        please use a dict `{module_name: {target_name: scaler}}`.
        If allocator meets an unspecified module name, it will try to use `scalers['_default'][target_name]` to scale its mask.
        If allocator meets an unspecified target name, it will try to use `scalers[module_name]['_default']` to scale its mask.
        Passing in a scaler instead of a `dict` of scalers will be treated as passed in `{'_default': {'_default': scalers}}`.
        Passing in `None` means no need to scale.
    continuous_mask
        If set True, the part that has been masked will be masked first.
        If set False, the part that has been masked may be unmasked due to the increase of its corresponding metric.
    """
    pruner: Incomplete
    scalers: Incomplete
    continuous_mask: Incomplete
    def __init__(self, pruner: Pruner, scalers: Dict[str, Dict[str, Scaling]] | Scaling | None = None, continuous_mask: bool = True) -> None: ...
    def common_target_masks_generation(self, metrics: Dict[str, Dict[str, Tensor]]) -> Dict[str, Dict[str, Tensor]]:
        """
        Generate masks for metrics-dependent targets.

        Parameters
        ----------
        metrics
            The format is {module_name: {target_name: target_metric}}.
            The metric of usually has the same size with shrinked mask.

        Return
        ------
        Dict[str, Dict[str, Tensor]]
            The format is {module_name: {target_name: mask}}.
            Return the masks of the same size as its target.
        """
    def special_target_masks_generation(self, masks: Dict[str, Dict[str, Tensor]]) -> Dict[str, Dict[str, Tensor]]:
        """
        Some pruning targets' mask generation depends on other targets, i.e., bias mask depends on weight mask.
        This function is used to generate these masks, and it be called at the end of `generate_sparsity`.

        Parameters
        ----------
        masks
            The format is {module_name: {target_name: mask}}.
            It is usually the return value of `common_target_masks_generation`.
        """
    def generate_sparsity(self, metrics: Dict) -> Dict[str, Dict[str, Tensor]]:
        """
        The main function of `SparsityAllocator`, generate a set of masks based on the given metrics.

        Parameters
        ----------
        metrics
            A metric dict with format {module_name: weight_metric}

        Returns
        -------
        Dict[str, Dict[str, Tensor]]
            The masks format is {module_name: {target_name: mask}}.
        """

class TaskGenerator:
    """
    This class used to generate config list for pruner in each iteration.

    Parameters
    ----------
    origin_model
        The origin unwrapped pytorch model to be pruned.
    origin_masks
        The pre masks on the origin model. This mask maybe user-defined or maybe generate by previous pruning.
    origin_config_list
        The origin config list provided by the user. Note that this config_list is directly config the origin model.
        This means the sparsity provided by the origin_masks should also be recorded in the origin_config_list.
    log_dir
        The log directory use to saving the task generator log.
    keep_intermediate_result
        If keeping the intermediate result, including intermediate model and masks during each iteration.
    best_result_mode
        The way to decide which one is the best result. Three modes are supported.
        If the task results don't contain scores (task_result.score is None), it will fall back to ``latest``.

        1. latest: The newest received result is the best result.
        2. maximize: The one with largest task result score is the best result.
        3. minimize: The one with smallest task result score is the best result.
    """
    def __init__(self, origin_model: Module | None, origin_masks: Dict[str, Dict[str, Tensor]] | None = {}, origin_config_list: List[Dict] | None = [], log_dir: str | Path = '.', keep_intermediate_result: bool = False, best_result_mode: Literal['latest', 'maximize', 'minimize'] = 'maximize') -> None: ...
    def reset(self, model: Module, config_list: List[Dict] = [], masks: Dict[str, Dict[str, Tensor]] = {}): ...
    def update_best_result(self, task_result: TaskResult): ...
    def init_pending_tasks(self) -> List[Task]: ...
    def generate_tasks(self, task_result: TaskResult) -> List[Task]: ...
    def receive_task_result(self, task_result: TaskResult):
        """
        Parameters
        ----------
        task_result
            The result of the task.
        """
    def next(self) -> Task | None:
        """
        Returns
        -------
        Optional[Task]
            Return the next task from pending tasks.
        """
    def get_best_result(self) -> Tuple[int | str, Module, Dict[str, Dict[str, Tensor]], float | None, List[Dict]] | None:
        """
        Returns
        -------
        Optional[Tuple[int, Module, Dict[str, Dict[str, Tensor]], float, List[Dict]]]
            If self._best_task_id is not None,
            return best task id, best compact model, masks on the compact model, score, config list used in this task.
        """
