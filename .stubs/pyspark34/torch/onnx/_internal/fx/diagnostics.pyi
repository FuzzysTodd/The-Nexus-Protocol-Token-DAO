from _typeshed import Incomplete
from onnxscript.function_libs.torch_aten import graph_building as graph_building
from torch.onnx._internal import diagnostics as diagnostics
from torch.onnx._internal.diagnostics import infra as infra
from torch.onnx._internal.diagnostics.infra import decorator as decorator, formatter as formatter, utils as utils
from typing import Any

def format_argument(obj: Any) -> str: ...

diagnose_call: Incomplete
diagnose_step: Incomplete
rules: Incomplete
export_context: Incomplete
levels: Incomplete
