from .common import aot_autograd as aot_autograd
from _typeshed import Incomplete
from torch._functorch.compilers import ts_compile as ts_compile

def eager(gm, fake_tensor_inputs): ...
def torchscript(gm, fake_tensor_inputs): ...

aot_eager: Incomplete
aot_eager_decomp_partition: Incomplete
aot_ts: Incomplete
