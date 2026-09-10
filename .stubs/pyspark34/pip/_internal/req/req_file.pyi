import optparse
from _typeshed import Incomplete
from optparse import Values
from pip._internal.index.package_finder import PackageFinder
from pip._internal.network.session import PipSession
from typing import Any, Callable, Dict, Generator, Iterable, Tuple

__all__ = ['parse_requirements']

ReqFileLines = Iterable[Tuple[int, str]]
LineParser = Callable[[str], Tuple[str, Values]]

class ParsedRequirement:
    requirement: Incomplete
    is_editable: Incomplete
    comes_from: Incomplete
    options: Incomplete
    constraint: Incomplete
    line_source: Incomplete
    def __init__(self, requirement: str, is_editable: bool, comes_from: str, constraint: bool, options: Dict[str, Any] | None = None, line_source: str | None = None) -> None: ...

class ParsedLine:
    filename: Incomplete
    lineno: Incomplete
    opts: Incomplete
    constraint: Incomplete
    is_requirement: bool
    is_editable: bool
    requirement: Incomplete
    def __init__(self, filename: str, lineno: int, args: str, opts: Values, constraint: bool) -> None: ...

def parse_requirements(filename: str, session: PipSession, finder: PackageFinder | None = None, options: optparse.Values | None = None, constraint: bool = False) -> Generator[ParsedRequirement, None, None]:
    """Parse a requirements file and yield ParsedRequirement instances.

    :param filename:    Path or url of requirements file.
    :param session:     PipSession instance.
    :param finder:      Instance of pip.index.PackageFinder.
    :param options:     cli options.
    :param constraint:  If true, parsing a constraint file rather than
        requirements file.
    """

class RequirementsFileParser:
    def __init__(self, session: PipSession, line_parser: LineParser) -> None: ...
    def parse(self, filename: str, constraint: bool) -> Generator[ParsedLine, None, None]:
        """Parse a given file, yielding parsed lines."""

class OptionParsingError(Exception):
    msg: Incomplete
    def __init__(self, msg: str) -> None: ...
