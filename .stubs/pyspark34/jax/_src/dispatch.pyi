import dataclasses
import jax
import threading
from _typeshed import Incomplete
from collections.abc import Iterator, Sequence
from jax._src import api_util as api_util, basearray as basearray, core as core, dtypes as dtypes, linear_util as lu, source_info_util as source_info_util, traceback_util as traceback_util, tree_util as tree_util, util as util
from jax._src.config import config as config
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, pxla as pxla, xla as xla
from jax._src.lib import xla_extension_version as xla_extension_version
from jax._src.monitoring import record_event_duration_secs as record_event_duration_secs
from jax._src.partition_spec import PartitionSpec as PartitionSpec
from jax._src.sharding import Sharding as Sharding
from jax._src.sharding_impls import GSPMDSharding as GSPMDSharding, NamedSharding as NamedSharding, PmapSharding as PmapSharding, SingleDeviceSharding as SingleDeviceSharding, TransferToMemoryKind as TransferToMemoryKind, UNSPECIFIED as UNSPECIFIED, XLACompatibleSharding as XLACompatibleSharding
from typing import Any, Callable, NamedTuple

JAXPR_TRACE_EVENT: str
JAXPR_TO_MLIR_MODULE_EVENT: str
BACKEND_COMPILE_EVENT: str
xe: Incomplete
Backend: Incomplete
Device: Incomplete
CompileOptions: Incomplete
map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
logger: Incomplete

class _ArgSpec(NamedTuple):
    aval: core.AbstractValue
    sharding: XLACompatibleSharding | None

@dataclasses.dataclass(frozen=True)
class OrigShardings:
    shardings: Sequence[GSPMDSharding | None]
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __init__(self, shardings) -> None: ...

def apply_primitive(prim, *args, **params):
    """Impl rule that compiles and runs a single primitive 'prim' using XLA."""
def xla_primitive_callable(prim: core.Primitive, in_avals: tuple[core.AbstractValue, ...], in_tree, orig_in_shardings: OrigShardings, **params) -> Callable: ...
def sharded_lowering(fun: lu.WrappedFun, name: str, donated_invars: Sequence[bool], keep_unused: bool, inline: bool, in_avals: tuple[core.AbstractValue, ...], in_shardings: Sequence[Sharding | None], lowering_parameters: mlir.LoweringParameters) -> pxla.MeshComputation: ...
def simple_impl(prim) -> None: ...
RuntimeToken = Any

class RuntimeTokenSet(threading.local):
    """See docstring for effect.py module for the calling convention for tokens."""
    current_tokens: dict[core.Effect, jax.Array]
    output_runtime_tokens: dict[Device, RuntimeToken]
    def __init__(self) -> None: ...
    def get_token_input(self, eff: core.Effect, devices: list[Device]) -> jax.Array: ...
    def set_token_result(self, eff: core.Effect, token: jax.Array): ...
    def set_output_runtime_token(self, device: Device, token: RuntimeToken): ...
    def clear(self) -> None: ...
    def block_until_ready(self) -> None: ...

runtime_tokens: RuntimeTokenSet

def wait_for_tokens() -> None: ...
def is_single_device_sharding(sharding: Sharding) -> bool: ...
def log_elapsed_time(fmt: str, fun_name: str, event: str | None = None): ...
def should_tuple_args(num_args: int, platform: str) -> bool: ...
def jaxpr_has_primitive(jaxpr: core.Jaxpr, prim_name: str) -> bool:
    """Whether there is a primitive given by user anywhere inside a Jaxpr."""

class SourceInfo(NamedTuple):
    source_info: str
    eqn_name: str

def jaxpr_shardings(jaxpr: core.Jaxpr) -> Iterator[tuple[XLACompatibleSharding, SourceInfo]]: ...
def jaxpr_has_bints(jaxpr: core.Jaxpr) -> bool: ...

outfeed_rewriter: Callable[[core.Jaxpr], core.Jaxpr] | None

def apply_outfeed_rewriter(jaxpr: core.Jaxpr) -> core.Jaxpr: ...
def check_arg(arg: Any): ...
def jaxpr_replicas(jaxpr: core.Jaxpr) -> int:
    """The number of replicas needed for a jaxpr.

  For a eqn, multiply the `axis_size` with the `jaxpr_replicas` of the
  subjaxprs. For a list of eqns, take the maximum number of replicas.
  """
def needs_check_special() -> bool: ...
def check_special(name: str, bufs: Sequence[basearray.Array]) -> None: ...

device_put_p: Incomplete

def device_put_transpose_rule(ct, _, device, src): ...
