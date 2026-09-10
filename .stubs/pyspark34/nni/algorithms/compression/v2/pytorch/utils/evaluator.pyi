import pytorch_lightning as pl
from .constructor_helper import LRSchedulerConstructHelper as LRSchedulerConstructHelper, OptimizerConstructHelper as OptimizerConstructHelper
from _typeshed import Incomplete
from nni.common import is_traceable as is_traceable
from torch import Tensor
from torch.nn import Module
from torch.optim import Optimizer
from torch.optim.lr_scheduler import _LRScheduler
from torch.utils.hooks import RemovableHandle as RemovableHandle
from transformers.trainer import Trainer as HFTrainer
from typing import Any, Callable, Dict, List, Tuple

LIGHTNING_INSTALLED: bool
TRANSFORMERS_INSTALLED: bool

class Hook:
    """
    The base class used to generate, register and remove torch hook.

    Parameters
    ----------
    target
        The hook target, a torch.Tensor or a torch.nn.Module.
    target_name
        The name of the target, use periods to separate, e.g., 'model.layers.0.conv1.weight'.
    hook_factory
        A factory fucntion, input is an empty list, output is a hook function.
        The empty list is used to store some useful information in hook.
    """
    target: Incomplete
    target_name: Incomplete
    hook_factory: Incomplete
    buffer: Incomplete
    handle: Incomplete
    def __init__(self, target: Module | Tensor, target_name: str, hook_factory: Callable[[List], Callable]) -> None: ...
    def register(self) -> None: ...
    def remove(self) -> None: ...

class TensorHook(Hook):
    """
    Here is an example for hook_factory, in this example, the gradient on this tensor will be saved in the buffer::

        def hook_factory(buffer):
            def hook(grad):
                buffer.append(grad.clone())
            return hook
    """
    def __init__(self, target: Tensor, target_name: str, hook_factory: Callable[[List], Callable[[Tensor], Tensor | None]]) -> None: ...

class ModuleHook(Hook):
    def __init__(self, target: Module, target_name: str, hook_factory: Callable[[List], Callable[[Module, Any, Any], Any]]) -> None: ...

class ForwardHook(ModuleHook):
    """
    Here is an example for hook_factory, in this example, the output of this module will be saved in the buffer::

        def hook_factory(buffer):
            def hook(module, input, output):
                buffer.append(output.clone())
            return hook
    """
class BackwardHook(ModuleHook):
    """
    Here is an example for hook_factory, in this example, the gradient of this module input will be saved in the buffer::

        def hook_factory(buffer):
            def hook(module, grad_input, grad_output):
                buffer.append(grad_input.clone())
            return hook
    """

