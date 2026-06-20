import os
import types
from _typeshed import Incomplete
from mypy.checker import TypeChecker as TypeChecker
from mypy.config_parser import parse_mypy_comments as parse_mypy_comments
from mypy.errors import CompileError as CompileError, ErrorInfo as ErrorInfo, Errors as Errors, report_internal_error as report_internal_error
from mypy.fixup import fixup_module as fixup_module
from mypy.freetree import free_tree as free_tree
from mypy.fscache import FileSystemCache as FileSystemCache
from mypy.indirection import TypeIndirectionVisitor as TypeIndirectionVisitor
from mypy.messages import MessageBuilder as MessageBuilder
from mypy.metastore import FilesystemMetadataStore as FilesystemMetadataStore, MetadataStore as MetadataStore, SqliteMetadataStore as SqliteMetadataStore
from mypy.modulefinder import BuildSource as BuildSource, BuildSourceSet as BuildSourceSet, FindModuleCache as FindModuleCache, ModuleNotFoundReason as ModuleNotFoundReason, ModuleSearchResult as ModuleSearchResult, SearchPaths as SearchPaths, compute_search_paths as compute_search_paths
from mypy.nodes import Expression as Expression, Import as Import, ImportAll as ImportAll, ImportBase as ImportBase, ImportFrom as ImportFrom, MypyFile as MypyFile, SymbolTable as SymbolTable, TypeInfo as TypeInfo
from mypy.options import Options as Options
from mypy.parse import parse as parse
from mypy.partially_defined import PossiblyUndefinedVariableVisitor as PossiblyUndefinedVariableVisitor
from mypy.plugin import ChainedPlugin as ChainedPlugin, Plugin as Plugin, ReportConfigContext as ReportConfigContext
from mypy.plugins.default import DefaultPlugin as DefaultPlugin
from mypy.renaming import LimitedVariableRenameVisitor as LimitedVariableRenameVisitor, VariableRenameVisitor as VariableRenameVisitor
from mypy.report import Reports as Reports
from mypy.semanal import SemanticAnalyzer as SemanticAnalyzer
from mypy.semanal_pass1 import SemanticAnalyzerPreAnalysis as SemanticAnalyzerPreAnalysis
from mypy.stats import dump_type_stats as dump_type_stats
from mypy.stubinfo import is_legacy_bundled_package as is_legacy_bundled_package, legacy_bundled_packages as legacy_bundled_packages, non_bundled_packages as non_bundled_packages, stub_package_name as stub_package_name
from mypy.types import Type as Type
from mypy.typestate import reset_global_state as reset_global_state, type_state as type_state
from mypy.util import DecodeError as DecodeError, decode_python_encoding as decode_python_encoding, get_mypy_comments as get_mypy_comments, get_top_two_prefixes as get_top_two_prefixes, hash_digest as hash_digest, is_stub_package_file as is_stub_package_file, is_sub_path as is_sub_path, is_typeshed_file as is_typeshed_file, module_prefix as module_prefix, read_py_file as read_py_file, time_ref as time_ref, time_spent_us as time_spent_us
from mypy.version import __version__ as __version__
from typing import AbstractSet, Any, Callable, ClassVar, Iterable, Iterator, Mapping, NamedTuple, Sequence, TextIO, TypeVar
from typing_extensions import Final, TypeAlias as _TypeAlias, TypedDict

DEBUG_FINE_GRAINED: Final[bool]
CORE_BUILTIN_MODULES: Final[Incomplete]
Graph: _TypeAlias

class BuildResult:
    """The result of a successful build.

    Attributes:
      manager: The build manager.
      files:   Dictionary from module name to related AST node.
      types:   Dictionary from parse tree node to its inferred type.
      used_cache: Whether the build took advantage of a pre-existing cache
      errors:  List of error messages.
    """
    manager: Incomplete
    graph: Incomplete
    files: Incomplete
    types: Incomplete
    used_cache: Incomplete
    errors: Incomplete
    def __init__(self, manager: BuildManager, graph: Graph) -> None: ...

