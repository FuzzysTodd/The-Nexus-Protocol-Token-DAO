from _typeshed import Incomplete
from torch import Tensor
from torch.nn import Module as Module
from typing import Dict, List, Tuple

weighted_modules: Incomplete

def config_list_canonical(model: Module, config_list: List[Dict]) -> List[Dict]:
    """
    Split the config by op_names if 'sparsity' or 'sparsity_per_layer' in config,
    and set the sub_config['total_sparsity'] = config['sparsity_per_layer'].
    And every item in 'op_partial_names' will match corresponding 'op_names' in model,
    then convert 'op_partial_names' to 'op_names' in config.

    Example::
        model = models.resnet18()
        config_list = [{'op_types': ['Conv2d'], 'sparsity': 0.8, 'op_partial_names': ['conv1']}]
        pruner = L1NormPruner(model, config_list)
        pruner.compress()
        pruner.show_pruned_weights()

    In this process, the config_list will implicitly convert to the following:

    [{'op_types': ['Conv2d'], 'sparsity_per_layer': 0.8,
        'op_names': ['conv1', 'layer1.0.conv1', 'layer1.1.conv1',
        'layer2.0.conv1', 'layer2.1.conv1', 'layer3.0.conv1', 'layer3.1.conv1',
        'layer4.0.conv1', 'layer4.1.conv1']}]
    """
def unfold_config_list(model: Module, config_list: List[Dict]) -> List[Dict]:
    """
    Unfold config_list to op_names level.
    """
def dedupe_config_list(config_list: List[Dict]) -> List[Dict]:
    """
    Dedupe the op_names in unfolded config_list.
    """
def compute_sparsity_compact2origin(origin_model: Module, compact_model: Module, config_list: List[Dict]) -> List[Dict]:
    """
    Compare origin model and compact model, return the sparsity of each group mentioned in config list.
    A group means all layer mentioned in one config.
    e.g., a linear named 'linear1' and its weight size is [100, 100] in origin model, but in compact model,
    the layer weight size with same layer name is [100, 50],
    then this function will return [{'op_names': 'linear1', 'total_sparsity': 0.5}].
    """
def compute_sparsity_mask2compact(compact_model: Module, compact_model_masks: Dict[str, Dict[str, Tensor]], config_list: List[Dict]):
    """
    Apply masks on compact model, return the sparsity of each group mentioned in config list.
    A group means all layer mentioned in one config.
    This function count all zero elements of the masks in one group,
    then divide by the elements number of the weights in this group to compute sparsity.
    """
def compute_sparsity(origin_model: Module, compact_model: Module, compact_model_masks: Dict[str, Dict[str, Tensor]], config_list: List[Dict]) -> Tuple[List[Dict], List[Dict], List[Dict]]:
    """
    This function computes how much the origin model has been compressed in the current state.
    The current state means `compact_model` + `compact_model_masks`
    (i.e., `compact_model_masks` applied on `compact_model`).
    The compact model is the origin model after pruning,
    and it may have different structure with origin_model cause of speedup.

    Parameters
    ----------
    origin_model : torch.nn.Module
        The original un-pruned model.
    compact_model : torch.nn.Module
        The model after speedup or original model.
    compact_model_masks: Dict[str, Dict[str, Tensor]]
        The masks applied on the compact model, if the original model have been speedup, this should be {}.
    config_list : List[Dict]
        The config_list used by pruning the original model.

    Returns
    -------
    Tuple[List[Dict], List[Dict], List[Dict]]
        (current2origin_sparsity, compact2origin_sparsity, mask2compact_sparsity).
        current2origin_sparsity is how much the origin model has been compressed in the current state.
        compact2origin_sparsity is the sparsity obtained by comparing the structure of origin model and compact model.
        mask2compact_sparsity is the sparsity computed by count the zero value in the mask.
    """
def get_model_weights_numel(model: Module, config_list: List[Dict], masks: Dict[str, Dict[str, Tensor]] = {}) -> Tuple[Dict[str, int], Dict[str, float]]:
    """
    Count the layer weight elements number in config_list.
    If masks is not empty, the masked weight will not be counted.
    """
def get_module_by_name(model, module_name):
    """
    Get a module specified by its module name
    Parameters
    ----------
    model : pytorch model
        the pytorch model from which to get its module
    module_name : str
        the name of the required module
    Returns
    -------
    module, module
        the parent module of the required module, the required module
    """
def get_output_batch_dims(t: Tensor, module: Module): ...
