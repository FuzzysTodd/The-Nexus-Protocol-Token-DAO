from ..backends.common import aot_autograd as aot_autograd, mem_efficient_fusion_kwargs as mem_efficient_fusion_kwargs
from .registry import register_backend as register_backend, register_debug_backend as register_debug_backend
from _typeshed import Incomplete

log: Incomplete

def prims_executor(gm, inputs, *, executor): ...
def nvprims_fw_bw_partition_fn(joint_module, joint_inputs, *, num_fwd_outputs): ...
def create_nvprims_backend(*, executor): ...

aot_nvprims_nvfuser: Incomplete
aot_nvprims_aten: Incomplete
aot_mem_efficient_fusion: Incomplete