def build(sources: list[BuildSource], options: Options, alt_lib_path: str | None = None, flush_errors: Callable[[list[str], bool], None] | None = None, fscache: FileSystemCache | None = None, stdout: TextIO | None = None, stderr: TextIO | None = None, extra_plugins: Sequence[Plugin] | None = None) -> BuildResult:
    """Analyze a program.

    A single call to build performs parsing, semantic analysis and optionally
    type checking for the program *and* all imported modules, recursively.

    Return BuildResult if successful or only non-blocking errors were found;
    otherwise raise CompileError.

    If a flush_errors callback is provided, all error messages will be
    passed to it and the errors and messages fields of BuildResult and
    CompileError (respectively) will be empty. Otherwise those fields will
    report any error messages.

    Args:
      sources: list of sources to build
      options: build options
      alt_lib_path: an additional directory for looking up library modules
        (takes precedence over other directories)
      flush_errors: optional function to flush errors after a file is processed
      fscache: optionally a file-system cacher

    """
def default_data_dir() -> str:
    """Returns directory containing typeshed directory."""
def normpath(path: str, options: Options) -> str:
    """Convert path to absolute; but to relative in bazel mode.

    (Bazel's distributed cache doesn't like filesystem metadata to
    end up in output files.)
    """

class CacheMeta(NamedTuple):
    id: str
    path: str
    mtime: int
    size: int
    hash: str
    dependencies: list[str]
    data_mtime: int
    data_json: str
    suppressed: list[str]
    options: dict[str, object] | None
    dep_prios: list[int]
    dep_lines: list[int]
    interface_hash: str
    version_id: str
    ignore_all: bool
    plugin_data: Any

class FgDepMeta(TypedDict):
    path: str
    mtime: int

def cache_meta_from_dict(meta: dict[str, Any], data_json: str) -> CacheMeta:
    """Build a CacheMeta object from a json metadata dictionary

    Args:
      meta: JSON metadata read from the metadata cache file
      data_json: Path to the .data.json file containing the AST trees
    """

PRI_HIGH: Final[int]
PRI_MED: Final[int]
PRI_LOW: Final[int]
PRI_MYPY: Final[int]
PRI_INDIRECT: Final[int]
PRI_ALL: Final[int]

def import_priority(imp: ImportBase, toplevel_priority: int) -> int:
    """Compute import priority from an import node."""
def load_plugins_from_config(options: Options, errors: Errors, stdout: TextIO) -> tuple[list[Plugin], dict[str, str]]:
    """Load all configured plugins.

    Return a list of all the loaded plugins from the config file.
    The second return value is a snapshot of versions/hashes of loaded user
    plugins (for cache validation).
    """
def load_plugins(options: Options, errors: Errors, stdout: TextIO, extra_plugins: Sequence[Plugin]) -> tuple[Plugin, dict[str, str]]:
    """Load all configured plugins.

    Return a plugin that encapsulates all plugins chained together. Always
    at least include the default plugin (it's last in the chain).
    The second return value is a snapshot of versions/hashes of loaded user
    plugins (for cache validation).
    """
def take_module_snapshot(module: types.ModuleType) -> str:
    """Take plugin module snapshot by recording its version and hash.

    We record _both_ hash and the version to detect more possible changes
    (e.g. if there is a change in modules imported by a plugin).
    """
def find_config_file_line_number(path: str, section: str, setting_name: str) -> int:
    """Return the approximate location of setting_name within mypy config file.

    Return -1 if can't determine the line unambiguously.
    """

