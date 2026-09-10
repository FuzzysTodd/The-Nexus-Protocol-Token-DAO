import pytorch_lightning as pl
from .base_lightning import BaseOneShotLightningModule as BaseOneShotLightningModule, MANUAL_OPTIMIZATION_NOTE as MANUAL_OPTIMIZATION_NOTE, MutationHook as MutationHook, no_default_hook as no_default_hook
from .enas import ReinforceController as ReinforceController, ReinforceField as ReinforceField
from .supermodule.base import sub_state_dict as sub_state_dict
from .supermodule.operation import NATIVE_MIXED_OPERATIONS as NATIVE_MIXED_OPERATIONS, NATIVE_SUPPORTED_OP_NAMES as NATIVE_SUPPORTED_OP_NAMES
from .supermodule.sampling import MixedOpPathSamplingPolicy as MixedOpPathSamplingPolicy, PathSamplingCell as PathSamplingCell, PathSamplingInput as PathSamplingInput, PathSamplingLayer as PathSamplingLayer, PathSamplingRepeat as PathSamplingRepeat
from _typeshed import Incomplete
from typing import Any, Dict

class RandomSamplingLightningModule(BaseOneShotLightningModule):
    __doc__: Incomplete
    @property
    def automatic_optimization(self) -> bool: ...
    def default_mutation_hooks(self) -> list[MutationHook]:
        """Replace modules with differentiable versions"""
    def mutate_kwargs(self):
        """Use path sampling strategy for mixed-operations."""
    def training_step(self, *args, **kwargs): ...
    def export(self) -> dict[str, Any]:
        """
        Export of Random one-shot. It will return an arbitrary architecture.
        """
    def state_dict(self, destination: Any = None, prefix: str = '', keep_vars: bool = False) -> Dict[str, Any]: ...
    def load_state_dict(self, state_dict, strict: bool = True) -> None: ...
    def sub_state_dict(self, arch: dict[str, Any], destination: Any = None, prefix: str = '', keep_vars: bool = False) -> Dict[str, Any]:
        """Given the architecture dict, return the state_dict which can be directly loaded by the fixed subnet.

        Parameters
        ----------
        arch : dict[str, Any]
            subnet architecture dict.
        destination: dict
            If provided, the state of module will be updated into the dict and the same object is returned.
            Otherwise, an ``OrderedDict`` will be created and returned.
        prefix: str
            A prefix added to parameter and buffer names to compose the keys in state_dict.
        keep_vars: bool
            by default the :class:`~torch.Tensor` s returned in the state dict are detached from autograd.
            If it's set to ``True``, detaching will not be performed.

        Returns
        -------
        dict
            Subnet state dict.
        """

class EnasLightningModule(RandomSamplingLightningModule):
    __doc__: Incomplete
    @property
    def automatic_optimization(self) -> bool: ...
    nas_fields: Incomplete
    controller: Incomplete
    entropy_weight: Incomplete
    skip_weight: Incomplete
    baseline_decay: Incomplete
    baseline: float
    ctrl_steps_aggregate: Incomplete
    ctrl_grad_clip: Incomplete
    log_prob_every_n_step: Incomplete
    reward_metric_name: Incomplete
    def __init__(self, inner_module: pl.LightningModule, *, ctrl_kwargs: dict[str, Any] | None = None, entropy_weight: float = 0.0001, skip_weight: float = 0.8, baseline_decay: float = 0.999, ctrl_steps_aggregate: float = 20, ctrl_grad_clip: float = 0, log_prob_every_n_step: int = 10, reward_metric_name: str | None = None, mutation_hooks: list[MutationHook] | None = None) -> None: ...
    def configure_architecture_optimizers(self): ...
    def training_step(self, batch_packed, batch_idx): ...
    def on_train_epoch_start(self): ...
    def resample(self):
        """Resample the architecture with ENAS controller."""
    def export_probs(self):
        """Export the probability from ENAS controller directly."""
    def export(self):
        """Run one more inference of ENAS controller."""
