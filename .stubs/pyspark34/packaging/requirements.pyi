from ._tokenizer import ParserSyntaxError as ParserSyntaxError
from .markers import Marker as Marker
from .specifiers import SpecifierSet as SpecifierSet
from .utils import canonicalize_name as canonicalize_name
from _typeshed import Incomplete
from typing import Any

class InvalidRequirement(ValueError):
    """
    An invalid requirement was found, users should refer to PEP 508.
    """

class Requirement:
    """Parse a requirement.

    Parse a given requirement string into its parts, such as name, specifier,
    URL, and extras. Raises InvalidRequirement on a badly-formed requirement
    string.
    """
    name: Incomplete
    url: Incomplete
    extras: Incomplete
    specifier: Incomplete
    marker: Incomplete
    def __init__(self, requirement_string: str) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
