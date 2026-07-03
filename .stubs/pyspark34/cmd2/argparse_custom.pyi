import argparse
from . import ansi as ansi, constants as constants
from .argparse_completer import ArgparseCompleter as ArgparseCompleter
from _typeshed import Incomplete
from typing import Any, Dict, List, NoReturn, Sequence, Set, Type
from typing_extensions import Protocol

def generate_range_error(range_min: int, range_max: int | float) -> str:
    """Generate an error message when the the number of arguments provided is not within the expected range"""

class CompletionItem(str):
    """
    Completion item with descriptive text attached

    See header of this file for more information
    """
    def __new__(cls, value: object, *args: Any, **kwargs: Any) -> CompletionItem: ...
    description: Incomplete
    def __init__(self, value: object, description: str = '', *args: Any) -> None:
        """
        CompletionItem Initializer

        :param value: the value being tab completed
        :param description: description text to display
        :param args: args for str __init__
        :param kwargs: kwargs for str __init__
        """
    @property
    def orig_value(self) -> Any:
        """Read-only property for _orig_value"""

class ChoicesProviderFuncBase(Protocol):
    """
    Function that returns a list of choices in support of tab completion
    """
    def __call__(self) -> List[str]: ...

class ChoicesProviderFuncWithTokens(Protocol):
    """
    Function that returns a list of choices in support of tab completion and accepts a dictionary of prior arguments.
    """
    def __call__(self, *, arg_tokens: Dict[str, List[str]] = {}) -> List[str]: ...
ChoicesProviderFunc = ChoicesProviderFuncBase | ChoicesProviderFuncWithTokens

class CompleterFuncBase(Protocol):
    """
    Function to support tab completion with the provided state of the user prompt
    """
    def __call__(self, text: str, line: str, begidx: int, endidx: int) -> List[str]: ...

class CompleterFuncWithTokens(Protocol):
    """
    Function to support tab completion with the provided state of the user prompt and accepts a dictionary of prior
    arguments.
    """
    def __call__(self, text: str, line: str, begidx: int, endidx: int, *, arg_tokens: Dict[str, List[str]] = {}) -> List[str]: ...
CompleterFunc = CompleterFuncBase | CompleterFuncWithTokens

class ChoicesCallable:
    """
    Enables using a callable as the choices provider for an argparse argument.
    While argparse has the built-in choices attribute, it is limited to an iterable.
    """
    is_completer: Incomplete
    to_call: Incomplete
    def __init__(self, is_completer: bool, to_call: CompleterFunc | ChoicesProviderFunc) -> None:
        """
        Initializer
        :param is_completer: True if to_call is a tab completion routine which expects
                             the args: text, line, begidx, endidx
        :param to_call: the callable object that will be called to provide choices for the argument
        """
    @property
    def completer(self) -> CompleterFunc: ...
    @property
    def choices_provider(self) -> ChoicesProviderFunc: ...

ATTR_CHOICES_CALLABLE: str
ATTR_DESCRIPTIVE_HEADER: str
ATTR_NARGS_RANGE: str
ATTR_SUPPRESS_TAB_HINT: str
CUSTOM_ACTION_ATTRIBS: Set[str]

def register_argparse_argument_parameter(param_name: str, param_type: Type[Any] | None) -> None:
    """
    Registers a custom argparse argument parameter.

    The registered name will then be a recognized keyword parameter to the parser's `add_argument()` function.

    An accessor functions will be added to the parameter's Action object in the form of: ``get_{param_name}()``
    and ``set_{param_name}(value)``.

    :param param_name: Name of the parameter to add.
    :param param_type: Type of the parameter to add.
    """

orig_actions_container_add_argument: Incomplete
orig_argument_parser_get_nargs_pattern: Incomplete
orig_argument_parser_match_argument: Incomplete
ATTR_AP_COMPLETER_TYPE: str

class Cmd2HelpFormatter(argparse.RawTextHelpFormatter):
    """Custom help formatter to configure ordering of help text"""

class Cmd2ArgumentParser(argparse.ArgumentParser):
    """Custom ArgumentParser class that improves error and help output"""
    def __init__(self, prog: str | None = None, usage: str | None = None, description: str | None = None, epilog: str | None = None, parents: Sequence[argparse.ArgumentParser] = (), formatter_class: Type[argparse.HelpFormatter] = ..., prefix_chars: str = '-', fromfile_prefix_chars: str | None = None, argument_default: str | None = None, conflict_handler: str = 'error', add_help: bool = True, allow_abbrev: bool = True, *, ap_completer_type: Type['ArgparseCompleter'] | None = None) -> None:
        """
        # Custom parameter added by cmd2

        :param ap_completer_type: optional parameter which specifies a subclass of ArgparseCompleter for custom tab completion
                                  behavior on this parser. If this is None or not present, then cmd2 will use
                                  argparse_completer.DEFAULT_AP_COMPLETER when tab completing this parser's arguments
        """
    def add_subparsers(self, **kwargs: Any) -> argparse._SubParsersAction:
        """
        Custom override. Sets a default title if one was not given.

        :param kwargs: additional keyword arguments
        :return: argparse Subparser Action
        """
    def error(self, message: str) -> NoReturn:
        """Custom override that applies custom formatting to the error message"""
    def format_help(self) -> str:
        """Copy of format_help() from argparse.ArgumentParser with tweaks to separately display required parameters"""

class Cmd2AttributeWrapper:
    """
    Wraps a cmd2-specific attribute added to an argparse Namespace.
    This makes it easy to know which attributes in a Namespace are
    arguments from a parser and which were added by cmd2.
    """
    def __init__(self, attribute: Any) -> None: ...
    def get(self) -> Any:
        """Get the value of the attribute"""
    def set(self, new_val: Any) -> None:
        """Set the value of the attribute"""

DEFAULT_ARGUMENT_PARSER: Type[argparse.ArgumentParser]

def set_default_argument_parser_type(parser_type: Type[argparse.ArgumentParser]) -> None:
    """
    Set the default ArgumentParser class for a cmd2 app. This must be called prior to loading cmd2.py if
    you want to override the parser for cmd2's built-in commands. See examples/override_parser.py.
    """
