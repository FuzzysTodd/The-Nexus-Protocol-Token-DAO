from _typeshed import Incomplete
from setuptools import Distribution as Distribution
from typing import Dict, Iterable, Iterator, List, Mapping, Tuple

StrIter = Iterator[str]
chain_iter: Incomplete

class _Filter:
    """
    Given a list of patterns, create a callable that will be true only if
    the input matches at least one of the patterns.
    """
    def __init__(self, *patterns: str) -> None: ...
    def __call__(self, item: str) -> bool: ...
    def __contains__(self, item: str) -> bool: ...

class _Finder:
    """Base class that exposes functionality for module/package finders"""
    ALWAYS_EXCLUDE: Tuple[str, ...]
    DEFAULT_EXCLUDE: Tuple[str, ...]
    @classmethod
    def find(cls, where: _Path = '.', exclude: Iterable[str] = (), include: Iterable[str] = ('*',)) -> List[str]:
        '''Return a list of all Python items (packages or modules, depending on
        the finder implementation) found within directory \'where\'.

        \'where\' is the root directory which will be searched.
        It should be supplied as a "cross-platform" (i.e. URL-style) path;
        it will be converted to the appropriate local path syntax.

        \'exclude\' is a sequence of names to exclude; \'*\' can be used
        as a wildcard in the names.
        When finding packages, \'foo.*\' will exclude all subpackages of \'foo\'
        (but not \'foo\' itself).

        \'include\' is a sequence of names to include.
        If it\'s specified, only the named items will be included.
        If it\'s not specified, all found items will be included.
        \'include\' can contain shell style wildcard patterns just like
        \'exclude\'.
        '''

class PackageFinder(_Finder):
    """
    Generate a list of all Python packages found within a directory
    """
    ALWAYS_EXCLUDE: Incomplete

class PEP420PackageFinder(PackageFinder): ...
class ModuleFinder(_Finder):
    """Find isolated Python modules.
    This function will **not** recurse subdirectories.
    """

class FlatLayoutPackageFinder(PEP420PackageFinder):
    DEFAULT_EXCLUDE: Incomplete

class FlatLayoutModuleFinder(ModuleFinder):
    DEFAULT_EXCLUDE: Incomplete

class ConfigDiscovery:
    """Fill-in metadata and options that can be automatically derived
    (from other metadata/options, the file system or conventions)
    """
    dist: Incomplete
    def __init__(self, distribution: Distribution) -> None: ...
    def __call__(self, force: bool = False, name: bool = True, ignore_ext_modules: bool = False) -> None:
        """Automatically discover missing configuration fields
        and modifies the given ``distribution`` object in-place.

        Note that by default this will only have an effect the first time the
        ``ConfigDiscovery`` object is called.

        To repeatedly invoke automatic discovery (e.g. when the project
        directory changes), please use ``force=True`` (or create a new
        ``ConfigDiscovery`` instance).
        """
    def analyse_name(self) -> None:
        """The packages/modules are the essential contribution of the author.
        Therefore the name of the distribution can be derived from them.
        """

def remove_nested_packages(packages: List[str]) -> List[str]:
    '''Remove nested packages from a list of packages.

    >>> remove_nested_packages(["a", "a.b1", "a.b2", "a.b1.c1"])
    [\'a\']
    >>> remove_nested_packages(["a", "b", "c.d", "c.d.e.f", "g.h", "a.a1"])
    [\'a\', \'b\', \'c.d\', \'g.h\']
    '''
def remove_stubs(packages: List[str]) -> List[str]:
    '''Remove type stubs (:pep:`561`) from a list of packages.

    >>> remove_stubs(["a", "a.b", "a-stubs", "a-stubs.b.c", "b", "c-stubs"])
    [\'a\', \'a.b\', \'b\']
    '''
def find_parent_package(packages: List[str], package_dir: Mapping[str, str], root_dir: _Path) -> str | None:
    """Find the parent package that is not a namespace."""
def find_package_path(name: str, package_dir: Mapping[str, str], root_dir: _Path) -> str:
    '''Given a package name, return the path where it should be found on
    disk, considering the ``package_dir`` option.

    >>> path = find_package_path("my.pkg", {"": "root/is/nested"}, ".")
    >>> path.replace(os.sep, "/")
    \'./root/is/nested/my/pkg\'

    >>> path = find_package_path("my.pkg", {"my": "root/is/nested"}, ".")
    >>> path.replace(os.sep, "/")
    \'./root/is/nested/pkg\'

    >>> path = find_package_path("my.pkg", {"my.pkg": "root/is/nested"}, ".")
    >>> path.replace(os.sep, "/")
    \'./root/is/nested\'

    >>> path = find_package_path("other.pkg", {"my.pkg": "root/is/nested"}, ".")
    >>> path.replace(os.sep, "/")
    \'./other/pkg\'
    '''
def construct_package_dir(packages: List[str], package_path: _Path) -> Dict[str, str]: ...
