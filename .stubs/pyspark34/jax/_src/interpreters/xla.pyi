import dataclasses
from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Sequence
from jax._src import core as core, dtypes as dtypes, source_info_util as source_info_util
from jax._src.abstract_arrays import numpy_scalar_types as numpy_scalar_types
from jax._src.core import ConcreteArray as ConcreteArray, ShapedArray as ShapedArray
from jax._src.lib import xla_client as xc
from jax._src.sharding_impls import AxisEnv as AxisEnv
from jax._src.typing import Shape as Shape
from jax._src.util import safe_map as safe_map, safe_zip as safe_zip
from typing import Any, Callable

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
xe: Incomplete
xops: Incomplete

def identity(x): ...
def parameter(builder, num, shape, name: Incomplete | None = None, replicated: Incomplete | None = None): ...
SpatialSharding = Shape | None | tuple[Shape | None, ...]

def sharding_to_proto(sharding: SpatialSharding):
    """Converts a SpatialSharding to an OpSharding.

  See
  https://github.com/tensorflow/tensorflow/blob/main/tensorflow/compiler/xla/xla_data.proto#L601
  for details on the OpSharding proto.
  """
def tuple_sharding_proto(elems): ...
def aval_to_xla_shapes(aval: core.AbstractValue) -> Sequence[xc.Shape]: ...
def canonicalize_dtype(x): ...

canonicalize_dtype_handlers: dict[Any, Callable]

def abstractify(x) -> Any: ...

pytype_aval_mappings: dict[Any, Callable[[Any], core.AbstractValue]]

def primitive_subcomputation(platform: str, axis_env: AxisEnv, prim: core.Primitive, avals_in: Sequence[core.AbstractValue], avals_out: Sequence[core.AbstractValue], **params): ...

@dataclasses.dataclass
class TranslationContext:
    builder: xc.XlaBuilder
    platform: str | None
    axis_env: AxisEnv
    name_stack: str | source_info_util.NameStack
    def replace(self, **kw): ...
    def __init__(self, builder, platform, axis_env, name_stack) -> None: ...

def xla_destructure(c, ans): ...

MYPY: bool
TranslationRule = Any
initial_style_primitives: set[core.Primitive]

def register_initial_style_primitive(prim: core.Primitive): ...
def register_translation(prim: core.Primitive, rule: TranslationRule, *, platform: str | None = None) -> None: ...

class _TranslationRuleAdapter:
    def __init__(self, translations, wrap_fn: Callable[[core.Primitive, Callable], TranslationRule]) -> None: ...
    def __setitem__(self, key: core.Primitive, value: Callable): ...

translations: _TranslationRuleAdapter

class _BackendSpecificTranslationsAdapter(defaultdict):
    def __missing__(self, key): ...

backend_specific_translations: dict[str, _TranslationRuleAdapter]
