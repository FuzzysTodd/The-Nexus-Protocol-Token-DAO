from ..utils import rand_like_with_shape as rand_like_with_shape
from .compress_modules import replace_module as replace_module
from .infer_mask import AutoMaskInference as AutoMaskInference
from .jit_translate import jit_to_python_function as jit_to_python_function
from _typeshed import Incomplete
from nni.common.graph_utils import build_module_graph as build_module_graph
from nni.compression.pytorch.utils.mask_conflict import fix_mask_conflict as fix_mask_conflict
from nni.compression.pytorch.utils.utils import get_module_by_name as get_module_by_name

class ModelSpeedup:
    """
    This class is to speedup the model with provided weight mask.

    Parameters
    ----------
    model : pytorch model
        The model user wants to speedup
    dummy_input : pytorch tensor, tuple of tensor, list of tensor
        Note: The first dimension of the dummy_input should be the batchsize.
        The dummy input for ```jit.trace```, users should put it on the right
        device.
    masks_file : str/dict
        The path of user provided mask file, or the mask object
    map_location : str
        the device on which masks are placed, same to map_location in ```torch.load```
    batch_dim : int
        the index of batch dimension in the dummy_input
    confidence: the confidence coefficient of the sparsity inference. This value is
        actually used as the batchsize of the dummy_input.
    customized_replace_func: None/Dict
        If `customized_replace_func` is not None, then we will use the given function to replace the
        corresponding modules. The `key` of the dict is the opertor types and the `value`
        is the replace function of corresponding opertor. The replace function should take
        two input parameters, one is the original module, the second input parameter is tuple
        of the input mask, output mask and weight mask. This replace function should prune the module
        accordingly. Here is an example of the replace function(more examples can refer to compress_modules.py)::

            def example_replace(ori_module, masks):
                in_mask, out_mask, weight_mask = masks
                # prune the ori_module to a new smaller module according to the mask
                return new_small_module

    """
    ori_state_dict: Incomplete
    bound_model: Incomplete
    inferred_masks: Incomplete
    batch_dim: Incomplete
    confidence: Incomplete
    torch_graph: Incomplete
    auto_inferences: Incomplete
    debugname_to_value: Incomplete
    masks: Incomplete
    constant: Incomplete
    internal_result: Incomplete
    customized_replace_func: Incomplete
    def __init__(self, model, dummy_input, masks_file, map_location: Incomplete | None = None, batch_dim: int = 0, confidence: int = 8, customized_replace_func: Incomplete | None = None) -> None: ...
    def update_direct_sparsity(self, node) -> None:
        """
        Update the direct sparsity for the target node. Here the direct sparsity
        means that the sparsity in the output tensor that caused by the sparsity
        in the input tensors/weight tensors.
        """
    def update_indirect_sparsity(self, node) -> None:
        """
        This function will update the indirect sparsity. To explain what's
        indirect sparsity, for example, there is two tensors TA and TB, and
        we perform the calculation: TC = TA x TB in which TC is also a tensor.
        Once some values in TA are masked to zeros, then the corresponding
        positions in TB are also potential sparsities, because these have no
        effect of the final output(the gradient of these positions in TB equal
        to 0 all the time). This function it to fine the potential sparsity caused
        by other sparsity(we call it indirect sparsity here). Basically we can find
        these potential sparsity through gradient.

        Parameters
        ---------
        node: the NodePy
            The target node to update the indirect sparsity
        """
    def infer_modules_masks(self) -> None:
        """
        Infer the mask for all layers in the module, this function can be divided into
        two steps: first, forward inference of the the masks. Second, backward inference
        of the mask. We keep repeating these two steps until the masks of the model doesn't
        change.
        """
    def replace_compressed_modules(self) -> None:
        """
        Replace all the modules that have changed (weights/inputs/output) shape.
        The new module is created using the same arguments of the to-be-replaced module,
        and correctly inherits its weights.

        NOTE: ```func``` type cannot be replaced as it is not a module, thus, one limitation
        is that ```func``` should be not required to be replaced.
        """
    ori_module: Incomplete
    reindex_dim: Incomplete
    reindex: Incomplete
    t_index: Incomplete
    def replace_submodule(self, unique_name, reindex_dim: Incomplete | None = None, reindex: Incomplete | None = None):
        """
        Replace the submodule according to the inferred sparsity.

        Parameters
        ----------
        unique_name: str
            The unique_name of the submodule to replace.
        reindex_dim: int
            The dimension of the re-index operation.
        reindex: Reindex
            The index tensor. Normally this variable is None. If we want to reindex the
            output of this submodule, we can pass the index by this parameter.
        """
    def initialize_speedup(self) -> None:
        """
        Do some initial work for speedup.
        """
    def speedup_model(self) -> None:
        """
        There are basically two steps: first, do mask/shape inference,
        second, replace modules.
        """
