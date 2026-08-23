from _typeshed import Incomplete
from typing_extensions import Final

error_codes: dict[str, ErrorCode]
sub_code_map: dict[str, set[str]]

class ErrorCode:
    code: Incomplete
    description: Incomplete
    category: Incomplete
    default_enabled: Incomplete
    sub_code_of: Incomplete
    def __init__(self, code: str, description: str, category: str, default_enabled: bool = True, sub_code_of: ErrorCode | None = None) -> None: ...

ATTR_DEFINED: Final[Incomplete]
NAME_DEFINED: Final[Incomplete]
CALL_ARG: Final[ErrorCode]
ARG_TYPE: Final[Incomplete]
CALL_OVERLOAD: Final[Incomplete]
VALID_TYPE: Final[ErrorCode]
VAR_ANNOTATED: Final[Incomplete]
OVERRIDE: Final[Incomplete]
RETURN: Final[ErrorCode]
RETURN_VALUE: Final[ErrorCode]
ASSIGNMENT: Final[ErrorCode]
METHOD_ASSIGN: Final[ErrorCode]
TYPE_ARG: Final[Incomplete]
TYPE_VAR: Final[Incomplete]
UNION_ATTR: Final[Incomplete]
INDEX: Final[Incomplete]
OPERATOR: Final[Incomplete]
LIST_ITEM: Final[Incomplete]
DICT_ITEM: Final[Incomplete]
TYPEDDICT_ITEM: Final[Incomplete]
TYPEDDICT_UNKNOWN_KEY: Final[Incomplete]
HAS_TYPE: Final[Incomplete]
IMPORT: Final[Incomplete]
NO_REDEF: Final[Incomplete]
FUNC_RETURNS_VALUE: Final[Incomplete]
ABSTRACT: Final[Incomplete]
TYPE_ABSTRACT: Final[Incomplete]
VALID_NEWTYPE: Final[Incomplete]
STRING_FORMATTING: Final[Incomplete]
STR_BYTES_PY3: Final[Incomplete]
EXIT_RETURN: Final[Incomplete]
LITERAL_REQ: Final[Incomplete]
UNUSED_COROUTINE: Final[Incomplete]
EMPTY_BODY: Final[ErrorCode]
SAFE_SUPER: Final[Incomplete]
TOP_LEVEL_AWAIT: Final[Incomplete]
NO_UNTYPED_DEF: Final[ErrorCode]
NO_UNTYPED_CALL: Final[Incomplete]
REDUNDANT_CAST: Final[Incomplete]
ASSERT_TYPE: Final[Incomplete]
COMPARISON_OVERLAP: Final[Incomplete]
NO_ANY_UNIMPORTED: Final[Incomplete]
NO_ANY_RETURN: Final[Incomplete]
UNREACHABLE: Final[Incomplete]
ANNOTATION_UNCHECKED: Incomplete
POSSIBLY_UNDEFINED: Final[ErrorCode]
REDUNDANT_EXPR: Final[Incomplete]
TRUTHY_BOOL: Final[ErrorCode]
TRUTHY_FUNCTION: Final[ErrorCode]
TRUTHY_ITERABLE: Final[ErrorCode]
NAME_MATCH: Final[Incomplete]
NO_OVERLOAD_IMPL: Final[Incomplete]
IGNORE_WITHOUT_CODE: Final[Incomplete]
UNUSED_AWAITABLE: Final[Incomplete]
REDUNDANT_SELF_TYPE: Incomplete
USED_BEFORE_DEF: Final[ErrorCode]
UNUSED_IGNORE: Final[Incomplete]
SYNTAX: Final[ErrorCode]
FILE: Final[Incomplete]
MISC: Final[Incomplete]
