from .hlo_helpers import DimensionSize as DimensionSize, ShapeTypePair as ShapeTypePair, custom_call as custom_call, ensure_hlo_s32 as ensure_hlo_s32, hlo_s32 as hlo_s32, mk_result_types_and_shapes as mk_result_types_and_shapes
from _typeshed import Incomplete
from jaxlib import xla_client as xla_client

cuda_getrf: Incomplete
rocm_getrf: Incomplete
cuda_geqrf: Incomplete
rocm_geqrf: Incomplete
cuda_geqrf_batched: Incomplete
rocm_geqrf_batched: Incomplete
cuda_csrlsvqr: Incomplete
cuda_orgqr: Incomplete
rocm_orgqr: Incomplete
cuda_syevd: Incomplete
rocm_syevd: Incomplete
cuda_gesvd: Incomplete
rocm_gesvd: Incomplete
cuda_sytrd: Incomplete
rocm_sytrd: Incomplete
