from _typeshed import Incomplete
from mypy.build import BuildManager as BuildManager, BuildResult as BuildResult, DEBUG_FINE_GRAINED as DEBUG_FINE_GRAINED, FAKE_ROOT_MODULE as FAKE_ROOT_MODULE, Graph as Graph, State as State, load_graph as load_graph, process_fresh_modules as process_fresh_modules
from mypy.checker import FineGrainedDeferredNode as FineGrainedDeferredNode
from mypy.errors import CompileError as CompileError
from mypy.fscache import FileSystemCache as FileSystemCache
from mypy.modulefinder import BuildSource as BuildSource
from mypy.nodes import Decorator as Decorator, FuncDef as FuncDef, ImportFrom as ImportFrom, MypyFile as MypyFile, OverloadedFuncDef as OverloadedFuncDef, SymbolNode as SymbolNode, SymbolTable as SymbolTable, TypeInfo as TypeInfo
from mypy.options import Options as Options
from mypy.semanal_main import core_modules as core_modules, semantic_analysis_for_scc as semantic_analysis_for_scc, semantic_analysis_for_targets as semantic_analysis_for_targets
from mypy.server.astdiff import SymbolSnapshot as SymbolSnapshot, compare_symbol_table_snapshots as compare_symbol_table_snapshots, snapshot_symbol_table as snapshot_symbol_table
from mypy.server.astmerge import merge_asts as merge_asts
from mypy.server.aststrip import SavedAttributes as SavedAttributes, strip_target as strip_target
from mypy.server.deps import get_dependencies_of_target as get_dependencies_of_target, merge_dependencies as merge_dependencies
from mypy.server.target import trigger_to_target as trigger_to_target
from mypy.server.trigger import WILDCARD_TAG as WILDCARD_TAG, make_trigger as make_trigger
from mypy.typestate import type_state as type_state
from mypy.util import module_prefix as module_prefix, split_target as split_target
from typing import Callable, NamedTuple, Sequence
from typing_extensions import Final, TypeAlias as _TypeAlias

MAX_ITER: Final[int]
SENSITIVE_INTERNAL_MODULES: Incomplete

class FineGrainedBuildManager:
    manager: Incomplete
    graph: Incomplete
    previous_modules: Incomplete
    deps: Incomplete
    previous_targets_with_errors: Incomplete
    previous_messages: Incomplete
    blocking_error: Incomplete
    stale: Incomplete
    triggered: Incomplete
    changed_modules: Incomplete
    updated_modules: Incomplete
    processed_targets: Incomplete
    def __init__(self, result: BuildResult) -> None:
        """Initialize fine-grained build based on a batch build.

        Args:
            result: Result from the initialized build.
                    The manager and graph will be taken over by this class.
            manager: State of the build (mutated by this class)
            graph: Additional state of the build (mutated by this class)
        """
    def update(self, changed_modules: list[tuple[str, str]], removed_modules: list[tuple[str, str]], followed: bool = False) -> list[str]:
        """Update previous build result by processing changed modules.

        Also propagate changes to other modules as needed, but only process
        those parts of other modules that are affected by the changes. Retain
        the existing ASTs and symbol tables of unaffected modules.

        Reuses original BuildManager and Graph.

        Args:
            changed_modules: Modules changed since the previous update/build; each is
                a (module id, path) tuple. Includes modified and added modules.
                Assume this is correct; it's not validated here.
            removed_modules: Modules that have been deleted since the previous update
                or removed from the build.
            followed: If True, the modules were found through following imports

        Returns:
            A list of errors.
        """
    def trigger(self, target: str) -> list[str]:
        """Trigger a specific target explicitly.

        This is intended for use by the suggestions engine.
        """
    def flush_cache(self) -> None:
        """Flush AST cache.

        This needs to be called after each increment, or file changes won't
        be detected reliably.
        """
    def update_one(self, changed_modules: list[tuple[str, str]], initial_set: set[str], removed_set: set[str], blocking_error: str | None, followed: bool) -> tuple[list[tuple[str, str]], tuple[str, str], list[str] | None]:
        """Process a module from the list of changed modules.

        Returns:
            Tuple with these items:

            - Updated list of pending changed modules as (module id, path) tuples
            - Module which was actually processed as (id, path) tuple
            - If there was a blocking error, the error messages from it
        """
    def update_module(self, module: str, path: str, force_removed: bool, followed: bool) -> tuple[list[tuple[str, str]], tuple[str, str], list[str] | None]:
        """Update a single modified module.

        If the module contains imports of previously unseen modules, only process one of
        the new modules and return the remaining work to be done.

        Args:
            module: Id of the module
            path: File system path of the module
            force_removed: If True, consider module removed from the build even if path
                exists (used for removing an existing file from the build)
            followed: Was this found via import following?

        Returns:
            Tuple with these items:

            - Remaining modules to process as (module id, path) tuples
            - Module which was actually processed as (id, path) tuple
            - If there was a blocking error, the error messages from it
        """

