from _typeshed import Incomplete
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class ScalarType(Enum):
    u8: Incomplete
    i8: Incomplete
    i16: Incomplete
    i32: Incomplete
    i64: Incomplete
    f16: Incomplete
    f32: Incomplete
    f64: Incomplete
    c32: Incomplete
    c64: Incomplete
    c128: Incomplete
    b8: Incomplete
    bf16: Incomplete

class Layout(Enum):
    strided: Incomplete
    sparse_coo: Incomplete
    sparse_csr: Incomplete
    sparse_csc: Incomplete
    sparse_bsr: Incomplete
    sparse_bsc: Incomplete

class MemoryFormat(Enum):
    contiguous_format: Incomplete
    channels_last: Incomplete
    channels_last_3d: Incomplete
    preserve_format: Incomplete

@dataclass
class Device:
    type: str
    index: int
    def __init__(self, type, index) -> None: ...

@dataclass
class SymInt:
    as_int: int = ...
    as_sym: str = ...
    def __init__(self, as_int, as_sym) -> None: ...

@dataclass
class TensorArgument:
    name: str
    def __init__(self, name) -> None: ...

@dataclass
class SymIntArgument:
    name: str
    def __init__(self, name) -> None: ...

@dataclass
class ReturnArgument:
    as_tensor: TensorArgument = ...
    as_symint: SymIntArgument = ...
    def __init__(self, as_tensor, as_symint) -> None: ...

@dataclass
class Argument:
    as_none: bool = ...
    as_tensor: TensorArgument = ...
    as_tensors: List[TensorArgument] = ...
    as_symint: SymIntArgument = ...
    as_symints: List[SymIntArgument] = ...
    as_bool: bool = ...
    as_bools: List[bool] = ...
    as_int: int = ...
    as_ints: List[int] = ...
    as_float: float = ...
    as_floats: List[float] = ...
    as_str: str = ...
    as_gm: GraphModule = ...
    as_scalar_type: ScalarType = ...
    as_memory_format: MemoryFormat = ...
    as_layout: Layout = ...
    as_device: Device = ...
    def __init__(self, as_none, as_tensor, as_tensors, as_symint, as_symints, as_bool, as_bools, as_int, as_ints, as_float, as_floats, as_str, as_gm, as_scalar_type, as_memory_format, as_layout, as_device) -> None: ...

@dataclass
class TensorMeta:
    dtype: ScalarType
    sizes: List[SymInt]
    requires_grad: bool
    device: Device
    strides: List[SymInt]
    storage_offset: SymInt
    layout: Layout
    def __init__(self, dtype, sizes, requires_grad, device, strides, storage_offset, layout) -> None: ...

@dataclass
class Buffer:
    buffer: bytes
    def __init__(self, buffer) -> None: ...

@dataclass
class ExternalBuffer:
    location: str
    offset: str
    length: str
    checksum: str
    def __init__(self, location, offset, length, checksum) -> None: ...

@dataclass
class Storage:
    class DataLocation(Enum):
        Internal = ...
        External = ...
    data_location: DataLocation
    data: Buffer | ExternalBuffer
    def __init__(self, data_location, data) -> None: ...

@dataclass
class Tensor:
    storage: Storage
    meta: TensorMeta
    def __init__(self, storage, meta) -> None: ...

@dataclass
class TensorValue:
    name: str
    meta: TensorMeta
    def __init__(self, name, meta) -> None: ...

@dataclass
class SymIntValue:
    name: str
    value: SymInt
    def __init__(self, name, value) -> None: ...

@dataclass
class NodeMetadata:
    stack_trace: str
    nn_module_stack: str
    extra: Dict[str, str]
    def __init__(self, stack_trace, nn_module_stack, extra) -> None: ...

@dataclass
class Node:
    target: str
    args: List[Argument]
    kwargs: Dict[str, Argument]
    outputs: List[ReturnArgument]
    metadata: NodeMetadata
    def __init__(self, target, args, kwargs, outputs, metadata) -> None: ...

@dataclass(init=False)
class Graph:
    inputs: List[TensorArgument]
    outputs: List[TensorArgument]
    nodes: List[Node]
    tensor_values: List[TensorValue]
    symint_values: List[SymIntValue]

@dataclass(init=False)
class GraphModule:
    name: str
    graph: Graph
    metadata: Dict[str, str]
    parameters: Dict[str, Tensor]
    buffers: Dict[str, Tensor]
