from _typeshed import Incomplete
from typing import Any, Dict, Final

PREFIX: Final[str]
NATIVE_PREFIX: Final[str]
DUNDER_PREFIX: Final[str]
REG_PREFIX: Final[str]
STATIC_PREFIX: Final[str]
TYPE_PREFIX: Final[str]
MODULE_PREFIX: Final[str]
ATTR_PREFIX: Final[str]
ENV_ATTR_NAME: Final[str]
NEXT_LABEL_ATTR_NAME: Final[str]
TEMP_ATTR_NAME: Final[str]
LAMBDA_NAME: Final[str]
PROPSET_PREFIX: Final[str]
SELF_NAME: Final[str]
TOP_LEVEL_NAME: Final[str]
FAST_ISINSTANCE_MAX_SUBCLASSES: Final[int]
SIZEOF_SIZE_T_SYSCONFIG: Final[Incomplete]
SIZEOF_SIZE_T: Final[Incomplete]
IS_32_BIT_PLATFORM: Final[Incomplete]
PLATFORM_SIZE: Incomplete
MAX_SHORT_INT: Final[Incomplete]
MIN_SHORT_INT: Final[Incomplete]
MAX_LITERAL_SHORT_INT: Final[Incomplete]
MIN_LITERAL_SHORT_INT: Final[Incomplete]
BITMAP_TYPE: Final[str]
BITMAP_BITS: Final[int]
RUNTIME_C_FILES: Final[Incomplete]
JsonDict = Dict[str, Any]

def shared_lib_name(group_name: str) -> str:
    """Given a group name, return the actual name of its extension module.

    (This just adds a suffix to the final component.)
    """
def short_name(name: str) -> str: ...
def use_vectorcall(capi_version: tuple[int, int]) -> bool: ...
def use_method_vectorcall(capi_version: tuple[int, int]) -> bool: ...
def get_id_from_name(name: str, fullname: str, line: int) -> str:
    """Create a unique id for a function.

    This creates an id that is unique for any given function definition, so that it can be used as
    a dictionary key. This is usually the fullname of the function, but this is different in that
    it handles the case where the function is named '_', in which case multiple different functions
    could have the same name."""
def short_id_from_name(func_name: str, shortname: str, line: int | None) -> str: ...
def bitmap_name(index: int) -> str: ...
