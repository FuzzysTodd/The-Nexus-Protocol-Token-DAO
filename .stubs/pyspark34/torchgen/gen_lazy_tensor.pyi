from .gen_backend_stubs import error_on_missing_kernels as error_on_missing_kernels, gen_dispatcher_registrations as gen_dispatcher_registrations, gen_dispatchkey_nativefunc_headers as gen_dispatchkey_nativefunc_headers, parse_backend_yaml as parse_backend_yaml
from _typeshed import Incomplete
from torchgen.api.lazy import setValueT as setValueT
from torchgen.api.types import BaseCppType as BaseCppType
from torchgen.dest.lazy_ir import GenLazyIR as GenLazyIR, GenLazyNativeFuncDefinition as GenLazyNativeFuncDefinition, GenTSLazyIR as GenTSLazyIR
from torchgen.gen import get_grouped_native_functions as get_grouped_native_functions, parse_native_yaml as parse_native_yaml
from torchgen.model import NativeFunction as NativeFunction, NativeFunctionsGroup as NativeFunctionsGroup, OperatorName as OperatorName
from torchgen.selective_build.selector import SelectiveBuilder as SelectiveBuilder
from torchgen.utils import FileManager as FileManager, NamespaceHelper as NamespaceHelper, YamlLoader as YamlLoader, concatMap as concatMap
from typing import Any, List, NamedTuple, Sequence, Tuple, Type

class ParsedExternalYaml(NamedTuple):
    backend_key: Incomplete
    autograd_key: Incomplete
    cpp_namespace: Incomplete
    backend_indices: Incomplete
    full_codegen: Incomplete

def parse_native_functions_keys(backend_yaml_path: str, grouped_native_functions: Sequence[NativeFunction | NativeFunctionsGroup]) -> Tuple[List[OperatorName], List[Any], List[OperatorName]]: ...
def validate_shape_inference_header(shape_inference_hdr: str, expected_shape_infr_decls: List[str]) -> None: ...
def get_ltc_helper_fns() -> str: ...

class default_args:
    node_base: str
    node_base_hdr: str | None
    shape_inference_hdr: str
    tensor_class: str
    tensor_class_hdr: str
    lazy_ir_generator: Type[GenLazyIR]
    native_func_definition_generator: Type[GenLazyNativeFuncDefinition]
    backend_name: str

def main() -> None: ...
def run_gen_lazy_tensor(aten_path: str, source_yaml: str, output_dir: str, dry_run: bool, impl_path: str | None, node_base: str = ..., node_base_hdr: str | None = ..., tensor_class: str = ..., tensor_class_hdr: str = ..., shape_inference_hdr: str = ..., lazy_ir_generator: Type[GenLazyIR] = ..., native_func_definition_generator: Type[GenLazyNativeFuncDefinition] = ..., build_in_tree: bool = False, per_operator_headers: bool = False, backend_name: str = ..., gen_forced_fallback_code: bool = False, use_lazy_shape: bool = True, backend_namespace: str = 'torch::lazy', get_tensorlist: str = 'GetTensorList', get_tensor_or_wrap_number: str = 'GetLtcTensorOrCreateForWrappedNumber', try_get_tensor: str = 'TryGetLtcTensor', metrics_counter: str = 'TORCH_LAZY_FN_COUNTER("lazy::")', create_tensor: str = 'LazyTensor::Create', create_from_first_tensor: bool = False, create_aten_from_ltc_tensor: str = 'torch::lazy::CreateAtenFromLtcTensor', tuple_aten_from_ltc_tensors: str = 'torch::lazy::TupleAtenFromLtcTensors', lazy_value_class: str = 'torch::lazy::Value', lazy_tensor_ptr: str = 'LazyTensorPtr', get_device_fn: str = 'torch::lazy::GetBackendDevice') -> None: ...
