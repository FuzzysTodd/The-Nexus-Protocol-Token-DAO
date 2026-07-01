from _typeshed import Incomplete
from collections.abc import Mapping
from statsmodels.tools.sm_exceptions import ParseError as ParseError
from typing import NamedTuple

def dedent_lines(lines):
    """Deindent a list of lines maximally"""
def strip_blank_lines(line):
    """Remove leading and trailing blank lines from a list of lines"""

class Reader:
    """
    A line-based string reader.
    """
    def __init__(self, data) -> None:
        """
        Parameters
        ----------
        data : str
           String with lines separated by '
'.
        """
    def __getitem__(self, n): ...
    def reset(self) -> None: ...
    def read(self): ...
    def seek_next_non_empty_line(self) -> None: ...
    def eof(self): ...
    def read_to_condition(self, condition_func): ...
    def read_to_next_empty_line(self): ...
    def read_to_next_unindented_line(self): ...
    def peek(self, n: int = 0): ...
    def is_empty(self): ...

class Parameter(NamedTuple):
    name: Incomplete
    type: Incomplete
    desc: Incomplete

class NumpyDocString(Mapping):
    """Parses a numpydoc string to an abstract representation

    Instances define a mapping from section title to structured data.
    """
    sections: Incomplete
    def __init__(self, docstring) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, val) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    empty_description: str

class Docstring:
    """
    Docstring modification.

    Parameters
    ----------
    docstring : str
        The docstring to modify.
    """
    def __init__(self, docstring) -> None: ...
    def remove_parameters(self, parameters) -> None:
        """
        Parameters
        ----------
        parameters : str, list[str]
            The names of the parameters to remove.
        """
    def insert_parameters(self, after, parameters) -> None:
        """
        Parameters
        ----------
        after : {None, str}
            If None, inset the parameters before the first parameter in the
            docstring.
        parameters : Parameter, list[Parameter]
            A Parameter of a list of Parameters.
        """
    def replace_block(self, block_name, block) -> None:
        """
        Parameters
        ----------
        block_name : str
            Name of the block to replace, e.g., 'Summary'.
        block : object
            The replacement block. The structure of the replacement block must
            match how the block is stored by NumpyDocString.
        """
    def extract_parameters(self, parameters, indent: int = 0): ...

def remove_parameters(docstring, parameters):
    """
    Parameters
    ----------
    docstring : str
        The docstring to modify.
    parameters : str, list[str]
        The names of the parameters to remove.

    Returns
    -------
    str
        The modified docstring.
    """
def indent(text, prefix, predicate: Incomplete | None = None):
    '''
    Non-protected indent

    Parameters
    ----------
    text : {None, str}
        If None, function always returns ""
    prefix : str
        Prefix to add to the start of each line
    predicate : callable, optional
        If provided, \'prefix\' will only be added to the lines
        where \'predicate(line)\' is True. If \'predicate\' is not provided,
        it will default to adding \'prefix\' to all non-empty lines that do not
        consist solely of whitespace characters.

    Returns
    -------

    '''
