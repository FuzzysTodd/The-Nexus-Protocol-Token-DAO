import dataclasses
import torch
from torch.onnx._internal.fx import function_dispatcher as function_dispatcher
from typing import Callable, Dict

@dataclasses.dataclass
class ExportOptions:
    """Options for FX-ONNX export.
    Attributes:
        opset_version: The export ONNX version.
        use_binary_format: Whether to Return ModelProto in binary format.
        decomposition_table: The decomposition table for graph ops. Default is for torch ops, including aten and prim.
        op_level_debug: Whether to export the model with op level debug information with onnxruntime evaluator.
    """
    opset_version: int = ...
    use_binary_format: bool = ...
    op_level_debug: bool = ...
    decomposition_table: Dict[torch._ops.OpOverload, Callable] = ...
    def update(self, **kwargs) -> None: ...
    def __init__(self, opset_version, use_binary_format, op_level_debug, decomposition_table) -> None: ...
