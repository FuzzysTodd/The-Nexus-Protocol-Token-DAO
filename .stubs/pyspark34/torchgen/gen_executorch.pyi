from dataclasses import dataclass
from torchgen import dest as dest
from torchgen.api.types import CType as CType, CppSignature as CppSignature, CppSignatureGroup as CppSignatureGroup, NamedCType as NamedCType
from torchgen.context import method_with_native_function as method_with_native_function, with_native_function_and_index as with_native_function_and_index
from torchgen.executorch.api import et_cpp as et_cpp
from torchgen.executorch.api.custom_ops import ComputeNativeFunctionStub as ComputeNativeFunctionStub, gen_custom_ops_registration as gen_custom_ops_registration
from torchgen.executorch.api.types import ExecutorchCppSignature as ExecutorchCppSignature
from torchgen.executorch.api.unboxing import Unboxing as Unboxing
from torchgen.gen import LineLoader as LineLoader, ParsedYaml as ParsedYaml, get_custom_build_selector as get_custom_build_selector, get_native_function_declarations as get_native_function_declarations, get_native_function_schema_registrations as get_native_function_schema_registrations, parse_native_yaml as parse_native_yaml
from torchgen.model import BackendIndex as BackendIndex, BackendMetadata as BackendMetadata, DispatchKey as DispatchKey, Location as Location, NativeFunction as NativeFunction, NativeFunctionsGroup as NativeFunctionsGroup, OperatorName as OperatorName, Variant as Variant, is_cuda_dispatch_key as is_cuda_dispatch_key
from torchgen.selective_build.selector import SelectiveBuilder as SelectiveBuilder
from torchgen.utils import FileManager as FileManager, NamespaceHelper as NamespaceHelper, context as context, make_file_manager as make_file_manager, mapMaybe as mapMaybe
from typing import Callable, Dict, List, Sequence, TextIO, Tuple

def static_dispatch(sig: CppSignature | ExecutorchCppSignature, f: NativeFunction, backend_indices: List[BackendIndex]) -> str:
    '''
    For a given `NativeFunction`, find out the corresponding native function and dispatch to it. If zero or more than one
    native function exists, error out. A simplified version of register_dispatch_key.py
    Arguments:
        sig: A CppSignature for this native function we want to use.
        f: NativeFunction to generate static dispatch.
        backend_indices: All available backends.
    Return:
        C++ code to call backend-specific functions, e.g., "return at::native::add(self, other, scale);"
    '''

@dataclass(frozen=True)
class ComputeFunction:
    static_dispatch_backend_indices: List[BackendIndex]
    selector: SelectiveBuilder
    use_aten_lib: bool
    is_custom_op: Callable[[NativeFunction], bool]
    def __call__(self, f: NativeFunction) -> str | None: ...
    def __init__(self, static_dispatch_backend_indices, selector, use_aten_lib, is_custom_op) -> None: ...

@dataclass(frozen=True)
class ComputeCodegenUnboxedKernels:
    selector: SelectiveBuilder
    use_aten_lib: bool
    def __call__(self, f: NativeFunction) -> str: ...
    def __init__(self, selector, use_aten_lib) -> None: ...

def gen_unboxing(*, native_functions: Sequence[NativeFunction], cpu_fm: FileManager, selector: SelectiveBuilder, use_aten_lib: bool) -> None: ...
def compute_native_function_declaration(g: NativeFunctionsGroup | NativeFunction, backend_index: BackendIndex) -> List[str]: ...
def gen_functions_declarations(*, native_functions: Sequence[NativeFunction], static_dispatch_idx: List[BackendIndex], selector: SelectiveBuilder, use_aten_lib: bool, custom_ops_native_functions: Sequence[NativeFunction] | None = None) -> str:
    """
    Generates namespace separated C++ function API inline declaration/definitions.
    Native functions are grouped by namespaces and the generated code is wrapped inside
    namespace blocks.

    E.g., for `custom_1::foo.out` in yaml file we will generate a C++ API as a symbol
    in `torch::executor::custom_1::foo_out`. This way we avoid symbol conflict when
    the other `custom_2::foo.out` is available.
    """
