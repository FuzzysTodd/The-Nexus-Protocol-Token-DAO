from _typeshed import Incomplete
from typing import Any, Dict, Tuple, Type, TypeVar

logger: Incomplete

def loads(input: str) -> Dict:
    """same as json.loads, no exception throws, only return empty dict on exception
    Args:
        input (str): [description]
    Returns:
        dict: [description]
    """
def marshal(obj, omit_empty: bool = True) -> str:
    """Attemp to convert any object to json str, no exceptions throws if failed

    Args:
        obj ([type]): anything
        omit_empty (bool, optional): ignore empty fields

    Returns:
        str: json string
    """
def obj_to_dict(obj, omit_empty: bool = True):
    """Convert any object to dict. You can customize how one class should be converted to dict by
    implement object_to_dict method under the class
    def object_to_dict() -> dict

    Args:
        obj ([type]): [description]
        omit_empty (bool, optional): ignore empty fields. Defaults to True.

    Returns:
        json dict
    """
def is_empty(obj): ...
def to_legal_json_key(input: str) -> str:
    """
    convert my-info to my_info, since - is not legal json key

    Returns:
        str: converted key
    """
def process_dict_key_to_be_legal(some_json: Dict[str, Any]): ...
T = TypeVar('T')

def unmarshal(json_input: Dict[str, Any], cls: Type[T]) -> Tuple[T, Exception]: ...
def unmarshal_from_str(str_input: str, cls: Type[T]) -> Tuple[T, Exception]: ...
def get_class(module_name: str, class_name: str) -> Type: ...
def to_real_class(current_module, cls) -> Type: ...
