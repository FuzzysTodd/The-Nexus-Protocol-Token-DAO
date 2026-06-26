from . import op_properties as op_properties, reference as reference
from .tree_map import tree_flatten as tree_flatten, tree_map as tree_map
from .wrap_type import wrap_type as wrap_type
from _typeshed import Incomplete
from functorch._C import dim as _C

dims: Incomplete
DimList: Incomplete
dimlists: Incomplete

class DimensionMismatchError(Exception): ...
class DimensionBindError(Exception): ...

pointwise: Incomplete
use_c: bool

class _Tensor:
    @property
    def dims(self): ...
    def dim(self): ...
    __torch_function__: Incomplete
    expand: Incomplete
    index: Incomplete

TensorLike: Incomplete

class Dim(_C.Dim, _Tensor):
    __format__: Incomplete

class Tensor(_Tensor, _C.Tensor):
    from_batched: Incomplete
    from_positional: Incomplete
    sum: Incomplete

def cat(tensors, dim, new_dim): ...

t__getitem__: Incomplete
stack: Incomplete
split: Incomplete
t__setitem__: Incomplete
softmax: Incomplete
