from .lib import telemetry as telemetry
from _typeshed import Incomplete
from typing_extensions import Literal

logger: Incomplete

def watch(models, criterion: Incomplete | None = None, log: Literal['gradients', 'parameters', 'all'] | None = 'gradients', log_freq: int = 1000, idx: int | None = None, log_graph: bool = False):
    '''Hook into the torch model to collect gradients and the topology.

    Should be extended to accept arbitrary ML models.

    Args:
        models: (torch.Module) The model to hook, can be a tuple
        criterion: (torch.F) An optional loss value being optimized
        log: (str) One of "gradients", "parameters", "all", or None
        log_freq: (int) log gradients and parameters every N batches
        idx: (int) an index to be used when calling wandb.watch on multiple models
        log_graph: (boolean) log graph topology

    Returns:
        `wandb.Graph`: The graph object that will populate after the first backward pass

    Raises:
        ValueError: If called before `wandb.init` or if any of models is not a torch.nn.Module.
    '''
def unwatch(models: Incomplete | None = None) -> None:
    """Remove pytorch model topology, gradient and parameter hooks.

    Args:
        models: (list) Optional list of pytorch models that have had watch called on them
    """
