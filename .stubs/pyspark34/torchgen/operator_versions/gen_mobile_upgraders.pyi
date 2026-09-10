from _typeshed import Incomplete
from enum import Enum
from torchgen.code_template import CodeTemplate as CodeTemplate
from torchgen.operator_versions.gen_mobile_upgraders_constant import MOBILE_UPGRADERS_HEADER_DESCRIPTION as MOBILE_UPGRADERS_HEADER_DESCRIPTION
from typing import Any, Dict, List

class ByteCode(Enum):
    instructions: int
    constants: int
    types: int
    operators: int
    register_size: int

EXCLUDED_OP_SET: Incomplete
EXCLUE_UPGRADER_SET: Incomplete
ONE_INSTRUCTION: Incomplete
INSTRUCTION_LIST: Incomplete
ONE_CONSTANT: Incomplete
CONSTANT_LIST: Incomplete
CONSTANTS_LIST_EMPTY: str
ONE_TYPE: Incomplete
TYPE_LIST: Incomplete
TYPE_LIST_EMPTY: str
ONE_OPERATOTR_STRING: Incomplete
OPERATOR_STRING_LIST: Incomplete
ONE_UPGRADER_FUNCTION: Incomplete
ONE_UPGRADER_SRC: Incomplete
ONE_UPGRADER_IN_VERSION_MAP: Incomplete
ONE_OPERATOR_IN_VERSION_MAP: Incomplete
OPERATOR_VERSION_MAP: Incomplete
UPGRADER_CPP_SRC: Incomplete
UPGRADER_MOBILE_FILE_NAME: str
UPGRADER_ELEMENT: Incomplete
PER_OPERATOR_UPGRADER_LIST: Incomplete

def construct_instruction(instruction_list_from_yaml: List[Any]) -> str: ...
def construct_constants(constants_list_from_yaml: List[Any]) -> str: ...
def construct_operators(operator_list_from_yaml: List[Any]) -> str: ...
def construct_types(types_tr_list_from_yaml: List[Any]) -> str: ...
def construct_register_size(register_size_from_yaml: int) -> str: ...
def construct_version_maps(upgrader_bytecode_function_to_index_map: Dict[str, Any]) -> str: ...
def get_upgrader_bytecode_function_to_index_map(upgrader_dict: List[Dict[str, Any]]) -> Dict[str, Any]: ...
def write_cpp(cpp_path: str, upgrader_dict: List[Dict[str, Any]]) -> None: ...
def sort_upgrader(upgrader_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]: ...
def main() -> None: ...
