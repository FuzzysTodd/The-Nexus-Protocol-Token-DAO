from _typeshed import Incomplete
from mypy import message_registry as message_registry
from mypy.constant_fold import constant_fold_expr as constant_fold_expr
from mypy.errorcodes import ErrorCode as ErrorCode
from mypy.errors import Errors as Errors, report_internal_error as report_internal_error
from mypy.exprtotype import TypeTranslationError as TypeTranslationError, expr_to_unanalyzed_type as expr_to_unanalyzed_type
from mypy.messages import MessageBuilder as MessageBuilder, SUGGESTED_TEST_FIXTURES as SUGGESTED_TEST_FIXTURES, TYPES_FOR_UNIMPORTED_HINTS as TYPES_FOR_UNIMPORTED_HINTS, best_matches as best_matches, pretty_seq as pretty_seq
from mypy.mro import MroError as MroError, calculate_mro as calculate_mro
from mypy.nodes import ARG_NAMED as ARG_NAMED, ARG_POS as ARG_POS, ARG_STAR as ARG_STAR, ARG_STAR2 as ARG_STAR2, ArgKind as ArgKind, AssertStmt as AssertStmt, AssertTypeExpr as AssertTypeExpr, AssignmentExpr as AssignmentExpr, AssignmentStmt as AssignmentStmt, AwaitExpr as AwaitExpr, Block as Block, BreakStmt as BreakStmt, CONTRAVARIANT as CONTRAVARIANT, COVARIANT as COVARIANT, CallExpr as CallExpr, CastExpr as CastExpr, ClassDef as ClassDef, ComparisonExpr as ComparisonExpr, ConditionalExpr as ConditionalExpr, Context as Context, ContinueStmt as ContinueStmt, DataclassTransformSpec as DataclassTransformSpec, Decorator as Decorator, DelStmt as DelStmt, DictExpr as DictExpr, DictionaryComprehension as DictionaryComprehension, EllipsisExpr as EllipsisExpr, EnumCallExpr as EnumCallExpr, Expression as Expression, ExpressionStmt as ExpressionStmt, FakeExpression as FakeExpression, ForStmt as ForStmt, FuncBase as FuncBase, FuncDef as FuncDef, FuncItem as FuncItem, GDEF as GDEF, GeneratorExpr as GeneratorExpr, GlobalDecl as GlobalDecl, IMPLICITLY_ABSTRACT as IMPLICITLY_ABSTRACT, INVARIANT as INVARIANT, IS_ABSTRACT as IS_ABSTRACT, IfStmt as IfStmt, Import as Import, ImportAll as ImportAll, ImportBase as ImportBase, ImportFrom as ImportFrom, IndexExpr as IndexExpr, LDEF as LDEF, LambdaExpr as LambdaExpr, ListComprehension as ListComprehension, ListExpr as ListExpr, Lvalue as Lvalue, MDEF as MDEF, MatchStmt as MatchStmt, MemberExpr as MemberExpr, MypyFile as MypyFile, NOT_ABSTRACT as NOT_ABSTRACT, NameExpr as NameExpr, NamedTupleExpr as NamedTupleExpr, Node as Node, NonlocalDecl as NonlocalDecl, OpExpr as OpExpr, OperatorAssignmentStmt as OperatorAssignmentStmt, OverloadPart as OverloadPart, OverloadedFuncDef as OverloadedFuncDef, ParamSpecExpr as ParamSpecExpr, PassStmt as PassStmt, PlaceholderNode as PlaceholderNode, PromoteExpr as PromoteExpr, REVEAL_LOCALS as REVEAL_LOCALS, REVEAL_TYPE as REVEAL_TYPE, RUNTIME_PROTOCOL_DECOS as RUNTIME_PROTOCOL_DECOS, RaiseStmt as RaiseStmt, RefExpr as RefExpr, ReturnStmt as ReturnStmt, RevealExpr as RevealExpr, SetComprehension as SetComprehension, SetExpr as SetExpr, SliceExpr as SliceExpr, StarExpr as StarExpr, Statement as Statement, StrExpr as StrExpr, SuperExpr as SuperExpr, SymbolNode as SymbolNode, SymbolTable as SymbolTable, SymbolTableNode as SymbolTableNode, TempNode as TempNode, TryStmt as TryStmt, TupleExpr as TupleExpr, TypeAlias as TypeAlias, TypeAliasExpr as TypeAliasExpr, TypeApplication as TypeApplication, TypeInfo as TypeInfo, TypeVarExpr as TypeVarExpr, TypeVarLikeExpr as TypeVarLikeExpr, TypeVarTupleExpr as TypeVarTupleExpr, TypedDictExpr as TypedDictExpr, UnaryExpr as UnaryExpr, Var as Var, WhileStmt as WhileStmt, WithStmt as WithStmt, YieldExpr as YieldExpr, YieldFromExpr as YieldFromExpr, get_member_expr_fullname as get_member_expr_fullname, get_nongen_builtins as get_nongen_builtins, implicit_module_attrs as implicit_module_attrs, is_final_node as is_final_node, type_aliases as type_aliases, type_aliases_source_versions as type_aliases_source_versions, typing_extensions_aliases as typing_extensions_aliases
from mypy.options import Options as Options, TYPE_VAR_TUPLE as TYPE_VAR_TUPLE
from mypy.patterns import AsPattern as AsPattern, ClassPattern as ClassPattern, MappingPattern as MappingPattern, OrPattern as OrPattern, SequencePattern as SequencePattern, StarredPattern as StarredPattern, ValuePattern as ValuePattern
from mypy.plugin import ClassDefContext as ClassDefContext, DynamicClassDefContext as DynamicClassDefContext, Plugin as Plugin, SemanticAnalyzerPluginInterface as SemanticAnalyzerPluginInterface
from mypy.reachability import ALWAYS_FALSE as ALWAYS_FALSE, ALWAYS_TRUE as ALWAYS_TRUE, MYPY_FALSE as MYPY_FALSE, MYPY_TRUE as MYPY_TRUE, infer_condition_value as infer_condition_value, infer_reachability_of_if_statement as infer_reachability_of_if_statement, infer_reachability_of_match_statement as infer_reachability_of_match_statement
from mypy.scope import Scope as Scope
from mypy.semanal_enum import EnumCallAnalyzer as EnumCallAnalyzer
from mypy.semanal_namedtuple import NamedTupleAnalyzer as NamedTupleAnalyzer
from mypy.semanal_newtype import NewTypeAnalyzer as NewTypeAnalyzer
from mypy.semanal_shared import ALLOW_INCOMPATIBLE_OVERRIDE as ALLOW_INCOMPATIBLE_OVERRIDE, PRIORITY_FALLBACKS as PRIORITY_FALLBACKS, SemanticAnalyzerInterface as SemanticAnalyzerInterface, calculate_tuple_fallback as calculate_tuple_fallback, find_dataclass_transform_spec as find_dataclass_transform_spec, has_placeholder as has_placeholder, parse_bool as parse_bool, require_bool_literal_argument as require_bool_literal_argument
from mypy.semanal_typeddict import TypedDictAnalyzer as TypedDictAnalyzer
from mypy.tvar_scope import TypeVarLikeScope as TypeVarLikeScope
from mypy.typeanal import SELF_TYPE_NAMES as SELF_TYPE_NAMES, TypeAnalyser as TypeAnalyser, TypeVarLikeList as TypeVarLikeList, TypeVarLikeQuery as TypeVarLikeQuery, analyze_type_alias as analyze_type_alias, check_for_explicit_any as check_for_explicit_any, detect_diverging_alias as detect_diverging_alias, find_self_type as find_self_type, fix_instance_types as fix_instance_types, has_any_from_unimported_type as has_any_from_unimported_type, no_subscript_builtin_alias as no_subscript_builtin_alias, remove_dups as remove_dups, type_constructors as type_constructors
from mypy.typeops import function_type as function_type, get_type_vars as get_type_vars, try_getting_str_literals_from_type as try_getting_str_literals_from_type
from mypy.types import ASSERT_TYPE_NAMES as ASSERT_TYPE_NAMES, AnyType as AnyType, CallableType as CallableType, DATACLASS_TRANSFORM_NAMES as DATACLASS_TRANSFORM_NAMES, FINAL_DECORATOR_NAMES as FINAL_DECORATOR_NAMES, FINAL_TYPE_NAMES as FINAL_TYPE_NAMES, FunctionLike as FunctionLike, Instance as Instance, LiteralType as LiteralType, NEVER_NAMES as NEVER_NAMES, NoneType as NoneType, OVERLOAD_NAMES as OVERLOAD_NAMES, OVERRIDE_DECORATOR_NAMES as OVERRIDE_DECORATOR_NAMES, Overloaded as Overloaded, PROTOCOL_NAMES as PROTOCOL_NAMES, ParamSpecType as ParamSpecType, Parameters as Parameters, PlaceholderType as PlaceholderType, ProperType as ProperType, REVEAL_TYPE_NAMES as REVEAL_TYPE_NAMES, TPDICT_NAMES as TPDICT_NAMES, TYPED_NAMEDTUPLE_NAMES as TYPED_NAMEDTUPLE_NAMES, TYPE_ALIAS_NAMES as TYPE_ALIAS_NAMES, TrivialSyntheticTypeTranslator as TrivialSyntheticTypeTranslator, TupleType as TupleType, Type as Type, TypeAliasType as TypeAliasType, TypeOfAny as TypeOfAny, TypeType as TypeType, TypeVarLikeType as TypeVarLikeType, TypeVarTupleType as TypeVarTupleType, TypeVarType as TypeVarType, TypedDictType as TypedDictType, UnboundType as UnboundType, UnpackType as UnpackType, get_proper_type as get_proper_type, get_proper_types as get_proper_types, is_named_instance as is_named_instance
from mypy.types_utils import is_invalid_recursive_alias as is_invalid_recursive_alias, store_argument_type as store_argument_type
from mypy.typevars import fill_typevars as fill_typevars
from mypy.util import correct_relative_import as correct_relative_import, is_dunder as is_dunder, is_typeshed_file as is_typeshed_file, module_prefix as module_prefix, unmangle as unmangle, unnamed_function as unnamed_function
from mypy.visitor import NodeVisitor as NodeVisitor
from typing import Callable, Collection, Iterable, Iterator, TypeVar
from typing_extensions import Final, TypeAlias as _TypeAlias

