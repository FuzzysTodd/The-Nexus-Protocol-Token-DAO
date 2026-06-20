import tokenize
from _typeshed import Incomplete
from typing import Any, NamedTuple, Sequence
from typing_extensions import Final, TypeAlias as _TypeAlias

Sig: _TypeAlias

def is_valid_type(s: str) -> bool:
    """Try to determine whether a string might be a valid type annotation."""

class ArgSig:
    """Signature info for a single argument."""
    name: Incomplete
    type: Incomplete
    default: Incomplete
    def __init__(self, name: str, type: str | None = None, default: bool = False) -> None: ...
    def __eq__(self, other: Any) -> bool: ...

class FunctionSig(NamedTuple):
    name: str
    args: list[ArgSig]
    ret_type: str

STATE_INIT: Final[int]
STATE_FUNCTION_NAME: Final[int]
STATE_ARGUMENT_LIST: Final[int]
STATE_ARGUMENT_TYPE: Final[int]
STATE_ARGUMENT_DEFAULT: Final[int]
STATE_RETURN_VALUE: Final[int]
STATE_OPEN_BRACKET: Final[int]

class DocStringParser:
    """Parse function signatures in documentation."""
    function_name: Incomplete
    state: Incomplete
    accumulator: str
    arg_type: Incomplete
    arg_name: str
    arg_default: Incomplete
    ret_type: str
    found: bool
    args: Incomplete
    signatures: Incomplete
    def __init__(self, function_name: str) -> None: ...
    def add_token(self, token: tokenize.TokenInfo) -> None:
        """Process next token from the token stream."""
    def reset(self) -> None: ...
    def get_signatures(self) -> list[FunctionSig]:
        """Return sorted copy of the list of signatures found so far."""

def infer_sig_from_docstring(docstr: str | None, name: str) -> list[FunctionSig] | None:
    """Convert function signature to list of TypedFunctionSig

    Look for function signatures of function in docstring. Signature is a string of
    the format <function_name>(<signature>) -> <return type> or perhaps without
    the return type.

    Returns empty list, when no signature is found, one signature in typical case,
    multiple signatures, if docstring specifies multiple signatures for overload functions.
    Return None if the docstring is empty.

    Arguments:
        * docstr: docstring
        * name: name of function for which signatures are to be found
    """
def infer_arg_sig_from_anon_docstring(docstr: str) -> list[ArgSig]:
    '''Convert signature in form of "(self: TestClass, arg0: str=\'ada\')" to List[TypedArgList].'''
def infer_ret_type_sig_from_docstring(docstr: str, name: str) -> str | None:
    '''Convert signature in form of "func(self: TestClass, arg0) -> int" to their return type.'''
def infer_ret_type_sig_from_anon_docstring(docstr: str) -> str | None:
    '''Convert signature in form of "(self: TestClass, arg0) -> int" to their return type.'''
def parse_signature(sig: str) -> tuple[str, list[str], list[str]] | None:
    '''Split function signature into its name, positional an optional arguments.

    The expected format is "func_name(arg, opt_arg=False)". Return the name of function
    and lists of positional and optional argument names.
    '''
def build_signature(positional: Sequence[str], optional: Sequence[str]) -> str:
    """Build function signature from lists of positional and optional argument names."""
def parse_all_signatures(lines: Sequence[str]) -> tuple[list[Sig], list[Sig]]:
    """Parse all signatures in a given reST document.

    Return lists of found signatures for functions and classes.
    """
def find_unique_signatures(sigs: Sequence[Sig]) -> list[Sig]:
    """Remove names with duplicate found signatures."""
def infer_prop_type_from_docstring(docstr: str | None) -> str | None:
    '''Check for Google/Numpy style docstring type annotation for a property.

    The docstring has the format "<type>: <descriptions>".
    In the type string, we allow the following characters:
    * dot: because sometimes classes are annotated using full path
    * brackets: to allow type hints like List[int]
    * comma/space: things like Tuple[int, int]
    '''
