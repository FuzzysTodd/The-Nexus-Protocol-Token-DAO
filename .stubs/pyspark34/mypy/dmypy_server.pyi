import mypy.build
from _typeshed import Incomplete
from mypy.dmypy_util import receive as receive
from mypy.find_sources import InvalidSourceList as InvalidSourceList, create_source_list as create_source_list
from mypy.fscache import FileSystemCache as FileSystemCache
from mypy.fswatcher import FileData as FileData, FileSystemWatcher as FileSystemWatcher
from mypy.inspections import InspectionEngine as InspectionEngine
from mypy.ipc import IPCServer as IPCServer
from mypy.modulefinder import BuildSource as BuildSource, FindModuleCache as FindModuleCache, SearchPaths as SearchPaths, compute_search_paths as compute_search_paths
from mypy.options import Options as Options
from mypy.server.update import FineGrainedBuildManager as FineGrainedBuildManager, refresh_suppressed_submodules as refresh_suppressed_submodules
from mypy.suggestions import SuggestionEngine as SuggestionEngine, SuggestionFailure as SuggestionFailure
from mypy.typestate import reset_global_state as reset_global_state
from mypy.util import FancyFormatter as FancyFormatter, count_stats as count_stats
from mypy.version import __version__ as __version__
from typing import AbstractSet, Any, Sequence
from typing_extensions import Final, TypeAlias as _TypeAlias

MEM_PROFILE: Final[bool]

def daemonize(options: Options, status_file: str, timeout: int | None = None, log_file: str | None = None) -> int:
    """Run the mypy daemon in a grandchild of the current process

        Return 0 for success, exit status for failure, negative if
        subprocess killed by signal.
        """

CONNECTION_NAME: Final[str]

def process_start_options(flags: list[str], allow_sources: bool) -> Options: ...
def ignore_suppressed_imports(module: str) -> bool:
    """Can we skip looking for newly unsuppressed imports to module?"""

ModulePathPair: _TypeAlias
ModulePathPairs: _TypeAlias
ChangesAndRemovals: _TypeAlias

