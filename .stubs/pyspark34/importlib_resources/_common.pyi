import types
from ._compat import wrap_spec as wrap_spec
from .abc import ResourceReader as ResourceReader, Traversable as Traversable

Package = types.ModuleType | str
Anchor = Package

def package_to_anchor(func):
    """
    Replace 'package' parameter as 'anchor' and warn about the change.

    Other errors should fall through.

    >>> files('a', 'b')
    Traceback (most recent call last):
    TypeError: files() takes from 0 to 1 positional arguments but 2 were given
    """
def files(anchor: Anchor | None = None) -> Traversable:
    """
    Get a Traversable resource for an anchor.
    """
def get_resource_reader(package: types.ModuleType) -> ResourceReader | None:
    """
    Return the package's loader if it's a ResourceReader.
    """
def resolve(cand: Anchor | None) -> types.ModuleType: ...
def _(cand: str) -> types.ModuleType: ...
def from_package(package: types.ModuleType):
    """
    Return a Traversable object for the given package.

    """
def as_file(path):
    """
    Given a Traversable object, return that object as a
    path on the local file system in a context manager.
    """