class Evaluator:
    """
    Evaluator is a package for the training & evaluation process. In model compression,
    NNI have the need to intervene in the training process to collect intermediate information,
    and even modify part of the training loop. Evaluator provides a series of member functions that are convenient to modify these,
    and the pruner (or quantizer) can easily intervene in training by calling these functions.

    Notes
    -----
    Users are not recommended to use any member functions of this class.
    """
    def bind_model(self, model: Module | pl.LightningModule, param_names_map: Dict[str, str] | None = None):
        """
        Bind the model suitable for this ``Evaluator`` to use the evaluator's abilities of model modification,
        model training, and model evaluation.

        Parameter
        ---------
        model
            The model bind to this ``Evaluator``, usually a wrapped model.
        param_names_map
            ``param_names_map`` maps the names of the parameters in the pure_model to the names of the parameters in the bound model.
            The format of param_names_map is {pure_model_param_name: bound_model_param_name}.
            It is for initializing the optimizers for the bound model.
        """
    def unbind_model(self) -> None:
        """
        Unbind the model bound by ``bind_model``. Then ``Evaluator`` can be reused by binding a new model by `bind_model`.
        """
    def patch_loss(self, patch: Callable[[Tensor], Tensor]):
        """
        The patch may add additional loss or replace the original loss. Here is an example::

            def loss_patch(original_loss):
                params_norm = 0
                for param in model.parameters():
                    params_norm += torch.norm(param)
                return original_loss + params_norm

        Something like ``loss = patch(criterion(result, target))`` will happen during each time loss computation.
        """
    def revert_loss(self) -> None:
        """
        Revert the loss to the original one.
        """
    def patch_optimizer_step(self, before_step_tasks: List[Callable], after_step_tasks: List[Callable]):
        """
        Run tasks in `before_step_tasks` before `optimizer.step()` each time.
        Run tasks in `after_step_tasks` after `optimizer.step()` each time.

        Notes
        -----
        If the model has multiple optimizers, this function only patches tasks to the first optimizer right now.
        """
    def revert_optimizer_step(self) -> None:
        """
        Revert the optimizer step to the original one.
        """
    def register_hooks(self, hooks: List[Hook]):
        """
        The input is a list of ``TensorHook``, ``ForwardHook``, ``BackwardHook``,
        please view how to use ``TensorHook``, ``ForwardHook``, ``BackwardHook``.
        This function will call ``Hook.register()`` of hook in ``hooks``, and record the hook in ``self._hooks``.
        """
    def get_all_hooks(self) -> List[Hook]:
        """
        Get all registered ``Hook``.
        """
    def remove_all_hooks(self) -> None:
        """
        Call ``Hook.remove()`` of all ``Hook`` instances in ``self._hooks``, then clear ``self._hooks``.
        """
    def train(self, max_steps: int | None = None, max_epochs: int | None = None):
        """
        Train the bound model with default optimization loop defined by user and only change the training duration.
        """
    def finetune(self) -> None:
        """
        Finetune the bound model with default optimization loop defined by user.
        """
    def evaluate(self) -> float | None | Tuple[float, Any] | Tuple[None, Any]:
        """
        NNI assume the evaluation function user passed in should return a float number or a dict as metric.
        If the evaluation function returned a dict, take the value with dict key ``default``
        as the first element of ``evaluate`` returned value,
        and put the dict as the second element of the returned value.
        For any other type of the metric returned by evaluation function, ``evaluate`` will directly returned
        (it should be a float, but NNI does not prevent other types from being returned,
        this will handle by the object calling ``evaluate``).
        """
    def get_dummy_input(self) -> Any:
        """
        The returned value is a dummy input for the model, always used by ``torch.jit.trace``.
        """

class LightningEvaluator(Evaluator):
    """
    LightningEvaluator is the Evaluator based on PyTorchLightning.
    It is very friendly to the users who are familiar to PyTorchLightning
    or already have training/validation/testing code written in PyTorchLightning.
    The only need is to use ``nni.trace`` to trace the Trainer & LightningDataModule.

    Additionally, please make sure the ``Optimizer`` class and ``LR_Scheduler`` class used in ``LightningModule.configure_optimizers()``
    are also be traced by ``nni.trace``.

    Please refer to the :doc:`/compression/compression_evaluator` for the evaluator initialization example.

    Parameters
    ----------
    trainer
        Pytorch-Lightning Trainer. It should be traced by nni, e.g., ``trainer = nni.trace(pl.Trainer)(...)``.
    data_module
        Pytorch-Lightning LightningDataModule. It should be traced by nni, e.g., ``data_module = nni.trace(pl.LightningDataModule)(...)``.
    dummy_input
        The dummy_input is used to trace the graph. If dummy_input is not given, will use the data in data_module.train_dataloader().

    Notes
    -----
    If the the test metric is needed by nni, please make sure log metric with key ``default`` in ``LightningModule.test_step()``.
    """
    trainer: Incomplete
    data_module: Incomplete
    model: Incomplete
    def __init__(self, trainer: pl.Trainer, data_module: pl.LightningDataModule, dummy_input: Any | None = None) -> None: ...
    def bind_model(self, model: pl.LightningModule, param_names_map: Dict[str, str] | None = None): ...
    def unbind_model(self) -> None: ...
    def patch_loss(self, patch: Callable[[Tensor], Tensor]): ...
    def revert_loss(self) -> None: ...
    def patch_optimizer_step(self, before_step_tasks: List[Callable], after_step_tasks: List[Callable]): ...
    def revert_optimizer_step(self) -> None: ...
    def train(self, max_steps: int | None = None, max_epochs: int | None = None): ...
    def finetune(self) -> None: ...
    def evaluate(self) -> Tuple[float | None, List[Dict[str, float]]]:
        """
        NNI will use metric with key ``default`` for evaluating model,
        please make sure you have this key in your ``Trainer.test()`` returned metric dicts.
        If ``Trainer.test()`` returned list contains multiple dicts with key ``default``,
        NNI will take their average as the final metric.
        E.g., if ``Trainer.test()`` returned ``[{'default': 0.8, 'loss': 2.3}, {'default': 0.6, 'loss': 2.4}]``,
        NNI will take the final metric ``(0.8 + 0.6) / 2 = 0.7``.
        """
    def get_dummy_input(self) -> Any: ...

