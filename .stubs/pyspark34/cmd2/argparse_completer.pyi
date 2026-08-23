import argparse
from .ansi import style_aware_wcswidth as style_aware_wcswidth, widest_line as widest_line
from .argparse_custom import ChoicesCallable as ChoicesCallable, ChoicesProviderFuncWithTokens as ChoicesProviderFuncWithTokens, CompletionItem as CompletionItem, generate_range_error as generate_range_error
from .cmd2 import Cmd as Cmd
from .command_definition import CommandSet as CommandSet
from .constants import INFINITY as INFINITY
from .exceptions import CompletionError as CompletionError
from .table_creator import Column as Column, HorizontalAlignment as HorizontalAlignment, SimpleTable as SimpleTable
from _typeshed import Incomplete
from typing import Dict, List, Type

DEFAULT_DESCRIPTIVE_HEADER: str
ARG_TOKENS: str

class _ArgumentState:
    """Keeps state of an argument being parsed"""
    action: Incomplete
    min: Incomplete
    max: Incomplete
    count: int
    is_remainder: Incomplete
    def __init__(self, arg_action: argparse.Action) -> None: ...

class _UnfinishedFlagError(CompletionError):
    def __init__(self, flag_arg_state: _ArgumentState) -> None:
        """
        CompletionError which occurs when the user has not finished the current flag
        :param flag_arg_state: information about the unfinished flag action
        """

class _NoResultsError(CompletionError):
    def __init__(self, parser: argparse.ArgumentParser, arg_action: argparse.Action) -> None:
        """
        CompletionError which occurs when there are no results. If hinting is allowed, then its message will
        be a hint about the argument being tab completed.
        :param parser: ArgumentParser instance which owns the action being tab completed
        :param arg_action: action being tab completed
        """

class ArgparseCompleter:
    """Automatic command line tab completion based on argparse parameters"""
    def __init__(self, parser: argparse.ArgumentParser, cmd2_app: Cmd, *, parent_tokens: Dict[str, List[str]] | None = None) -> None:
        """
        Create an ArgparseCompleter

        :param parser: ArgumentParser instance
        :param cmd2_app: reference to the Cmd2 application that owns this ArgparseCompleter
        :param parent_tokens: optional dictionary mapping parent parsers' arg names to their tokens
                              This is only used by ArgparseCompleter when recursing on subcommand parsers
                              Defaults to None
        """
    def complete(self, text: str, line: str, begidx: int, endidx: int, tokens: List[str], *, cmd_set: CommandSet | None = None) -> List[str]:
        """
        Complete text using argparse metadata

        :param text: the string prefix we are attempting to match (all matches must begin with it)
        :param line: the current input line with leading whitespace removed
        :param begidx: the beginning index of the prefix text
        :param endidx: the ending index of the prefix text
        :param tokens: list of argument tokens being passed to the parser
        :param cmd_set: if tab completing a command, the CommandSet the command's function belongs to, if applicable.
                        Defaults to None.

        :raises: CompletionError for various types of tab completion errors
        """
    def complete_subcommand_help(self, text: str, line: str, begidx: int, endidx: int, tokens: List[str]) -> List[str]:
        """
        Supports cmd2's help command in the completion of subcommand names
        :param text: the string prefix we are attempting to match (all matches must begin with it)
        :param line: the current input line with leading whitespace removed
        :param begidx: the beginning index of the prefix text
        :param endidx: the ending index of the prefix text
        :param tokens: arguments passed to command/subcommand
        :return: List of subcommand completions
        """
    def format_help(self, tokens: List[str]) -> str:
        """
        Supports cmd2's help command in the retrieval of help text
        :param tokens: arguments passed to help command
        :return: help text of the command being queried
        """

DEFAULT_AP_COMPLETER: Type[ArgparseCompleter]

def set_default_ap_completer_type(completer_type: Type[ArgparseCompleter]) -> None:
    """
    Set the default ArgparseCompleter class for a cmd2 app.

    :param completer_type: Type that is a subclass of ArgparseCompleter.
    """
