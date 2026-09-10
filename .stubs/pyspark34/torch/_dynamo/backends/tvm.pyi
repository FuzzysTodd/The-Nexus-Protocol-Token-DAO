from .common import device_from_inputs as device_from_inputs, fake_tensor_unsupported as fake_tensor_unsupported
from .registry import register_backend as register_backend
from _typeshed import Incomplete

log: Incomplete

def tvm(gm, example_inputs, *, scheduler: Incomplete | None = None, trials: int = 20000): ...

tvm_meta_schedule: Incomplete
tvm_auto_scheduler: Incomplete

def has_tvm(): ...
def llvm_target(): ...