T = TypeVar('T')
FUTURE_IMPORTS: Final[Incomplete]
CORE_BUILTIN_CLASSES: Final[Incomplete]
Tag: _TypeAlias

class SemanticAnalyzer(NodeVisitor[None], SemanticAnalyzerInterface, SemanticAnalyzerPluginInterface):
    """Semantically analyze parsed mypy files.

    The analyzer binds names and does various consistency checks for an
    AST. Note that type checking is performed as a separate pass.
    """
    __deletable__: Incomplete
    modules: dict[str, MypyFile]
    globals: SymbolTable
    global_decls: list[set[str]]
    nonlocal_decls: list[set[str]]
    locals: list[SymbolTable | None]
    is_comprehension_stack: list[bool]
    block_depth: list[int]
    type_stack: list[TypeInfo | None]
    tvar_scope: TypeVarLikeScope
    options: Options
    function_stack: list[FuncItem]
    progress: bool
    deferred: bool
    incomplete: bool
    missing_names: list[set[str]]
    patches: list[tuple[int, Callable[[], None]]]
    loop_depth: list[int]
    cur_mod_id: str
    imports: set[str]
    errors: Errors
    plugin: Plugin
    statement: Statement | None
    wrapped_coro_return_types: dict[FuncDef, Type]
    saved_locals: Incomplete
    incomplete_type_stack: Incomplete
    msg: Incomplete
    missing_modules: Incomplete
    incomplete_namespaces: Incomplete
    all_exports: Incomplete
    export_map: Incomplete
    recurse_into_functions: bool
    scope: Incomplete
    deferral_debug_context: Incomplete
    basic_type_applications: bool
    allow_unbound_tvars: bool
    def __init__(self, modules: dict[str, MypyFile], missing_modules: set[str], incomplete_namespaces: set[str], errors: Errors, plugin: Plugin) -> None:
        """Construct semantic analyzer.

        We reuse the same semantic analyzer instance across multiple modules.

        Args:
            modules: Global modules dictionary
            missing_modules: Modules that could not be imported encountered so far
            incomplete_namespaces: Namespaces that are being populated during semantic analysis
                (can contain modules and classes within the current SCC; mutated by the caller)
            errors: Report analysis errors using this instance
        """
    @property
    def type(self) -> TypeInfo | None: ...
    @property
    def is_stub_file(self) -> bool: ...
    @property
    def is_typeshed_stub_file(self) -> bool: ...
    @property
    def final_iteration(self) -> bool: ...
    def allow_unbound_tvars_set(self) -> Iterator[None]: ...
    def prepare_file(self, file_node: MypyFile) -> None:
        """Prepare a freshly parsed file for semantic analysis."""
    def prepare_typing_namespace(self, file_node: MypyFile, aliases: dict[str, str]) -> None:
        """Remove dummy alias definitions such as List = TypeAlias(object) from typing.

        They will be replaced with real aliases when corresponding targets are ready.
        """
    def prepare_builtins_namespace(self, file_node: MypyFile) -> None:
        """Add certain special-cased definitions to the builtins module.

        Some definitions are too special or fundamental to be processed
        normally from the AST.
        """
    def refresh_partial(self, node: MypyFile | FuncDef | OverloadedFuncDef, patches: list[tuple[int, Callable[[], None]]], final_iteration: bool, file_node: MypyFile, options: Options, active_type: TypeInfo | None = None) -> None:
        """Refresh a stale target in fine-grained incremental mode."""
    def refresh_top_level(self, file_node: MypyFile) -> None:
        """Reanalyze a stale module top-level in fine-grained incremental mode."""
    def add_implicit_module_attrs(self, file_node: MypyFile) -> None:
        """Manually add implicit definitions of module '__name__' etc."""
    def add_builtin_aliases(self, tree: MypyFile) -> None:
        """Add builtin type aliases to typing module.

        For historical reasons, the aliases like `List = list` are not defined
        in typeshed stubs for typing module. Instead we need to manually add the
        corresponding nodes on the fly. We explicitly mark these aliases as normalized,
        so that a user can write `typing.List[int]`.
        """
    def add_typing_extension_aliases(self, tree: MypyFile) -> None:
        """Typing extensions module does contain some type aliases.

        We need to analyze them as such, because in typeshed
        they are just defined as `_Alias()` call.
        Which is not supported natively.
        """
    def create_alias(self, tree: MypyFile, target_name: str, alias: str, name: str) -> None: ...
    def adjust_public_exports(self) -> None:
        """Adjust the module visibility of globals due to __all__."""
    cur_mod_node: Incomplete
    named_tuple_analyzer: Incomplete
    typed_dict_analyzer: Incomplete
    enum_call_analyzer: Incomplete
    newtype_analyzer: Incomplete
    num_incomplete_refs: int
    def file_context(self, file_node: MypyFile, options: Options, active_type: TypeInfo | None = None) -> Iterator[None]:
        """Configure analyzer for analyzing targets within a file/class.

        Args:
            file_node: target file
            options: options specific to the file
            active_type: must be the surrounding class to analyze method targets
        """
    def visit_func_def(self, defn: FuncDef) -> None: ...
    def analyze_func_def(self, defn: FuncDef) -> None: ...
    def remove_unpack_kwargs(self, defn: FuncDef, typ: CallableType) -> CallableType: ...
    def prepare_method_signature(self, func: FuncDef, info: TypeInfo, has_self_type: bool) -> None:
        """Check basic signature validity and tweak annotation of self/cls argument."""
    def is_expected_self_type(self, typ: Type, is_classmethod: bool) -> bool:
        """Does this (analyzed or not) type represent the expected Self type for a method?"""
    def set_original_def(self, previous: Node | None, new: FuncDef | Decorator) -> bool:
        """If 'new' conditionally redefine 'previous', set 'previous' as original

        We reject straight redefinitions of functions, as they are usually
        a programming error. For example:

          def f(): ...
          def f(): ...  # Error: 'f' redefined
        """
    def update_function_type_variables(self, fun_type: CallableType, defn: FuncItem) -> bool:
        """Make any type variables in the signature of defn explicit.

        Update the signature of defn to contain type variable definitions
        if defn is generic. Return True, if the signature contains typing.Self
        type, or False otherwise.
        """
    def setup_self_type(self) -> None:
        """Setup a (shared) Self type variable for current class.

        We intentionally don't add it to the class symbol table,
        so it can be accessed only by mypy and will not cause
        clashes with user defined names.
        """
    def visit_overloaded_func_def(self, defn: OverloadedFuncDef) -> None: ...
    def analyze_overloaded_func_def(self, defn: OverloadedFuncDef) -> None: ...
    def process_overload_impl(self, defn: OverloadedFuncDef) -> None:
        """Set flags for an overload implementation.

        Currently, this checks for a trivial body in protocols classes,
        where it makes the method implicitly abstract.
        """
    def analyze_overload_sigs_and_impl(self, defn: OverloadedFuncDef) -> tuple[list[CallableType], OverloadPart | None, list[int]]:
        """Find overload signatures, the implementation, and items with missing @overload.

        Assume that the first was already analyzed. As a side effect:
        analyzes remaining items and updates 'is_overload' flags.
        """
    def handle_missing_overload_decorators(self, defn: OverloadedFuncDef, non_overload_indexes: list[int], some_overload_decorators: bool) -> None:
        """Generate errors for overload items without @overload.

        Side effect: remote non-overload items.
        """
    def handle_missing_overload_implementation(self, defn: OverloadedFuncDef) -> None:
        """Generate error about missing overload implementation (only if needed)."""
    def process_final_in_overload(self, defn: OverloadedFuncDef) -> None:
        """Detect the @final status of an overloaded function (and perform checks)."""
    def process_static_or_class_method_in_overload(self, defn: OverloadedFuncDef) -> None: ...
    def analyze_property_with_multi_part_definition(self, defn: OverloadedFuncDef) -> None:
        """Analyze a property defined using multiple methods (e.g., using @x.setter).

        Assume that the first method (@property) has already been analyzed.
        """
    def add_function_to_symbol_table(self, func: FuncDef | OverloadedFuncDef) -> None: ...
    def analyze_arg_initializers(self, defn: FuncItem) -> None: ...
    def analyze_function_body(self, defn: FuncItem) -> None: ...
    def check_classvar_in_signature(self, typ: ProperType) -> None: ...
    def check_function_signature(self, fdef: FuncItem) -> None: ...
    def check_paramspec_definition(self, defn: FuncDef) -> None: ...
    def visit_decorator(self, dec: Decorator) -> None: ...
    def check_decorated_function_is_method(self, decorator: str, context: Context) -> None: ...
    def visit_class_def(self, defn: ClassDef) -> None: ...
    def analyze_class(self, defn: ClassDef) -> None: ...
    def setup_type_vars(self, defn: ClassDef, tvar_defs: list[TypeVarLikeType]) -> None: ...
    def setup_alias_type_vars(self, defn: ClassDef) -> None: ...
    def is_core_builtin_class(self, defn: ClassDef) -> bool: ...
    def analyze_class_body_common(self, defn: ClassDef) -> None:
        """Parts of class body analysis that are common to all kinds of class defs."""
    def analyze_typeddict_classdef(self, defn: ClassDef) -> bool: ...
    def analyze_namedtuple_classdef(self, defn: ClassDef, tvar_defs: list[TypeVarLikeType]) -> bool:
        """Check if this class can define a named tuple."""
    def apply_class_plugin_hooks(self, defn: ClassDef) -> None:
        """Apply a plugin hook that may infer a more precise definition for a class."""
    def get_fullname_for_hook(self, expr: Expression) -> str | None: ...
    def analyze_class_keywords(self, defn: ClassDef) -> None: ...
    def enter_class(self, info: TypeInfo) -> None: ...
    def leave_class(self) -> None:
        """Restore analyzer state."""
    def analyze_class_decorator(self, defn: ClassDef, decorator: Expression) -> None: ...
    def clean_up_bases_and_infer_type_variables(self, defn: ClassDef, base_type_exprs: list[Expression], context: Context) -> tuple[list[Expression], list[TypeVarLikeType], bool]:
        """Remove extra base classes such as Generic and infer type vars.

        For example, consider this class:

          class Foo(Bar, Generic[T]): ...

        Now we will remove Generic[T] from bases of Foo and infer that the
        type variable 'T' is a type argument of Foo.

        Note that this is performed *before* semantic analysis.

        Returns (remaining base expressions, inferred type variables, is protocol).
        """
    def analyze_class_typevar_declaration(self, base: Type) -> tuple[TypeVarLikeList, bool] | None:
        """Analyze type variables declared using Generic[...] or Protocol[...].

        Args:
            base: Non-analyzed base class

        Return None if the base class does not declare type variables. Otherwise,
        return the type variables.
        """
    def analyze_unbound_tvar(self, t: Type) -> tuple[str, TypeVarLikeExpr] | None: ...
    def get_all_bases_tvars(self, base_type_exprs: list[Expression], removed: list[int]) -> TypeVarLikeList:
        """Return all type variable references in bases."""
    def get_and_bind_all_tvars(self, type_exprs: list[Expression]) -> list[TypeVarLikeType]:
        """Return all type variable references in item type expressions.

        This is a helper for generic TypedDicts and NamedTuples. Essentially it is
        a simplified version of the logic we use for ClassDef bases. We duplicate
        some amount of code, because it is hard to refactor common pieces.
        """
    def prepare_class_def(self, defn: ClassDef, info: TypeInfo | None = None, custom_names: bool = False) -> None:
        """Prepare for the analysis of a class definition.

        Create an empty TypeInfo and store it in a symbol table, or if the 'info'
        argument is provided, store it instead (used for magic type definitions).
        """
    def make_empty_type_info(self, defn: ClassDef) -> TypeInfo: ...
    def get_name_repr_of_expr(self, expr: Expression) -> str | None:
        """Try finding a short simplified textual representation of a base class expression."""
    def analyze_base_classes(self, base_type_exprs: list[Expression]) -> tuple[list[tuple[ProperType, Expression]], bool] | None:
        """Analyze base class types.

        Return None if some definition was incomplete. Otherwise, return a tuple
        with these items:

         * List of (analyzed type, original expression) tuples
         * Boolean indicating whether one of the bases had a semantic analysis error
        """
    def configure_base_classes(self, defn: ClassDef, bases: list[tuple[ProperType, Expression]]) -> None:
        """Set up base classes.

        This computes several attributes on the corresponding TypeInfo defn.info
        related to the base classes: defn.info.bases, defn.info.mro, and
        miscellaneous others (at least tuple_type, fallback_to_any, and is_enum.)
        """
    def configure_tuple_base_class(self, defn: ClassDef, base: TupleType) -> Instance: ...
    def set_dummy_mro(self, info: TypeInfo) -> None: ...
    def set_any_mro(self, info: TypeInfo) -> None: ...
    def calculate_class_mro(self, defn: ClassDef, obj_type: Callable[[], Instance] | None = None) -> None:
        """Calculate method resolution order for a class.

        `obj_type` exists just to fill in empty base class list in case of an error.
        """
    def infer_metaclass_and_bases_from_compat_helpers(self, defn: ClassDef) -> None:
        """Lookup for special metaclass declarations, and update defn fields accordingly.

        * six.with_metaclass(M, B1, B2, ...)
        * @six.add_metaclass(M)
        * future.utils.with_metaclass(M, B1, B2, ...)
        * past.utils.with_metaclass(M, B1, B2, ...)
        """
    def verify_base_classes(self, defn: ClassDef) -> bool: ...
    def verify_duplicate_base_classes(self, defn: ClassDef) -> bool: ...
    def is_base_class(self, t: TypeInfo, s: TypeInfo) -> bool:
        """Determine if t is a base class of s (but do not use mro)."""
    def get_declared_metaclass(self, name: str, metaclass_expr: Expression | None) -> tuple[Instance | None, bool, bool]:
        """Get declared metaclass from metaclass expression.

        Returns a tuple of three values:
          * A metaclass instance or None
          * A boolean indicating whether we should defer
          * A boolean indicating whether we should set metaclass Any fallback
            (either for Any metaclass or invalid/dynamic metaclass).

        The two boolean flags can only be True if instance is None.
        """
    def recalculate_metaclass(self, defn: ClassDef, declared_metaclass: Instance | None) -> None: ...
    def visit_import(self, i: Import) -> None: ...
    def visit_import_from(self, imp: ImportFrom) -> None: ...
    def process_imported_symbol(self, node: SymbolTableNode, module_id: str, id: str, imported_id: str, fullname: str, module_public: bool, context: ImportBase) -> None: ...
    def report_missing_module_attribute(self, import_id: str, source_id: str, imported_id: str, module_public: bool, module_hidden: bool, context: Node, add_unknown_imported_symbol: bool = True) -> None: ...
    def process_import_over_existing_name(self, imported_id: str, existing_symbol: SymbolTableNode, module_symbol: SymbolTableNode, import_node: ImportBase) -> bool: ...
    def correct_relative_import(self, node: ImportFrom | ImportAll) -> str: ...
    def visit_import_all(self, i: ImportAll) -> None: ...
    def visit_assignment_expr(self, s: AssignmentExpr) -> None: ...
    def check_valid_comprehension(self, s: AssignmentExpr) -> bool:
        """Check that assignment expression is not nested within comprehension at class scope.

        class C:
            [(j := i) for i in [1, 2, 3]]
        is a syntax error that is not enforced by Python parser, but at later steps.
        """
    def visit_assignment_stmt(self, s: AssignmentStmt) -> None: ...
    def analyze_identity_global_assignment(self, s: AssignmentStmt) -> bool:
        """Special case 'X = X' in global scope.

        This allows supporting some important use cases.

        Return true if special casing was applied.
        """
    def should_wait_rhs(self, rv: Expression) -> bool:
        """Can we already classify this r.h.s. of an assignment or should we wait?

        This returns True if we don't have enough information to decide whether
        an assignment is just a normal variable definition or a special form.
        Always return False if this is a final iteration. This will typically cause
        the lvalue to be classified as a variable plus emit an error.
        """
    def can_be_type_alias(self, rv: Expression, allow_none: bool = False) -> bool:
        """Is this a valid r.h.s. for an alias definition?

        Note: this function should be only called for expressions where self.should_wait_rhs()
        returns False.
        """
    def can_possibly_be_type_form(self, s: AssignmentStmt) -> bool:
        """Like can_be_type_alias(), but simpler and doesn't require fully analyzed rvalue.

        Instead, use lvalues/annotations structure to figure out whether this can potentially be
        a type alias definition, NamedTuple, or TypedDict. Another difference from above function
        is that we are only interested IndexExpr, CallExpr and OpExpr rvalues, since only those
        can be potentially recursive (things like `A = A` are never valid).
        """
    def is_type_ref(self, rv: Expression, bare: bool = False) -> bool:
        """Does this expression refer to a type?

        This includes:
          * Special forms, like Any or Union
          * Classes (except subscripted enums)
          * Other type aliases
          * PlaceholderNodes with becomes_typeinfo=True (these can be not ready class
            definitions, and not ready aliases).

        If bare is True, this is not a base of an index expression, so some special
        forms are not valid (like a bare Union).

        Note: This method should be only used in context of a type alias definition.
        This method can only return True for RefExprs, to check if C[int] is a valid
        target for type alias call this method on expr.base (i.e. on C in C[int]).
        See also can_be_type_alias().
        """
    def is_none_alias(self, node: Expression) -> bool:
        """Is this a r.h.s. for a None alias?

        We special case the assignments like Void = type(None), to allow using
        Void in type annotations.
        """
    def record_special_form_lvalue(self, s: AssignmentStmt) -> None:
        """Record minimal necessary information about l.h.s. of a special form.

        This exists mostly for compatibility with the old semantic analyzer.
        """
    def analyze_enum_assign(self, s: AssignmentStmt) -> bool:
        """Check if s defines an Enum."""
    def analyze_namedtuple_assign(self, s: AssignmentStmt) -> bool:
        """Check if s defines a namedtuple."""
    def analyze_typeddict_assign(self, s: AssignmentStmt) -> bool:
        """Check if s defines a typed dict."""
    def analyze_lvalues(self, s: AssignmentStmt) -> None: ...
    def apply_dynamic_class_hook(self, s: AssignmentStmt) -> None: ...
    def unwrap_final(self, s: AssignmentStmt) -> bool:
        """Strip Final[...] if present in an assignment.

        This is done to invoke type inference during type checking phase for this
        assignment. Also, Final[...] doesn't affect type in any way -- it is rather an
        access qualifier for given `Var`.

        Also perform various consistency checks.

        Returns True if Final[...] was present.
        """
    def check_final_implicit_def(self, s: AssignmentStmt) -> None:
        """Do basic checks for final declaration on self in __init__.

        Additional re-definition checks are performed by `analyze_lvalue`.
        """
    def store_final_status(self, s: AssignmentStmt) -> None:
        """If this is a locally valid final declaration, set the corresponding flag on `Var`."""
    def flatten_lvalues(self, lvalues: list[Expression]) -> list[Expression]: ...
    def process_type_annotation(self, s: AssignmentStmt) -> None:
        """Analyze type annotation or infer simple literal type."""
    def is_annotated_protocol_member(self, s: AssignmentStmt) -> bool:
        """Check whether a protocol member is annotated.

        There are some exceptions that can be left unannotated, like ``__slots__``."""
    def analyze_simple_literal_type(self, rvalue: Expression, is_final: bool) -> Type | None:
        '''Return builtins.int if rvalue is an int literal, etc.

        If this is a \'Final\' context, we return "Literal[...]" instead.
        '''
    def analyze_alias(self, name: str, rvalue: Expression, allow_placeholder: bool = False) -> tuple[Type | None, list[TypeVarLikeType], set[str], list[str]]:
        """Check if 'rvalue' is a valid type allowed for aliasing (e.g. not a type variable).

        If yes, return the corresponding type, a list of
        qualified type variable names for generic aliases, a set of names the alias depends on,
        and a list of type variables if the alias is generic.
        A schematic example for the dependencies:
            A = int
            B = str
            analyze_alias(Dict[A, B])[2] == {'__main__.A', '__main__.B'}
        """
    def is_pep_613(self, s: AssignmentStmt) -> bool: ...
    def check_and_set_up_type_alias(self, s: AssignmentStmt) -> bool:
        """Check if assignment creates a type alias and set it up as needed.

        Return True if it is a type alias (even if the target is not ready),
        or False otherwise.

        Note: the resulting types for subscripted (including generic) aliases
        are also stored in rvalue.analyzed.
        """
    def disable_invalid_recursive_aliases(self, s: AssignmentStmt, current_node: TypeAlias) -> None:
        """Prohibit and fix recursive type aliases that are invalid/unsupported."""
    def analyze_lvalue(self, lval: Lvalue, nested: bool = False, explicit_type: bool = False, is_final: bool = False, escape_comprehensions: bool = False, has_explicit_value: bool = False) -> None:
        """Analyze an lvalue or assignment target.

        Args:
            lval: The target lvalue
            nested: If true, the lvalue is within a tuple or list lvalue expression
            explicit_type: Assignment has type annotation
            escape_comprehensions: If we are inside a comprehension, set the variable
                in the enclosing scope instead. This implements
                https://www.python.org/dev/peps/pep-0572/#scope-of-the-target
        """
    def analyze_name_lvalue(self, lvalue: NameExpr, explicit_type: bool, is_final: bool, escape_comprehensions: bool, has_explicit_value: bool) -> None:
        '''Analyze an lvalue that targets a name expression.

        Arguments are similar to "analyze_lvalue".
        '''
    def is_final_redefinition(self, kind: int, name: str) -> bool: ...
    def is_alias_for_final_name(self, name: str) -> bool: ...
    def make_name_lvalue_var(self, lvalue: NameExpr, kind: int, inferred: bool, has_explicit_value: bool) -> Var:
        """Return a Var node for an lvalue that is a name expression."""
    def make_name_lvalue_point_to_existing_def(self, lval: NameExpr, explicit_type: bool, is_final: bool) -> None:
        '''Update an lvalue to point to existing definition in the same scope.

        Arguments are similar to "analyze_lvalue".

        Assume that an existing name exists.
        '''
    def analyze_tuple_or_list_lvalue(self, lval: TupleExpr, explicit_type: bool = False) -> None:
        """Analyze an lvalue or assignment target that is a list or tuple."""
    def analyze_member_lvalue(self, lval: MemberExpr, explicit_type: bool, is_final: bool, has_explicit_value: bool) -> None:
        """Analyze lvalue that is a member expression.

        Arguments:
            lval: The target lvalue
            explicit_type: Assignment has type annotation
            is_final: Is the target final
        """
    def is_self_member_ref(self, memberexpr: MemberExpr) -> bool:
        """Does memberexpr to refer to an attribute of self?"""
    def check_lvalue_validity(self, node: Expression | SymbolNode | None, ctx: Context) -> None: ...
    def store_declared_types(self, lvalue: Lvalue, typ: Type) -> None: ...
    def process_typevar_declaration(self, s: AssignmentStmt) -> bool:
        """Check if s declares a TypeVar; it yes, store it in symbol table.

        Return True if this looks like a type variable declaration (but maybe
        with errors), otherwise return False.
        """
    def check_typevarlike_name(self, call: CallExpr, name: str, context: Context) -> bool:
        """Checks that the name of a TypeVar or ParamSpec matches its variable."""
    def get_typevarlike_declaration(self, s: AssignmentStmt, typevarlike_types: tuple[str, ...]) -> CallExpr | None:
        """Returns the call expression if `s` is a declaration of `typevarlike_type`
        (TypeVar or ParamSpec), or None otherwise.
        """
    def process_typevar_parameters(self, args: list[Expression], names: list[str | None], kinds: list[ArgKind], num_values: int, context: Context) -> tuple[int, Type, Type] | None: ...
    def get_typevarlike_argument(self, typevarlike_name: str, param_name: str, param_value: Expression, context: Context, *, allow_unbound_tvars: bool = False, allow_param_spec_literals: bool = False, report_invalid_typevar_arg: bool = True) -> ProperType | None: ...
    def extract_typevarlike_name(self, s: AssignmentStmt, call: CallExpr) -> str | None: ...
    def process_paramspec_declaration(self, s: AssignmentStmt) -> bool:
        """Checks if s declares a ParamSpec; if yes, store it in symbol table.

        Return True if this looks like a ParamSpec (maybe with errors), otherwise return False.

        In the future, ParamSpec may accept bounds and variance arguments, in which
        case more aggressive sharing of code with process_typevar_declaration should be pursued.
        """
    def process_typevartuple_declaration(self, s: AssignmentStmt) -> bool:
        """Checks if s declares a TypeVarTuple; if yes, store it in symbol table.

        Return True if this looks like a TypeVarTuple (maybe with errors), otherwise return False.
        """
    def basic_new_typeinfo(self, name: str, basetype_or_fallback: Instance, line: int) -> TypeInfo: ...
    def analyze_value_types(self, items: list[Expression]) -> list[Type]:
        """Analyze types from values expressions in type variable definition."""
    def check_classvar(self, s: AssignmentStmt) -> None:
        """Check if assignment defines a class variable."""
    def is_classvar(self, typ: Type) -> bool: ...
    def is_final_type(self, typ: Type | None) -> bool: ...
    def fail_invalid_classvar(self, context: Context) -> None: ...
    def process_module_assignment(self, lvals: list[Lvalue], rval: Expression, ctx: AssignmentStmt) -> None:
        """Propagate module references across assignments.

        Recursively handles the simple form of iterable unpacking; doesn't
        handle advanced unpacking with *rest, dictionary unpacking, etc.

        In an expression like x = y = z, z is the rval and lvals will be [x,
        y].

        """
    def process__all__(self, s: AssignmentStmt) -> None:
        """Export names if argument is a __all__ assignment."""
    def process__deletable__(self, s: AssignmentStmt) -> None: ...
    def process__slots__(self, s: AssignmentStmt) -> None:
        """
        Processing ``__slots__`` if defined in type.

        See: https://docs.python.org/3/reference/datamodel.html#slots
        """
    def visit_block(self, b: Block) -> None: ...
    def visit_block_maybe(self, b: Block | None) -> None: ...
    def visit_expression_stmt(self, s: ExpressionStmt) -> None: ...
    def visit_return_stmt(self, s: ReturnStmt) -> None: ...
    def visit_raise_stmt(self, s: RaiseStmt) -> None: ...
    def visit_assert_stmt(self, s: AssertStmt) -> None: ...
    def visit_operator_assignment_stmt(self, s: OperatorAssignmentStmt) -> None: ...
    def visit_while_stmt(self, s: WhileStmt) -> None: ...
    def visit_for_stmt(self, s: ForStmt) -> None: ...
    def visit_break_stmt(self, s: BreakStmt) -> None: ...
    def visit_continue_stmt(self, s: ContinueStmt) -> None: ...
    def visit_if_stmt(self, s: IfStmt) -> None: ...
    def visit_try_stmt(self, s: TryStmt) -> None: ...
    def analyze_try_stmt(self, s: TryStmt, visitor: NodeVisitor[None]) -> None: ...
    def visit_with_stmt(self, s: WithStmt) -> None: ...
    def visit_del_stmt(self, s: DelStmt) -> None: ...
    def is_valid_del_target(self, s: Expression) -> bool: ...
    def visit_global_decl(self, g: GlobalDecl) -> None: ...
    def visit_nonlocal_decl(self, d: NonlocalDecl) -> None: ...
    def visit_match_stmt(self, s: MatchStmt) -> None: ...
    def visit_name_expr(self, expr: NameExpr) -> None: ...
    def bind_name_expr(self, expr: NameExpr, sym: SymbolTableNode) -> None:
        """Bind name expression to a symbol table node."""
    def visit_super_expr(self, expr: SuperExpr) -> None: ...
    def visit_tuple_expr(self, expr: TupleExpr) -> None: ...
    def visit_list_expr(self, expr: ListExpr) -> None: ...
    def visit_set_expr(self, expr: SetExpr) -> None: ...
    def visit_dict_expr(self, expr: DictExpr) -> None: ...
    def visit_star_expr(self, expr: StarExpr) -> None: ...
    def visit_yield_from_expr(self, e: YieldFromExpr) -> None: ...
    def visit_call_expr(self, expr: CallExpr) -> None:
        """Analyze a call expression.

        Some call expressions are recognized as special forms, including
        cast(...).
        """
    def translate_dict_call(self, call: CallExpr) -> DictExpr | None:
        """Translate 'dict(x=y, ...)' to {'x': y, ...} and 'dict()' to {}.

        For other variants of dict(...), return None.
        """
    def check_fixed_args(self, expr: CallExpr, numargs: int, name: str) -> bool:
        """Verify that expr has specified number of positional args.

        Return True if the arguments are valid.
        """
    def visit_member_expr(self, expr: MemberExpr) -> None: ...
    def visit_op_expr(self, expr: OpExpr) -> None: ...
    def visit_comparison_expr(self, expr: ComparisonExpr) -> None: ...
    def visit_unary_expr(self, expr: UnaryExpr) -> None: ...
    def visit_index_expr(self, expr: IndexExpr) -> None: ...
    def analyze_type_application(self, expr: IndexExpr) -> None:
        """Analyze special form -- type application (either direct or via type aliasing)."""
    def analyze_type_application_args(self, expr: IndexExpr) -> list[Type] | None:
        """Analyze type arguments (index) in a type application.

        Return None if anything was incomplete.
        """
    def visit_slice_expr(self, expr: SliceExpr) -> None: ...
    def visit_cast_expr(self, expr: CastExpr) -> None: ...
    def visit_assert_type_expr(self, expr: AssertTypeExpr) -> None: ...
    def visit_reveal_expr(self, expr: RevealExpr) -> None: ...
    def visit_type_application(self, expr: TypeApplication) -> None: ...
    def visit_list_comprehension(self, expr: ListComprehension) -> None: ...
    def visit_set_comprehension(self, expr: SetComprehension) -> None: ...
    def visit_dictionary_comprehension(self, expr: DictionaryComprehension) -> None: ...
    def visit_generator_expr(self, expr: GeneratorExpr) -> None: ...
    def analyze_comp_for(self, expr: GeneratorExpr | DictionaryComprehension) -> None:
        """Analyses the 'comp_for' part of comprehensions (part 1).

        That is the part after 'for' in (x for x in l if p). This analyzes
        variables and conditions which are analyzed in a local scope.
        """
    def analyze_comp_for_2(self, expr: GeneratorExpr | DictionaryComprehension) -> None:
        """Analyses the 'comp_for' part of comprehensions (part 2).

        That is the part after 'for' in (x for x in l if p). This analyzes
        the 'l' part which is analyzed in the surrounding scope.
        """
    def visit_lambda_expr(self, expr: LambdaExpr) -> None: ...
    def visit_conditional_expr(self, expr: ConditionalExpr) -> None: ...
    def visit__promote_expr(self, expr: PromoteExpr) -> None: ...
    def visit_yield_expr(self, e: YieldExpr) -> None: ...
    def visit_await_expr(self, expr: AwaitExpr) -> None: ...
    def visit_as_pattern(self, p: AsPattern) -> None: ...
    def visit_or_pattern(self, p: OrPattern) -> None: ...
    def visit_value_pattern(self, p: ValuePattern) -> None: ...
    def visit_sequence_pattern(self, p: SequencePattern) -> None: ...
    def visit_starred_pattern(self, p: StarredPattern) -> None: ...
    def visit_mapping_pattern(self, p: MappingPattern) -> None: ...
    def visit_class_pattern(self, p: ClassPattern) -> None: ...
    def lookup(self, name: str, ctx: Context, suppress_errors: bool = False) -> SymbolTableNode | None:
        """Look up an unqualified (no dots) name in all active namespaces.

        Note that the result may contain a PlaceholderNode. The caller may
        want to defer in that case.

        Generate an error if the name is not defined unless suppress_errors
        is true or the current namespace is incomplete. In the latter case
        defer.
        """
    def is_active_symbol_in_class_body(self, node: SymbolNode | None) -> bool:
        """Can a symbol defined in class body accessed at current statement?

        Only allow access to class attributes textually after
        the definition, so that it's possible to fall back to the
        outer scope. Example:

            class X: ...

            class C:
                X = X  # Initializer refers to outer scope

        Nested classes are an exception, since we want to support
        arbitrary forward references in type annotations. Also, we
        allow forward references to type aliases to support recursive
        types.
        """
    def is_textually_before_statement(self, node: SymbolNode) -> bool:
        """Check if a node is defined textually before the current statement

        Note that decorated functions' line number are the same as
        the top decorator.
        """
    def is_overloaded_item(self, node: SymbolNode, statement: Statement) -> bool:
        """Check whether the function belongs to the overloaded variants"""
    def is_defined_in_current_module(self, fullname: str | None) -> bool: ...
    def lookup_qualified(self, name: str, ctx: Context, suppress_errors: bool = False) -> SymbolTableNode | None:
        """Lookup a qualified name in all activate namespaces.

        Note that the result may contain a PlaceholderNode. The caller may
        want to defer in that case.

        Generate an error if the name is not defined unless suppress_errors
        is true or the current namespace is incomplete. In the latter case
        defer.
        """
    def lookup_type_node(self, expr: Expression) -> SymbolTableNode | None: ...
    def get_module_symbol(self, node: MypyFile, name: str) -> SymbolTableNode | None:
        """Look up a symbol from a module.

        Return None if no matching symbol could be bound.
        """
    def is_missing_module(self, module: str) -> bool: ...
    def implicit_symbol(self, sym: SymbolTableNode, name: str, parts: list[str], source_type: AnyType) -> SymbolTableNode:
        """Create symbol for a qualified name reference through Any type."""
    def create_getattr_var(self, getattr_defn: SymbolTableNode, name: str, fullname: str) -> Var | None:
        """Create a dummy variable using module-level __getattr__ return type.

        If not possible, return None.

        Note that multiple Var nodes can be created for a single name. We
        can use the from_module_getattr and the fullname attributes to
        check if two dummy Var nodes refer to the same thing. Reusing Var
        nodes would require non-local mutable state, which we prefer to
        avoid.
        """
    def lookup_fully_qualified(self, fullname: str) -> SymbolTableNode: ...
    def lookup_fully_qualified_or_none(self, fullname: str) -> SymbolTableNode | None:
        """Lookup a fully qualified name that refers to a module-level definition.

        Don't assume that the name is defined. This happens in the global namespace --
        the local module namespace is ignored. This does not dereference indirect
        refs.

        Note that this can't be used for names nested in class namespaces.
        """
    def object_type(self) -> Instance: ...
    def str_type(self) -> Instance: ...
    def named_type(self, fullname: str, args: list[Type] | None = None) -> Instance: ...
    def named_type_or_none(self, fullname: str, args: list[Type] | None = None) -> Instance | None: ...
    def builtin_type(self, fully_qualified_name: str) -> Instance:
        """Legacy function -- use named_type() instead."""
    def lookup_current_scope(self, name: str) -> SymbolTableNode | None: ...
    def add_symbol(self, name: str, node: SymbolNode, context: Context, module_public: bool = True, module_hidden: bool = False, can_defer: bool = True, escape_comprehensions: bool = False) -> bool:
        """Add symbol to the currently active symbol table.

        Generally additions to symbol table should go through this method or
        one of the methods below so that kinds, redefinitions, conditional
        definitions, and skipped names are handled consistently.

        Return True if we actually added the symbol, or False if we refused to do so
        (because something is not ready).

        If can_defer is True, defer current target if adding a placeholder.
        """
    def add_symbol_skip_local(self, name: str, node: SymbolNode) -> None:
        """Same as above, but skipping the local namespace.

        This doesn't check for previous definition and is only used
        for serialization of method-level classes.

        Classes defined within methods can be exposed through an
        attribute type, but method-level symbol tables aren't serialized.
        This method can be used to add such classes to an enclosing,
        serialized symbol table.
        """
    def add_symbol_table_node(self, name: str, symbol: SymbolTableNode, context: Context | None = None, can_defer: bool = True, escape_comprehensions: bool = False) -> bool:
        """Add symbol table node to the currently active symbol table.

        Return True if we actually added the symbol, or False if we refused
        to do so (because something is not ready or it was a no-op).

        Generate an error if there is an invalid redefinition.

        If context is None, unconditionally add node, since we can't report
        an error. Note that this is used by plugins to forcibly replace nodes!

        TODO: Prevent plugins from replacing nodes, as it could cause problems?

        Args:
            name: short name of symbol
            symbol: Node to add
            can_defer: if True, defer current target if adding a placeholder
            context: error context (see above about None value)
        """
    def add_redefinition(self, names: SymbolTable, name: str, symbol: SymbolTableNode) -> None:
        """Add a symbol table node that reflects a redefinition as a function or a class.

        Redefinitions need to be added to the symbol table so that they can be found
        through AST traversal, but they have dummy names of form 'name-redefinition[N]',
        where N ranges over 2, 3, ... (omitted for the first redefinition).

        Note: we always store redefinitions independently of whether they are valid or not
        (so they will be semantically analyzed), the caller should give an error for invalid
        redefinitions (such as e.g. variable redefined as a class).
        """
    def add_local(self, node: Var | FuncDef | OverloadedFuncDef, context: Context) -> None:
        """Add local variable or function."""
    def add_imported_symbol(self, name: str, node: SymbolTableNode, context: ImportBase, module_public: bool, module_hidden: bool) -> None:
        """Add an alias to an existing symbol through import."""
    def add_unknown_imported_symbol(self, name: str, context: Context, target_name: str | None, module_public: bool, module_hidden: bool) -> None:
        """Add symbol that we don't know what it points to because resolving an import failed.

        This can happen if a module is missing, or it is present, but doesn't have
        the imported attribute. The `target_name` is the name of symbol in the namespace
        it is imported from. For example, for 'from mod import x as y' the target_name is
        'mod.x'. This is currently used only to track logical dependencies.
        """
    def tvar_scope_frame(self, frame: TypeVarLikeScope) -> Iterator[None]: ...
    def defer(self, debug_context: Context | None = None, force_progress: bool = False) -> None:
        """Defer current analysis target to be analyzed again.

        This must be called if something in the current target is
        incomplete or has a placeholder node. However, this must *not*
        be called during the final analysis iteration! Instead, an error
        should be generated. Often 'process_placeholder' is a good
        way to either defer or generate an error.

        NOTE: Some methods, such as 'anal_type', 'mark_incomplete' and
              'record_incomplete_ref', call this implicitly, or when needed.
              They are usually preferable to a direct defer() call.
        """
    def track_incomplete_refs(self) -> Tag:
        """Return tag that can be used for tracking references to incomplete names."""
    def found_incomplete_ref(self, tag: Tag) -> bool:
        """Have we encountered an incomplete reference since starting tracking?"""
    def record_incomplete_ref(self) -> None:
        """Record the encounter of an incomplete reference and defer current analysis target."""
    def mark_incomplete(self, name: str, node: Node, becomes_typeinfo: bool = False, module_public: bool = True, module_hidden: bool = False) -> None:
        """Mark a definition as incomplete (and defer current analysis target).

        Also potentially mark the current namespace as incomplete.

        Args:
            name: The name that we weren't able to define (or '*' if the name is unknown)
            node: The node that refers to the name (definition or lvalue)
            becomes_typeinfo: Pass this to PlaceholderNode (used by special forms like
                named tuples that will create TypeInfos).
        """
    def is_incomplete_namespace(self, fullname: str) -> bool:
        """Is a module or class namespace potentially missing some definitions?

        If a name is missing from an incomplete namespace, we'll need to defer the
        current analysis target.
        """
    def process_placeholder(self, name: str | None, kind: str, ctx: Context, force_progress: bool = False) -> None:
        """Process a reference targeting placeholder node.

        If this is not a final iteration, defer current node,
        otherwise report an error.

        The 'kind' argument indicates if this a name or attribute expression
        (used for better error message).
        """
    def cannot_resolve_name(self, name: str | None, kind: str, ctx: Context) -> None: ...
    def qualified_name(self, name: str) -> str: ...
    def enter(self, function: FuncItem | GeneratorExpr | DictionaryComprehension) -> Iterator[None]:
        """Enter a function, generator or comprehension scope."""
    def is_func_scope(self) -> bool: ...
    def is_nested_within_func_scope(self) -> bool:
        """Are we underneath a function scope, even if we are in a nested class also?"""
    def is_class_scope(self) -> bool: ...
    def is_module_scope(self) -> bool: ...
    def current_symbol_kind(self) -> int: ...
    def current_symbol_table(self, escape_comprehensions: bool = False) -> SymbolTable: ...
    def is_global_or_nonlocal(self, name: str) -> bool: ...
    def add_exports(self, exp_or_exps: Iterable[Expression] | Expression) -> None: ...
    def name_not_defined(self, name: str, ctx: Context, namespace: str | None = None) -> None: ...
    def already_defined(self, name: str, ctx: Context, original_ctx: SymbolTableNode | SymbolNode | None, noun: str) -> None: ...
    def name_already_defined(self, name: str, ctx: Context, original_ctx: SymbolTableNode | SymbolNode | None = None) -> None: ...
    def attribute_already_defined(self, name: str, ctx: Context, original_ctx: SymbolTableNode | SymbolNode | None = None) -> None: ...
    def is_local_name(self, name: str) -> bool:
        """Does name look like reference to a definition in the current module?"""
    def in_checked_function(self) -> bool:
        """Should we type-check the current function?

        - Yes if --check-untyped-defs is set.
        - Yes outside functions.
        - Yes in annotated functions.
        - No otherwise.
        """
    def fail(self, msg: str, ctx: Context, serious: bool = False, *, code: ErrorCode | None = None, blocker: bool = False) -> None: ...
    def note(self, msg: str, ctx: Context, code: ErrorCode | None = None) -> None: ...
    def incomplete_feature_enabled(self, feature: str, ctx: Context) -> bool: ...
    def accept(self, node: Node) -> None: ...
    def expr_to_analyzed_type(self, expr: Expression, report_invalid_types: bool = True, allow_placeholder: bool = False, allow_type_any: bool = False, allow_unbound_tvars: bool = False, allow_param_spec_literals: bool = False) -> Type | None: ...
    def analyze_type_expr(self, expr: Expression) -> None: ...
    def type_analyzer(self, *, tvar_scope: TypeVarLikeScope | None = None, allow_tuple_literal: bool = False, allow_unbound_tvars: bool = False, allow_placeholder: bool = False, allow_required: bool = False, allow_param_spec_literals: bool = False, report_invalid_types: bool = True, prohibit_self_type: str | None = None, allow_type_any: bool = False) -> TypeAnalyser: ...
    def expr_to_unanalyzed_type(self, node: Expression) -> ProperType: ...
    def anal_type(self, typ: Type, *, tvar_scope: TypeVarLikeScope | None = None, allow_tuple_literal: bool = False, allow_unbound_tvars: bool = False, allow_placeholder: bool = False, allow_required: bool = False, allow_param_spec_literals: bool = False, report_invalid_types: bool = True, prohibit_self_type: str | None = None, allow_type_any: bool = False, third_pass: bool = False) -> Type | None:
        """Semantically analyze a type.

        Args:
            typ: Type to analyze (if already analyzed, this is a no-op)
            allow_placeholder: If True, may return PlaceholderType if
                encountering an incomplete definition
            third_pass: Unused; only for compatibility with old semantic
                analyzer

        Return None only if some part of the type couldn't be bound *and* it
        referred to an incomplete namespace or definition. In this case also
        defer as needed. During a final iteration this won't return None;
        instead report an error if the type can't be analyzed and return
        AnyType.

        In case of other errors, report an error message and return AnyType.

        NOTE: The caller shouldn't defer even if this returns None or a
              placeholder type.
        """
    def class_type(self, self_type: Type) -> Type: ...
    def schedule_patch(self, priority: int, patch: Callable[[], None]) -> None: ...
    def report_hang(self) -> None: ...
    def add_plugin_dependency(self, trigger: str, target: str | None = None) -> None:
        """Add dependency from trigger to a target.

        If the target is not given explicitly, use the current target.
        """
    def add_type_alias_deps(self, aliases_used: Collection[str], target: str | None = None) -> None:
        """Add full names of type aliases on which the current node depends.

        This is used by fine-grained incremental mode to re-check the corresponding nodes.
        If `target` is None, then the target node used will be the current scope.
        """
    def is_mangled_global(self, name: str) -> bool: ...
    def is_initial_mangled_global(self, name: str) -> bool: ...
    def parse_bool(self, expr: Expression) -> bool | None: ...
    def parse_str_literal(self, expr: Expression) -> str | None:
        """Attempt to find the string literal value of the given expression. Returns `None` if no
        literal value can be found."""
    def set_future_import_flags(self, module_name: str) -> None: ...
    def is_future_flag_set(self, flag: str) -> bool: ...
    def parse_dataclass_transform_spec(self, call: CallExpr) -> DataclassTransformSpec:
        """Build a DataclassTransformSpec from the arguments passed to the given call to
        typing.dataclass_transform."""
    def parse_dataclass_transform_field_specifiers(self, arg: Expression) -> tuple[str, ...]: ...

