import abc
import pathlib
from . import _meta
from ._compat import NullFinder, StrPath
from ._meta import PackageMetadata as PackageMetadata, SimplePath
from _typeshed import Incomplete
from collections.abc import Generator
from importlib.abc import MetaPathFinder
from typing import Iterable, List, Mapping, Set

__all__ = ['Distribution', 'DistributionFinder', 'PackageMetadata', 'PackageNotFoundError', 'distribution', 'distributions', 'entry_points', 'files', 'metadata', 'packages_distributions', 'requires', 'version']

class PackageNotFoundError(ModuleNotFoundError):
    """The package was not found."""
    @property
    def name(self) -> str: ...

class Sectioned:
    """
    A simple entry point config parser for performance

    >>> for item in Sectioned.read(Sectioned._sample):
    ...     print(item)
    Pair(name='sec1', value='# comments ignored')
    Pair(name='sec1', value='a = 1')
    Pair(name='sec1', value='b = 2')
    Pair(name='sec2', value='a = 2')

    >>> res = Sectioned.section_pairs(Sectioned._sample)
    >>> item = next(res)
    >>> item.name
    'sec1'
    >>> item.value
    Pair(name='a', value='1')
    >>> item = next(res)
    >>> item.value
    Pair(name='b', value='2')
    >>> item = next(res)
    >>> item.name
    'sec2'
    >>> item.value
    Pair(name='a', value='2')
    >>> list(res)
    []
    """
    @classmethod
    def section_pairs(cls, text): ...
    @staticmethod
    def read(text, filter_: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
    @staticmethod
    def valid(line: str): ...

class DeprecatedTuple:
    """
    Provide subscript item access for backward compatibility.

    >>> recwarn = getfixture('recwarn')
    >>> ep = EntryPoint(name='name', value='value', group='group')
    >>> ep[:]
    ('name', 'value', 'group')
    >>> ep[0]
    'name'
    >>> len(recwarn)
    1
    """
    def __getitem__(self, item): ...

class EntryPoint(DeprecatedTuple):
    """An entry point as defined by Python packaging conventions.

    See `the packaging docs on entry points
    <https://packaging.python.org/specifications/entry-points/>`_
    for more information.

    >>> ep = EntryPoint(
    ...     name=None, group=None, value='package.module:attr [extra1, extra2]')
    >>> ep.module
    'package.module'
    >>> ep.attr
    'attr'
    >>> ep.extras
    ['extra1', 'extra2']
    """
    pattern: Incomplete
    name: str
    value: str
    group: str
    dist: Distribution | None
    def __init__(self, name: str, value: str, group: str) -> None: ...
    def load(self):
        """Load the entry point from its definition. If only a module
        is indicated by the value, return that module. Otherwise,
        return the named object.
        """
    @property
    def module(self) -> str: ...
    @property
    def attr(self) -> str: ...
    @property
    def extras(self) -> List[str]: ...
    def matches(self, **params):
        """
        EntryPoint matches the given parameters.

        >>> ep = EntryPoint(group='foo', name='bar', value='bing:bong [extra1, extra2]')
        >>> ep.matches(group='foo')
        True
        >>> ep.matches(name='bar', value='bing:bong [extra1, extra2]')
        True
        >>> ep.matches(group='foo', name='other')
        False
        >>> ep.matches()
        True
        >>> ep.matches(extras=['extra1', 'extra2'])
        True
        >>> ep.matches(module='bing')
        True
        >>> ep.matches(attr='bong')
        True
        """
    def __lt__(self, other): ...
    def __eq__(self, other): ...
    def __setattr__(self, name, value) -> None: ...
    def __hash__(self) -> int: ...

class EntryPoints(tuple):
    """
    An immutable collection of selectable EntryPoint objects.
    """
    def __getitem__(self, name: str) -> EntryPoint:
        """
        Get the EntryPoint in self matching name.
        """
    def select(self, **params):
        """
        Select entry points from self that match the
        given parameters (typically group and/or name).
        """
    @property
    def names(self) -> Set[str]:
        """
        Return the set of all names of all entry points.
        """
    @property
    def groups(self) -> Set[str]:
        """
        Return the set of all groups of all entry points.
        """

class PackagePath(pathlib.PurePosixPath):
    """A reference to a path in a package"""
    hash: FileHash | None
    size: int
    dist: Distribution
    def read_text(self, encoding: str = 'utf-8') -> str: ...
    def read_binary(self) -> bytes: ...
    def locate(self) -> pathlib.Path:
        """Return a path-like object for this path"""

class FileHash:
    def __init__(self, spec: str) -> None: ...

class DeprecatedNonAbstract:
    def __new__(cls, *args, **kwargs): ...

class Distribution(DeprecatedNonAbstract, metaclass=abc.ABCMeta):
    """A Python distribution package."""
    @abc.abstractmethod
    def read_text(self, filename) -> str | None:
        """Attempt to load metadata file given by the name.

        :param filename: The name of the file in the distribution info.
        :return: The text if found, otherwise None.
        """
    @abc.abstractmethod
    def locate_file(self, path: StrPath) -> pathlib.Path:
        """
        Given a path to a file in this distribution, return a path
        to it.
        """
    @classmethod
    def from_name(cls, name: str) -> Distribution:
        """Return the Distribution for the given package name.

        :param name: The name of the distribution package to search for.
        :return: The Distribution instance (or subclass thereof) for the named
            package, if found.
        :raises PackageNotFoundError: When the named package's distribution
            metadata cannot be found.
        :raises ValueError: When an invalid value is supplied for name.
        """
    @classmethod
    def discover(cls, **kwargs) -> Iterable['Distribution']:
        """Return an iterable of Distribution objects for all packages.

        Pass a ``context`` or pass keyword arguments for constructing
        a context.

        :context: A ``DistributionFinder.Context`` object.
        :return: Iterable of Distribution objects for all packages.
        """
    @staticmethod
    def at(path: StrPath) -> Distribution:
        """Return a Distribution for the indicated metadata path

        :param path: a string or path-like object
        :return: a concrete Distribution instance for the path
        """
    @property
    def metadata(self) -> _meta.PackageMetadata:
        """Return the parsed metadata for this Distribution.

        The returned object will have keys that name the various bits of
        metadata.  See PEP 566 for details.
        """
    @property
    def name(self) -> str:
        """Return the 'Name' metadata for the distribution package."""
    @property
    def version(self) -> str:
        """Return the 'Version' metadata for the distribution package."""
    @property
    def entry_points(self) -> EntryPoints: ...
    @property
    def files(self) -> List[PackagePath] | None:
        """Files in this distribution.

        :return: List of PackagePath for this distribution or None

        Result is `None` if the metadata file that enumerates files
        (i.e. RECORD for dist-info, or installed-files.txt or
        SOURCES.txt for egg-info) is missing.
        Result may be empty if the metadata exists but is empty.
        """
    @property
    def requires(self) -> List[str] | None:
        """Generated requirements specified for this Distribution"""

class DistributionFinder(MetaPathFinder, metaclass=abc.ABCMeta):
    """
    A MetaPathFinder capable of discovering installed distributions.
    """
    class Context:
        """
        Keyword arguments presented by the caller to
        ``distributions()`` or ``Distribution.discover()``
        to narrow the scope of a search for distributions
        in all DistributionFinders.

        Each DistributionFinder may expect any parameters
        and should attempt to honor the canonical
        parameters defined below when appropriate.
        """
        name: Incomplete
        def __init__(self, **kwargs) -> None: ...
        @property
        def path(self) -> List[str]:
            '''
            The sequence of directory path that a distribution finder
            should search.

            Typically refers to Python installed package paths such as
            "site-packages" directories and defaults to ``sys.path``.
            '''
    @abc.abstractmethod
    def find_distributions(self, context=...) -> Iterable[Distribution]:
        """
        Find distributions.

        Return an iterable of all Distribution instances capable of
        loading the metadata for packages matching the ``context``,
        a DistributionFinder.Context instance.
        """

class FastPath:
    """
    Micro-optimized class for searching a path for
    children.

    >>> FastPath('').children()
    ['...']
    """
    def __new__(cls, root): ...
    root: Incomplete
    def __init__(self, root) -> None: ...
    def joinpath(self, child): ...
    def children(self): ...
    def zip_children(self): ...
    def search(self, name): ...
    @property
    def mtime(self): ...
    def lookup(self, mtime): ...

class Lookup:
    infos: Incomplete
    eggs: Incomplete
    def __init__(self, path: FastPath) -> None: ...
    def search(self, prepared): ...

class Prepared:
    """
    A prepared search for metadata on a possibly-named package.
    """
    normalized: Incomplete
    legacy_normalized: Incomplete
    name: Incomplete
    def __init__(self, name) -> None: ...
    @staticmethod
    def normalize(name):
        """
        PEP 503 normalization plus dashes as underscores.
        """
    @staticmethod
    def legacy_normalize(name):
        """
        Normalize the package name as found in the convention in
        older packaging tools versions and specs.
        """
    def __bool__(self) -> bool: ...

class MetadataPathFinder(NullFinder, DistributionFinder):
    """A degenerate finder for distribution packages on the file system.

    This finder supplies only a find_distributions() method for versions
    of Python that do not have a PathFinder find_distributions().
    """
    def find_distributions(self, context=...) -> Iterable['PathDistribution']:
        """
        Find distributions.

        Return an iterable of all Distribution instances capable of
        loading the metadata for packages matching ``context.name``
        (or all names if ``None`` indicated) along the paths in the list
        of directories ``context.path``.
        """
    def invalidate_caches(cls) -> None: ...

class PathDistribution(Distribution):
    def __init__(self, path: SimplePath) -> None:
        """Construct a distribution.

        :param path: SimplePath indicating the metadata directory.
        """
    def read_text(self, filename: StrPath) -> str | None: ...
    def locate_file(self, path: StrPath) -> pathlib.Path: ...

def distribution(distribution_name: str) -> Distribution:
    """Get the ``Distribution`` instance for the named package.

    :param distribution_name: The name of the distribution package as a string.
    :return: A ``Distribution`` instance (or subclass thereof).
    """
def distributions(**kwargs) -> Iterable[Distribution]:
    """Get all ``Distribution`` instances in the current environment.

    :return: An iterable of ``Distribution`` instances.
    """
def metadata(distribution_name: str) -> _meta.PackageMetadata:
    """Get the metadata for the named package.

    :param distribution_name: The name of the distribution package to query.
    :return: A PackageMetadata containing the parsed metadata.
    """
def version(distribution_name: str) -> str:
    '''Get the version string for the named package.

    :param distribution_name: The name of the distribution package to query.
    :return: The version string for the package as defined in the package\'s
        "Version" metadata key.
    '''
def entry_points(**params) -> EntryPoints:
    """Return EntryPoint objects for all installed packages.

    Pass selection parameters (group or name) to filter the
    result to entry points matching those properties (see
    EntryPoints.select()).

    :return: EntryPoints for all installed packages.
    """
def files(distribution_name: str) -> List[PackagePath] | None:
    """Return a list of files for the named package.

    :param distribution_name: The name of the distribution package to query.
    :return: List of files composing the distribution.
    """
def requires(distribution_name: str) -> List[str] | None:
    """
    Return a list of requirements for the named package.

    :return: An iterable of requirements, suitable for
        packaging.requirement.Requirement.
    """
def packages_distributions() -> Mapping[str, List[str]]:
    """
    Return a mapping of top-level packages to their
    distributions.

    >>> import collections.abc
    >>> pkgs = packages_distributions()
    >>> all(isinstance(dist, collections.abc.Sequence) for dist in pkgs.values())
    True
    """