class TorchEvaluator(Evaluator):
    """
    TorchEvaluator is the Evaluator for native PyTorch users.
    Please refer to the :doc:`/compression/compression_evaluator` for the evaluator initialization example.

    Parameters
    ----------
    training_func
        The training function is used to train the model, note that this a entire optimization training loop.
        Training function has three required parameters, ``model``, ``optimizers`` and ``criterion``,
        and three optional parameters, ``lr_schedulers``, ``max_steps``, ``max_epochs``.

        Let's explain these six parameters NNI passed in, but in most cases, users don't need to care about these.
        Users only need to treat these six parameters as the original parameters during the training process.

        * The ``model`` is a wrapped model from the original model, it has a similar structure to the model to be pruned,
          so it can share training function with the original model.
        * ``optimizers`` are re-initialized from the ``optimizers`` passed to the evaluator and the wrapped model's parameters.
        * ``criterion`` also based on the ``criterion`` passed to the evaluator,
          it might be modified modified by the pruner during model pruning.
        * If users use ``lr_schedulers`` in the ``training_func``, NNI will re-initialize the ``lr_schedulers`` with the re-initialized
          optimizers.
        * ``max_steps`` is the NNI training duration limitation. It is for pruner (or quantizer) to control the number of training steps.
          The user implemented ``training_func`` should respect ``max_steps`` by stopping the training loop after ``max_steps`` is reached.
          Pruner may pass ``None`` to ``max_steps`` when it only controls ``max_epochs``.
        * ``max_epochs`` is similar to the ``max_steps``, the only different is that it controls the number of training epochs.
          The user implemented ``training_func`` should respect ``max_epochs`` by stopping the training loop
          after ``max_epochs`` is reached. Pruner may pass ``None`` to ``max_epochs`` when it only controls ``max_steps``.

        Note that when the pruner passes ``None`` to both ``max_steps`` and ``max_epochs``,
        it treats ``training_func`` as a function of model fine-tuning.
        Users should assign proper values to ``max_steps`` and ``max_epochs``.

        .. code-block:: python

            def training_func(model: torch.nn.Module, optimizers: torch.optim.Optimizer,
                              criterion: Callable[[Any, Any], torch.Tensor],
                              lr_schedulers: _LRScheduler | None = None, max_steps: int | None = None,
                              max_epochs: int | None = None, *args, **kwargs):

                ...

                total_epochs = max_epochs if max_epochs else 20
                total_steps = max_steps if max_steps else 1000000
                current_steps = 0

                ...

                for epoch in range(total_epochs):

                    ...

                    if current_steps >= total_steps:
                        return

        Note that ``optimizers`` and ``lr_schedulers`` passed to the ``training_func`` have the same type as the ``optimizers``
        and ``lr_schedulers`` passed to evaluator, a single ``torch.optim.Optimzier``/ ``torch.optim._LRScheduler`` instance or
        a list of them.

    optimziers
        A single traced optimizer instance or a list of traced optimizers by ``nni.trace``.

        NNI may modify the ``torch.optim.Optimizer`` member function ``step`` and/or optimize compressed models,
        so NNI needs to have the ability to re-initialize the optimizer. ``nni.trace`` can record the initialization parameters
        of a function/class, which can then be used by NNI to re-initialize the optimizer for a new but structurally similar model.

        E.g. ``traced_optimizer = nni.trace(torch.nn.Adam)(model.parameters())``.
    criterion
        The criterion function used in trainer. Take model output and target as input, and return the loss.

        E.g. ``criterion = torch.nn.functional.nll_loss``.
    lr_schedulers
        Optional. A single traced lr_scheduler instance or a list of traced lr_schedulers by ``nni.trace``.
        For the same reason with ``optimizers``, NNI needs the traced lr_scheduler to re-initialize it.

        E.g. ``traced_lr_scheduler = nni.trace(ExponentialLR)(optimizer, 0.1)``.
    dummy_input
        Optional. The dummy_input is used to trace the graph, it's same with ``example_inputs`` in
        `torch.jit.trace <https://pytorch.org/docs/stable/generated/torch.jit.trace.html?highlight=torch%20jit%20trace#torch.jit.trace>`_.
    evaluating_func
        Optional. A function that input is model and return the evaluation metric.
        This is the function used to evaluate the compressed model performance.
        The input is a model and the output is a ``float`` metric or a ``dict``
        (``dict`` should contains key ``default`` with a ``float`` value).
        NNI will take the float number as the model score, and assume the higher score means the better performance.
        If you want to provide additional information, please put it into a dict
        and NNI will take the value of key ``default`` as evaluation metric.

    Notes
    -----
    It is also worth to note that not all the arguments of ``TorchEvaluator`` must be provided.
    Some pruners (or quantizers) only require ``evaluating_func`` as they do not train the model,
    some pruners (or quantizers) only require ``training_func``.
    Please refer to each pruner's (or quantizer's) doc to check the required arguments.
    But, it is fine to provide more arguments than the pruner's (or quantizer's) need.
    """
    training_func: Incomplete
    dummy_input: Incomplete
    evaluating_func: Incomplete
    model: Incomplete
    def __init__(self, training_func: _TRAINING_FUNC, optimizers: Optimizer | List[Optimizer], criterion: _CRITERION, lr_schedulers: _LRScheduler | List[_LRScheduler] | None = None, dummy_input: Any | None = None, evaluating_func: _EVALUATING_FUNC | None = None) -> None: ...
    def bind_model(self, model: Module, param_names_map: Dict[str, str] | None = None): ...
    def unbind_model(self) -> None: ...
    def patch_loss(self, patch: Callable[[Tensor], Tensor]): ...
    def revert_loss(self) -> None: ...
    def patch_optimizer_step(self, before_step_tasks: List[Callable], after_step_tasks: List[Callable]): ...
    def revert_optimizer_step(self) -> None: ...
    def train(self, max_steps: int | None = None, max_epochs: int | None = None): ...
    def finetune(self) -> None: ...
    def evaluate(self) -> float | None | Tuple[float, Dict[str, Any]] | Tuple[None, Dict[str, Any]]: ...
    def get_dummy_input(self) -> Any: ...

