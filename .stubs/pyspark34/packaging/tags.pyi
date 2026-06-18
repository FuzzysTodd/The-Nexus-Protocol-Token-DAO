from _typeshed import Incomplete
from typing import Dict, FrozenSet, Iterable, Iterator, Sequence, Tuple

logger: Incomplete
PythonVersion = Sequence[int]
MacVersion = Tuple[int, int]
INTERPRETER_SHORT_NAMES: Dict[str, str]

class Tag:
    """
    A representation of the tag triple for a wheel.

    Instances are considered immutable and thus are hashable. Equality checking
    is also supported.
    """
    def __init__(self, interpreter: str, abi: str, platform: str) -> None: ...
    @property
    def interpreter(self) -> str: ...
    @property
    def abi(self) -> str: ...
    @property
    def platform(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

def parse_tag(tag: str) -> FrozenSet[Tag]:
    """
    Parses the provided tag (e.g. `py3-none-any`) into a frozenset of Tag instances.

    Returning a set is required due to the possibility that the tag is a
    compressed tag set.
    """
def cpython_tags(python_version: PythonVersion | None = None, abis: Iterable[str] | None = None, platforms: Iterable[str] | None = None, *, warn: bool = False) -> Iterator[Tag]:
    """
    Yields the tags for a CPython interpreter.

    The tags consist of:
    - cp<python_version>-<abi>-<platform>
    - cp<python_version>-abi3-<platform>
    - cp<python_version>-none-<platform>
    - cp<less than python_version>-abi3-<platform>  # Older Python versions down to 3.2.

    If python_version only specifies a major version then user-provided ABIs and
    the 'none' ABItag will be used.

    If 'abi3' or 'none' are specified in 'abis' then they will be yielded at
    their normal position and not at the beginning.
    """
def generic_tags(interpreter: str | None = None, abis: Iterable[str] | None = None, platforms: Iterable[str] | None = None, *, warn: bool = False) -> Iterator[Tag]:
    '''
    Yields the tags for a generic interpreter.

    The tags consist of:
    - <interpreter>-<abi>-<platform>

    The "none" ABI will be added if it was not explicitly provided.
    '''
def compatible_tags(python_version: PythonVersion | None = None, interpreter: str | None = None, platforms: Iterable[str] | None = None) -> Iterator[Tag]:
    """
    Yields the sequence of tags that are compatible with a specific version of Python.

    The tags consist of:
    - py*-none-<platform>
    - <interpreter>-none-any  # ... if `interpreter` is provided.
    - py*-none-any
    """
def mac_platforms(version: MacVersion | None = None, arch: str | None = None) -> Iterator[str]:
    """
    Yields the platform tags for a macOS system.

    The `version` parameter is a two-item tuple specifying the macOS version to
    generate platform tags for. The `arch` parameter is the CPU architecture to
    generate platform tags for. Both parameters default to the appropriate value
    for the current system.
    """
def platform_tags() -> Iterator[str]:
    """
    Provides the platform tags for this installation.
    """
def interpreter_name() -> str:
    """
    Returns the name of the running interpreter.

    Some implementations have a reserved, two-letter abbreviation which will
    be returned when appropriate.
    """
def interpreter_version(*, warn: bool = False) -> str:
    """
    Returns the version of the running interpreter.
    """
def sys_tags(*, warn: bool = False) -> Iterator[Tag]:
    """
    Returns the sequence of tag triples for the running interpreter.

    The order of the sequence corresponds to priority order for the
    interpreter, from most to least important.
    """
