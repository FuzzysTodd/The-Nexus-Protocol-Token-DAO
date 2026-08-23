from _typeshed import Incomplete
from torch import Tensor
from torch.types import _device as Device, _dtype as DType
from typing import List

__all__ = ['to_padded_tensor', 'as_nested_tensor', 'nested_tensor']

def as_nested_tensor(tensor_list: List[Tensor], dtype: DType | None = None, device: Device | None = None) -> Tensor:
    """
    Constructs a nested tensor preserving autograd history from :attr:`tensor_list` a list of tensors.

    .. note::
        Tensors within the list are always copied by this function due to current nested tensor semantics.

    Args:
        tensor_list (List[Tensor]): a list of tensors with the same ndim

    Keyword arguments:
        dtype (:class:`torch.dtype`, optional): the desired type of returned nested tensor.
            Default: if None, same :class:`torch.dtype` as leftmost tensor in the list.
        device (:class:`torch.device`, optional): the desired device of returned nested tensor.
            Default: if None, same :class:`torch.device` as leftmost tensor in the list

    Example::

        >>> a = torch.arange(3, dtype=torch.float, requires_grad=True)
        >>> b = torch.arange(5, dtype=torch.float, requires_grad=True)
        >>> nt = torch.nested.as_nested_tensor([a, b])
        >>> nt.is_leaf
        False
        >>> fake_grad = torch.nested.nested_tensor([torch.ones_like(a), torch.zeros_like(b)])
        >>> nt.backward(fake_grad)
        >>> a.grad
        tensor([1., 1., 1.])
        >>> b.grad
        tensor([0., 0., 0., 0., 0.])
    """

to_padded_tensor: Incomplete
nested_tensor: Incomplete
