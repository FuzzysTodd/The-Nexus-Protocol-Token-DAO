from _typeshed import Incomplete
from collections.abc import Generator
from pkg_resources.extern import packaging
from pkg_resources.extern.jaraco.text import yield_lines as yield_lines
from pkgutil import get_importer as get_importer
from typing import NamedTuple

__all__ = ['require', 'run_script', 'get_provider', 'get_distribution', 'load_entry_point', 'get_entry_map', 'get_entry_info', 'iter_entry_points', 'resource_string', 'resource_stream', 'resource_filename', 'resource_listdir', 'resource_exists', 'resource_isdir', 'declare_namespace', 'working_set', 'add_activation_listener', 'find_distributions', 'set_extraction_path', 'cleanup_resources', 'get_default_cache', 'Environment', 'WorkingSet', 'ResourceManager', 'Distribution', 'Requirement', 'EntryPoint', 'ResolutionError', 'VersionConflict', 'DistributionNotFound', 'UnknownExtra', 'ExtractionError', 'PEP440Warning', 'parse_requirements', 'parse_version', 'safe_name', 'safe_version', 'get_platform', 'compatible_platforms', 'yield_lines', 'split_sections', 'safe_extra', 'to_filename', 'invalid_marker', 'evaluate_marker', 'ensure_directory', 'normalize_path', 'EGG_DIST', 'BINARY_DIST', 'SOURCE_DIST', 'CHECKOUT_DIST', 'DEVELOP_DIST', 'IMetadataProvider', 'IResourceProvider', 'FileMetadata', 'PathMetadata', 'EggMetadata', 'EmptyProvider', 'empty_provider', 'NullProvider', 'EggProvider', 'DefaultProvider', 'ZipProvider', 'register_finder', 'register_namespace_handler', 'register_loader_type', 'fixup_namespace_packages', 'get_importer', 'PkgResourcesDeprecationWarning', 'run_main', 'AvailableDistributions']

FileExistsError = OSError
require: Incomplete
working_set: Incomplete
add_activation_listener: Incomplete
cleanup_resources: Incomplete
resource_stream: Incomplete
set_extraction_path: Incomplete
resource_isdir: Incomplete
resource_string: Incomplete
iter_entry_points: Incomplete
resource_listdir: Incomplete
resource_filename: Incomplete
resource_exists: Incomplete

class PEP440Warning(RuntimeWarning):
    """
    Used when there is an issue with a version or specifier not complying with
    PEP 440.
    """

parse_version: Incomplete

class ResolutionError(Exception):
    """Abstract base for dependency resolution errors"""

class VersionConflict(ResolutionError):
    """
    An already-installed version conflicts with the requested version.

    Should be initialized with the installed Distribution and the requested
    Requirement.
    """
    @property
    def dist(self): ...
    @property
    def req(self): ...
    def report(self): ...
    def with_context(self, required_by):
        """
        If required_by is non-empty, return a version of self that is a
        ContextualVersionConflict.
        """

class ContextualVersionConflict(VersionConflict):
    """
    A VersionConflict that accepts a third parameter, the set of the
    requirements that required the installed Distribution.
    """
    @property
    def required_by(self): ...

class DistributionNotFound(ResolutionError):
    """A requested distribution was not found"""
    @property
    def req(self): ...
    @property
    def requirers(self): ...
    @property
    def requirers_str(self): ...
    def report(self): ...

class UnknownExtra(ResolutionError):
    '''Distribution doesn\'t have an "extra feature" of the given name'''

EGG_DIST: int
BINARY_DIST: int
SOURCE_DIST: int
CHECKOUT_DIST: int
DEVELOP_DIST: int

def register_loader_type(loader_type, provider_factory) -> None:
    """Register `provider_factory` to make providers for `loader_type`

    `loader_type` is the type or class of a PEP 302 ``module.__loader__``,
    and `provider_factory` is a function that, passed a *module* object,
    returns an ``IResourceProvider`` for that module.
    """
def get_provider(moduleOrReq):
    """Return an IResourceProvider for the named module or requirement"""
get_platform = get_build_platform

def compatible_platforms(provided, required):
    """Can code for the `provided` platform run on the `required` platform?

    Returns true if either platform is ``None``, or the platforms are equal.

    XXX Needs compatibility checks for Linux and other unixy OSes.
    """
def run_script(dist_spec, script_name) -> None:
    """Locate distribution `dist_spec` and run its `script_name` script"""
