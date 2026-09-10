import torch
from _typeshed import Incomplete
from typing import Dict, Tuple

CT_METADATA_VERSION: str
CT_METADATA_SOURCE: str

class ScalarType:
    Float: int
    Double: int
    Int: int
    Long: int
    Undefined: int

torch_to_mil_types: Incomplete

class CoreMLComputeUnit:
    CPU: str
    CPUAndGPU: str
    ALL: str

class CoreMLQuantizationMode:
    LINEAR: str
    LINEAR_SYMMETRIC: str
    NONE: str

def TensorSpec(shape, dtype=...): ...
def CompileSpec(inputs, outputs, backend=..., allow_low_precision: bool = True, quantization_mode=..., mlmodel_export_path: Incomplete | None = None): ...
def preprocess(script_module: torch._C.ScriptObject, compile_spec: Dict[str, Tuple]): ...
