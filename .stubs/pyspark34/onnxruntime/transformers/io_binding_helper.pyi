import numpy
import torch
from _typeshed import Incomplete
from onnxruntime import InferenceSession as InferenceSession
from typing import Any, Dict, List

logger: Incomplete

class TypeHelper:
    @staticmethod
    def get_input_type(ort_session: InferenceSession, name: str) -> str: ...
    @staticmethod
    def get_output_type(ort_session, name: str) -> str: ...
    @staticmethod
    def ort_type_to_numpy_type(ort_type: str): ...
    @staticmethod
    def ort_type_to_torch_type(ort_type: str): ...
    @staticmethod
    def numpy_type_to_torch_type(numpy_type: numpy.dtype): ...
    @staticmethod
    def torch_type_to_numpy_type(torch_type: torch.dtype): ...
    @staticmethod
    def get_io_numpy_type_map(ort_session: InferenceSession) -> Dict[str, numpy.dtype]:
        """Create a mapping from input/output name to numpy data type"""

class IOBindingHelper:
    @staticmethod
    def get_output_buffers(ort_session: InferenceSession, output_shapes, device):
        """Returns a dictionary of output name as key, and 1D tensor as value. The tensor has enough space for given shape."""
    @staticmethod
    def prepare_io_binding(ort_session, input_ids: torch.Tensor, position_ids: torch.Tensor, attention_mask: torch.Tensor, past: List[torch.Tensor], output_buffers, output_shapes, name_to_np_type: Incomplete | None = None):
        """Returnas IO binding object for a session."""
    @staticmethod
    def get_outputs_from_io_binding_buffer(ort_session, output_buffers, output_shapes, return_numpy: bool = True):
        """Copy results to cpu. Returns a list of numpy array."""

class CudaSession:
    """Inference Session with IO Binding for ONNX Runtime CUDA or TensorRT provider"""
    ort_session: Incomplete
    input_names: Incomplete
    output_names: Incomplete
    io_name_to_numpy_type: Incomplete
    io_binding: Incomplete
    enable_cuda_graph: Incomplete
    input_tensors: Incomplete
    output_tensors: Incomplete
    device: Incomplete
    def __init__(self, ort_session: InferenceSession, device: torch.device, enable_cuda_graph: bool = False) -> None: ...
    def __del__(self) -> None: ...
    def allocate_buffers(self, shape_dict: Dict[str, tuple]):
        """Allocate tensors for I/O Binding"""
    def infer(self, feed_dict: Dict[str, torch.Tensor]):
        """Bind input tensors and run inference"""
    @staticmethod
    def get_cuda_provider_options(device_id: int, enable_cuda_graph: bool) -> Dict[str, Any]: ...