def gen_headers(*, native_functions: Sequence[NativeFunction], custom_ops_native_functions: Sequence[NativeFunction], static_dispatch_idx: List[BackendIndex], selector: SelectiveBuilder, backend_indices: Dict[DispatchKey, BackendIndex], cpu_fm: FileManager, use_aten_lib: bool) -> None: ...
def gen_custom_ops(*, native_functions: Sequence[NativeFunction], selector: SelectiveBuilder, backend_indices: Dict[DispatchKey, BackendIndex], cpu_fm: FileManager, rocm: bool) -> None: ...
def translate_native_yaml(tags_yaml_path: str, aten_yaml_path: str, native_yaml_path: str | None, use_aten_lib: bool, out_file: TextIO) -> None:
    '''Translates Executorch DSL dialect to use the same syntax as
    native_functions.yaml. The major difference is that Executorch DSL dialect
    supports "op" key, where it refers to the operator name in native_functions.yaml.

    For example, a functions.yaml may have the following entry:

    - op: add.out
      ...

    It needs to be translated to the following:

    - func: add.out(Tensor self, Tensor other, *, Scalar alpha=1, Tensor(a!) out) -> Tensor(a!)
      ...

    We go in aten_yaml_path and find the operator schema for "add.out" and add it
    to the original functions.yaml. We also add required field "variants", where for
    Executorch it will always be "function".

    For ATen mode we don\'t have to do the translation because native_yaml_path is
    the same as native_functions.yaml.

    Args:
        tags_yaml_path: Path to a tags.yaml file to satisfy codegen parsing.
            It is not optional.
        aten_yaml_path: Path to ATen operator yaml file native_functions.yaml.
        native_yaml_path: Path to a functions.yaml file to parse.
            If the path does not exist in the filesystem, it is treated as an
            empty file. If `custom_ops_yaml_path` exists, the contents of that
            file are appended to the yaml input to be parsed.
        use_aten_lib: We use this flag to determine if we want to generate native
            functions. In ATen mode we should generate out= variants.
        out_file: The IO object that we are writing into.
    Returns:
        None
    '''
def convert_backend_indices(bs: Dict[DispatchKey, Dict[OperatorName, BackendMetadata]]) -> Dict[DispatchKey, BackendIndex]: ...
def parse_yaml(path: str | None, tags_yaml_path: str, function_filter: Callable[[NativeFunction], bool], skip_native_fns_gen: bool = False) -> Tuple[List[NativeFunction], Dict[DispatchKey, Dict[OperatorName, BackendMetadata]]]: ...
def parse_yaml_files(tags_yaml_path: str, aten_yaml_path: str, native_yaml_path: str | None, custom_ops_yaml_path: str | None, selector: SelectiveBuilder, use_aten_lib: bool) -> Tuple[ParsedYaml, ParsedYaml | None]:
    """Parses functions.yaml and custom_ops.yaml files.

    Args:
        tags_yaml_path: Path to a tags.yaml file to satisfy codegen parsing.
            It is not optional.
        aten_yaml_path: Path to ATen operator yaml file native_functions.yaml.
        native_yaml_path: Path to a functions.yaml file to parse.
            If the path does not exist in the filesystem, it is treated as an
            empty file. If `custom_ops_yaml_path` exists, the contents of that
            file are appended to the yaml input to be parsed.
        custom_ops_yaml_path: Path to a custom_ops.yaml file to parse. If
            the path does not exist in the filesystem, it is ignored.
        selector: For selective build.
        use_aten_lib: We use this flag to determine if we want to generate native
            functions. In ATen mode we should generate out= variants.
    Returns:
        A tuple with two elements:
        [0]: The parsed results of concatenating the contents of
             `native_yaml_path` and `custom_ops_yaml_path`.
        [1]: The parsed results of the contents of `custom_ops_yaml_path`, if
             present. If not present, None.
    """
def main() -> None: ...