class BuildManager:
    """This class holds shared state for building a mypy program.

    It is used to coordinate parsing, import processing, semantic
    analysis and type checking.  The actual build steps are carried
    out by dispatch().

    Attributes:
      data_dir:        Mypy data directory (contains stubs)
      search_paths:    SearchPaths instance indicating where to look for modules
      modules:         Mapping of module ID to MypyFile (shared by the passes)
      semantic_analyzer:
                       Semantic analyzer, pass 2
      all_types:       Map {Expression: Type} from all modules (enabled by export_types)
      options:         Build options
      missing_modules: Set of modules that could not be imported encountered so far
      stale_modules:   Set of modules that needed to be rechecked (only used by tests)
      fg_deps_meta:    Metadata for fine-grained dependencies caches associated with modules
      fg_deps:         A fine-grained dependency map
      version_id:      The current mypy version (based on commit id when possible)
      plugin:          Active mypy plugin(s)
      plugins_snapshot:
                       Snapshot of currently active user plugins (versions and hashes)
      old_plugins_snapshot:
                       Plugins snapshot from previous incremental run (or None in
                       non-incremental mode and if cache was not found)
      errors:          Used for reporting all errors
      flush_errors:    A function for processing errors after each SCC
      cache_enabled:   Whether cache is being read. This is set based on options,
                       but is disabled if fine-grained cache loading fails
                       and after an initial fine-grained load. This doesn't
                       determine whether we write cache files or not.
      quickstart_state:
                       A cache of filename -> mtime/size/hash info used to avoid
                       needing to hash source files when using a cache with mismatching mtimes
      stats:           Dict with various instrumentation numbers, it is used
                       not only for debugging, but also required for correctness,
                       in particular to check consistency of the fine-grained dependency cache.
      fscache:         A file system cacher
      ast_cache:       AST cache to speed up mypy daemon
    """
    stats: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    start_time: Incomplete
    data_dir: Incomplete
    errors: Incomplete
    search_paths: Incomplete
    source_set: Incomplete
    reports: Incomplete
    options: Incomplete
    version_id: Incomplete
    modules: Incomplete
    missing_modules: Incomplete
    fg_deps_meta: Incomplete
    fg_deps: Incomplete
    plugin: Incomplete
    incomplete_namespaces: Incomplete
    semantic_analyzer: Incomplete
    all_types: Incomplete
    indirection_detector: Incomplete
    stale_modules: Incomplete
    rechecked_modules: Incomplete
    flush_errors: Incomplete
    cache_enabled: Incomplete
    fscache: Incomplete
    find_module_cache: Incomplete
    metastore: Incomplete
    shadow_map: Incomplete
    shadow_equivalence_map: Incomplete
    plugins_snapshot: Incomplete
    old_plugins_snapshot: Incomplete
    quickstart_state: Incomplete
    processed_targets: Incomplete
    missing_stub_packages: Incomplete
    ast_cache: Incomplete
    def __init__(self, data_dir: str, search_paths: SearchPaths, ignore_prefix: str, source_set: BuildSourceSet, reports: Reports | None, options: Options, version_id: str, plugin: Plugin, plugins_snapshot: dict[str, str], errors: Errors, flush_errors: Callable[[list[str], bool], None], fscache: FileSystemCache, stdout: TextIO, stderr: TextIO) -> None: ...
    def dump_stats(self) -> None: ...
    def use_fine_grained_cache(self) -> bool: ...
    def maybe_swap_for_shadow_path(self, path: str) -> str: ...
    def get_stat(self, path: str) -> os.stat_result: ...
    def getmtime(self, path: str) -> int:
        """Return a file's mtime; but 0 in bazel mode.

        (Bazel's distributed cache doesn't like filesystem metadata to
        end up in output files.)
        """
    def all_imported_modules_in_file(self, file: MypyFile) -> list[tuple[int, str, int]]:
        """Find all reachable import statements in a file.

        Return list of tuples (priority, module id, import line number)
        for all modules imported in file; lower numbers == higher priority.

        Can generate blocking errors on bogus relative imports.
        """
    def is_module(self, id: str) -> bool:
        """Is there a file in the file system corresponding to module id?"""
    def parse_file(self, id: str, path: str, source: str, ignore_errors: bool, options: Options) -> MypyFile:
        """Parse the source of a file with the given name.

        Raise CompileError if there is a parse error.
        """
    def load_fine_grained_deps(self, id: str) -> dict[str, set[str]]: ...
    def report_file(self, file: MypyFile, type_map: dict[Expression, Type], options: Options) -> None: ...
    def verbosity(self) -> int: ...
    def log(self, *message: str) -> None: ...
    def log_fine_grained(self, *message: str) -> None: ...
    def trace(self, *message: str) -> None: ...
    def add_stats(self, **kwds: Any) -> None: ...
    def stats_summary(self) -> Mapping[str, object]: ...

def deps_to_json(x: dict[str, set[str]]) -> str: ...

DEPS_META_FILE: Final[str]
DEPS_ROOT_FILE: Final[str]
FAKE_ROOT_MODULE: Final[str]

def write_deps_cache(rdeps: dict[str, dict[str, set[str]]], manager: BuildManager, graph: Graph) -> None:
    """Write cache files for fine-grained dependencies.

    Serialize fine-grained dependencies map for fine grained mode.

    Dependencies on some module 'm' is stored in the dependency cache
    file m.deps.json.  This entails some spooky action at a distance:
    if module 'n' depends on 'm', that produces entries in m.deps.json.
    When there is a dependency on a module that does not exist in the
    build, it is stored with its first existing parent module. If no
    such module exists, it is stored with the fake module FAKE_ROOT_MODULE.

    This means that the validity of the fine-grained dependency caches
    are a global property, so we store validity checking information for
    fine-grained dependencies in a global cache file:
     * We take a snapshot of current sources to later check consistency
       between the fine-grained dependency cache and module cache metadata
     * We store the mtime of all of the dependency files to verify they
       haven't changed
    """