def find_unloaded_deps(manager: BuildManager, graph: dict[str, State], initial: Sequence[str]) -> list[str]:
    """Find all the deps of the nodes in initial that haven't had their tree loaded.

    The key invariant here is that if a module is loaded, so are all
    of their dependencies. This means that when we encounter a loaded
    module, we don't need to explore its dependencies.  (This
    invariant is slightly violated when dependencies are added, which
    can be handled by calling find_unloaded_deps directly on the new
    dependencies.)
    """
def ensure_deps_loaded(module: str, deps: dict[str, set[str]], graph: dict[str, State]) -> None:
    """Ensure that the dependencies on a module are loaded.

    Dependencies are loaded into the 'deps' dictionary.

    This also requires loading dependencies from any parent modules,
    since dependencies will get stored with parent modules when a module
    doesn't exist.
    """
def ensure_trees_loaded(manager: BuildManager, graph: dict[str, State], initial: Sequence[str]) -> None:
    """Ensure that the modules in initial and their deps have loaded trees."""

class NormalUpdate(NamedTuple):
    module: str
    path: str
    remaining: list[tuple[str, str]]
    tree: MypyFile | None

class BlockedUpdate(NamedTuple):
    module: str
    path: str
    remaining: list[tuple[str, str]]
    messages: list[str]

UpdateResult: _TypeAlias

def update_module_isolated(module: str, path: str, manager: BuildManager, previous_modules: dict[str, str], graph: Graph, force_removed: bool, followed: bool) -> UpdateResult:
    """Build a new version of one changed module only.

    Don't propagate changes to elsewhere in the program. Raise CompileError on
    encountering a blocking error.

    Args:
        module: Changed module (modified, created or deleted)
        path: Path of the changed module
        manager: Build manager
        graph: Build graph
        force_removed: If True, consider the module removed from the build even it the
            file exists

    Returns a named tuple describing the result (see above for details).
    """
def find_relative_leaf_module(modules: list[tuple[str, str]], graph: Graph) -> tuple[str, str]:
    """Find a module in a list that directly imports no other module in the list.

    If no such module exists, return the lexicographically first module from the list.
    Always return one of the items in the modules list.

    NOTE: If both 'abc' and 'typing' have changed, an effect of the above rule is that
        we prefer 'abc', even if both are in the same SCC. This works around a false
        positive in 'typing', at least in tests.

    Args:
        modules: List of (module, path) tuples (non-empty)
        graph: Program import graph that contains all modules in the module list
    """
def delete_module(module_id: str, path: str, graph: Graph, manager: BuildManager) -> None: ...
def dedupe_modules(modules: list[tuple[str, str]]) -> list[tuple[str, str]]: ...
def get_module_to_path_map(graph: Graph) -> dict[str, str]: ...
def get_sources(fscache: FileSystemCache, modules: dict[str, str], changed_modules: list[tuple[str, str]], followed: bool) -> list[BuildSource]: ...
def calculate_active_triggers(manager: BuildManager, old_snapshots: dict[str, dict[str, SymbolSnapshot]], new_modules: dict[str, MypyFile | None]) -> set[str]:
    """Determine activated triggers by comparing old and new symbol tables.

    For example, if only the signature of function m.f is different in the new
    symbol table, return {'<m.f>'}.
    """
