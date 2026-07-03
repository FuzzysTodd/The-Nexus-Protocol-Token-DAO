from _typeshed import Incomplete
from stable_baselines3.common.callbacks import BaseCallback
from typing import Literal

logger: Incomplete

class WandbCallback(BaseCallback):
    '''Callback for logging experiments to Weights and Biases.

    Log SB3 experiments to Weights and Biases
        - Added model tracking and uploading
        - Added complete hyperparameters recording
        - Added gradient logging
        - Note that `wandb.init(...)` must be called before the WandbCallback can be used.

    Args:
        verbose: The verbosity of sb3 output
        model_save_path: Path to the folder where the model will be saved, The default value is `None` so the model is not logged
        model_save_freq: Frequency to save the model
        gradient_save_freq: Frequency to log gradient. The default value is 0 so the gradients are not logged
        log: What to log. One of "gradients", "parameters", or "all".
    '''
    model_save_freq: Incomplete
    model_save_path: Incomplete
    gradient_save_freq: Incomplete
    log: Incomplete
    path: Incomplete
    def __init__(self, verbose: int = 0, model_save_path: str | None = None, model_save_freq: int = 0, gradient_save_freq: int = 0, log: Literal['gradients', 'parameters', 'all'] | None = 'all') -> None: ...
    def save_model(self) -> None: ...
