from _typeshed import Incomplete
from torchgen.api.types import DispatcherSignature as DispatcherSignature
from torchgen.code_template import CodeTemplate as CodeTemplate
from torchgen.context import native_function_manager as native_function_manager
from torchgen.gen import get_grouped_native_functions as get_grouped_native_functions, parse_native_yaml as parse_native_yaml
from torchgen.model import BackendIndex as BackendIndex, BackendMetadata as BackendMetadata, DispatchKey as DispatchKey, NativeFunction as NativeFunction, NativeFunctionsGroup as NativeFunctionsGroup, OperatorName as OperatorName
from torchgen.selective_build.selector import SelectiveBuilder as SelectiveBuilder
from torchgen.utils import FileManager as FileManager, NamespaceHelper as NamespaceHelper, Target as Target, YamlLoader as YamlLoader, concatMap as concatMap, context as context
from typing import Dict, List, NamedTuple, Sequence

class ParsedExternalYaml(NamedTuple):
    backend_key: Incomplete
    autograd_key: Incomplete
    class_name: Incomplete
    cpp_namespace: Incomplete
    backend_indices: Incomplete

def parse_backend_yaml(backend_yaml_path: str, grouped_native_functions: Sequence[NativeFunction | NativeFunctionsGroup], backend_indices: Dict[DispatchKey, BackendIndex]) -> ParsedExternalYaml: ...
def error_on_missing_kernels(native_functions: Sequence[NativeFunction], backend_indices: Dict[DispatchKey, BackendIndex], backend_key: DispatchKey, autograd_key: DispatchKey | None, class_name: str, kernel_defn_file_path: str, full_codegen: List[OperatorName] | None = None) -> None: ...
def main() -> None: ...
def gen_dispatchkey_nativefunc_headers(fm: FileManager, class_name: str, cpp_namespace: str, backend_indices: Dict[DispatchKey, BackendIndex], grouped_native_functions: Sequence[NativeFunction | NativeFunctionsGroup], backend_dispatch_key: DispatchKey, autograd_dispatch_key: DispatchKey | None, backend_name: str = '') -> None: ...
def gen_dispatcher_registrations(fm: FileManager, output_dir: str, class_name: str, backend_indices: Dict[DispatchKey, BackendIndex], grouped_native_functions: Sequence[NativeFunction | NativeFunctionsGroup], backend_dispatch_key: DispatchKey, dispatch_key: DispatchKey, selector: SelectiveBuilder, build_in_tree: bool = False, per_operator_headers: bool = False, backend_name: str = '', eager_registration: bool = True) -> None: ...
def run(source_yaml: str, output_dir: str, dry_run: bool, impl_path: str | None = None) -> None: ...
