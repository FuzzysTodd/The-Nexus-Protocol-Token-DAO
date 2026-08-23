from _typeshed import Incomplete
from torchgen.model import NativeFunctionsGroup as NativeFunctionsGroup, NativeFunctionsViewGroup as NativeFunctionsViewGroup
from typing import Dict

def func_name_base_str(g: NativeFunctionsGroup | NativeFunctionsViewGroup) -> str: ...

is_hand_written_ops_: Incomplete

def is_hand_written(g: NativeFunctionsGroup | NativeFunctionsViewGroup) -> bool: ...
def override_test_values(arg_map: Dict[str, str], op_name: str, index: int) -> None: ...
