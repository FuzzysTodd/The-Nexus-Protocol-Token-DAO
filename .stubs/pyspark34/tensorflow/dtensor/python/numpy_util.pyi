import numpy as np
from tensorflow.dtensor.python import api as api, layout as layout_lib
from tensorflow.python.eager.polymorphic_function import polymorphic_function as polymorphic_function
from tensorflow.python.ops import array_ops as array_ops, sparse_ops as sparse_ops, stateless_random_ops as stateless_random_ops
from tensorflow.python.types.core import Tensor as Tensor, TensorLike as TensorLike
from typing import List

def to_numpy(tensor: TensorLike) -> np.ndarray:
    """Copy `input` DTensor to an equivalent local numpy array."""
def unpacked_to_numpy(unpacked: List[TensorLike], layout: layout_lib.Layout) -> np.ndarray:
    """Heals local Tensor components to a numpy array."""
def unpack(t: TensorLike, layout: layout_lib.Layout, split_fn=..., stack_fn=...) -> List[TensorLike]:
    """Slice `t` into a flattened list of tensors suitable for `pack`."""
def pack_numpy(value: np.ndarray, layout: layout_lib.Layout, make_sparse: bool = False) -> Tensor: ...
def pack_tf_tensor(value: Tensor, layout: layout_lib.Layout) -> Tensor: ...
def stateless_random_uniform(shape, seed, layout):
    """Creates uniform random tensor with the given layout."""
