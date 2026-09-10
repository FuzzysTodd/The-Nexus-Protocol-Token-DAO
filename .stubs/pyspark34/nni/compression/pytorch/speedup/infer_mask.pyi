from ..utils import randomize_tensor as randomize_tensor, torch_float_dtype as torch_float_dtype, torch_integer_dtype as torch_integer_dtype
from _typeshed import Incomplete

STD_DELTA: float

class AutoMaskInference:
    module: Incomplete
    dummy_input: Incomplete
    in_masks: Incomplete
    in_constants: Incomplete
    output: Incomplete
    output_mask: Incomplete
    weights: Incomplete
    weight_mask: Incomplete
    name: Incomplete
    state_dict: Incomplete
    batch_dim: Incomplete
    batch_size: Incomplete
    def __init__(self, module, dummy_input, speedup, in_masks: Incomplete | None = None, weight_mask: Incomplete | None = None, output_mask: Incomplete | None = None, name: Incomplete | None = None, in_constants: Incomplete | None = None, state_dict: Incomplete | None = None) -> None:
        """
        This class will infer the mask of the target module automatically.
        This update_direct_sparsity will infer the output mask according
        to the input masks, in constrast, update_indirect_sparsity will
        infer the input masks according to given output masks. The newly
        found sparsity will be incrementally updated to the original in_masks
        and output_mask.

        Parameters
        ----------
        module: torch.nn.Module/function
            The target module to infer the mask. Need to be callable.
        dummy_input: torch.Tensor/list of Tensor
            The dummy_input of the target module.
        speedup: ModelSpeedup
            The reference of the ModelSpeedup object.
        in_masks:  list of torch.Tensor
            The input masks of the target module, if in_masks is not None, then
            update_direct_sparsity and update_indirect_sparsity will incrementally
            update the given in_masks, else, AutoMaskInference will create a new
            in_masks for the target module.
        output_mask: torch.Tensor
            The output mask of the target module. Similar to in_masks, if output_mask
            is not None, then update_direct_sparsity and update_indirect_sparsity will
            incrementally update the given output_mask, else AutoMaskInference will create
            one output_mask for the target module.
        weight_mask: dict of the weight masks
            The weight masks of the target module, the key is the corresponding name of
            the mask. For example: {'weight':torch.ones(1000, 1000), bias:torch.ones(1000)}
        name: str
            Name of the target module.
        in_constants: list of torch.Tensor
            The correponding constant values of the in_masks.
        state_dict: dict of torch.Tensor
            The original values of the weights.

        """
    def random_init(self, start: float = 0.1, end: float = 8.0) -> None:
        """
        Random initialize the weights of the module. The value of
        the tensor will not affect the mask auto inference.
        """
    def zero_grad(self) -> None:
        """
        Set the gradient of the weight, input tensor to be zeros.
        """
    def requires_grad_(self, flag: bool = True) -> None:
        """
        Set the requires_grad of input tensor and parameters to flag.
        """
    def apply_mask(self) -> None: ...
    def isconstants(self, tout):
        """
        Find the constants in the tensor tout. This function return a mask tensor that
        indicates if a value in tout is a constant, and return one more tensor to indicate
        that the values of the constant.

        Paramters
        ---------
        tout: torch.Tensor
            The target output tensor to find the constants
        Returns
        -------
        mask: torch.Tensor
            The mask tensor(same shape with tout) that indicates that whether
            the correponding value is a constant.
        constant: torch.Tensor
            The mask tensot(same shape with tout) that indicates the values of
            the constants in the tout.
        """
    def update_indirect_sparsity(self) -> None:
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
        """
    out_constant: Incomplete
    def update_direct_sparsity(self) -> None: ...
    def get_masks(self): ...
