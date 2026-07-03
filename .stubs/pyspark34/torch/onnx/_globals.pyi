import torch._C._onnx as _C_onnx
from _typeshed import Incomplete

class _InternalGlobals:
    """Globals used internally by ONNX exporter.

    NOTE: Be very judicious when adding any new variables. Do not create new
    global variables unless they are absolutely necessary.
    """
    export_training: bool
    operator_export_type: Incomplete
    onnx_shape_inference: bool
    runtime_type_check_state: Incomplete
    def __init__(self) -> None: ...
    @property
    def training_mode(self):
        """The training mode for the exporter."""
    @training_mode.setter
    def training_mode(self, training_mode: _C_onnx.TrainingMode): ...
    @property
    def export_onnx_opset_version(self) -> int:
        """Opset version used during export."""
    @export_onnx_opset_version.setter
    def export_onnx_opset_version(self, value: int): ...
    @property
    def in_onnx_export(self) -> bool:
        """Whether it is in the middle of ONNX export."""
    @in_onnx_export.setter
    def in_onnx_export(self, value: bool): ...

GLOBALS: Incomplete