run_main = run_script

def get_distribution(dist):
    """Return a current distribution object for a Requirement or string"""
def load_entry_point(dist, group, name):
    """Return `name` entry point of `group` for `dist` or raise ImportError"""
def get_entry_map(dist, group: Incomplete | None = None):
    """Return the entry point map for `group`, or the full entry map"""
def get_entry_info(dist, group, name):
    """Return the EntryPoint object for `group`+`name`, or ``None``"""

class IMetadataProvider:
    def has_metadata(name) -> None:
        """Does the package's distribution contain the named metadata?"""
    def get_metadata(name) -> None:
        """The named metadata resource as a string"""
    def get_metadata_lines(name) -> None:
        """Yield named metadata resource as list of non-blank non-comment lines

        Leading and trailing whitespace is stripped from each line, and lines
        with ``#`` as the first non-blank character are omitted."""
    def metadata_isdir(name) -> None:
        """Is the named metadata a directory?  (like ``os.path.isdir()``)"""
    def metadata_listdir(name) -> None:
        """List of metadata names in the directory (like ``os.listdir()``)"""
    def run_script(script_name, namespace) -> None:
        """Execute the named script in the supplied namespace dictionary"""

class IResourceProvider(IMetadataProvider):
    """An object that provides access to package resources"""
    def get_resource_filename(manager, resource_name) -> None:
        """Return a true filesystem path for `resource_name`

        `manager` must be an ``IResourceManager``"""
    def get_resource_stream(manager, resource_name) -> None:
        """Return a readable file-like object for `resource_name`

        `manager` must be an ``IResourceManager``"""
    def get_resource_string(manager, resource_name) -> None:
        """Return a string containing the contents of `resource_name`

        `manager` must be an ``IResourceManager``"""
    def has_resource(resource_name) -> None:
        """Does the package contain the named resource?"""
    def resource_isdir(resource_name) -> None:
        """Is the named resource a directory?  (like ``os.path.isdir()``)"""
    def resource_listdir(resource_name) -> None:
        """List of resource names in the directory (like ``os.listdir()``)"""

