from _typeshed import Incomplete
from torch._prims_common import ELEMENTWISE_TYPE_PROMOTION_KIND as ELEMENTWISE_TYPE_PROMOTION_KIND, Number as Number, NumberType as NumberType, ShapeType as ShapeType, TensorLike as TensorLike, TensorLikeType as TensorLikeType
from torch.utils._pytree import tree_flatten as tree_flatten, tree_unflatten as tree_unflatten
from typing import Callable, Sequence

class elementwise_type_promotion_wrapper:
    """
    Adds elementwise type promotion to a Python reference implementation.

    Takes two kwargs, type_promoting_args and type_promotion_kind.

    type_promoting_args must be a string Sequence specifiying the argument names of all
    arguments that participate in type promotion (and should be type promoted). If the
    arg specifies a Sequence-type then every element of the Sequence will participate in
    type promotion.

    type_promotion_kind must be one of the kinds specified by ELEMENTWISE_TYPE_PROMOTION_KIND.
    See its documentation for details.

    Other type promotion behavior, like validating the Python type of scalar arguments, must
    be handled separately.
    """
    type_promoting_arg_names: Incomplete
    type_promotion_kind: Incomplete
    def __init__(self, *, type_promotion_kind: ELEMENTWISE_TYPE_PROMOTION_KIND, type_promoting_args: Sequence[str] = None) -> None: ...
    def __call__(self, fn: Callable) -> Callable: ...

def out_wrapper(*out_names: str, exact_dtype: bool = False): ...
def backwards_not_supported(prim): ...
def elementwise_unary_scalar_wrapper(fn: Callable) -> Callable:
    """
    Allows unary operators that accept tensors to work with Python numbers.
    """
