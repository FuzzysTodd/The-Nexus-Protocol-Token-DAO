from ..warnings import SetuptoolsWarning as SetuptoolsWarning
from _typeshed import Incomplete
from distutils.dist import DistributionMetadata as DistributionMetadata
from importlib.machinery import ModuleSpec
from setuptools.discovery import ConfigDiscovery as ConfigDiscovery
from setuptools.dist import Distribution as Distribution
from typing import Callable, Dict, Iterable, Iterator, List, Mapping, Tuple

chain_iter: Incomplete

class StaticModule:
    """Proxy to a module object that avoids executing arbitrary code."""
    def __init__(self, name: str, spec: ModuleSpec) -> None: ...
    def __getattr__(self, attr):
        '''Attempt to load an attribute "statically", via :func:`ast.literal_eval`.'''

def glob_relative(patterns: Iterable[str], root_dir: _Path | None = None) -> List[str]:
    """Expand the list of glob patterns, but preserving relative paths.

    :param list[str] patterns: List of glob patterns
    :param str root_dir: Path to which globs should be relative
                         (current directory by default)
    :rtype: list
    """
def read_files(filepaths: str | bytes | Iterable[_Path], root_dir: Incomplete | None = None) -> str:
    """Return the content of the files concatenated using ``
`` as str

    This function is sandboxed and won't reach anything outside ``root_dir``

    (By default ``root_dir`` is the current directory).
    """
def read_attr(attr_desc: str, package_dir: Mapping[str, str] | None = None, root_dir: _Path | None = None):
    '''Reads the value of an attribute from a module.

    This function will try to read the attributed statically first
    (via :func:`ast.literal_eval`), and only evaluate the module if it fails.

    Examples:
        read_attr("package.attr")
        read_attr("package.module.attr")

    :param str attr_desc: Dot-separated string describing how to reach the
        attribute (see examples above)
    :param dict[str, str] package_dir: Mapping of package names to their
        location in disk (represented by paths relative to ``root_dir``).
    :param str root_dir: Path to directory containing all the packages in
        ``package_dir`` (current directory by default).
    :rtype: str
    '''
def resolve_class(qualified_class_name: str, package_dir: Mapping[str, str] | None = None, root_dir: _Path | None = None) -> Callable:
    """Given a qualified class name, return the associated class object"""
def cmdclass(values: Dict[str, str], package_dir: Mapping[str, str] | None = None, root_dir: _Path | None = None) -> Dict[str, Callable]:
    """Given a dictionary mapping command names to strings for qualified class
    names, apply :func:`resolve_class` to the dict values.
    """
def find_packages(*, namespaces: bool = True, fill_package_dir: Dict[str, str] | None = None, root_dir: _Path | None = None, **kwargs) -> List[str]:
    """Works similarly to :func:`setuptools.find_packages`, but with all
    arguments given as keyword arguments. Moreover, ``where`` can be given
    as a list (the results will be simply concatenated).

    When the additional keyword argument ``namespaces`` is ``True``, it will
    behave like :func:`setuptools.find_namespace_packages`` (i.e. include
    implicit namespaces as per :pep:`420`).

    The ``where`` argument will be considered relative to ``root_dir`` (or the current
    working directory when ``root_dir`` is not given).

    If the ``fill_package_dir`` argument is passed, this function will consider it as a
    similar data structure to the ``package_dir`` configuration parameter add fill-in
    any missing package location.

    :rtype: list
    """
def version(value: Callable | Iterable[str | int] | str) -> str:
    """When getting the version directly from an attribute,
    it should be normalised to string.
    """
def canonic_package_data(package_data: dict) -> dict: ...
def canonic_data_files(data_files: list | dict, root_dir: _Path | None = None) -> List[Tuple[str, List[str]]]:
    """For compatibility with ``setup.py``, ``data_files`` should be a list
    of pairs instead of a dict.

    This function also expands glob patterns.
    """
def entry_points(text: str, text_source: str = 'entry-points') -> Dict[str, dict]:
    """Given the contents of entry-points file,
    process it into a 2-level dictionary (``dict[str, dict[str, str]]``).
    The first level keys are entry-point groups, the second level keys are
    entry-point names, and the second level values are references to objects
    (that correspond to the entry-point value).
    """

class EnsurePackagesDiscovered:
    """Some expand functions require all the packages to already be discovered before
    they run, e.g. :func:`read_attr`, :func:`resolve_class`, :func:`cmdclass`.

    Therefore in some cases we will need to run autodiscovery during the evaluation of
    the configuration. However, it is better to postpone calling package discovery as
    much as possible, because some parameters can influence it (e.g. ``package_dir``),
    and those might not have been processed yet.
    """
    def __init__(self, distribution: Distribution) -> None: ...
    def __call__(self) -> None:
        """Trigger the automatic package discovery, if it is still necessary."""
    def __enter__(self): ...
    def __exit__(self, _exc_type: type[BaseException] | None, _exc_value: BaseException | None, _traceback: types.TracebackType | None) -> None: ...
    @property
    def package_dir(self) -> Mapping[str, str]:
        """Proxy to ``package_dir`` that may trigger auto-discovery when used."""

class LazyMappingProxy(Mapping[_K, _V]):
    '''Mapping proxy that delays resolving the target object, until really needed.

    >>> def obtain_mapping():
    ...     print("Running expensive function!")
    ...     return {"key": "value", "other key": "other value"}
    >>> mapping = LazyMappingProxy(obtain_mapping)
    >>> mapping["key"]
    Running expensive function!
    \'value\'
    >>> mapping["other key"]
    \'other value\'
    '''
    def __init__(self, obtain_mapping_value: Callable[[], Mapping[_K, _V]]) -> None: ...
    def __getitem__(self, key: _K) -> _V: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_K]: ...