class WorkingSet:
    """A collection of active distributions on sys.path (or a similar list)"""
    entries: Incomplete
    entry_keys: Incomplete
    by_key: Incomplete
    normalized_to_canonical_keys: Incomplete
    callbacks: Incomplete
    def __init__(self, entries: Incomplete | None = None) -> None:
        """Create working set from list of path entries (default=sys.path)"""
    def add_entry(self, entry) -> None:
        """Add a path item to ``.entries``, finding any distributions on it

        ``find_distributions(entry, True)`` is used to find distributions
        corresponding to the path entry, and they are added.  `entry` is
        always appended to ``.entries``, even if it is already present.
        (This is because ``sys.path`` can contain the same value more than
        once, and the ``.entries`` of the ``sys.path`` WorkingSet should always
        equal ``sys.path``.)
        """
    def __contains__(self, dist) -> bool:
        """True if `dist` is the active distribution for its project"""
    def find(self, req):
        """Find a distribution matching requirement `req`

        If there is an active distribution for the requested project, this
        returns it as long as it meets the version requirement specified by
        `req`.  But, if there is an active distribution for the project and it
        does *not* meet the `req` requirement, ``VersionConflict`` is raised.
        If there is no active distribution for the requested project, ``None``
        is returned.
        """
    def iter_entry_points(self, group, name: Incomplete | None = None):
        """Yield entry point objects from `group` matching `name`

        If `name` is None, yields all entry points in `group` from all
        distributions in the working set, otherwise only ones matching
        both `group` and `name` are yielded (in distribution order).
        """
    def run_script(self, requires, script_name) -> None:
        """Locate distribution for `requires` and run `script_name` script"""
    def __iter__(self):
        """Yield distributions for non-duplicate projects in the working set

        The yield order is the order in which the items' path entries were
        added to the working set.
        """
    def add(self, dist, entry: Incomplete | None = None, insert: bool = True, replace: bool = False) -> None:
        """Add `dist` to working set, associated with `entry`

        If `entry` is unspecified, it defaults to the ``.location`` of `dist`.
        On exit from this routine, `entry` is added to the end of the working
        set's ``.entries`` (if it wasn't already present).

        `dist` is only added to the working set if it's for a project that
        doesn't already have a distribution in the set, unless `replace=True`.
        If it's added, any callbacks registered with the ``subscribe()`` method
        will be called.
        """
    def resolve(self, requirements, env: Incomplete | None = None, installer: Incomplete | None = None, replace_conflicting: bool = False, extras: Incomplete | None = None):
        '''List all distributions needed to (recursively) meet `requirements`

        `requirements` must be a sequence of ``Requirement`` objects.  `env`,
        if supplied, should be an ``Environment`` instance.  If
        not supplied, it defaults to all distributions available within any
        entry or distribution in the working set.  `installer`, if supplied,
        will be invoked with each requirement that cannot be met by an
        already-installed distribution; it should return a ``Distribution`` or
        ``None``.

        Unless `replace_conflicting=True`, raises a VersionConflict exception
        if
        any requirements are found on the path that have the correct name but
        the wrong version.  Otherwise, if an `installer` is supplied it will be
        invoked to obtain the correct version of the requirement and activate
        it.

        `extras` is a list of the extras to be used with these requirements.
        This is important because extra requirements may look like `my_req;
        extra = "my_extra"`, which would otherwise be interpreted as a purely
        optional requirement.  Instead, we want to be able to assert that these
        requirements are truly required.
        '''
    def find_plugins(self, plugin_env, full_env: Incomplete | None = None, installer: Incomplete | None = None, fallback: bool = True):
        '''Find all activatable distributions in `plugin_env`

        Example usage::

            distributions, errors = working_set.find_plugins(
                Environment(plugin_dirlist)
            )
            # add plugins+libs to sys.path
            map(working_set.add, distributions)
            # display errors
            print(\'Could not load\', errors)

        The `plugin_env` should be an ``Environment`` instance that contains
        only distributions that are in the project\'s "plugin directory" or
        directories. The `full_env`, if supplied, should be an ``Environment``
        contains all currently-available distributions.  If `full_env` is not
        supplied, one is created automatically from the ``WorkingSet`` this
        method is called on, which will typically mean that every directory on
        ``sys.path`` will be scanned for distributions.

        `installer` is a standard installer callback as used by the
        ``resolve()`` method. The `fallback` flag indicates whether we should
        attempt to resolve older versions of a plugin if the newest version
        cannot be resolved.

        This method returns a 2-tuple: (`distributions`, `error_info`), where
        `distributions` is a list of the distributions found in `plugin_env`
        that were loadable, along with any other distributions that are needed
        to resolve their dependencies.  `error_info` is a dictionary mapping
        unloadable plugin distributions to an exception instance describing the
        error that occurred. Usually this will be a ``DistributionNotFound`` or
        ``VersionConflict`` instance.
        '''
    def require(self, *requirements):
        """Ensure that distributions matching `requirements` are activated

        `requirements` must be a string or a (possibly-nested) sequence
        thereof, specifying the distributions and versions required.  The
        return value is a sequence of the distributions that needed to be
        activated to fulfill the requirements; all relevant distributions are
        included, even if they were already activated in this working set.
        """
    def subscribe(self, callback, existing: bool = True) -> None:
        """Invoke `callback` for all distributions

        If `existing=True` (default),
        call on all existing ones, as well.
        """

class _ReqExtras(dict):
    """
    Map each requirement to the extras that demanded it.
    """
    def markers_pass(self, req, extras: Incomplete | None = None):
        """
        Evaluate markers for req against each extra that
        demanded it.

        Return False if the req has a marker and fails
        evaluation. Otherwise, return True.
        """

