import pytorch_lightning as pl
import torch.nn as nn
import torch.optim as optim
from .supermodule.base import BaseSuperNetModule as BaseSuperNetModule
from _typeshed import Incomplete
from nni.common.hpo_utils import ParameterSpec
from torch.optim import Optimizer
from typing import Any

__all__ = ['MANUAL_OPTIMIZATION_NOTE', 'MutationHook', 'BaseSuperNetModule', 'BaseOneShotLightningModule', 'traverse_and_mutate_submodules', 'no_default_hook']

MANUAL_OPTIMIZATION_NOTE: str
MutationHook: Incomplete

def traverse_and_mutate_submodules(root_module: nn.Module, hooks: list[MutationHook], mutate_kwargs: dict[str, Any], topdown: bool = True) -> list[BaseSuperNetModule]:
    """
    Traverse the module-tree of ``root_module``, and call ``hooks`` on every tree node.

    Parameters
    ----------
    root_module : nn.Module
        User-defined model space.
        Since this method is called in the ``__init__`` of :class:`BaseOneShotLightningModule`,
        it's usually a ``pytorch_lightning.LightningModule``.
        The mutation will be in-place on ``root_module``.
    hooks : list[MutationHook]
        List of mutation hooks. See :class:`BaseOneShotLightningModule` for how to write hooks.
        When a hook returns an module, the module will be replaced (mutated) to the new module.
    mutate_kwargs : dict
        Extra keyword arguments passed to hooks.
    topdown : bool, default = False
        If topdown is true, hooks are first called, before traversing its sub-module (i.e., pre-order DFS).
        Otherwise, sub-modules are first traversed, before calling hooks on this node (i.e., post-order DFS).

    Returns
    ----------
    modules : dict[str, nn.Module]
        The replace result.
    """
def no_default_hook(module: nn.Module, name: str, memo: dict[str, Any], mutate_kwargs: dict[str, Any]) -> bool:
    """Add this hook at the end of your hook list to raise error for unsupported mutation primitives."""

class BaseOneShotLightningModule(pl.LightningModule):
    __doc__: Incomplete
    trainer: pl.Trainer
    @property
    def automatic_optimization(self) -> bool: ...
    def default_mutation_hooks(self) -> list[MutationHook]:
        """Override this to define class-default mutation hooks."""
    def mutate_kwargs(self) -> dict[str, Any]:
        """Extra keyword arguments passed to mutation hooks. Usually algo-specific."""
    model: Incomplete
    nas_modules: Incomplete
    def __init__(self, model: pl.LightningModule, mutation_hooks: list[MutationHook] | None = None) -> None: ...
    def search_space_spec(self) -> dict[str, ParameterSpec]:
        """Get the search space specification from :attr:`nas_modules`.

        Returns
        -------
        dict
            Key is the name of the choice, value is the corresponding :class:`ParameterSpec`.
        """
    def resample(self, memo: Incomplete | None = None) -> dict[str, Any]:
        """Trigger the resample for each :attr:`nas_modules`.
        Sometimes (e.g., in differentiable cases), it does nothing.

        Parameters
        ----------
        memo : dict[str, Any]
            Used to ensure the consistency of samples with the same label.

        Returns
        -------
        dict
            Sampled architecture.
        """
    def export(self) -> dict[str, Any]:
        """
        Export the NAS result, ideally the best choice of each :attr:`nas_modules`.
        You may implement an ``export`` method for your customized :attr:`nas_modules`.

        Returns
        --------
        dict
            Keys are names of ``nas_modules``, and values are the choice indices of them.
        """
    def export_probs(self) -> dict[str, Any]:
        """
        Export the probability of every choice in the search space got chosen.

        .. note:: If such method of some modules is not implemented, they will be simply ignored.

        Returns
        -------
        dict
            In most cases, keys are names of ``nas_modules`` suffixed with ``/`` and choice name.
            Values are the probability / logits depending on the implementation.
        """
    def forward(self, x): ...
    def configure_optimizers(self) -> Any:
        """
        Transparently configure optimizers for the inner model,
        unless one-shot algorithm has its own optimizer (via :meth:`configure_architecture_optimizers`),
        in which case, the optimizer will be appended to the list.

        The return value is still one of the 6 types defined in PyTorch-Lightning.
        """
    def setup(self, stage: str = ...): ...
    def teardown(self, stage: str = ...): ...
    def configure_architecture_optimizers(self) -> list[optim.Optimizer] | optim.Optimizer | None:
        """
        Hook kept for subclasses. A specific NAS method inheriting this base class should return its architecture optimizers here
        if architecture parameters are needed. Note that lr schedulers are not supported now for architecture_optimizers.

        Returns
        -------
        Optimizers used by a specific NAS algorithm. Return None if no architecture optimizers are needed.
        """
    def advance_optimization(self, loss: Any, batch_idx: int, gradient_clip_val: int | float | None = None, gradient_clip_algorithm: str | None = None):
        """
        Run the optimizer defined in evaluators, when manual optimization is turned on.

        Call this method when the model should be optimized.
        To keep it as neat as possible, we only implement the basic ``zero_grad``, ``backward``, ``grad_clip``, and ``step`` here.
        Many hooks and pre/post-processing are omitted.
        Inherit this method if you need more advanced behavior.

        The full optimizer step could be found
        `here <https://github.com/Lightning-AI/lightning/blob/0e531283/src/pytorch_lightning/loops/optimization/optimizer_loop.py>`__.
        We only implement part of the optimizer loop here.

        Parameters
        ----------
        batch_idx: int
            The current batch index.
        """
    def advance_lr_schedulers(self, batch_idx: int):
        """
        Advance the learning rates, when manual optimization is turned on.

        The full implementation is
        `here <https://github.com/Lightning-AI/lightning/blob/0e531283/src/pytorch_lightning/loops/epoch/training_epoch_loop.py>`__.
        We only include a partial implementation here.
        Advanced features like Reduce-lr-on-plateau are not supported.
        """
    def architecture_optimizers(self) -> list[Optimizer] | Optimizer | None:
        """
        Get the optimizers configured in :meth:`configure_architecture_optimizers`.
        """
    def on_train_start(self): ...
    def on_train_end(self): ...
    def on_validation_start(self): ...
    def on_validation_end(self): ...
    def on_fit_start(self): ...
    def on_fit_end(self): ...
    def on_train_batch_start(self, batch, batch_idx, *args, **kwargs): ...
    def on_train_batch_end(self, outputs, batch, batch_idx, *args, **kwargs): ...
    def on_train_epoch_start(self): ...
    def on_train_epoch_end(self): ...
    def on_before_backward(self, loss): ...
    def on_after_backward(self): ...
