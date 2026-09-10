from _typeshed import Incomplete
from mypy.build import Graph as Graph, State as State
from mypy.checker import FineGrainedDeferredNode as FineGrainedDeferredNode
from mypy.errors import Errors as Errors
from mypy.nodes import Decorator as Decorator, FuncDef as FuncDef, MypyFile as MypyFile, OverloadedFuncDef as OverloadedFuncDef, TypeInfo as TypeInfo, Var as Var
from mypy.options import Options as Options
from mypy.plugin import ClassDefContext as ClassDefContext
from mypy.semanal import SemanticAnalyzer as SemanticAnalyzer, apply_semantic_analyzer_patches as apply_semantic_analyzer_patches, remove_imported_names_from_symtable as remove_imported_names_from_symtable
from mypy.semanal_classprop import add_type_promotion as add_type_promotion, calculate_class_abstract_status as calculate_class_abstract_status, calculate_class_vars as calculate_class_vars, check_protocol_status as check_protocol_status
from mypy.semanal_infer import infer_decorator_signature_if_simple as infer_decorator_signature_if_simple
from mypy.semanal_shared import find_dataclass_transform_spec as find_dataclass_transform_spec
from mypy.semanal_typeargs import TypeArgumentAnalyzer as TypeArgumentAnalyzer
from mypy.server.aststrip import SavedAttributes as SavedAttributes
from mypy.util import is_typeshed_file as is_typeshed_file
from typing_extensions import Final, TypeAlias as _TypeAlias

Patches: _TypeAlias
MAX_ITERATIONS: Final[int]
CORE_WARMUP: Final[int]
core_modules: Final[Incomplete]

def semantic_analysis_for_scc(graph: Graph, scc: list[str], errors: Errors) -> None:
    """Perform semantic analysis for all modules in a SCC (import cycle).

    Assume that reachability analysis has already been performed.

    The scc will be processed roughly in the order the modules are included
    in the list.
    """
def cleanup_builtin_scc(state: State) -> None:
    """Remove imported names from builtins namespace.

    This way names imported from typing in builtins.pyi aren't available
    by default (without importing them). We can only do this after processing
    the whole SCC is finished, when the imported names aren't needed for
    processing builtins.pyi itself.
    """
def semantic_analysis_for_targets(state: State, nodes: list[FineGrainedDeferredNode], graph: Graph, saved_attrs: SavedAttributes) -> None:
    """Semantically analyze only selected nodes in a given module.

    This essentially mirrors the logic of semantic_analysis_for_scc()
    except that we process only some targets. This is used in fine grained
    incremental mode, when propagating an update.

    The saved_attrs are implicitly declared instance attributes (attributes
    defined on self) removed by AST stripper that may need to be reintroduced
    here.  They must be added before any methods are analyzed.
    """
def restore_saved_attrs(saved_attrs: SavedAttributes) -> None:
    """Restore instance variables removed during AST strip that haven't been added yet."""
def process_top_levels(graph: Graph, scc: list[str], patches: Patches) -> None: ...
def process_functions(graph: Graph, scc: list[str], patches: Patches) -> None: ...
def process_top_level_function(analyzer: SemanticAnalyzer, state: State, module: str, target: str, node: FuncDef | OverloadedFuncDef | Decorator, active_type: TypeInfo | None, patches: Patches) -> None:
    """Analyze single top-level function or method.

    Process the body of the function (including nested functions) again and again,
    until all names have been resolved (or iteration limit reached).
    """

TargetInfo: _TypeAlias

def get_all_leaf_targets(file: MypyFile) -> list[TargetInfo]:
    """Return all leaf targets in a symbol table (module-level and methods)."""
def semantic_analyze_target(target: str, module: str, state: State, node: MypyFile | FuncDef | OverloadedFuncDef | Decorator, active_type: TypeInfo | None, final_iteration: bool, patches: Patches) -> tuple[list[str], bool, bool]:
    """Semantically analyze a single target.

    Return tuple with these items:
    - list of deferred targets
    - was some definition incomplete (need to run another pass)
    - were any new names defined (or placeholders replaced)
    """
def check_type_arguments(graph: Graph, scc: list[str], errors: Errors) -> None: ...
def check_type_arguments_in_targets(targets: list[FineGrainedDeferredNode], state: State, errors: Errors) -> None:
    """Check type arguments against type variable bounds and restrictions.

    This mirrors the logic in check_type_arguments() except that we process only
    some targets. This is used in fine grained incremental mode.
    """
def apply_class_plugin_hooks(graph: Graph, scc: list[str], errors: Errors) -> None:
    """Apply class plugin hooks within a SCC.

    We run these after to the main semantic analysis so that the hooks
    don't need to deal with incomplete definitions such as placeholder
    types.

    Note that some hooks incorrectly run during the main semantic
    analysis pass, for historical reasons.
    """
def apply_hooks_to_class(self, module: str, info: TypeInfo, options: Options, file_node: MypyFile, errors: Errors) -> bool: ...
def calculate_class_properties(graph: Graph, scc: list[str], errors: Errors) -> None: ...
def check_blockers(graph: Graph, scc: list[str]) -> None: ...
