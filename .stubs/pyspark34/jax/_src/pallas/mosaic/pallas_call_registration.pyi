import jax
from jax import core as jax_core
from jax._src.lib.mlir import ir as ir
from jax._src.pallas import core as core
from jax._src.pallas.mosaic import lowering as lowering
from jax._src.pallas.pallas_call import pallas_call_p as pallas_call_p
from jax.experimental import mosaic as mosaic
from jax.experimental.mosaic.dialects import tpu as tpu
from jax.interpreters import mlir as mlir
from typing import Any

def pallas_call_tpu_lowering_rule(ctx: mlir.LoweringRuleContext, *in_nodes, jaxpr: jax_core.Jaxpr, name: str, which_linear: tuple[bool, ...], grid_mapping: core.GridMapping, input_output_aliases: tuple[tuple[int, int], ...], in_shapes: tuple[jax.ShapeDtypeStruct, ...], out_shapes: tuple[jax.ShapeDtypeStruct, ...], debug: bool, interpret: bool, mosaic_params: dict[str, Any] | None = None, **compiler_params: Any):
    """Lowers a pallas_call to a Mosaic TPU custom call."""