class Environment:
    """Searchable snapshot of distributions on a search path"""
    platform: Incomplete
    python: Incomplete
    def __init__(self, search_path: Incomplete | None = None, platform=..., python=...) -> None:
        """Snapshot distributions available on a search path

        Any distributions found on `search_path` are added to the environment.
        `search_path` should be a sequence of ``sys.path`` items.  If not
        supplied, ``sys.path`` is used.

        `platform` is an optional string specifying the name of the platform
        that platform-specific distributions must be compatible with.  If
        unspecified, it defaults to the current platform.  `python` is an
        optional string naming the desired version of Python (e.g. ``'3.6'``);
        it defaults to the current version.

        You may explicitly set `platform` (and/or `python`) to ``None`` if you
        wish to map *all* distributions, not just those compatible with the
        running platform or Python version.
        """
    def can_add(self, dist):
        """Is distribution `dist` acceptable for this environment?

        The distribution must match the platform and python version
        requirements specified when this environment was created, or False
        is returned.
        """
    def remove(self, dist) -> None:
        """Remove `dist` from the environment"""
    def scan(self, search_path: Incomplete | None = None) -> None:
        """Scan `search_path` for distributions usable in this environment

        Any distributions found are added to the environment.
        `search_path` should be a sequence of ``sys.path`` items.  If not
        supplied, ``sys.path`` is used.  Only distributions conforming to
        the platform/python version defined at initialization are added.
        """
    def __getitem__(self, project_name):
        """Return a newest-to-oldest list of distributions for `project_name`

        Uses case-insensitive `project_name` comparison, assuming all the
        project's distributions use their project's name converted to all
        lowercase as their key.

        """
    def add(self, dist) -> None:
        """Add `dist` if we ``can_add()`` it and it has not already been added"""
    def best_match(self, req, working_set, installer: Incomplete | None = None, replace_conflicting: bool = False):
        """Find distribution best matching `req` and usable on `working_set`

        This calls the ``find(req)`` method of the `working_set` to see if a
        suitable distribution is already active.  (This may raise
        ``VersionConflict`` if an unsuitable version of the project is already
        active in the specified `working_set`.)  If a suitable distribution
        isn't active, this method returns the newest distribution in the
        environment that meets the ``Requirement`` in `req`.  If no suitable
        distribution is found, and `installer` is supplied, then the result of
        calling the environment's ``obtain(req, installer)`` method will be
        returned.
        """
    def obtain(self, requirement, installer: Incomplete | None = None):
        """Obtain a distribution matching `requirement` (e.g. via download)

        Obtain a distro that matches requirement (e.g. via download).  In the
        base ``Environment`` class, this routine just returns
        ``installer(requirement)``, unless `installer` is None, in which case
        None is returned instead.  This method is a hook that allows subclasses
        to attempt other ways of obtaining a distribution before falling back
        to the `installer` argument."""
    def __iter__(self):
        """Yield the unique project names of the available distributions"""
    def __iadd__(self, other):
        """In-place addition of a distribution or environment"""
    def __add__(self, other):
        """Add an environment or distribution to an environment"""
AvailableDistributions = Environment

class ExtractionError(RuntimeError):
    """An error occurred extracting a resource

    The following attributes are available from instances of this exception:

    manager
        The resource manager that raised this exception

    cache_path
        The base directory for resource extraction

    original_error
        The exception instance that caused extraction to fail
    """

class ResourceManager:
    """Manage resource extraction and packages"""
    extraction_path: Incomplete
    cached_files: Incomplete
    def __init__(self) -> None: ...
    def resource_exists(self, package_or_requirement, resource_name):
        """Does the named resource exist?"""
    def resource_isdir(self, package_or_requirement, resource_name):
        """Is the named resource an existing directory?"""
    def resource_filename(self, package_or_requirement, resource_name):
        """Return a true filesystem path for specified resource"""
    def resource_stream(self, package_or_requirement, resource_name):
        """Return a readable file-like object for specified resource"""
    def resource_string(self, package_or_requirement, resource_name):
        """Return specified resource as a string"""
    def resource_listdir(self, package_or_requirement, resource_name):
        """List the contents of the named resource directory"""
    def extraction_error(self) -> None:
        """Give an error message for problems extracting file(s)"""
    def get_cache_path(self, archive_name, names=()):
        '''Return absolute location in cache for `archive_name` and `names`

        The parent directory of the resulting path will be created if it does
        not already exist.  `archive_name` should be the base filename of the
        enclosing egg (which may not be the name of the enclosing zipfile!),
        including its ".egg" extension.  `names`, if provided, should be a
        sequence of path name parts "under" the egg\'s extraction location.

        This method should only be called by resource providers that need to
        obtain an extraction location, and only for names they intend to
        extract, as it tracks the generated names for possible cleanup later.
        '''
    def postprocess(self, tempname, filename) -> None:
        """Perform any platform-specific postprocessing of `tempname`

        This is where Mac header rewrites should be done; other platforms don't
        have anything special they should do.

        Resource providers should call this method ONLY after successfully
        extracting a compressed resource.  They must NOT call it on resources
        that are already in the filesystem.

        `tempname` is the current (temporary) name of the file, and `filename`
        is the name it will be renamed to by the caller after this routine
        returns.
        """
    def set_extraction_path(self, path) -> None:
        """Set the base path where resources will be extracted to, if needed.

        If you do not call this routine before any extractions take place, the
        path defaults to the return value of ``get_default_cache()``.  (Which
        is based on the ``PYTHON_EGG_CACHE`` environment variable, with various
        platform-specific fallbacks.  See that routine's documentation for more
        details.)

        Resources are extracted to subdirectories of this path based upon
        information given by the ``IResourceProvider``.  You may set this to a
        temporary directory, but then you must call ``cleanup_resources()`` to
        delete the extracted files when done.  There is no guarantee that
        ``cleanup_resources()`` will be able to remove all extracted files.

        (Note: you may not change the extraction path for a given resource
        manager once resources have been extracted, unless you first call
        ``cleanup_resources()``.)
        """
    def cleanup_resources(self, force: bool = False) -> None:
        """
        Delete all extracted resource files and directories, returning a list
        of the file and directory names that could not be successfully removed.
        This function does not have any concurrency protection, so it should
        generally only be called when the extraction path is a temporary
        directory exclusive to a single process.  This method is not
        automatically called; you must call it explicitly or register it as an
        ``atexit`` function if you wish to ensure cleanup of a temporary
        directory used for extractions.
        """

