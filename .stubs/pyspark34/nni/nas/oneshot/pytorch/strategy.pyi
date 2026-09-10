import torch.nn as nn
from .base_lightning import BaseOneShotLightningModule as BaseOneShotLightningModule
from .differentiable import DartsLightningModule as DartsLightningModule, GumbelDartsLightningModule as GumbelDartsLightningModule, ProxylessLightningModule as ProxylessLightningModule
from .sampling import EnasLightningModule as EnasLightningModule, RandomSamplingLightningModule as RandomSamplingLightningModule
from _typeshed import Incomplete
from nni.nas.evaluator.pytorch.lightning import Lightning as Lightning, LightningModule as LightningModule
from nni.nas.execution.common import Model as Model
from nni.nas.strategy.base import BaseStrategy as BaseStrategy
from typing import Any, Type

class OneShotStrategy(BaseStrategy):
    """Wrap an one-shot lightning module as a one-shot strategy."""
    oneshot_module: Incomplete
    oneshot_kwargs: Incomplete
    model: Incomplete
    def __init__(self, oneshot_module: Type[BaseOneShotLightningModule], **kwargs) -> None: ...
    def preprocess_dataloader(self, train_dataloaders: Any, val_dataloaders: Any) -> tuple[Any, Any]:
        """
        One-shot strategy typically requires fusing train and validation dataloader in an ad-hoc way.
        As one-shot strategy doesn't try to open the blackbox of a batch,
        theoretically, these dataloader can be
        `any dataloader types supported by Lightning <https://pytorch-lightning.readthedocs.io/en/stable/guides/data.html>`__.

        Returns
        -------
        A tuple of preprocessed train dataloaders and validation dataloaders.
        """
    def attach_model(self, base_model: Model | nn.Module): ...
    def run(self, base_model: Model, applied_mutators): ...
    def export_top_models(self, top_k: int = 1) -> list[Any]:
        """The behavior of export top models in strategy depends on the implementation of inner one-shot module."""

class DARTS(OneShotStrategy):
    __doc__: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def preprocess_dataloader(self, train_dataloaders, val_dataloaders): ...

class Proxyless(OneShotStrategy):
    __doc__: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def preprocess_dataloader(self, train_dataloaders, val_dataloaders): ...

class GumbelDARTS(OneShotStrategy):
    __doc__: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def preprocess_dataloader(self, train_dataloaders, val_dataloaders): ...

class ENAS(OneShotStrategy):
    __doc__: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def preprocess_dataloader(self, train_dataloaders, val_dataloaders): ...

class RandomOneShot(OneShotStrategy):
    __doc__: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def sub_state_dict(self, arch: dict[str, Any]):
        """Export the state dict of a chosen architecture.
        This is useful in weight inheritance of subnet as was done in
        `SPOS <https://arxiv.org/abs/1904.00420>`__,
        `OFA <https://arxiv.org/abs/1908.09791>`__ and
        `AutoFormer <https://arxiv.org/abs/2106.13008>`__.

        Parameters
        ----------
        arch
            The architecture to be exported.

        Examples
        --------
        To obtain a state dict of a chosen architecture, you can use the following code::

            # Train or load a random one-shot strategy
            experiment.run(...)
            best_arch = experiment.export_top_models()[0]

            # If users are to manipulate checkpoint in an evaluator,
            # they should use this `no_fixed_arch()` statement to make sure
            # instantiating model space works properly, as evaluator is running in a fixed context.
            from nni.nas.fixed import no_fixed_arch
            with no_fixed_arch():
                model_space = MyModelSpace()    # must create a model space again here

            # If the strategy has been created previously, directly use it.
            strategy = experiment.strategy

            # Or load a strategy from a checkpoint
            strategy = RandomOneShot()
            strategy.attach_model(model_space)
            strategy.model.load_state_dict(torch.load(...))

            state_dict = strategy.sub_state_dict(best_arch)

        The state dict can be directly loaded into a fixed architecture using ``fixed_arch``::

            with fixed_arch(best_arch):
                model = MyModelSpace()
            model.load_state_dict(state_dict)

        Another common use case is to search for a subnet on supernet with a multi-trial strategy (e.g., evolution).
        The key step here is to write a customized evaluator that loads the checkpoint from the supernet and run evaluations::

            def evaluate_model(model_fn):
                model = model_fn()

                # Put this into `on_validation_start` or `on_train_start` if using Lightning evaluator.
                model.load_state_dict(get_subnet_state_dict())
                # Batch-norm calibration is often needed for better performance,
                # which is often running several hundreds of mini-batches to
                # re-compute running statistics of batch normalization for subnets.
                # See https://arxiv.org/abs/1904.00420 for details.
                finetune_bn(model)
                # Alternatively, you can also set batch norm to train mode to disable running statistics.
                # model.train()

                # Evaluate the model and validation dataloader.
                evaluate_acc(model)

        ``get_subnet_state_dict()`` here is a bit tricky. It's mostly the same as the pervious use case,
        but the architecture dict should be obtained from ``mutation_summary`` in ``get_current_parameter()``,
        which corresponds to the architecture of the current trial::

            def get_subnet_state_dict():
                random_oneshot_strategy = load_random_oneshot_strategy()     # Load a strategy from checkpoint, same as above
                arch_dict = nni.get_current_parameter()['mutation_summary']
                print('Architecture dict:', arch_dict)                       # Print here to see what it looks like
                return random_oneshot_strategy.sub_state_dict(arch_dict)
        """
