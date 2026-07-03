import pytorch_lightning as pl
from .base_lightning import BaseOneShotLightningModule as BaseOneShotLightningModule, MANUAL_OPTIMIZATION_NOTE as MANUAL_OPTIMIZATION_NOTE, MutationHook as MutationHook, no_default_hook as no_default_hook
from .supermodule.differentiable import DifferentiableMixedCell as DifferentiableMixedCell, DifferentiableMixedInput as DifferentiableMixedInput, DifferentiableMixedLayer as DifferentiableMixedLayer, DifferentiableMixedRepeat as DifferentiableMixedRepeat, GumbelSoftmax as GumbelSoftmax, MixedOpDifferentiablePolicy as MixedOpDifferentiablePolicy
from .supermodule.operation import NATIVE_MIXED_OPERATIONS as NATIVE_MIXED_OPERATIONS, NATIVE_SUPPORTED_OP_NAMES as NATIVE_SUPPORTED_OP_NAMES
from .supermodule.proxyless import ProxylessMixedInput as ProxylessMixedInput, ProxylessMixedLayer as ProxylessMixedLayer
from _typeshed import Incomplete

class DartsLightningModule(BaseOneShotLightningModule):
    __doc__: Incomplete
    def default_mutation_hooks(self) -> list[MutationHook]:
        """Replace modules with differentiable versions"""
    def mutate_kwargs(self):
        """Use differentiable strategy for mixed operations."""
    arc_learning_rate: Incomplete
    gradient_clip_val: Incomplete
    def __init__(self, inner_module: pl.LightningModule, mutation_hooks: list[MutationHook] | None = None, arc_learning_rate: float = 0.0003, gradient_clip_val: float | None = None) -> None: ...
    def training_step(self, batch, batch_idx): ...
    def configure_architecture_optimizers(self): ...

class ProxylessLightningModule(DartsLightningModule):
    __doc__: Incomplete
    def default_mutation_hooks(self) -> list[MutationHook]:
        """Replace modules with gumbel-differentiable versions"""

class GumbelDartsLightningModule(DartsLightningModule):
    def mutate_kwargs(self):
        """Use gumbel softmax."""
    temp: Incomplete
    init_temp: Incomplete
    use_temp_anneal: Incomplete
    min_temp: Incomplete
    def __init__(self, inner_module, mutation_hooks: list[MutationHook] | None = None, arc_learning_rate: float = 0.0003, gradient_clip_val: float | None = None, gumbel_temperature: float = 1.0, use_temp_anneal: bool = False, min_temp: float = 0.33) -> None: ...
    def on_train_epoch_start(self): ...