def replace_implicit_first_type(sig: FunctionLike, new: Type) -> FunctionLike: ...
def refers_to_fullname(node: Expression, fullnames: str | tuple[str, ...]) -> bool:
    """Is node a name or member expression with the given full name?"""
def refers_to_class_or_function(node: Expression) -> bool:
    """Does semantically analyzed node refer to a class?"""
def find_duplicate(list: list[T]) -> T | None:
    """If the list has duplicates, return one of the duplicates.

    Otherwise, return None.
    """
def remove_imported_names_from_symtable(names: SymbolTable, module: str) -> None:
    """Remove all imported names from the symbol table of a module."""
def make_any_non_explicit(t: Type) -> Type:
    """Replace all Any types within in with Any that has attribute 'explicit' set to False"""

class MakeAnyNonExplicit(TrivialSyntheticTypeTranslator):
    def visit_any(self, t: AnyType) -> Type: ...
    def visit_type_alias_type(self, t: TypeAliasType) -> Type: ...

def apply_semantic_analyzer_patches(patches: list[tuple[int, Callable[[], None]]]) -> None:
    """Call patch callbacks in the right order.

    This should happen after semantic analyzer pass 3.
    """
def names_modified_by_assignment(s: AssignmentStmt) -> list[NameExpr]:
    """Return all unqualified (short) names assigned to in an assignment statement."""
