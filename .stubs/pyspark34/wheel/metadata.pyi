from .vendored.packaging.requirements import Requirement as Requirement
from _typeshed import Incomplete
from collections.abc import Generator
from email.message import Message
from typing import Iterator

def yield_lines(iterable):
    """
    Yield valid lines of a string or iterable.
    >>> list(yield_lines(''))
    []
    >>> list(yield_lines(['foo', 'bar']))
    ['foo', 'bar']
    >>> list(yield_lines('foo\\nbar'))
    ['foo', 'bar']
    >>> list(yield_lines('\\nfoo\\n#bar\\nbaz #comment'))
    ['foo', 'baz #comment']
    >>> list(yield_lines(['foo\\nbar', 'baz', 'bing\\n\\n\\n']))
    ['foo', 'bar', 'baz', 'bing']
    """
def _(text): ...
def split_sections(s) -> Generator[Incomplete, None, None]:
    '''Split a string or iterable thereof into (section, content) pairs
    Each ``section`` is a stripped version of the section header ("[section]")
    and each ``content`` is a list of stripped lines excluding blank lines and
    comment-only lines.  If there are any such lines before the first section
    header, they\'re returned in a first ``section`` of ``None``.
    '''
def safe_extra(extra):
    """Convert an arbitrary string to a standard 'extra' name
    Any runs of non-alphanumeric characters are replaced with a single '_',
    and the result is always lowercased.
    """
def safe_name(name):
    """Convert an arbitrary string to a standard distribution name
    Any runs of non-alphanumeric/. characters are replaced with a single '-'.
    """
def requires_to_requires_dist(requirement: Requirement) -> str:
    """Return the version specifier for a requirement in PEP 345/566 fashion."""
def convert_requirements(requirements: list[str]) -> Iterator[str]:
    """Yield Requires-Dist: strings for parsed requirements strings."""
def generate_requirements(extras_require: dict[str, list[str]]) -> Iterator[tuple[str, str]]:
    """
    Convert requirements from a setup()-style dictionary to
    ('Requires-Dist', 'requirement') and ('Provides-Extra', 'extra') tuples.

    extras_require is a dictionary of {extra: [requirements]} as passed to setup(),
    using the empty extra {'': [requirements]} to hold install_requires.
    """
def pkginfo_to_metadata(egg_info_path: str, pkginfo_path: str) -> Message:
    """
    Convert .egg-info directory with PKG-INFO to the Metadata 2.1 format
    """
