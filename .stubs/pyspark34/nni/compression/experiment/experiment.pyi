import torch
from .config import CompressionExperimentConfig as CompressionExperimentConfig, CompressionVessel as CompressionVessel
from _typeshed import Incomplete
from nni.compression.experiment.config import generate_compression_search_space as generate_compression_search_space
from nni.experiment import Experiment as Experiment
from torch.nn import Module as Module
from torch.optim import Optimizer
from typing import Any, Callable, List

class CompressionExperiment(Experiment):
    '''
    Note: This is an experimental feature, the interface is not stable.

    Parameters
    ----------
    config_or_platform
        A `CompressionExperimentConfig` or the training service name or list of the training service name or None.
    model
        The pytorch model wanted to compress.
    finetuner
        The finetuner handled all finetune logic, use a pytorch module as input.
    evaluator
        Evaluate the pruned model and give a score.
    dummy_input
        It is used by `torch.jit.trace` to trace the model.
    trainer
        A callable function used to train model or just inference. Take model, optimizer, criterion as input.
        Note that the model should only trained or inferenced one epoch in the trainer.

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
        The traced optimizer instance which the optimizer class is wrapped by nni.trace.
        E.g. ``traced_optimizer = nni.trace(torch.nn.Adam)(model.parameters())``.
    criterion
        The criterion function used in trainer. Take model output and target value as input, and return the loss.
    device
        The selected device.
    '''
    config: Incomplete
    temp_directory: Incomplete
    vessel: Incomplete
    def __init__(self, config_or_platform: CompressionExperimentConfig | str | List[str] | None, model: Module, finetuner: Callable[[Module], None], evaluator: Callable[[Module], float], dummy_input: Any | None, trainer: Callable[[Module, Optimizer, Callable[[Any, Any], Any]], None] | None, optimizer: Optimizer | None, criterion: Callable[[Any, Any], Any] | None, device: str | torch.device) -> None: ...
    def start(self, port: int = 8080, debug: bool = False) -> None: ...
