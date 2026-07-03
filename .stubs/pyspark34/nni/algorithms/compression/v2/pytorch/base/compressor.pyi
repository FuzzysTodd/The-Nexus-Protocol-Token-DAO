from _typeshed import Incomplete
from nni.common.graph_utils import TorchModuleGraph
from torch.nn import Module
from typing import Any, Dict, List

__all__ = ['LayerInfo', 'Compressor']

class LayerInfo:
    module: Incomplete
    name: Incomplete
    type: Incomplete
    def __init__(self, name: str, module: Module) -> None: ...

class ModuleWrapper(Module):
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
    def forward(self, *inputs) -> None: ...

class Compressor:
    """
    The abstract base pytorch compressor.

    Parameters
    ----------
    model
        The model under compressed.
    config_list
        The config list used by compressor, usually specifies the 'op_types' or 'op_names' that want to compress.
    """
    is_wrapped: bool
    def __init__(self, model: Module | None, config_list: List[Dict] | None) -> None: ...
    bound_model: Incomplete
    config_list: Incomplete
    modules_wrapper: Incomplete
    def reset(self, model: Module, config_list: List[Dict]):
        """
        Reset the compressor with model and config_list.

        Parameters
        ----------
        model
            The model under compressed.
        config_list
            The config list used by compressor, usually specifies the 'op_types' or 'op_names' that want to compress.
        """
    def clear_model_references(self) -> None:
        """
        Clear all references to the model in this compressor. Just to free up memory.
        Need reset first before the next time call compressor function.
        """
    def get_modules_wrapper(self) -> Dict[str, ModuleWrapper]:
        """
        Returns
        -------
        Dict[str, ModuleWrapper]
            An dict, key is the name of the module, value is the wrapper of the module.
        """
    def set_wrappers_attribute(self, name: str, value: Any):
        """
        To register attributes used in wrapped module's forward method.
        If the type of the value is Torch.tensor, then this value is registered as a buffer in wrapper,
        which will be saved by model.state_dict. Otherwise, this value is just a regular variable in wrapper.

        Parameters
        ----------
        name
            Name of the variable.
        value
            Value of the variable.
        """
    def generate_graph(self, dummy_input: Any) -> TorchModuleGraph:
        """
        Generate a `TorchModuleGraph` instance of `self.bound_model` based on `jit.trace`.

        Parameters
        ----------
        dummy_input
            The dummy input for `jit.trace`, users should put it on right device before pass in.

        Returns
        -------
        TorchModuleGraph
            A `TorchModuleGraph` instance.
        """
    def generate_module_groups(self) -> Dict[int, List[str]]:
        """
        Get all module names in each config in config_list.

        Returns
        -------
        Dict[int, List[str]]
            A dict. The key is the config idx in config_list, the value is the module name list. i.e., {1: ['layer.0', 'layer.2']}.
        """
    def get_origin2wrapped_parameter_name_map(self) -> Dict[str, str]:
        """
        Get the name mapping of parameters from original model to wrapped model.

        Returns
        -------
        Dict[str, str]
            Return a dict `{original_model_parameter_name: wrapped_model_parameter_name}`
        """
    def validate_config(self, model: Module, config_list: List[Dict]):
        """
        Subclass can optionally implement this method to check if config_list is valid.

        Parameters
        ----------
        model
            The model under compressed.
        config_list
            The config list used by compressor, usually specifies the 'op_types' or 'op_names' that want to compress.
        """
    def compress(self) -> Module:
        """
        Compress the model with algorithm implemented by subclass.

        The model will be instrumented and user should never edit it after calling this method.
        `self._modules_to_compress` records all the to-be-compressed layers.

        Returns
        -------
        torch.nn.Module
            model with specified modules compressed.
        """