def invert_deps(deps: dict[str, set[str]], graph: Graph) -> dict[str, dict[str, set[str]]]:
    """Splits fine-grained dependencies based on the module of the trigger.

    Returns a dictionary from module ids to all dependencies on that
    module. Dependencies not associated with a module in the build will be
    associated with the nearest parent module that is in the build, or the
    fake module FAKE_ROOT_MODULE if none are.
    """
def generate_deps_for_cache(manager: BuildManager, graph: Graph) -> dict[str, dict[str, set[str]]]:
    """Generate fine-grained dependencies into a form suitable for serializing.

    This does a couple things:
    1. Splits fine-grained deps based on the module of the trigger
    2. For each module we generated fine-grained deps for, load any previous
       deps and merge them in.

    Returns a dictionary from module ids to all dependencies on that
    module. Dependencies not associated with a module in the build will be
    associated with the nearest parent module that is in the build, or the
    fake module FAKE_ROOT_MODULE if none are.
    """

PLUGIN_SNAPSHOT_FILE: Final[str]

def write_plugins_snapshot(manager: BuildManager) -> None:
    """Write snapshot of versions and hashes of currently active plugins."""
def read_plugins_snapshot(manager: BuildManager) -> dict[str, str] | None:
    """Read cached snapshot of versions and hashes of plugins from previous run."""
def read_quickstart_file(options: Options, stdout: TextIO) -> dict[str, tuple[float, int, str]] | None: ...
def read_deps_cache(manager: BuildManager, graph: Graph) -> dict[str, FgDepMeta] | None:
    """Read and validate the fine-grained dependencies cache.

    See the write_deps_cache documentation for more information on
    the details of the cache.

    Returns None if the cache was invalid in some way.
    """
def add_catch_all_gitignore(target_dir: str) -> None:
    """Add catch-all .gitignore to an existing directory.

    No-op if the .gitignore already exists.
    """
def exclude_from_backups(target_dir: str) -> None:
    """Exclude the directory from various archives and backups supporting CACHEDIR.TAG.

    If the CACHEDIR.TAG file exists the function is a no-op.
    """
def create_metastore(options: Options) -> MetadataStore:
    """Create the appropriate metadata store."""
def get_cache_names(id: str, path: str, options: Options) -> tuple[str, str, str | None]:
    """Return the file names for the cache files.

    Args:
      id: module ID
      path: module path
      cache_dir: cache directory
      pyversion: Python version (major, minor)

    Returns:
      A tuple with the file names to be used for the meta JSON, the
      data JSON, and the fine-grained deps JSON, respectively.
    """
def find_cache_meta(id: str, path: str, manager: BuildManager) -> CacheMeta | None:
    """Find cache data for a module.

    Args:
      id: module ID
      path: module path
      manager: the build manager (for pyversion, log/trace, and build options)

    Returns:
      A CacheMeta instance if the cache data was found and appears
      valid; otherwise None.
    """
def validate_meta(meta: CacheMeta | None, id: str, path: str | None, ignore_all: bool, manager: BuildManager) -> CacheMeta | None:
    """Checks whether the cached AST of this module can be used.

    Returns:
      None, if the cached AST is unusable.
      Original meta, if mtime/size matched.
      Meta with mtime updated to match source file, if hash/size matched but mtime/path didn't.
    """
def compute_hash(text: str) -> str: ...
def json_dumps(obj: Any, debug_cache: bool) -> str: ...
def write_cache(id: str, path: str, tree: MypyFile, dependencies: list[str], suppressed: list[str], dep_prios: list[int], dep_lines: list[int], old_interface_hash: str, source_hash: str, ignore_all: bool, manager: BuildManager) -> tuple[str, CacheMeta | None]:
    """Write cache files for a module.

    Note that this mypy's behavior is still correct when any given
    write_cache() call is replaced with a no-op, so error handling
    code that bails without writing anything is okay.

    Args:
      id: module ID
      path: module path
      tree: the fully checked module data
      dependencies: module IDs on which this module depends
      suppressed: module IDs which were suppressed as dependencies
      dep_prios: priorities (parallel array to dependencies)
      dep_lines: import line locations (parallel array to dependencies)
      old_interface_hash: the hash from the previous version of the data cache file
      source_hash: the hash of the source code
      ignore_all: the ignore_all flag for this module
      manager: the build manager (for pyversion, log/trace)

    Returns:
      A tuple containing the interface hash and CacheMeta
      corresponding to the metadata that was written (the latter may
      be None if the cache could not be written).
    """
