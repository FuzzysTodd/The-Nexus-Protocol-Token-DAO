import pytorch_lightning as pl
from pytorch_lightning.strategies import SingleDeviceStrategy

class BypassStrategy(SingleDeviceStrategy):
    strategy_name: str
    def model_to_device(self) -> None: ...

class Trainer(pl.Trainer):
    """
    Trainer for cross-graph optimization.

    Parameters
    ----------
    use_cgo : bool
        Whether cross-graph optimization (CGO) is used.
        If it is True, CGO will manage device placement.
        Any device placement from pytorch lightning will be bypassed.
        default: False
    trainer_kwargs : dict
        Optional keyword arguments passed to trainer. See
        `Lightning documentation <https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html>`__ for details.
    """
    def __init__(self, use_cgo: bool = False, **trainer_kwargs) -> None: ...
