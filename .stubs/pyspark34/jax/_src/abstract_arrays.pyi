from _typeshed import Incomplete
from jax._src import ad_util as ad_util, core as core, dtypes as dtypes, traceback_util as traceback_util

UnshapedArray: Incomplete
ShapedArray: Incomplete
ConcreteArray: Incomplete
AbstractToken: Incomplete
abstract_token: Incomplete
canonicalize_shape: Incomplete
raise_to_shaped: Incomplete

def zeros_like_array(x): ...

numpy_scalar_types: set[type]
array_types: set[type]

def canonical_concrete_aval(val, weak_type: Incomplete | None = None): ...
def masked_array_error(*args, **kwargs) -> None: ...
