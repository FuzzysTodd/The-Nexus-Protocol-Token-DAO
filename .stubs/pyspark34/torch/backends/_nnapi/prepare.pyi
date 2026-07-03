import torch
from _typeshed import Incomplete
from typing import List

ANEURALNETWORKS_PREFER_LOW_POWER: int
ANEURALNETWORKS_PREFER_FAST_SINGLE_ANSWER: int
ANEURALNETWORKS_PREFER_SUSTAINED_SPEED: int

class NnapiModule(torch.nn.Module):
    """Torch Module that wraps an NNAPI Compilation.

    This module handles preparing the weights, initializing the
    NNAPI TorchBind object, and adjusting the memory formats
    of all inputs and outputs.
    """
    comp: torch.classes._nnapi.Compilation | None
    weights: List[torch.Tensor]
    out_templates: List[torch.Tensor]
    shape_compute_module: Incomplete
    ser_model: Incomplete
    inp_mem_fmts: Incomplete
    out_mem_fmts: Incomplete
    compilation_preference: Incomplete
    relax_f32_to_f16: Incomplete
    def __init__(self, shape_compute_module: torch.nn.Module, ser_model: torch.Tensor, weights: List[torch.Tensor], inp_mem_fmts: List[int], out_mem_fmts: List[int], compilation_preference: int, relax_f32_to_f16: bool) -> None: ...
    def init(self, args: List[torch.Tensor]): ...
    def forward(self, args: List[torch.Tensor]) -> List[torch.Tensor]: ...

def convert_model_to_nnapi(model, inputs, serializer: Incomplete | None = None, return_shapes: Incomplete | None = None, use_int16_for_qint16: bool = False, compilation_preference=..., relax_f32_to_f16: bool = False): ...
def process_for_nnapi(model, inputs, serializer: Incomplete | None = None, return_shapes: Incomplete | None = None, use_int16_for_qint16: bool = False): ...