def get_default_cache():
    '''
    Return the ``PYTHON_EGG_CACHE`` environment variable
    or a platform-relevant user cache dir for an app
    named "Python-Eggs".
    '''
def safe_name(name):
    """Convert an arbitrary string to a standard distribution name

    Any runs of non-alphanumeric/. characters are replaced with a single '-'.
    """
def safe_version(version):
    """
    Convert an arbitrary string to a standard version string
    """
def safe_extra(extra):
    """Convert an arbitrary string to a standard 'extra' name

    Any runs of non-alphanumeric characters are replaced with a single '_',
    and the result is always lowercased.
    """
def to_filename(name):
    """Convert a project or version name to its filename-escaped form

    Any '-' characters are currently replaced with '_'.
    """
def invalid_marker(text):
    """
    Validate text as a PEP 508 environment marker; return an exception
    if invalid or False otherwise.
    """
def evaluate_marker(text, extra: Incomplete | None = None):
    """
    Evaluate a PEP 508 environment marker.
    Return a boolean indicating the marker result in this environment.
    Raise SyntaxError if marker is invalid.

    This implementation uses the 'pyparsing' module.
    """

class NullProvider:
    """Try to implement resources and metadata for arbitrary PEP 302 loaders"""
    egg_name: Incomplete
    egg_info: Incomplete
    loader: Incomplete
    module_path: Incomplete
    def __init__(self, module) -> None: ...
    def get_resource_filename(self, manager, resource_name): ...
    def get_resource_stream(self, manager, resource_name): ...
    def get_resource_string(self, manager, resource_name): ...
    def has_resource(self, resource_name): ...
    def has_metadata(self, name): ...
    def get_metadata(self, name): ...
    def get_metadata_lines(self, name): ...
    def resource_isdir(self, resource_name): ...
    def metadata_isdir(self, name): ...
    def resource_listdir(self, resource_name): ...
    def metadata_listdir(self, name): ...
    def run_script(self, script_name, namespace) -> None: ...

class EggProvider(NullProvider):
    """Provider based on a virtual filesystem"""
    def __init__(self, module) -> None: ...

class DefaultProvider(EggProvider):
    """Provides access to package resources in the filesystem"""
    def get_resource_stream(self, manager, resource_name): ...

class EmptyProvider(NullProvider):
    """Provider that returns nothing for all requests"""
    module_path: Incomplete
    def __init__(self) -> None: ...

empty_provider: Incomplete

class ZipManifests(dict):
    """
    zip manifest builder
    """
    @classmethod
    def build(cls, path):
        """
        Build a dictionary similar to the zipimport directory
        caches, except instead of tuples, store ZipInfo objects.

        Use a platform-specific path separator (os.sep) for the path keys
        for compatibility with pypy on Windows.
        """
    load = build

class MemoizedZipManifests(ZipManifests):
    """
    Memoized zipfile manifests.
    """

    class manifest_mod(NamedTuple):
        manifest: Incomplete
        mtime: Incomplete
    def load(self, path):
        """
        Load a manifest at path or return a suitable manifest already loaded.
        """

class ZipProvider(EggProvider):
    """Resource support for zips and eggs"""
    eagers: Incomplete
    zip_pre: Incomplete
    def __init__(self, module) -> None: ...
    @property
    def zipinfo(self): ...
    def get_resource_filename(self, manager, resource_name): ...

