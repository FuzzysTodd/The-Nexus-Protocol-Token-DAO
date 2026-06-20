from .compressor import Compressor
from _typeshed import Incomplete
from torch import Tensor
from torch.nn import Module
from typing import Dict, List, OrderedDict, Tuple

__all__ = ['Pruner']

class PrunerModuleWrapper(Module):
    """
    Wrap a module to enable data parallel, forward method customization and buffer registeration.

    Parameters
    ----------
    module
        The module user wants to compress.
    config
        The configurations that users specify for compression.
    module_name
        The name of the module to compress, wrapper module shares same name.
    """
    module: Incomplete
    name: Incomplete
    config: Incomplete
    def __init__(self, module: Module, module_name: str, config: Dict) -> None: ...
    def forward(self, *inputs): ...

class Pruner(Compressor):
    """
    The abstract class for pruning algorithm. Inherit this class and implement the `_reset_tools` to customize a pruner.
    """
    def reset(self, model: Module | None = None, config_list: List[Dict] | None = None): ...
    def get_modules_wrapper(self) -> OrderedDict[str, PrunerModuleWrapper]:
        """
        Returns
        -------
        OrderedDict[str, PrunerModuleWrapper]
            An ordered dict, key is the name of the module, value is the wrapper of the module.
        """
    def get_origin2wrapped_parameter_name_map(self) -> Dict[str, str]:
        """
        Get the name mapping of parameters from original model to wrapped model.

        Returns
        -------
        Dict[str, str]
            Return a dict `{original_model_parameter_name: wrapped_model_parameter_name}`
        """
    def load_masks(self, masks: Dict[str, Dict[str, Tensor]]):
        """
        Load an exist masks on the wrapper. You can train the model with an exist masks after load the masks.

        Parameters
        ----------
        masks
            The masks dict with format {'op_name': {'weight': mask, 'bias': mask}}.
        """
    def compress(self) -> Tuple[Module, Dict[str, Dict[str, Tensor]]]:
        """
        Returns
        -------
        Tuple[Module, Dict]
            Return the wrapped model and mask.
        """
    def show_pruned_weights(self, dim: int = 0):
        """
        Log the simulated prune sparsity.

        Parameters
        ----------
        dim
            The pruned dim.
        """
    def export_model(self, model_path: str, mask_path: str | None = None):
        """
        Export pruned model weights, masks and onnx model(optional)

        Parameters
        ----------
        model_path
            Path to save pruned model state_dict. The weight and bias have already multiplied the masks.
        mask_path
            Path to save mask dict.
        """
