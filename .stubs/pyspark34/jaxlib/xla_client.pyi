import enum
from . import xla_extension as _xla
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, List, Sequence, Tuple

ops = _xla.ops
profiler = _xla.profiler
mlir_api_version: int
xla_platform_names: Incomplete
logger: Incomplete

def make_interpreter_client(): ...
def make_cpu_client(*, use_tfrt: bool = True) -> ...: ...
def make_gpu_client(distributed_client: Incomplete | None = None, node_id: int = 0, num_nodes: int = 1, platform_name: Incomplete | None = None, allowed_devices: Incomplete | None = None):
    """Returns a GPU client. BFC allocator is used by default."""
def make_tfrt_tpu_c_api_client(options: _NameValueMapping | None = None): ...
DeviceTopology = _xla.DeviceTopology

def make_tfrt_tpu_c_api_device_topology(topology_name: str = '', **kwargs) -> DeviceTopology:
    """Creates a PJRT C API TopologyDescription."""
def pjrt_plugin_loaded(plugin_name: str) -> bool: ...
def load_pjrt_plugin_dynamically(plugin_name: str, library_path: str) -> None: ...
def make_c_api_client(plugin_name: str, options: _NameValueMapping | None = None, distributed_client: _xla.DistributedRuntimeClient | None = None):
    """Creates a PJRT C API client for a PJRT plugin.

  It is required that load_pjrt_plugin_dynamically is called once with the same
  plugin_name before this method is called.

  Args:
     plugin_name: the name of the PJRT plugin.
     options: extra platform-specific options.
     distributed_client: distributed client.

  Returns:
     A PJRT C API client for plugin_name.
  """
def make_tpu_client(use_pjrt_c_api: bool = False):
    """Returns a TPU client. Defaults to allowing 32 in-flight computations."""

class OpMetadata:
    """Python representation of a xla.OpMetadata protobuf."""
    op_type: Incomplete
    op_name: Incomplete
    source_file: Incomplete
    source_line: Incomplete
    def __init__(self, op_type: str = '', op_name: str = '', source_file: str = '', source_line: int = 0) -> None: ...

def CurrentSourceInfoMetadata(op_type: Incomplete | None = None, op_name: Incomplete | None = None, skip_frames: int = 1):
    """Helper for use in source mapping that returns an OpMetadata object."""
PrimitiveType = _xla.PrimitiveType
bfloat16: Incomplete
float8_e4m3fn: Incomplete
float8_e4m3b11fnuz: Incomplete
float8_e4m3fnuz: Incomplete
float8_e5m2: Incomplete
float8_e5m2fnuz: Incomplete
XLA_ELEMENT_TYPE_TO_DTYPE: Incomplete
DTYPE_TO_XLA_ELEMENT_TYPE: Incomplete

def dtype_to_etype(dtype):
    """Convenience function for reading DTYPE_TO_XLA_ELEMENT_TYPE."""
Shape = _xla.Shape
ProgramShape = _xla.ProgramShape
ShapeIndex = _xla.ShapeIndex

def shape_from_pyval(pyval):
    """Returns a Shape that describes a tuple-tree of Numpy arrays."""
DeviceAssignment = _xla.DeviceAssignment
Device = _xla.Device
CompileOptions = _xla.CompileOptions
HostBufferSemantics = _xla.HostBufferSemantics

def execute_with_python_values(executable, arguments, backend):
    """Execute on one replica with Python values as arguments and output."""
def execute_with_python_values_replicated(executable, arguments, backend):
    """Execute on many replicas with Python values as arguments and output.

  Args:
    executable: the program to run.
    arguments: a list of lists of Python values indexed by `[replica][arg_num]`
      to pass as inputs.
    backend: the backend we are targeting.

  Returns:
    A list of python values, one per replica.
  """

class PaddingType(enum.Enum):
    VALID: int
    SAME: int

def window_padding_type_to_pad_values(padding_type, lhs_dims, rhs_dims, window_strides):
    """Maps PaddingType or string to pad values (list of pairs of ints)."""
XlaBuilder = _xla.XlaBuilder
XlaComputation = _xla.XlaComputation
XlaOp = _xla.XlaOp
FftType = _xla.FftType
Client = _xla.Client
Memory = _xla.Memory
ArrayImpl: Incomplete
LoadedExecutable = _xla.LoadedExecutable
OpSharding = _xla.OpSharding
HloSharding = _xla.HloSharding
Sharding = _xla.Sharding
XLACompatibleSharding = _xla.XLACompatibleSharding
NamedSharding = _xla.NamedSharding
SingleDeviceSharding = _xla.SingleDeviceSharding
PmapSharding = _xla.PmapSharding
GSPMDSharding = _xla.GSPMDSharding

def LoadedExecutable_execute(self, arguments, device: Incomplete | None = None): ...
def LoadedExecutable_execute_with_token(self, arguments, device: Incomplete | None = None): ...
def register_custom_call_target(name: str, fn: Any, platform: str = 'cpu') -> None:
    """Registers a custom call target.

  Args:
    name: bytes containing the name of the function.
    fn: a PyCapsule object containing the function pointer.
    platform: the target platform.
  """
register_cpu_custom_call_target = register_custom_call_target
register_custom_call_partitioner = _xla.register_custom_call_partitioner
encode_inspect_sharding_callback = _xla.encode_inspect_sharding_callback
hlo_sharding_util: Incomplete