def delete_cache(id: str, path: str, manager: BuildManager) -> None:
    """Delete cache files for a module.

    The cache files for a module are deleted when mypy finds errors there.
    This avoids inconsistent states with cache files from different mypy runs,
    see #4043 for an example.
    """

class ModuleNotFound(Exception):
    """Control flow exception to signal that a module was not found."""

class State:
    """The state for a module.

    The source is only used for the -c command line option; in that
    case path is None.  Otherwise source is None and path isn't.
    """
    manager: BuildManager
    order_counter: ClassVar[int]
    order: int
    id: str
    path: str | None
    abspath: str | None
    xpath: str
    source: str | None
    source_hash: str | None
    meta_source_hash: str | None
    meta: CacheMeta | None
    data: str | None
    tree: MypyFile | None
    dependencies: list[str]
    dependencies_set: set[str]
    suppressed: list[str]
    suppressed_set: set[str]
    priorities: dict[str, int]
    dep_line_map: dict[str, int]
    ancestors: list[str] | None
    import_context: list[tuple[str, int]]
    caller_state: State | None
    caller_line: int
    externally_same: bool
    interface_hash: str
    options: Options
    ignore_all: bool
    transitive_error: bool
    early_errors: list[ErrorInfo]
    fine_grained_deps_loaded: bool
    time_spent_us: int
    per_line_checking_time_ns: dict[int, int]
    def __init__(self, id: str | None, path: str | None, source: str | None, manager: BuildManager, caller_state: State | None = None, caller_line: int = 0, ancestor_for: State | None = None, root_source: bool = False, temporary: bool = False) -> None: ...
    @property
    def xmeta(self) -> CacheMeta: ...
    def add_ancestors(self) -> None: ...
    def is_fresh(self) -> bool:
        """Return whether the cache data for this file is fresh."""
    def is_interface_fresh(self) -> bool: ...
    def mark_as_rechecked(self) -> None:
        """Marks this module as having been fully re-analyzed by the type-checker."""
    def mark_interface_stale(self, *, on_errors: bool = False) -> None:
        """Marks this module as having a stale public interface, and discards the cache data."""
    def check_blockers(self) -> None:
        """Raise CompileError if a blocking error is detected."""
    def wrap_context(self, check_blockers: bool = True) -> Iterator[None]:
        """Temporarily change the error import context to match this state.

        Also report an internal error if an unexpected exception was raised
        and raise an exception on a blocking error, unless
        check_blockers is False. Skipping blocking error reporting is used
        in the semantic analyzer so that we can report all blocking errors
        for a file (across multiple targets) to maintain backward
        compatibility.
        """
    def load_fine_grained_deps(self) -> dict[str, set[str]]: ...
    def load_tree(self, temporary: bool = False) -> None: ...
    def fix_cross_refs(self) -> None: ...
    def parse_file(self) -> None:
        """Parse file and run first pass of semantic analysis.

        Everything done here is local to the file. Don't depend on imported
        modules in any way. Also record module dependencies based on imports.
        """
    def parse_inline_configuration(self, source: str) -> None:
        """Check for inline mypy: options directive and parse them."""
    def semantic_analysis_pass1(self) -> None:
        """Perform pass 1 of semantic analysis, which happens immediately after parsing.

        This pass can't assume that any other modules have been processed yet.
        """
    def add_dependency(self, dep: str) -> None: ...
    def suppress_dependency(self, dep: str) -> None: ...
    def compute_dependencies(self) -> None:
        """Compute a module's dependencies after parsing it.

        This is used when we parse a file that we didn't have
        up-to-date cache information for. When we have an up-to-date
        cache, we just use the cached info.
        """
    def type_check_first_pass(self) -> None: ...
    def type_checker(self) -> TypeChecker: ...
    def type_map(self) -> dict[Expression, Type]: ...
    def type_check_second_pass(self) -> bool: ...
    def detect_possibly_undefined_vars(self) -> None: ...
    def finish_passes(self) -> None: ...
    def free_state(self) -> None: ...
    def compute_fine_grained_deps(self) -> dict[str, set[str]]: ...
    def update_fine_grained_deps(self, deps: dict[str, set[str]]) -> None: ...
    def valid_references(self) -> set[str]: ...
    def write_cache(self) -> None: ...
    def verify_dependencies(self, suppressed_only: bool = False) -> None:
        """Report errors for import targets in modules that don't exist.

        If suppressed_only is set, only check suppressed dependencies.
        """
    def dependency_priorities(self) -> list[int]: ...
    def dependency_lines(self) -> list[int]: ...
    def generate_unused_ignore_notes(self) -> None: ...
    def generate_ignore_without_code_notes(self) -> None: ...

