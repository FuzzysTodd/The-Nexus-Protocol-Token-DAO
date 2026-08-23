from _typeshed import Incomplete
from torch import Tensor
from typing import Callable, List, overload
from typing_extensions import Literal

class Scaling:
    """
    In the process of generating masks, a large number of operations like pooling or upsampling are involved.
    This class provides tensor-related scaling functions for a given scaling kernel.

    Similar to the concept of convolutional kernel, the scaling kernel also moves over the tensor and does operations.
    The scaling kernel in this class is defined by two parts, kernel size and scaling function (shrink and expand).

    Parameters
    ----------
    kernel_size
        kernel_size is the scale, which determines how large a range in a tensor should shrink to a value,
        or how large a value in a tensor should expand.
        `-1` can be used to indicate that it is a full step in this dimension,
        and the dimension where -1 is located will be reduced or unsqueezed during scaling.

        Example::

            kernel_size = [2, -1]

            # For a given 2D-tensor with size (4, 3),
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             [10, 11, 12]]

            # shrinking it by shrink function, its size becomes (2,) after shrinking:
            [shrink([[1, 2, 3], [4, 5, 6]]), shrink([[7, 8, 9], [10, 11, 12]])]

            # expanding it by expand function with a given expand size,
            # if the expand function is repeating the values, and the expand size is (4, 6, 2):
            [[[1, 1],
              [1, 1],
              [2, 2],
              [2, 2],
              [3, 3],
              [3, 3]],
                ...
              [9, 9]]]
            # note that the original tensor with size (4, 3) will unsqueeze to size (4, 3, 1) at first
            # for the `-1` in kernel_size, then expand size (4, 3, 1) to size (4, 6, 2).
    kernel_padding_mode
        'front' or 'back', default is 'front'.
        If set 'front', for a given tensor when shrinking,
        padding `1` at front of kernel_size until `len(tensor.shape) == len(kernel_size)`;
        for a given expand size when expanding,
        padding `1` at front of kernel_size until `len(expand_size) == len(kernel_size)`.
        If set 'back', for a given tensor when shrinking,
        padding `-1` at back of kernel_size until `len(tensor.shape) == len(kernel_size)`;
        for a given expand size when expanding,
        padding `-1` at back of kernel_size until `len(expand_size) == len(kernel_size)`.
    """
    kernel_size: Incomplete
    kernel_padding_mode: Incomplete
    def __init__(self, kernel_size: List[int], kernel_padding_mode: Literal['front', 'back'] = 'front') -> None: ...
    def shrink(self, target: Tensor, reduce_func: Callable[[Tensor], Tensor] | None = None) -> Tensor: ...
    def expand(self, target: Tensor, expand_size: List[int]): ...
    @overload
    def validate(self, target: List[int]): ...
    @overload
    def validate(self, target: Tensor): ...
