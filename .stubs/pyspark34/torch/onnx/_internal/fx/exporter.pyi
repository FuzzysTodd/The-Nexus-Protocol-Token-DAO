import onnx
import torch
import torch._ops
import torch.fx
from _typeshed import Incomplete
from torch._subclasses import fake_tensor as fake_tensor
from torch.fx.experimental import proxy_tensor as proxy_tensor
from torch.fx.passes import fake_tensor_prop as fake_tensor_prop
from torch.nn.utils import stateless as stateless
from torch.onnx._internal.fx import diagnostics as diagnostics, function_dispatcher as function_dispatcher, options as options
from typing import Any, Callable, Dict, Tuple

class ModuleExpansionTracer(torch.fx._symbolic_trace.Tracer):
    """Tracer to create ONNX-exporting friendly FX graph.

    This tracer traces models into operators. That is,
    the traced graph mostly contains call_function nodes and
    has no call_module nodes. The call_module nodes
    are problematic to the use of make_fx(...) in ONNX
    exporter.
    """
    def is_leaf_module(self, module: torch.nn.Module, module_qualified_name: str) -> bool: ...
    def to_bool(self, obj: torch.fx.Proxy) -> bool: ...

def export(fn: torch.nn.Module | Callable, *args, use_binary_format: bool = True, opset_version: int = ..., op_level_debug: bool = False) -> onnx.ModelProto | bytes: ...
def export_without_kwargs(fn: torch.nn.Module | Callable, *args, use_binary_format: bool = True, opset_version: int = ..., op_level_debug: bool = False, **kwargs) -> onnx.ModelProto | bytes: ...
def export_without_parameters_and_buffers(module: torch.nn.Module, *args, decomposition_table: Dict[torch._ops.OpOverload, Callable] | None = None, use_binary_format: bool = True, opset_version: int = ..., op_level_debug: bool = False, **kwargs) -> Tuple[onnx.ModelProto | bytes, 'torch.fx.GraphModule', Tuple[Any, ...], Tuple[Any, ...]]: ...
def save_model_with_external_data(basepath: str, model_location: str, initializer_location: str, torch_load_paths: Tuple[str, ...], onnx_model: onnx.ModelProto) -> None:
    '''Load PyTorch tensors from files and add to "onnx_model" as external initializers.

    Output files:
        ONNX model file path:
        ONNX initializer folder: os.path.join(basepath, initializer_location)

    After running this function, you can do
        ort_sess = onnxruntime.InferenceSession(os.path.join(basepath, model_location))
    to execute the model.

    Arguments:
        basepath: Base path of the external data file (e.g., "/tmp/large-onnx-model").
        model_location: Relative location of the ONNX model file.
            E.g., "model.onnx" so that the model file is saved to
            "/tmp/large-onnx-model/model.onnx".
        initializer_location: Relative location of the ONNX initializer folder.
            E.g., "initializers" so that the initializers are saved to
            "/tmp/large-onnx-model/initializers".
        torch_load_paths: Files which containing serialized PyTorch tensors to be saved
            as ONNX initializers. They are loaded by torch.load.
        onnx_model: ONNX model to be saved with external initializers.
            If an input name matches a tensor loaded from "torch_load_paths",
            the tensor will be saved as that input\'s external initializer.
    '''

TORCH_TYPE_TO_ONNX: Incomplete
