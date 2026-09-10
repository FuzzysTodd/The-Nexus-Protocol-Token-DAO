import torch.nn as nn
from .error_code import EmptyLayerError as EmptyLayerError, InputsNumberError as InputsNumberError, OutputTypeError as OutputTypeError, ShapeMisMatchError as ShapeMisMatchError, UnBalancedGroupError as UnBalancedGroupError
from _typeshed import Incomplete

replace_module: Incomplete

def convert_to_coarse_mask(t_mask, dim):
    """
    Convert the mask tensor to the coarse-grained mask tensor.
    Parameters
    ---------
    t_mask: torch.Tensor
        The tensor only have 1s and 0s, 0 indicates this value is masked
        and 1 indicates the corresponding value is not masked.
    dim: int
        Try to reduce the mask tensor on this dimension.

    Returns
    -------
    indexes: torch.Tensor
        The indexes of the sparsity that can be structurally removed.
    remained_indexes: torch.Tensor
        The indexes of values that need to be remained.
    """
def convert_dense_shape(mask):
    """
    Get the dense shape of the tensor after removing the sparsity
    values.

    Parameters
    ----------
    mask: torch.Tensor
        The mask tensor.

    Returns
    -------
    dense_shape: tuple
        The dense shape after removing the sparsity values.
    """
def no_replace(module, masks):
    """
    No need to replace
    """
def replace_prelu(prelu, masks):
    """
    Parameters
    ----------
    module : torch.nn.PReLU
        The prelu module to be replace
    masks : tuple of masks
        The input/output/weight masks of the target module

    Returns
    -------
    torch.nn.PReLU
        The new prelu module
    """
def replace_linear(linear, masks):
    """
    This function will replace the original linear according to
    the infered masks. This function support the fine-grained and
    coarse-grained sparsity. In the fine-grained scenario, this function
    will remove the whole column/row that happen to be totally covered by
    the masks.

    Parameters
    ----------
    linear : torch.nn.Linear
        The linear module to be replace
    masks : Tuple of the input masks, output masks and weight masks
        Tuple of the masks, for example
        ([input_m1, input_m2], [output_m], {'weight':weight_m})

    Returns
    -------
    torch.nn.Linear
        The new linear module
    """
def replace_batchnorm1d(norm, masks):
    """
    Parameters
    ----------
    norm : torch.nn.BatchNorm1d
        The batchnorm module to be replace
    masks : Tuple of the input masks, output masks and weight masks
        Tuple of the masks, for example
        ([input_m1, input_m2], [output_m], {'weight':weight_m})

    Returns
    -------
    torch.nn.BatchNorm1d
        The new batchnorm module
    """
def replace_batchnorm2d(norm, masks):
    """
    Parameters
    ----------
    norm : torch.nn.BatchNorm2d
        The batchnorm module to be replace
    masks : Tuple of the input masks, output masks and weight masks
        Tuple of the masks, for example
        ([input_m1, input_m2], [output_m], {'weight':weight_m})

    Returns
    -------
    torch.nn.BatchNorm2d
        The new batchnorm module
    """
def replace_groupnorm(norm: nn.GroupNorm, masks):
    """
    Parameters
    ----------
    norm : torch.nn.GroupNorm
        The group norm module to be replace
    masks : Tuple of the input masks, output masks and weight masks
        Tuple of the masks, for example
        ([input_m1, input_m2], [output_m], {'weight':weight_m})

    Returns
    -------
    torch.nn.GroupNorm
        The new group norm module
    """
def replace_instancenorm2d(norm, masks):
    """
    Parameters
    ----------
    norm : torch.nn.InstanceNorm2d
        The instancenorm module to be replace
    masks : Tuple of the input masks, output masks and weight masks
        Tuple of the masks, for example
        ([input_m1, input_m2], [output_m], {'weight':weight_m})

    Returns
    -------
    torch.nn.InstanceNorm2d
        The new instancenorm module
    """
def replace_conv2d(conv, masks):
    """
    Replace the original conv with a new one according to the infered
    masks, the function support the fine-grained sparsity and coarse-grained
    sparsity. In the fine-grained scenario, this replace function will replace
    the filters that happen to be totally coverd by the fine-grained sparsity.

    Parameters
    ----------
    conv : torch.nn.Conv2d
        The conv2d module to be replaced
    masks : Tuple of the input masks, output masks and weight masks
        Tuple of the masks, for example
        ([input_m1, input_m2], [output_m], {'weight':weight_m})

    Returns
    -------
    torch.nn.Conv2d
        The new conv2d module
    """
def replace_convtranspose2d(convtrans, masks):
    """
    We need anothor replace function for
    convtranspose2d, because the layout of
    the weight is different from traditional
    conv layers. The layout of the weight is [N_in, N_out, ksize_1, ksize_2]
    Parameters
    ----------
    convtrans : torch.nn.ConvTranspose2d
        The conv2d module to be replaced
    masks : Tuple of the input masks, output masks and weight masks
        Tuple of the masks, for example
        ([input_m1, input_m2], [output_m], {'weight':weight_m})
    Returns
    -------
    torch.nn.ConvTranspose2d
        The new conv2d module
    """
def replace_layernorm(layernorm, masks): ...
def replace_embedding(embedding, masks):
    """
    Replace the embedding layer according the infered masks.
    We replace the embedding layer according the weight masks,
    """
def replace_pixelshuffle(pixelshuffle, masks):
    """
    This is a nearly `no_replace` function.

    We can not replace pixelshuffle easily right now, pixelshuffle is a kind of location mapping.
    It will map tensor with shape (r^2 * C, H, W) to (C, r * H, r* W). So we have a dependency here,
    the preserved input channel number should be a multiple of C, and the multiple can be squared to positive integer.
    This dependence is similar to the group dependency in ConvXD, but more restrictive,
    i.e., each `r^2 input channels` group can not be free to preserve any number of channels, must be a number in [1, 4, 9, 16, ... , r^2].
    """