class PaddingConfigDimension:
    """Python representation of a xla.PaddingConfigDimension protobuf."""
    edge_padding_low: int
    edge_padding_high: int
    interior_padding: int
    def __init__(self) -> None: ...

class PaddingConfig:
    """Python representation of a xla.PaddingConfig protobuf."""
    dimensions: Incomplete
    def __init__(self) -> None: ...

def make_padding_config(padding_config: PaddingConfig | Sequence[Tuple[int, int, int]]) -> PaddingConfig:
    """Create PaddingConfig proto from list of triples of integers.

  Args:
    padding_config: either a PaddingConfig or a list of integer triples
      (edge_padding_low, edge_padding_high, interior_padding) representing the
      configuration of the padding operation.

  Returns:
    A `PaddingConfig` object.
  """

class DotDimensionNumbers:
    """Python representation of a xla.DotDimensionNumbers protobuf."""
    lhs_contracting_dimensions: Incomplete
    rhs_contracting_dimensions: Incomplete
    lhs_batch_dimensions: Incomplete
    rhs_batch_dimensions: Incomplete
    def __init__(self) -> None: ...

def make_dot_dimension_numbers(dimension_numbers: DotDimensionNumbers | Tuple[Tuple[List[int], List[int]], Tuple[List[int], List[int]]]) -> DotDimensionNumbers:
    """Builds a DotDimensionNumbers object from a specification.

  Args:
    dimension_numbers: either a `DotDimensionNumbers` or a nested tuple
      `((lhs_contract, rhs_contract), (lhs_batch, rhs_batch))` of lists of
      integers representing the dimensions to treat as contracting dimensions
      and batch dimensions on each input operand.

  Returns:
    A `DotDimensionNumbers` object.
  """

class ConvolutionDimensionNumbers:
    """Python representation of a xla.ConvolutionDimensionNumbers protobuf."""
    input_batch_dimension: int
    input_feature_dimension: int
    input_spatial_dimensions: Incomplete
    kernel_input_feature_dimension: int
    kernel_output_feature_dimension: int
    kernel_spatial_dimensions: Incomplete
    output_batch_dimension: int
    output_feature_dimension: int
    output_spatial_dimensions: Incomplete
    def __init__(self) -> None: ...

def make_convolution_dimension_numbers(dimension_numbers: None | ConvolutionDimensionNumbers | Tuple[str, str, str], num_spatial_dimensions: int) -> ConvolutionDimensionNumbers:
    """Builds a ConvolutionDimensionNumbers object from a specification.

  Args:
    dimension_numbers: optional, either a ConvolutionDimensionNumbers object or
      a tuple (lhs_spec, rhs_spec, out_spec). Each element is a string of
      length N+2 identifying by position: (1) batch dimensions in lhs, rhs, and
        the output with the character 'N', (2) feature dimensions in lhs and the
        output with the character 'C', (3) input and output feature dimensions
        in rhs with the characters 'I' and 'O' respectively, and (4) spatial
        dimension correspondences between lhs, rhs, and the output using any
        distinct characters. For example, to indicate dimension numbers
        consistent with the Conv operation with two spatial dimensions, one
        could use ('NCHW', 'OIHW', 'NCHW'). As another example, to indicate
        dimension numbers consistent with the TensorFlow Conv2D operation, one
        could use ('NHWC', 'HWIO', 'NHWC'). When using the latter form of
        convolution dimension specification, window strides are associated with
        spatial dimension character labels according to the order in which the
        labels appear in the rhs_spec string, so that window_strides[0] is
        matched with the dimension corresponding to the first character
        appearing in rhs_spec that is not 'I' or 'O'. By default, use the same
        dimension numbering as Conv and ConvWithGeneralPadding.
    num_spatial_dimensions: the number of spatial dimensions.

  Returns:
    A `ConvolutionDimensionNumbers` object.
  """

class PrecisionConfig:
    """Python representation of a xla.PrecisionConfig protobuf."""
    Precision = _xla.PrecisionConfig_Precision
    operand_precision: Incomplete
    def __init__(self) -> None: ...

class GatherDimensionNumbers:
    """Python representation of a xla.GatherDimensionNumbers protobuf."""
    offset_dims: Incomplete
    collapsed_slice_dims: Incomplete
    start_index_map: Incomplete
    index_vector_dim: int
    def __init__(self) -> None: ...

class ScatterDimensionNumbers:
    """Python representation of a xla.ScatterDimensionNumbers protobuf."""
    update_window_dims: Incomplete
    inserted_window_dims: Incomplete
    scatter_dims_to_operand_dims: Incomplete
    index_vector_dim: int
    def __init__(self) -> None: ...

class ReplicaGroup:
    """Python representation of a xla.ReplicaGroup protobuf."""
    replica_ids: Incomplete
    def __init__(self) -> None: ...

def make_replica_groups(replica_groups): ...
Traceback = _xla.Traceback
Frame = _xla.Frame

def tracebacks(enabled: bool = True) -> Generator[None, None, None]:
    """Context manager that enables or disables traceback collection."""
def heap_profile(client: Client) -> bytes:
    """Returns a gzipped pprof protocol buffer containing a heap profile."""
XlaRuntimeError = _xla.XlaRuntimeError
weakref_lru_cache = _xla.weakref_lru_cache
array_result_handler = _xla.array_result_handler
copy_array_to_devices_with_sharding = _xla.copy_array_to_devices_with_sharding
batched_device_put = _xla.batched_device_put