class FileMetadata(EmptyProvider):
    '''Metadata handler for standalone PKG-INFO files

    Usage::

        metadata = FileMetadata("/path/to/PKG-INFO")

    This provider rejects all data and metadata requests except for PKG-INFO,
    which is treated as existing, and will be the contents of the file at
    the provided location.
    '''
    path: Incomplete
    def __init__(self, path) -> None: ...
    def has_metadata(self, name): ...
    def get_metadata(self, name): ...
    def get_metadata_lines(self, name): ...

class PathMetadata(DefaultProvider):
    '''Metadata provider for egg directories

    Usage::

        # Development eggs:

        egg_info = "/path/to/PackageName.egg-info"
        base_dir = os.path.dirname(egg_info)
        metadata = PathMetadata(base_dir, egg_info)
        dist_name = os.path.splitext(os.path.basename(egg_info))[0]
        dist = Distribution(basedir, project_name=dist_name, metadata=metadata)

        # Unpacked egg directories:

        egg_path = "/path/to/PackageName-ver-pyver-etc.egg"
        metadata = PathMetadata(egg_path, os.path.join(egg_path,\'EGG-INFO\'))
        dist = Distribution.from_filename(egg_path, metadata=metadata)
    '''
    module_path: Incomplete
    egg_info: Incomplete
    def __init__(self, path, egg_info) -> None: ...

class EggMetadata(ZipProvider):
    """Metadata provider for .egg files"""
    zip_pre: Incomplete
    loader: Incomplete
    module_path: Incomplete
    def __init__(self, importer) -> None:
        """Create a metadata provider from a zipimporter"""

def register_finder(importer_type, distribution_finder) -> None:
    '''Register `distribution_finder` to find distributions in sys.path items

    `importer_type` is the type or class of a PEP 302 "Importer" (sys.path item
    handler), and `distribution_finder` is a callable that, passed a path
    item and the importer instance, yields ``Distribution`` instances found on
    that path item.  See ``pkg_resources.find_on_path`` for an example.'''
def find_distributions(path_item, only: bool = False):
    """Yield distributions accessible via `path_item`"""

class NoDists:
    """
    >>> bool(NoDists())
    False

    >>> list(NoDists()('anything'))
    []
    """
    def __bool__(self) -> bool: ...
    def __call__(self, fullpath): ...

def register_namespace_handler(importer_type, namespace_handler) -> None:
    '''Register `namespace_handler` to declare namespace packages

    `importer_type` is the type or class of a PEP 302 "Importer" (sys.path item
    handler), and `namespace_handler` is a callable like this::

        def namespace_handler(importer, path_entry, moduleName, module):
            # return a path_entry to use for child packages

    Namespace handlers are only called if the importer object has already
    agreed that it can handle the relevant path item, and they should only
    return a subpath if the module __path__ does not already contain an
    equivalent subpath.  For an example namespace handler, see
    ``pkg_resources.file_ns_handler``.
    '''
def declare_namespace(packageName) -> None:
    """Declare that package 'packageName' is a namespace package"""
def fixup_namespace_packages(path_item, parent: Incomplete | None = None) -> None:
    """Ensure that previously-declared namespace packages include path_item"""
def normalize_path(filename):
    """Normalize a file/dir name for comparison purposes"""

class EntryPoint:
    """Object representing an advertised importable object"""
    name: Incomplete
    module_name: Incomplete
    attrs: Incomplete
    extras: Incomplete
    dist: Incomplete
    def __init__(self, name, module_name, attrs=(), extras=(), dist: Incomplete | None = None) -> None: ...
    def load(self, require: bool = True, *args, **kwargs):
        """
        Require packages for this EntryPoint, then resolve it.
        """
    def resolve(self):
        """
        Resolve the entry point from its module and attrs.
        """
    def require(self, env: Incomplete | None = None, installer: Incomplete | None = None) -> None: ...
    pattern: Incomplete
    @classmethod
    def parse(cls, src, dist: Incomplete | None = None):
        """Parse a single entry point from string `src`

        Entry point syntax follows the form::

            name = some.module:some.attr [extra1, extra2]

        The entry name and module name are required, but the ``:attrs`` and
        ``[extras]`` parts are optional
        """
    @classmethod
    def parse_group(cls, group, lines, dist: Incomplete | None = None):
        """Parse an entry point group"""
    @classmethod
    def parse_map(cls, data, dist: Incomplete | None = None):
        """Parse a map of entry point groups"""

