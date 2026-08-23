import torch
from _typeshed import Incomplete
from torch._dynamo import eval_frame as eval_frame
from torch._dynamo.utils import counters as counters
from torch._functorch.aot_autograd import aot_module_simplified as aot_module_simplified
from torch._subclasses import FakeTensor as FakeTensor

log: Incomplete

def aot_autograd(**kwargs): ...
def mem_efficient_fusion_kwargs(use_decomps): ...
def fake_tensor_unsupported(fn):
    """
    Decorator for backends that need real inputs.  We swap out fake
    tensors for zero tensors.
    """
def device_from_inputs(example_inputs) -> torch.device: ...
def dtype_from_inputs(example_inputs) -> torch.dtype: ...
