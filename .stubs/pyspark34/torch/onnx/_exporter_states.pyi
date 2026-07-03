import enum
from _typeshed import Incomplete
from torch import _C
from typing import Dict

class ExportTypes:
    """Specifies how the ONNX model is stored."""
    PROTOBUF_FILE: str
    ZIP_ARCHIVE: str
    COMPRESSED_ZIP_ARCHIVE: str
    DIRECTORY: str

class SymbolicContext:
    """Extra context for symbolic functions.

    Args:
        params_dict (Dict[str, _C.IValue]): Mapping from graph initializer name to IValue.
        env (Dict[_C.Value, _C.Value]): Mapping from Torch domain graph Value to ONNX domain graph Value.
        cur_node (_C.Node): Current node being converted to ONNX domain.
        onnx_block (_C.Block): Current ONNX block that converted nodes are being appended to.
    """
    params_dict: Incomplete
    env: Incomplete
    cur_node: Incomplete
    onnx_block: Incomplete
    def __init__(self, params_dict: Dict[str, _C.IValue], env: dict, cur_node: _C.Node, onnx_block: _C.Block) -> None: ...

class RuntimeTypeCheckState(enum.Enum):
    """Runtime type check state."""
    DISABLED: Incomplete
    WARNINGS: Incomplete
    ERRORS: Incomplete