class Distribution:
    """Wrap an actual or potential sys.path entry w/metadata"""
    PKG_INFO: str
    project_name: Incomplete
    py_version: Incomplete
    platform: Incomplete
    location: Incomplete
    precedence: Incomplete
    def __init__(self, location: Incomplete | None = None, metadata: Incomplete | None = None, project_name: Incomplete | None = None, version: Incomplete | None = None, py_version=..., platform: Incomplete | None = None, precedence=...) -> None: ...
    @classmethod
    def from_location(cls, location, basename, metadata: Incomplete | None = None, **kw): ...
    @property
    def hashcmp(self): ...
    def __hash__(self): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @property
    def key(self): ...
    @property
    def parsed_version(self): ...
    @property
    def version(self): ...
    def requires(self, extras=()):
        """List of Requirements needed for this distro if `extras` are used"""
    def activate(self, path: Incomplete | None = None, replace: bool = False) -> None:
        """Ensure distribution is importable on `path` (default=sys.path)"""
    def egg_name(self):
        """Return what this distribution's standard .egg filename should be"""
    def __getattr__(self, attr):
        """Delegate all unrecognized public attributes to .metadata provider"""
    def __dir__(self): ...
    @classmethod
    def from_filename(cls, filename, metadata: Incomplete | None = None, **kw): ...
    def as_requirement(self):
        """Return a ``Requirement`` that matches this distribution exactly"""
    def load_entry_point(self, group, name):
        """Return the `name` entry point of `group` or raise ImportError"""
    def get_entry_map(self, group: Incomplete | None = None):
        """Return the entry point map for `group`, or the full entry map"""
    def get_entry_info(self, group, name):
        """Return the EntryPoint object for `group`+`name`, or ``None``"""
    def insert_on(self, path, loc: Incomplete | None = None, replace: bool = False) -> None:
        """Ensure self.location is on path

        If replace=False (default):
            - If location is already in path anywhere, do nothing.
            - Else:
              - If it's an egg and its parent directory is on path,
                insert just ahead of the parent.
              - Else: add to the end of path.
        If replace=True:
            - If location is already on path anywhere (not eggs)
              or higher priority than its parent (eggs)
              do nothing.
            - Else:
              - If it's an egg and its parent directory is on path,
                insert just ahead of the parent,
                removing any lower-priority entries.
              - Else: add it to the front of path.
        """
    def check_version_conflict(self) -> None: ...
    def has_version(self): ...
    def clone(self, **kw):
        """Copy this distribution, substituting in any changed keyword args"""
    @property
    def extras(self): ...

class EggInfoDistribution(Distribution): ...

class DistInfoDistribution(Distribution):
    """
    Wrap an actual or potential sys.path entry
    w/metadata, .dist-info style.
    """
    PKG_INFO: str
    EQEQ: Incomplete

def parse_requirements(strs):
    """
    Yield ``Requirement`` objects for each specification in `strs`.

    `strs` must be a string, or a (possibly-nested) iterable thereof.
    """

class RequirementParseError(packaging.requirements.InvalidRequirement):
    """Compatibility wrapper for InvalidRequirement"""

class Requirement(packaging.requirements.Requirement):
    unsafe_name: Incomplete
    specs: Incomplete
    extras: Incomplete
    hashCmp: Incomplete
    def __init__(self, requirement_string) -> None:
        """DO NOT CALL THIS UNDOCUMENTED METHOD; use Requirement.parse()!"""
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __contains__(self, item) -> bool: ...
    def __hash__(self): ...
    @staticmethod
    def parse(s): ...

def ensure_directory(path) -> None:
    """Ensure that the parent directory of `path` exists"""
def split_sections(s) -> Generator[Incomplete, None, None]:
    '''Split a string or iterable thereof into (section, content) pairs

    Each ``section`` is a stripped version of the section header ("[section]")
    and each ``content`` is a list of stripped lines excluding blank lines and
    comment-only lines.  If there are any such lines before the first section
    header, they\'re returned in a first ``section`` of ``None``.
    '''

class PkgResourcesDeprecationWarning(Warning):
    """
    Base class for warning about deprecations in ``pkg_resources``

    This class is not derived from ``DeprecationWarning``, and as such is
    visible by default.
    """
