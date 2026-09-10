from .tags import Tag as Tag, parse_tag as parse_tag
from .version import InvalidVersion as InvalidVersion, Version as Version
from _typeshed import Incomplete
from typing import FrozenSet, Tuple

BuildTag = Tuple[()] | Tuple[int, str]
NormalizedName: Incomplete

class InvalidName(ValueError):
    """
    An invalid distribution name; users should refer to the packaging user guide.
    """
class InvalidWheelFilename(ValueError):
    """
    An invalid wheel filename was found, users should refer to PEP 427.
    """
class InvalidSdistFilename(ValueError):
    """
    An invalid sdist filename was found, users should refer to the packaging user guide.
    """

def canonicalize_name(name: str, *, validate: bool = False) -> NormalizedName: ...
def is_normalized_name(name: str) -> bool: ...
def canonicalize_version(version: Version | str, *, strip_trailing_zero: bool = True) -> str:
    """
    This is very similar to Version.__str__, but has one subtle difference
    with the way it handles the release segment.
    """
def parse_wheel_filename(filename: str) -> Tuple[NormalizedName, Version, BuildTag, FrozenSet[Tag]]: ...
def parse_sdist_filename(filename: str) -> Tuple[NormalizedName, Version]: ...
