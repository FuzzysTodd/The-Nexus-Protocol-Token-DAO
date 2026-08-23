from setuptools.extern.packaging.requirements import Requirement as Requirement
from typing import Callable, Iterator, overload

parse_req: Callable[[str], Requirement]

def parse_strings(strs: _StrOrIter) -> Iterator[str]:
    """
    Yield requirement strings for each specification in `strs`.

    `strs` must be a string, or a (possibly-nested) iterable thereof.
    """
@overload
def parse(strs: _StrOrIter) -> Iterator[Requirement]: ...
@overload
def parse(strs: _StrOrIter, parser: Callable[[str], _T]) -> Iterator[_T]: ...
