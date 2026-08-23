from torch.onnx._internal.diagnostics.infra import sarif as sarif
from typing import Any, Callable

def snake_case_to_camel_case(s: str) -> str: ...
def camel_case_to_snake_case(s: str) -> str: ...
def kebab_case_to_snake_case(s: str) -> str: ...
def sarif_to_json(attr_cls_obj: _SarifClass, indent: str | None = ' ') -> str: ...
def pretty_print_title(title: str, width: int = 80, fill_char: str = '=', print_output: bool = True) -> str:
    """Pretty prints title in below format:

    ==================== title ====================
    """
def pretty_print_item_title(title: str, fill_char: str = '=', print_output: bool = True) -> str:
    """Pretty prints title in below format:

    title
    =====
    """
def format_argument(obj: Any) -> str: ...
def display_name(fn: Callable) -> str: ...
