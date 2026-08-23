from ..backends.common import aot_autograd as aot_autograd
from _typeshed import Incomplete

log: Incomplete

def torchxla_trivial(gm, fake_tensor_inputs): ...
def torchxla_trace_once(model, fake_tensor_inputs): ...

aot_torchxla_trivial: Incomplete
aot_torchxla_trace_once: Incomplete
