import wandb
from _typeshed import Incomplete
from typing import List
from wandb import util as util
from wandb.data_types import Node as Node

torch: Incomplete

def nested_shape(array_or_tuple, seen: Incomplete | None = None):
    """Figure out the shape of tensors possibly embedded in tuples
    i.e
    [0,0] returns (2)
    ([0,0], [0,0]) returns (2,2)
    (([0,0], [0,0]),[0,0]) returns ((2,2),2)
    """

LOG_TRACK_COUNT: Incomplete
LOG_TRACK_THRESHOLD: Incomplete

def log_track_init(log_freq: int) -> List[int]:
    """create tracking structure used by log_track_update"""
def log_track_update(log_track: int) -> bool:
    """count (log_track[0]) up to threshold (log_track[1]), reset count (log_track[0]) and return true when reached"""

class TorchHistory:
    """History methods specific to PyTorch"""
    hook_torch: Incomplete
    def __init__(self) -> None: ...
    def add_log_parameters_hook(self, module: torch.nn.Module, name: str = '', prefix: str = '', log_freq: int = 0) -> None:
        """This instruments hooks into the pytorch module
        log parameters after a forward pass
        log_freq - log gradients/parameters every N batches
        """
    def add_log_gradients_hook(self, module: torch.nn.Module, name: str = '', prefix: str = '', log_freq: int = 0) -> None:
        """This instruments hooks into the pytorch module
        log gradients after a backward pass
        log_freq - log gradients/parameters every N batches
        """
    def log_tensor_stats(self, tensor, name) -> None:
        """Add distribution statistics on a tensor's elements to the current History entry"""
    def unhook_all(self) -> None: ...
    def unhook(self, name) -> None: ...

class TorchGraph(wandb.data_types.Graph):
    def __init__(self) -> None: ...
    @classmethod
    def hook_torch(cls, model, criterion: Incomplete | None = None, graph_idx: int = 0): ...
    def create_forward_hook(self, name, graph_idx): ...
    def hook_torch_modules(self, module, criterion: Incomplete | None = None, prefix: Incomplete | None = None, graph_idx: int = 0, parent: Incomplete | None = None) -> None: ...
    @classmethod
    def from_torch_layers(cls, module_graph, variable):
        """Recover something like neural net layers from PyTorch Module's and the
        compute graph from a Variable.

        Example output for a multi-layer RNN. We confusingly assign shared embedding values
        to the encoder, but ordered next to the decoder.

        rnns.0.linear.module.weight_raw rnns.0
        rnns.0.linear.module.bias rnns.0
        rnns.1.linear.module.weight_raw rnns.1
        rnns.1.linear.module.bias rnns.1
        rnns.2.linear.module.weight_raw rnns.2
        rnns.2.linear.module.bias rnns.2
        rnns.3.linear.module.weight_raw rnns.3
        rnns.3.linear.module.bias rnns.3
        decoder.weight encoder
        decoder.bias decoder
        """
    @classmethod
    def node_from_module(cls, nid, module): ...
