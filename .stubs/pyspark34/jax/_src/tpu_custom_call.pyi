import dataclasses
from _typeshed import Incomplete
from jax import core as core
from jax._src.config import config as config
from jax._src.lib import tpu_mosaic as tpu_mosaic, xla_client as xla_client
from jax.interpreters import mlir as mlir, xla as xla
from jaxlib.mlir import ir
from typing import Any, Callable

tpu: Incomplete
apply_vector_layout: Incomplete
infer_memref_layout: Incomplete
tpu_custom_call_p: Incomplete

@dataclasses.dataclass(frozen=True)
class CostEstimate:
    flops: int
    transcendentals: int
    bytes_accessed: int
    def to_json(self) -> bytes: ...
    def __init__(self, flops, transcendentals, bytes_accessed) -> None: ...

@dataclasses.dataclass(frozen=True)
class CustomCallBackendConfig:
    """Represents an unserialized backend config for custom calls."""
    lowered_module_asm: bytes
    has_communication: bool
    collective_id: int | None
    device_type: str | None
    cost_estimate: CostEstimate | None
    def to_json(self) -> bytes:
        """Serializes the backend config into JSON."""
    def __init__(self, lowered_module_asm, has_communication, collective_id, device_type, cost_estimate) -> None: ...

def as_tpu_kernel(module: ir.Module, out_type: Any, *, cost_estimate: CostEstimate | None = None, backend: str | xla_client.Client = 'tpu', device_type: str | None = None, kernel_name: str | None = None, kernel_regeneration_metadata: bytes | None = None) -> Callable[..., Any]:
    """Turns an MLIR Mosaic kernel into a JAX-compatible function."""
def dump_mlir(module: ir.Module, msg: str):
    """A helper function to print mlir module with a message."""