def names_modified_in_lvalue(lvalue: Lvalue) -> list[NameExpr]:
    """Return all NameExpr assignment targets in an Lvalue."""
def is_same_var_from_getattr(n1: SymbolNode | None, n2: SymbolNode | None) -> bool:
    """Do n1 and n2 refer to the same Var derived from module-level __getattr__?"""
def dummy_context() -> Context: ...
def is_valid_replacement(old: SymbolTableNode, new: SymbolTableNode) -> bool:
    """Can symbol table node replace an existing one?

    These are the only valid cases:

    1. Placeholder gets replaced with a non-placeholder
    2. Placeholder that isn't known to become type replaced with a
       placeholder that can become a type
    """
def is_same_symbol(a: SymbolNode | None, b: SymbolNode | None) -> bool: ...
def is_trivial_body(block: Block) -> bool:
    '''Returns \'true\' if the given body is "trivial" -- if it contains just a "pass",
    "..." (ellipsis), or "raise NotImplementedError()". A trivial body may also
    start with a statement containing just a string (e.g. a docstring).

    Note: Functions that raise other kinds of exceptions do not count as
    "trivial". We use this function to help us determine when it\'s ok to
    relax certain checks on body, but functions that raise arbitrary exceptions
    are more likely to do non-trivial work. For example:

       def halt(self, reason: str = ...) -> NoReturn:
           raise MyCustomError("Fatal error: " + reason, self.line, self.context)

    A function that raises just NotImplementedError is much less likely to be
    this complex.

    Note: If you update this, you may also need to update
    mypy.fastparse.is_possible_trivial_body!
    '''