class TransformersEvaluator(Evaluator):
    """
    TransformersEvaluator is for the users who using Huggingface ``transformers.trainer.Trainer``.

    Here is an example for using ``transformers.trainer.Trainer`` to initialize an evaluator:

    .. code-block:: python

        from transformers.trainer import Trainer

        # wrap Trainer class with nni.trace
        trainer = nni.trace(Trainer)(model=model)
        evaluator = TransformersEvaluator(trainer)

        # if you want to using customized optimizer & lr_scheduler, please also wrap Optimzier & _LRScheduler class
        optimizer = nni.trace(Adam)(...)
        lr_scheduler = nni.trace(LambdaLR)(...)
        trainer = nni.trace(Trainer)(model=model, ..., optimizers=(optimizer, lr_scheduler))
        evaluator = TransformersEvaluator(trainer)

    Parameters
    ----------
    trainer
        ``nni.trace(transformers.trainer.Trainer)`` instance. The trainer will be re-initialized inside evaluator,
        so wrap with ``nni.trace`` is required for getting the initialization arguments.
    dummy_input
        Optional. The dummy_input is used to trace the graph, it's same with ``example_inputs`` in
        `torch.jit.trace <https://pytorch.org/docs/stable/generated/torch.jit.trace.html?highlight=torch%20jit%20trace#torch.jit.trace>`_.
    """
    traced_trainer: Incomplete
    dummy_input: Incomplete
    model: Incomplete
    def __init__(self, trainer: HFTrainer, dummy_input: Any | None = None) -> None: ...
    trainer: Incomplete
    def bind_model(self, model: Module | pl.LightningModule, param_names_map: Dict[str, str] | None = None): ...
    def unbind_model(self) -> None: ...
    def patch_loss(self, patch: Callable[[Tensor], Tensor]): ...
    def revert_loss(self) -> None: ...
    def patch_optimizer_step(self, before_step_tasks: List[Callable], after_step_tasks: List[Callable]): ...
    def revert_optimizer_step(self) -> None: ...
    def train(self, max_steps: int | None = None, max_epochs: int | None = None): ...
    def finetune(self) -> None: ...
    def evaluate(self) -> float | None | Tuple[float, Dict[str, Any]] | Tuple[None, Dict[str, Any]]: ...
    def get_dummy_input(self) -> Any: ...
