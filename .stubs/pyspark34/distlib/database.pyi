from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['Distribution', 'BaseInstalledDistribution', 'InstalledDistribution', 'EggInfoDistribution', 'DistributionPath']

class _Cache:
    """
    A simple cache mapping names and .dist-info paths to distributions
    """
    name: Incomplete
    path: Incomplete
    generated: bool
    def __init__(self) -> None:
        """
        Initialise an instance. There is normally one for each DistributionPath.
        """
    def clear(self) -> None:
        """
        Clear the cache, setting it to its initial state.
        """
    def add(self, dist) -> None:
        """
        Add a distribution to the cache.
        :param dist: The distribution to add.
        """

class DistributionPath:
    """
    Represents a set of distributions installed on a path (typically sys.path).
    """
    path: Incomplete
    def __init__(self, path: Incomplete | None = None, include_egg: bool = False) -> None:
        """
        Create an instance from a path, optionally including legacy (distutils/
        setuptools/distribute) distributions.
        :param path: The path to use, as a list of directories. If not specified,
                     sys.path is used.
        :param include_egg: If True, this instance will look for and return legacy
                            distributions as well as those based on PEP 376.
        """
    cache_enabled: Incomplete
    def clear_cache(self) -> None:
        """
        Clears the internal cache.
        """
    @classmethod
    def distinfo_dirname(cls, name, version):
        """
        The *name* and *version* parameters are converted into their
        filename-escaped form, i.e. any ``'-'`` characters are replaced
        with ``'_'`` other than the one in ``'dist-info'`` and the one
        separating the name from the version number.

        :parameter name: is converted to a standard distribution name by replacing
                         any runs of non- alphanumeric characters with a single
                         ``'-'``.
        :type name: string
        :parameter version: is converted to a standard version string. Spaces
                            become dots, and all other non-alphanumeric characters
                            (except dots) become dashes, with runs of multiple
                            dashes condensed to a single dash.
        :type version: string
        :returns: directory name
        :rtype: string"""
    def get_distributions(self) -> Generator[Incomplete, None, None]:
        """
        Provides an iterator that looks for distributions and returns
        :class:`InstalledDistribution` or
        :class:`EggInfoDistribution` instances for each one of them.

        :rtype: iterator of :class:`InstalledDistribution` and
                :class:`EggInfoDistribution` instances
        """
    def get_distribution(self, name):
        """
        Looks for a named distribution on the path.

        This function only returns the first result found, as no more than one
        value is expected. If nothing is found, ``None`` is returned.

        :rtype: :class:`InstalledDistribution`, :class:`EggInfoDistribution`
                or ``None``
        """
    def provides_distribution(self, name, version: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """
        Iterates over all distributions to find which distributions provide *name*.
        If a *version* is provided, it will be used to filter the results.

        This function only returns the first result found, since no more than
        one values are expected. If the directory is not found, returns ``None``.

        :parameter version: a version specifier that indicates the version
                            required, conforming to the format in ``PEP-345``

        :type name: string
        :type version: string
        """
    def get_file_path(self, name, relative_path):
        """
        Return the path to a resource file.
        """
    def get_exported_entries(self, category, name: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """
        Return all of the exported entries in a particular category.

        :param category: The category to search for entries.
        :param name: If specified, only entries with that name are returned.
        """

class Distribution:
    """
    A base class for distributions, whether installed or from indexes.
    Either way, it must have some metadata, so that's all that's needed
    for construction.
    """
    build_time_dependency: bool
    requested: bool
    metadata: Incomplete
    name: Incomplete
    key: Incomplete
    version: Incomplete
    locator: Incomplete
    digest: Incomplete
    extras: Incomplete
    context: Incomplete
    download_urls: Incomplete
    digests: Incomplete
    def __init__(self, metadata) -> None:
        """
        Initialise an instance.
        :param metadata: The instance of :class:`Metadata` describing this
        distribution.
        """
    @property
    def source_url(self):
        """
        The source archive download URL for this distribution.
        """
    download_url = source_url
    @property
    def name_and_version(self):
        """
        A utility property which displays the name and version in parentheses.
        """
    @property
    def provides(self):
        '''
        A set of distribution names and versions provided by this distribution.
        :return: A set of "name (version)" strings.
        '''
    @property
    def run_requires(self): ...
    @property
    def meta_requires(self): ...
    @property
    def build_requires(self): ...
    @property
    def test_requires(self): ...
    @property
    def dev_requires(self): ...
    def matches_requirement(self, req):
        """
        Say if this instance matches (fulfills) a requirement.
        :param req: The requirement to match.
        :rtype req: str
        :return: True if it matches, else False.
        """
    def __eq__(self, other):
        """
        See if this distribution is the same as another.
        :param other: The distribution to compare with. To be equal to one
                      another. distributions must have the same type, name,
                      version and source_url.
        :return: True if it is the same, else False.
        """
    def __hash__(self):
        """
        Compute hash in a way which matches the equality test.
        """

class BaseInstalledDistribution(Distribution):
    """
    This is the base class for installed distributions (whether PEP 376 or
    legacy).
    """
    hasher: Incomplete
    path: Incomplete
    dist_path: Incomplete
    def __init__(self, metadata, path, env: Incomplete | None = None) -> None:
        """
        Initialise an instance.
        :param metadata: An instance of :class:`Metadata` which describes the
                         distribution. This will normally have been initialised
                         from a metadata file in the ``path``.
        :param path:     The path of the ``.dist-info`` or ``.egg-info``
                         directory for the distribution.
        :param env:      This is normally the :class:`DistributionPath`
                         instance where this distribution was found.
        """
    def get_hash(self, data, hasher: Incomplete | None = None):
        """
        Get the hash of some data, using a particular hash algorithm, if
        specified.

        :param data: The data to be hashed.
        :type data: bytes
        :param hasher: The name of a hash implementation, supported by hashlib,
                       or ``None``. Examples of valid values are ``'sha1'``,
                       ``'sha224'``, ``'sha384'``, '``sha256'``, ``'md5'`` and
                       ``'sha512'``. If no hasher is specified, the ``hasher``
                       attribute of the :class:`InstalledDistribution` instance
                       is used. If the hasher is determined to be ``None``, MD5
                       is used as the hashing algorithm.
        :returns: The hash of the data. If a hasher was explicitly specified,
                  the returned hash will be prefixed with the specified hasher
                  followed by '='.
        :rtype: str
        """

class InstalledDistribution(BaseInstalledDistribution):
    """
    Created with the *path* of the ``.dist-info`` directory provided to the
    constructor. It reads the metadata contained in ``pydist.json`` when it is
    instantiated., or uses a passed in Metadata instance (useful for when
    dry-run mode is being used).
    """
    hasher: str
    modules: Incomplete
    finder: Incomplete
    requested: Incomplete
    def __init__(self, path, metadata: Incomplete | None = None, env: Incomplete | None = None) -> None: ...
    def exports(self):
        """
        Return the information exported by this distribution.
        :return: A dictionary of exports, mapping an export category to a dict
                 of :class:`ExportEntry` instances describing the individual
                 export entries, and keyed by name.
        """
    def read_exports(self):
        """
        Read exports data from a file in .ini format.

        :return: A dictionary of exports, mapping an export category to a list
                 of :class:`ExportEntry` instances describing the individual
                 export entries.
        """
    def write_exports(self, exports) -> None:
        """
        Write a dictionary of exports to a file in .ini format.
        :param exports: A dictionary of exports, mapping an export category to
                        a list of :class:`ExportEntry` instances describing the
                        individual export entries.
        """
    def get_resource_path(self, relative_path):
        """
        NOTE: This API may change in the future.

        Return the absolute path to a resource file with the given relative
        path.

        :param relative_path: The path, relative to .dist-info, of the resource
                              of interest.
        :return: The absolute path where the resource is to be found.
        """
    def list_installed_files(self) -> Generator[Incomplete, None, None]:
        """
        Iterates over the ``RECORD`` entries and returns a tuple
        ``(path, hash, size)`` for each line.

        :returns: iterator of (path, hash, size)
        """
    def write_installed_files(self, paths, prefix, dry_run: bool = False):
        """
        Writes the ``RECORD`` file, using the ``paths`` iterable passed in. Any
        existing ``RECORD`` file is silently overwritten.

        prefix is used to determine when to write absolute paths.
        """
    def check_installed_files(self):
        """
        Checks that the hashes and sizes of the files in ``RECORD`` are
        matched by the files themselves. Returns a (possibly empty) list of
        mismatches. Each entry in the mismatch list will be a tuple consisting
        of the path, 'exists', 'size' or 'hash' according to what didn't match
        (existence is checked first, then size, then hash), the expected
        value and the actual value.
        """
    def shared_locations(self):
        """
        A dictionary of shared locations whose keys are in the set 'prefix',
        'purelib', 'platlib', 'scripts', 'headers', 'data' and 'namespace'.
        The corresponding value is the absolute path of that category for
        this distribution, and takes into account any paths selected by the
        user at installation time (e.g. via command-line arguments). In the
        case of the 'namespace' key, this would be a list of absolute paths
        for the roots of namespace packages in this distribution.

        The first time this property is accessed, the relevant information is
        read from the SHARED file in the .dist-info directory.
        """
    def write_shared_locations(self, paths, dry_run: bool = False):
        """
        Write shared location information to the SHARED file in .dist-info.
        :param paths: A dictionary as described in the documentation for
        :meth:`shared_locations`.
        :param dry_run: If True, the action is logged but no file is actually
                        written.
        :return: The path of the file written to.
        """
    def get_distinfo_resource(self, path): ...
    def get_distinfo_file(self, path):
        """
        Returns a path located under the ``.dist-info`` directory. Returns a
        string representing the path.

        :parameter path: a ``'/'``-separated path relative to the
                         ``.dist-info`` directory or an absolute path;
                         If *path* is an absolute path and doesn't start
                         with the ``.dist-info`` directory path,
                         a :class:`DistlibException` is raised
        :type path: str
        :rtype: str
        """
    def list_distinfo_files(self) -> Generator[Incomplete, None, None]:
        """
        Iterates over the ``RECORD`` entries and returns paths for each line if
        the path is pointing to a file located in the ``.dist-info`` directory
        or one of its subdirectories.

        :returns: iterator of paths
        """
    def __eq__(self, other): ...
    __hash__: Incomplete

class EggInfoDistribution(BaseInstalledDistribution):
    """Created with the *path* of the ``.egg-info`` directory or file provided
    to the constructor. It reads the metadata contained in the file itself, or
    if the given path happens to be a directory, the metadata is read from the
    file ``PKG-INFO`` under that directory."""
    requested: bool
    shared_locations: Incomplete
    path: Incomplete
    dist_path: Incomplete
    def __init__(self, path, env: Incomplete | None = None) -> None: ...
    def check_installed_files(self):
        """
        Checks that the hashes and sizes of the files in ``RECORD`` are
        matched by the files themselves. Returns a (possibly empty) list of
        mismatches. Each entry in the mismatch list will be a tuple consisting
        of the path, 'exists', 'size' or 'hash' according to what didn't match
        (existence is checked first, then size, then hash), the expected
        value and the actual value.
        """
    def list_installed_files(self):
        """
        Iterates over the ``installed-files.txt`` entries and returns a tuple
        ``(path, hash, size)`` for each line.

        :returns: a list of (path, hash, size)
        """
    def list_distinfo_files(self, absolute: bool = False) -> Generator[Incomplete, None, None]:
        """
        Iterates over the ``installed-files.txt`` entries and returns paths for
        each line if the path is pointing to a file located in the
        ``.egg-info`` directory or one of its subdirectories.

        :parameter absolute: If *absolute* is ``True``, each returned path is
                          transformed into a local absolute path. Otherwise the
                          raw value from ``installed-files.txt`` is returned.
        :type absolute: boolean
        :returns: iterator of paths
        """
    def __eq__(self, other): ...
    __hash__: Incomplete
new_dist_class = InstalledDistribution
old_dist_class = EggInfoDistribution

class DependencyGraph:
    """
    Represents a dependency graph between distributions.

    The dependency relationships are stored in an ``adjacency_list`` that maps
    distributions to a list of ``(other, label)`` tuples where  ``other``
    is a distribution and the edge is labeled with ``label`` (i.e. the version
    specifier, if such was provided). Also, for more efficient traversal, for
    every distribution ``x``, a list of predecessors is kept in
    ``reverse_list[x]``. An edge from distribution ``a`` to
    distribution ``b`` means that ``a`` depends on ``b``. If any missing
    dependencies are found, they are stored in ``missing``, which is a
    dictionary that maps distributions to a list of requirements that were not
    provided by any other distributions.
    """
    adjacency_list: Incomplete
    reverse_list: Incomplete
    missing: Incomplete
    def __init__(self) -> None: ...
    def add_distribution(self, distribution) -> None:
        """Add the *distribution* to the graph.

        :type distribution: :class:`distutils2.database.InstalledDistribution`
                            or :class:`distutils2.database.EggInfoDistribution`
        """
    def add_edge(self, x, y, label: Incomplete | None = None) -> None:
        """Add an edge from distribution *x* to distribution *y* with the given
        *label*.

        :type x: :class:`distutils2.database.InstalledDistribution` or
                 :class:`distutils2.database.EggInfoDistribution`
        :type y: :class:`distutils2.database.InstalledDistribution` or
                 :class:`distutils2.database.EggInfoDistribution`
        :type label: ``str`` or ``None``
        """
    def add_missing(self, distribution, requirement) -> None:
        """
        Add a missing *requirement* for the given *distribution*.

        :type distribution: :class:`distutils2.database.InstalledDistribution`
                            or :class:`distutils2.database.EggInfoDistribution`
        :type requirement: ``str``
        """
    def repr_node(self, dist, level: int = 1):
        """Prints only a subgraph"""
    def to_dot(self, f, skip_disconnected: bool = True) -> None:
        """Writes a DOT output for the graph to the provided file *f*.

        If *skip_disconnected* is set to ``True``, then all distributions
        that are not dependent on any other distribution are skipped.

        :type f: has to support ``file``-like operations
        :type skip_disconnected: ``bool``
        """
    def topological_sort(self):
        """
        Perform a topological sort of the graph.
        :return: A tuple, the first element of which is a topologically sorted
                 list of distributions, and the second element of which is a
                 list of distributions that cannot be sorted because they have
                 circular dependencies and so form a cycle.
        """