class Server:
    options: Incomplete
    options_snapshot: Incomplete
    timeout: Incomplete
    fine_grained_manager: Incomplete
    fscache: Incomplete
    status_file: Incomplete
    formatter: Incomplete
    def __init__(self, options: Options, status_file: str, timeout: int | None = None) -> None:
        """Initialize the server with the desired mypy flags."""
    def serve(self) -> None:
        """Serve requests, synchronously (no thread or fork)."""
    def run_command(self, command: str, data: dict[str, object]) -> dict[str, object]:
        """Run a specific command from the registry."""
    def cmd_status(self, fswatcher_dump_file: str | None = None) -> dict[str, object]:
        """Return daemon status."""
    def cmd_stop(self) -> dict[str, object]:
        """Stop daemon."""
    def cmd_run(self, version: str, args: Sequence[str], export_types: bool, is_tty: bool, terminal_width: int) -> dict[str, object]:
        """Check a list of files, triggering a restart if needed."""
    def cmd_check(self, files: Sequence[str], export_types: bool, is_tty: bool, terminal_width: int) -> dict[str, object]:
        """Check a list of files."""
    def cmd_recheck(self, is_tty: bool, terminal_width: int, export_types: bool, remove: list[str] | None = None, update: list[str] | None = None) -> dict[str, object]:
        """Check the same list of files we checked most recently.

        If remove/update is given, they modify the previous list;
        if all are None, stat() is called for each file in the previous list.
        """
    def check(self, sources: list[BuildSource], export_types: bool, is_tty: bool, terminal_width: int) -> dict[str, Any]:
        """Check using fine-grained incremental mode.

        If is_tty is True format the output nicely with colors and summary line
        (unless disabled in self.options). Also pass the terminal_width to formatter.
        """
    def flush_caches(self) -> None: ...
    def update_stats(self, res: dict[str, Any]) -> None: ...
    def following_imports(self) -> bool:
        """Are we following imports?"""
    fswatcher: Incomplete
    previous_sources: Incomplete
    def initialize_fine_grained(self, sources: list[BuildSource], is_tty: bool, terminal_width: int) -> dict[str, Any]: ...
    def fine_grained_increment(self, sources: list[BuildSource], remove: list[str] | None = None, update: list[str] | None = None) -> list[str]:
        """Perform a fine-grained type checking increment.

        If remove and update are None, determine changed paths by using
        fswatcher. Otherwise, assume that only these files have changes.

        Args:
            sources: sources passed on the command line
            remove: paths of files that have been removed
            update: paths of files that have been changed or created
        """
    def fine_grained_increment_follow_imports(self, sources: list[BuildSource]) -> list[str]:
        """Like fine_grained_increment, but follow imports."""
    def find_reachable_changed_modules(self, roots: list[BuildSource], graph: mypy.build.Graph, seen: set[str], changed_paths: AbstractSet[str]) -> tuple[list[tuple[str, str]], list[BuildSource]]:
        """Follow imports within graph from given sources until hitting changed modules.

        If we find a changed module, we can't continue following imports as the imports
        may have changed.

        Args:
            roots: modules where to start search from
            graph: module graph to use for the search
            seen: modules we've seen before that won't be visited (mutated here!!)
            changed_paths: which paths have changed (stop search here and return any found)

        Return (encountered reachable changed modules,
                unchanged files not in sources_set traversed).
        """
    def direct_imports(self, module: tuple[str, str], graph: mypy.build.Graph) -> list[BuildSource]:
        """Return the direct imports of module not included in seen."""
    def find_added_suppressed(self, graph: mypy.build.Graph, seen: set[str], search_paths: SearchPaths) -> list[tuple[str, str]]:
        """Find suppressed modules that have been added (and not included in seen).

        Args:
            seen: reachable modules we've seen before (mutated here!!)

        Return suppressed, added modules.
        """
    def increment_output(self, messages: list[str], sources: list[BuildSource], is_tty: bool, terminal_width: int) -> dict[str, Any]: ...
    def pretty_messages(self, messages: list[str], n_sources: int, is_tty: bool = False, terminal_width: int | None = None) -> list[str]: ...
    def update_sources(self, sources: list[BuildSource]) -> None: ...
    def update_changed(self, sources: list[BuildSource], remove: list[str], update: list[str]) -> ChangesAndRemovals: ...
    def find_changed(self, sources: list[BuildSource]) -> ChangesAndRemovals: ...
    def cmd_inspect(self, show: str, location: str, verbosity: int = 0, limit: int = 0, include_span: bool = False, include_kind: bool = False, include_object_attrs: bool = False, union_attrs: bool = False, force_reload: bool = False) -> dict[str, object]:
        """Locate and inspect expression(s)."""
    def cmd_suggest(self, function: str, callsites: bool, **kwargs: Any) -> dict[str, object]:
        """Suggest a signature for a function."""
    def cmd_hang(self) -> dict[str, object]:
        """Hang for 100 seconds, as a debug hack."""

MiB: Final[Incomplete]

def get_meminfo() -> dict[str, Any]: ...
def find_all_sources_in_build(graph: mypy.build.Graph, extra: Sequence[BuildSource] = ()) -> list[BuildSource]: ...
def fix_module_deps(graph: mypy.build.Graph) -> None:
    """After an incremental update, update module dependencies to reflect the new state.

    This can make some suppressed dependencies non-suppressed, and vice versa (if modules
    have been added to or removed from the build).
    """
def filter_out_missing_top_level_packages(packages: set[str], search_paths: SearchPaths, fscache: FileSystemCache) -> set[str]:
    """Quickly filter out obviously missing top-level packages.

    Return packages with entries that can't be found removed.

    This is approximate: some packages that aren't actually valid may be
    included. However, all potentially valid packages must be returned.
    """