def find_module_and_diagnose(manager: BuildManager, id: str, options: Options, caller_state: State | None = None, caller_line: int = 0, ancestor_for: State | None = None, root_source: bool = False, skip_diagnose: bool = False) -> tuple[str, str]:
    '''Find a module by name, respecting follow_imports and producing diagnostics.

    If the module is not found, then the ModuleNotFound exception is raised.

    Args:
      id: module to find
      options: the options for the module being loaded
      caller_state: the state of the importing module, if applicable
      caller_line: the line number of the import
      ancestor_for: the child module this is an ancestor of, if applicable
      root_source: whether this source was specified on the command line
      skip_diagnose: skip any error diagnosis and reporting (but ModuleNotFound is
          still raised if the module is missing)

    The specified value of follow_imports for a module can be overridden
    if the module is specified on the command line or if it is a stub,
    so we compute and return the "effective" follow_imports of the module.

    Returns a tuple containing (file path, target\'s effective follow_imports setting)
    '''
def exist_added_packages(suppressed: list[str], manager: BuildManager, options: Options) -> bool:
    """Find if there are any newly added packages that were previously suppressed.

    Exclude everything not in build for follow-imports=skip.
    """
def find_module_simple(id: str, manager: BuildManager) -> str | None:
    """Find a filesystem path for module `id` or `None` if not found."""
def find_module_with_reason(id: str, manager: BuildManager) -> ModuleSearchResult:
    """Find a filesystem path for module `id` or the reason it can't be found."""
def in_partial_package(id: str, manager: BuildManager) -> bool:
    """Check if a missing module can potentially be a part of a package.

    This checks if there is any existing parent __init__.pyi stub that
    defines a module-level __getattr__ (a.k.a. partial stub package).
    """
def module_not_found(manager: BuildManager, line: int, caller_state: State, target: str, reason: ModuleNotFoundReason) -> None: ...
def skipping_module(manager: BuildManager, line: int, caller_state: State | None, id: str, path: str) -> None:
    """Produce an error for an import ignored due to --follow_imports=error"""
def skipping_ancestor(manager: BuildManager, id: str, path: str, ancestor_for: State) -> None:
    """Produce an error for an ancestor ignored due to --follow_imports=error"""
def log_configuration(manager: BuildManager, sources: list[BuildSource]) -> None:
    """Output useful configuration information to LOG and TRACE"""
def dispatch(sources: list[BuildSource], manager: BuildManager, stdout: TextIO) -> Graph: ...

class NodeInfo:
    """Some info about a node in the graph of SCCs."""
    node_id: Incomplete
    scc: Incomplete
    sizes: Incomplete
    deps: Incomplete
    def __init__(self, index: int, scc: list[str]) -> None: ...
    def dumps(self) -> str:
        """Convert to JSON string."""

def dump_timing_stats(path: str, graph: Graph) -> None:
    """Dump timing stats for each file in the given graph."""
def dump_line_checking_stats(path: str, graph: Graph) -> None:
    """Dump per-line expression type checking stats."""
def dump_graph(graph: Graph, stdout: TextIO | None = None) -> None:
    """Dump the graph as a JSON string to stdout.

    This copies some of the work by process_graph()
    (sorted_components() and order_ascc()).
    """
def load_graph(sources: list[BuildSource], manager: BuildManager, old_graph: Graph | None = None, new_modules: list[State] | None = None) -> Graph:
    """Given some source files, load the full dependency graph.

    If an old_graph is passed in, it is used as the starting point and
    modified during graph loading.

    If a new_modules is passed in, any modules that are loaded are
    added to the list. This is an argument and not a return value
    so that the caller can access it even if load_graph fails.

    As this may need to parse files, this can raise CompileError in case
    there are syntax errors.
    """