def replace_modules_with_new_variants(manager: BuildManager, graph: dict[str, State], old_modules: dict[str, MypyFile | None], new_modules: dict[str, MypyFile | None]) -> None:
    """Replace modules with newly builds versions.

    Retain the identities of externally visible AST nodes in the
    old ASTs so that references to the affected modules from other
    modules will still be valid (unless something was deleted or
    replaced with an incompatible definition, in which case there
    will be dangling references that will be handled by
    propagate_changes_using_dependencies).
    """
def propagate_changes_using_dependencies(manager: BuildManager, graph: dict[str, State], deps: dict[str, set[str]], triggered: set[str], up_to_date_modules: set[str], targets_with_errors: set[str], processed_targets: list[str]) -> list[tuple[str, str]]:
    """Transitively rechecks targets based on triggers and the dependency map.

    Returns a list (module id, path) tuples representing modules that contain
    a target that needs to be reprocessed but that has not been parsed yet.

    Processed targets should be appended to processed_targets (used in tests only,
    to test the order of processing targets).
    """
def find_targets_recursive(manager: BuildManager, graph: Graph, triggers: set[str], deps: dict[str, set[str]], up_to_date_modules: set[str]) -> tuple[dict[str, set[FineGrainedDeferredNode]], set[str], set[TypeInfo]]:
    """Find names of all targets that need to reprocessed, given some triggers.

    Returns: A tuple containing a:
     * Dictionary from module id to a set of stale targets.
     * A set of module ids for unparsed modules with stale targets.
    """
def reprocess_nodes(manager: BuildManager, graph: dict[str, State], module_id: str, nodeset: set[FineGrainedDeferredNode], deps: dict[str, set[str]], processed_targets: list[str]) -> set[str]:
    """Reprocess a set of nodes within a single module.

    Return fired triggers.
    """
def find_symbol_tables_recursive(prefix: str, symbols: SymbolTable) -> dict[str, SymbolTable]:
    """Find all nested symbol tables.

    Args:
        prefix: Full name prefix (used for return value keys and to filter result so that
            cross references to other modules aren't included)
        symbols: Root symbol table

    Returns a dictionary from full name to corresponding symbol table.
    """
def update_deps(module_id: str, nodes: list[FineGrainedDeferredNode], graph: dict[str, State], deps: dict[str, set[str]], options: Options) -> None: ...
def lookup_target(manager: BuildManager, target: str) -> tuple[list[FineGrainedDeferredNode], TypeInfo | None]:
    """Look up a target by fully-qualified name.

    The first item in the return tuple is a list of deferred nodes that
    needs to be reprocessed. If the target represents a TypeInfo corresponding
    to a protocol, return it as a second item in the return tuple, otherwise None.
    """
def is_verbose(manager: BuildManager) -> bool: ...
def target_from_node(module: str, node: FuncDef | MypyFile | OverloadedFuncDef) -> str | None:
    """Return the target name corresponding to a deferred node.

    Args:
        module: Must be module id of the module that defines 'node'

    Returns the target name, or None if the node is not a valid target in the given
    module (for example, if it's actually defined in another module).
    """

INIT_SUFFIXES: Final[Incomplete]

def refresh_suppressed_submodules(module: str, path: str | None, deps: dict[str, set[str]], graph: Graph, fscache: FileSystemCache, refresh_file: Callable[[str, str], list[str]]) -> list[str] | None:
    '''Look for submodules that are now suppressed in target package.

    If a submodule a.b gets added, we need to mark it as suppressed
    in modules that contain "from a import b". Previously we assumed
    that \'a.b\' is not a module but a regular name.

    This is only relevant when following imports normally.

    Args:
        module: target package in which to look for submodules
        path: path of the module
        refresh_file: function that reads the AST of a module (returns error messages)

    Return a list of errors from refresh_file() if it was called. If the
    return value is None, we didn\'t call refresh_file().
    '''
def extract_fnam_from_message(message: str) -> str | None: ...
def extract_possible_fnam_from_message(message: str) -> str: ...
def sort_messages_preserving_file_order(messages: list[str], prev_messages: list[str]) -> list[str]:
    """Sort messages so that the order of files is preserved.

    An update generates messages so that the files can be in a fairly
    arbitrary order.  Preserve the order of files to avoid messages
    getting reshuffled continuously.  If there are messages in
    additional files, sort them towards the end.
    """
