from torch import Tensor as Tensor
from torch.utils._pytree import tree_flatten as tree_flatten, tree_unflatten as tree_unflatten
from typing import Callable, Tuple

in_dims_t = int | Tuple
out_dims_t = int | Tuple[int, ...]

def vmap(func: Callable, in_dims: in_dims_t = 0, out_dims: out_dims_t = 0) -> Callable:
    """
    Please use torch.vmap instead of this API.
    """