def process_graph(graph: Graph, manager: BuildManager) -> None:
    """Process everything in dependency order."""
def order_ascc(graph: Graph, ascc: AbstractSet[str], pri_max: int = ...) -> list[str]:
    '''Come up with the ideal processing order within an SCC.

    Using the priorities assigned by all_imported_modules_in_file(),
    try to reduce the cycle to a DAG, by omitting arcs representing
    dependencies of lower priority.

    In the simplest case, if we have A <--> B where A has a top-level
    "import B" (medium priority) but B only has the reverse "import A"
    inside a function (low priority), we turn the cycle into a DAG by
    dropping the B --> A arc, which leaves only A --> B.

    If all arcs have the same priority, we fall back to sorting by
    reverse global order (the order in which modules were first
    encountered).

    The algorithm is recursive, as follows: when as arcs of different
    priorities are present, drop all arcs of the lowest priority,
    identify SCCs in the resulting graph, and apply the algorithm to
    each SCC thus found.  The recursion is bounded because at each
    recursion the spread in priorities is (at least) one less.

    In practice there are only a few priority levels (less than a
    dozen) and in the worst case we just carry out the same algorithm
    for finding SCCs N times.  Thus the complexity is no worse than
    the complexity of the original SCC-finding algorithm -- see
    strongly_connected_components() below for a reference.
    '''
def process_fresh_modules(graph: Graph, modules: list[str], manager: BuildManager) -> None:
    """Process the modules in one group of modules from their cached data.

    This can be used to process an SCC of modules
    This involves loading the tree from JSON and then doing various cleanups.
    """
def process_stale_scc(graph: Graph, scc: list[str], manager: BuildManager) -> None:
    """Process the modules in one SCC from source code.

    Exception: If quick_and_dirty is set, use the cache for fresh modules.
    """
def sorted_components(graph: Graph, vertices: AbstractSet[str] | None = None, pri_max: int = ...) -> list[AbstractSet[str]]:
    """Return the graph's SCCs, topologically sorted by dependencies.

    The sort order is from leaves (nodes without dependencies) to
    roots (nodes on which no other nodes depend).

    This works for a subset of the full dependency graph too;
    dependencies that aren't present in graph.keys() are ignored.
    """
def deps_filtered(graph: Graph, vertices: AbstractSet[str], id: str, pri_max: int) -> list[str]:
    """Filter dependencies for id with pri < pri_max."""
def strongly_connected_components(vertices: AbstractSet[str], edges: dict[str, list[str]]) -> Iterator[set[str]]:
    """Compute Strongly Connected Components of a directed graph.

    Args:
      vertices: the labels for the vertices
      edges: for each vertex, gives the target vertices of its outgoing edges

    Returns:
      An iterator yielding strongly connected components, each
      represented as a set of vertices.  Each input vertex will occur
      exactly once; vertices not part of a SCC are returned as
      singleton sets.

    From https://code.activestate.com/recipes/578507/.
    """
T = TypeVar('T')

def topsort(data: dict[T, set[T]]) -> Iterable[set[T]]:
    """Topological sort.

    Args:
      data: A map from vertices to all vertices that it has an edge
            connecting it to.  NOTE: This data structure
            is modified in place -- for normalization purposes,
            self-dependencies are removed and entries representing
            orphans are added.

    Returns:
      An iterator yielding sets of vertices that have an equivalent
      ordering.

    Example:
      Suppose the input has the following structure:

        {A: {B, C}, B: {D}, C: {D}}

      This is normalized to:

        {A: {B, C}, B: {D}, C: {D}, D: {}}

      The algorithm will yield the following values:

        {D}
        {B, C}
        {A}

    From https://code.activestate.com/recipes/577413/.
    """
def missing_stubs_file(cache_dir: str) -> str: ...
def record_missing_stub_packages(cache_dir: str, missing_stub_packages: set[str]) -> None:
    '''Write a file containing missing stub packages.

    This allows a subsequent "mypy --install-types" run (without other arguments)
    to install missing stub packages.
    '''
def is_silent_import_module(manager: BuildManager, path: str) -> bool: ...
def write_undocumented_ref_info(state: State, metastore: MetadataStore, options: Options, type_map: dict[Expression, Type]) -> None: ...
