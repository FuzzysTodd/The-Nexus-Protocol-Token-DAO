from _typeshed import Incomplete
from torch._prims_common import DimsSequenceType as DimsSequenceType, ELEMENTWISE_TYPE_PROMOTION_KIND as ELEMENTWISE_TYPE_PROMOTION_KIND, NumberType as NumberType, ShapeType as ShapeType, TensorLikeType as TensorLikeType, elementwise_dtypes as elementwise_dtypes, getnvFuserDtype as getnvFuserDtype, make_contiguous_strides_for as make_contiguous_strides_for
from torch._prims_common.wrappers import backwards_not_supported as backwards_not_supported, elementwise_type_promotion_wrapper as elementwise_type_promotion_wrapper

nvprim_namespace: str
nvprim: Incomplete
nvprim_impl: Incomplete
nvprim_implicit_impl: Incomplete
nvprim_autograd_impl: Incomplete
nvprim_meta_impl: Incomplete
nvprim_names: Incomplete

def register_full(): ...
def register_native_batch_norm():
    """This function is used to register the native_batch_norm function in torch.ops.nvprims module."""
def register_rand_like(): ...
def register_var_mean():
    """This function is used to register the var_mean function in torch.ops.nvprims module."""
def register_view():
    """This function is used to register the view function in torch.ops.view module."""
def register_nvprims() -> None:
    """Registers all nvFuser primitives in the torch.ops.nvprims module."""
