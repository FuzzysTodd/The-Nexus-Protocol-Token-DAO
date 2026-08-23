import torch

__all__ = ['clip_grad_norm_', 'clip_grad_norm', 'clip_grad_value_']

def clip_grad_norm_(parameters: _tensor_or_tensors, max_norm: float, norm_type: float = 2.0, error_if_nonfinite: bool = False, foreach: bool | None = None) -> torch.Tensor:
    """Clips gradient norm of an iterable of parameters.

    The norm is computed over all gradients together, as if they were
    concatenated into a single vector. Gradients are modified in-place.

    Args:
        parameters (Iterable[Tensor] or Tensor): an iterable of Tensors or a
            single Tensor that will have gradients normalized
        max_norm (float): max norm of the gradients
        norm_type (float): type of the used p-norm. Can be ``'inf'`` for
            infinity norm.
        error_if_nonfinite (bool): if True, an error is thrown if the total
            norm of the gradients from :attr:`parameters` is ``nan``,
            ``inf``, or ``-inf``. Default: False (will switch to True in the future)
        foreach (bool): use the faster foreach-based implementation.
            If ``None``, use the foreach implementation for CUDA and CPU native tensors and silently
            fall back to the slow implementation for other device types.
            Default: ``None``

    Returns:
        Total norm of the parameter gradients (viewed as a single vector).
    """
def clip_grad_norm(parameters: _tensor_or_tensors, max_norm: float, norm_type: float = 2.0, error_if_nonfinite: bool = False, foreach: bool | None = None) -> torch.Tensor:
    """Clips gradient norm of an iterable of parameters.

    .. warning::
        This method is now deprecated in favor of
        :func:`torch.nn.utils.clip_grad_norm_`.
    """
def clip_grad_value_(parameters: _tensor_or_tensors, clip_value: float, foreach: bool | None = None) -> None:
    """Clips gradient of an iterable of parameters at specified value.

    Gradients are modified in-place.

    Args:
        parameters (Iterable[Tensor] or Tensor): an iterable of Tensors or a
            single Tensor that will have gradients normalized
        clip_value (float): maximum allowed value of the gradients.
            The gradients are clipped in the range
            :math:`\\left[\\text{-clip\\_value}, \\text{clip\\_value}\\right]`
        foreach (bool): use the faster foreach-based implementation
            If ``None``, use the foreach implementation for CUDA and CPU native tensors and
            silently fall back to the slow implementation for other device types.
            Default: ``None``
    """
