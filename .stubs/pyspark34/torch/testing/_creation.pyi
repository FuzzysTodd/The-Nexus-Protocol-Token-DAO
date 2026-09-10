import torch
from _typeshed import Incomplete
from typing import List, Tuple

complex_to_corresponding_float_type_map: Incomplete
float_to_corresponding_complex_type_map: Incomplete

def make_tensor(*shape: int | torch.Size | List[int] | Tuple[int, ...], dtype: torch.dtype, device: str | torch.device, low: float | None = None, high: float | None = None, requires_grad: bool = False, noncontiguous: bool = False, exclude_zero: bool = False, memory_format: torch.memory_format | None = None) -> torch.Tensor:
    '''Creates a tensor with the given :attr:`shape`, :attr:`device`, and :attr:`dtype`, and filled with
    values uniformly drawn from ``[low, high)``.

    If :attr:`low` or :attr:`high` are specified and are outside the range of the :attr:`dtype`\'s representable
    finite values then they are clamped to the lowest or highest representable finite value, respectively.
    If ``None``, then the following table describes the default values for :attr:`low` and :attr:`high`,
    which depend on :attr:`dtype`.

    +---------------------------+------------+----------+
    | ``dtype``                 | ``low``    | ``high`` |
    +===========================+============+==========+
    | boolean type              | ``0``      | ``2``    |
    +---------------------------+------------+----------+
    | unsigned integral type    | ``0``      | ``10``   |
    +---------------------------+------------+----------+
    | signed integral types     | ``-9``     | ``10``   |
    +---------------------------+------------+----------+
    | floating types            | ``-9``     | ``9``    |
    +---------------------------+------------+----------+
    | complex types             | ``-9``     | ``9``    |
    +---------------------------+------------+----------+

    Args:
        shape (Tuple[int, ...]): Single integer or a sequence of integers defining the shape of the output tensor.
        dtype (:class:`torch.dtype`): The data type of the returned tensor.
        device (Union[str, torch.device]): The device of the returned tensor.
        low (Optional[Number]): Sets the lower limit (inclusive) of the given range. If a number is provided it is
            clamped to the least representable finite value of the given dtype. When ``None`` (default),
            this value is determined based on the :attr:`dtype` (see the table above). Default: ``None``.
        high (Optional[Number]): Sets the upper limit (exclusive) of the given range. If a number is provided it is
            clamped to the greatest representable finite value of the given dtype. When ``None`` (default) this value
            is determined based on the :attr:`dtype` (see the table above). Default: ``None``.
        requires_grad (Optional[bool]): If autograd should record operations on the returned tensor. Default: ``False``.
        noncontiguous (Optional[bool]): If `True`, the returned tensor will be noncontiguous. This argument is
            ignored if the constructed tensor has fewer than two elements.
        exclude_zero (Optional[bool]): If ``True`` then zeros are replaced with the dtype\'s small positive value
            depending on the :attr:`dtype`. For bool and integer types zero is replaced with one. For floating
            point types it is replaced with the dtype\'s smallest positive normal number (the "tiny" value of the
            :attr:`dtype`\'s :func:`~torch.finfo` object), and for complex types it is replaced with a complex number
            whose real and imaginary parts are both the smallest positive normal number representable by the complex
            type. Default ``False``.
        memory_format (Optional[torch.memory_format]): The memory format of the returned tensor.  Incompatible
            with :attr:`noncontiguous`.

    Raises:
        ValueError: if ``requires_grad=True`` is passed for integral `dtype`
        ValueError: If ``low > high``.
        ValueError: If either :attr:`low` or :attr:`high` is ``nan``.
        TypeError: If :attr:`dtype` isn\'t supported by this function.

    Examples:
        >>> # xdoctest: +SKIP
        >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA)
        >>> from torch.testing import make_tensor
        >>> # Creates a float tensor with values in [-1, 1)
        >>> make_tensor((3,), device=\'cpu\', dtype=torch.float32, low=-1, high=1)
        >>> # xdoctest: +SKIP
        tensor([ 0.1205, 0.2282, -0.6380])
        >>> # Creates a bool tensor on CUDA
        >>> make_tensor((2, 2), device=\'cuda\', dtype=torch.bool)
        tensor([[False, False],
                [False, True]], device=\'cuda:0\')
    '''
