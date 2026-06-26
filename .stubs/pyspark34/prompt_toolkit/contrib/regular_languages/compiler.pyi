from .regex_parser import Node
from _typeshed import Incomplete
from typing import Callable, Dict, Iterable, Iterator, Match as RegexMatch, Pattern

__all__ = ['compile']

EscapeFuncDict = Dict[str, Callable[[str], str]]

class _CompiledGrammar:
    """
    Compiles a grammar. This will take the parse tree of a regular expression
    and compile the grammar.

    :param root_node: :class~`.regex_parser.Node` instance.
    :param escape_funcs: `dict` mapping variable names to escape callables.
    :param unescape_funcs: `dict` mapping variable names to unescape callables.
    """
    root_node: Incomplete
    escape_funcs: Incomplete
    unescape_funcs: Incomplete
    def __init__(self, root_node: Node, escape_funcs: EscapeFuncDict | None = None, unescape_funcs: EscapeFuncDict | None = None) -> None: ...
    def escape(self, varname: str, value: str) -> str:
        """
        Escape `value` to fit in the place of this variable into the grammar.
        """
    def unescape(self, varname: str, value: str) -> str:
        """
        Unescape `value`.
        """
    def match(self, string: str) -> Match | None:
        """
        Match the string with the grammar.
        Returns a :class:`Match` instance or `None` when the input doesn't match the grammar.

        :param string: The input string.
        """
    def match_prefix(self, string: str) -> Match | None:
        '''
        Do a partial match of the string with the grammar. The returned
        :class:`Match` instance can contain multiple representations of the
        match. This will never return `None`. If it doesn\'t match at all, the "trailing input"
        part will capture all of the input.

        :param string: The input string.
        '''

class Match:
    """
    :param string: The input string.
    :param re_matches: List of (compiled_re_pattern, re_match) tuples.
    :param group_names_to_nodes: Dictionary mapping all the re group names to the matching Node instances.
    """
    string: Incomplete
    def __init__(self, string: str, re_matches: list[tuple[Pattern[str], RegexMatch[str]]], group_names_to_nodes: dict[str, str], unescape_funcs: dict[str, Callable[[str], str]]) -> None: ...
    def variables(self) -> Variables:
        """
        Returns :class:`Variables` instance.
        """
    def trailing_input(self) -> MatchVariable | None:
        '''
        Get the `MatchVariable` instance, representing trailing input, if there is any.
        "Trailing input" is input at the end that does not match the grammar anymore, but
        when this is removed from the end of the input, the input would be a valid string.
        '''
    def end_nodes(self) -> Iterable[MatchVariable]:
        """
        Yields `MatchVariable` instances for all the nodes having their end
        position at the end of the input string.
        """

class Variables:
    def __init__(self, tuples: list[tuple[str, str, tuple[int, int]]]) -> None: ...
    def get(self, key: str, default: str | None = None) -> str | None: ...
    def getall(self, key: str) -> list[str]: ...
    def __getitem__(self, key: str) -> str | None: ...
    def __iter__(self) -> Iterator[MatchVariable]:
        """
        Yield `MatchVariable` instances.
        """

class MatchVariable:
    """
    Represents a match of a variable in the grammar.

    :param varname: (string) Name of the variable.
    :param value: (string) Value of this variable.
    :param slice: (start, stop) tuple, indicating the position of this variable
                  in the input string.
    """
    varname: Incomplete
    value: Incomplete
    slice: Incomplete
    start: Incomplete
    stop: Incomplete
    def __init__(self, varname: str, value: str, slice: tuple[int, int]) -> None: ...

def compile(expression: str, escape_funcs: EscapeFuncDict | None = None, unescape_funcs: EscapeFuncDict | None = None) -> _CompiledGrammar:
    """
    Compile grammar (given as regex string), returning a `CompiledGrammar`
    instance.
    """
