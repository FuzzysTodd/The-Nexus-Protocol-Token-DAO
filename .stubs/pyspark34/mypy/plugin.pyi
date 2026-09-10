import abc
from _typeshed import Incomplete
from abc import abstractmethod
from mypy.errorcodes import ErrorCode as ErrorCode
from mypy.lookup import lookup_fully_qualified as lookup_fully_qualified
from mypy.message_registry import ErrorMessage as ErrorMessage
from mypy.messages import MessageBuilder as MessageBuilder
from mypy.nodes import ArgKind as ArgKind, CallExpr as CallExpr, ClassDef as ClassDef, Context as Context, Expression as Expression, MypyFile as MypyFile, SymbolTableNode as SymbolTableNode, TypeInfo as TypeInfo
from mypy.options import Options as Options
from mypy.tvar_scope import TypeVarLikeScope as TypeVarLikeScope
from mypy.types import CallableType as CallableType, FunctionLike as FunctionLike, Instance as Instance, ProperType as ProperType, Type as Type, TypeList as TypeList, UnboundType as UnboundType
from typing import Any, Callable, NamedTuple, TypeVar

class TypeAnalyzerPluginInterface(metaclass=abc.ABCMeta):
    """Interface for accessing semantic analyzer functionality in plugins.

    Methods docstrings contain only basic info. Look for corresponding implementation
    docstrings in typeanal.py for more details.
    """
    options: Options
    @abstractmethod
    def fail(self, msg: str, ctx: Context, *, code: ErrorCode | None = None) -> None:
        """Emit an error message at given location."""
    @abstractmethod
    def named_type(self, name: str, args: list[Type]) -> Instance:
        """Construct an instance of a builtin type with given name."""
    @abstractmethod
    def analyze_type(self, typ: Type) -> Type:
        """Analyze an unbound type using the default mypy logic."""
    @abstractmethod
    def analyze_callable_args(self, arglist: TypeList) -> tuple[list[Type], list[ArgKind], list[str | None]] | None:
        """Find types, kinds, and names of arguments from extended callable syntax."""

class AnalyzeTypeContext(NamedTuple):
    type: UnboundType
    context: Context
    api: TypeAnalyzerPluginInterface

class CommonPluginApi(metaclass=abc.ABCMeta):
    """
    A common plugin API (shared between semantic analysis and type checking phases)
    that all plugin hooks get independently of the context.
    """
    options: Options
    @abstractmethod
    def lookup_fully_qualified(self, fullname: str) -> SymbolTableNode | None:
        """Lookup a symbol by its full name (including module).

        This lookup function available for all plugins. Return None if a name
        is not found. This function doesn't support lookup from current scope.
        Use SemanticAnalyzerPluginInterface.lookup_qualified() for this."""

class CheckerPluginInterface(metaclass=abc.ABCMeta):
    """Interface for accessing type checker functionality in plugins.

    Methods docstrings contain only basic info. Look for corresponding implementation
    docstrings in checker.py for more details.
    """
    msg: MessageBuilder
    options: Options
    path: str
    @property
    @abstractmethod
    def type_context(self) -> list[Type | None]:
        """Return the type context of the plugin"""
    @abstractmethod
    def fail(self, msg: str | ErrorMessage, ctx: Context, *, code: ErrorCode | None = None) -> None:
        """Emit an error message at given location."""
    @abstractmethod
    def named_generic_type(self, name: str, args: list[Type]) -> Instance:
        """Construct an instance of a builtin type with given type arguments."""

class SemanticAnalyzerPluginInterface(metaclass=abc.ABCMeta):
    """Interface for accessing semantic analyzer functionality in plugins.

    Methods docstrings contain only basic info. Look for corresponding implementation
    docstrings in semanal.py for more details.

    # TODO: clean-up lookup functions.
    """
    modules: dict[str, MypyFile]
    options: Options
    cur_mod_id: str
    msg: MessageBuilder
    @abstractmethod
    def named_type(self, fullname: str, args: list[Type] | None = None) -> Instance:
        """Construct an instance of a builtin type with given type arguments."""
    @abstractmethod
    def builtin_type(self, fully_qualified_name: str) -> Instance:
        """Legacy function -- use named_type() instead."""
    @abstractmethod
    def named_type_or_none(self, fullname: str, args: list[Type] | None = None) -> Instance | None:
        """Construct an instance of a type with given type arguments.

        Return None if a type could not be constructed for the qualified
        type name. This is possible when the qualified name includes a
        module name and the module has not been imported.
        """
    @abstractmethod
    def basic_new_typeinfo(self, name: str, basetype_or_fallback: Instance, line: int) -> TypeInfo: ...
    @abstractmethod
    def parse_bool(self, expr: Expression) -> bool | None:
        """Parse True/False literals."""
    @abstractmethod
    def parse_str_literal(self, expr: Expression) -> str | None:
        """Parse string literals."""
    @abstractmethod
    def fail(self, msg: str, ctx: Context, serious: bool = False, *, blocker: bool = False, code: ErrorCode | None = None) -> None:
        """Emit an error message at given location."""
    @abstractmethod
    def anal_type(self, t: Type, *, tvar_scope: TypeVarLikeScope | None = None, allow_tuple_literal: bool = False, allow_unbound_tvars: bool = False, report_invalid_types: bool = True, third_pass: bool = False) -> Type | None:
        """Analyze an unbound type.

        Return None if some part of the type is not ready yet. In this
        case the current target being analyzed will be deferred and
        analyzed again.
        """
    @abstractmethod
    def class_type(self, self_type: Type) -> Type:
        """Generate type of first argument of class methods from type of self."""
    @abstractmethod
    def lookup_fully_qualified(self, name: str) -> SymbolTableNode:
        """Lookup a symbol by its fully qualified name.

        Raise an error if not found.
        """
    @abstractmethod
    def lookup_fully_qualified_or_none(self, name: str) -> SymbolTableNode | None:
        """Lookup a symbol by its fully qualified name.

        Return None if not found.
        """
    @abstractmethod
    def lookup_qualified(self, name: str, ctx: Context, suppress_errors: bool = False) -> SymbolTableNode | None:
        """Lookup symbol using a name in current scope.

        This follows Python local->non-local->global->builtins rules.
        """
    @abstractmethod
    def add_plugin_dependency(self, trigger: str, target: str | None = None) -> None:
        """Specify semantic dependencies for generated methods/variables.

        If the symbol with full name given by trigger is found to be stale by mypy,
        then the body of node with full name given by target will be re-checked.
        By default, this is the node that is currently analyzed.

        For example, the dataclass plugin adds a generated __init__ method with
        a signature that depends on types of attributes in ancestor classes. If any
        attribute in an ancestor class gets stale (modified), we need to reprocess
        the subclasses (and thus regenerate __init__ methods).

        This is used by fine-grained incremental mode (mypy daemon). See mypy/server/deps.py
        for more details.
        """
    @abstractmethod
    def add_symbol_table_node(self, name: str, stnode: SymbolTableNode) -> Any:
        """Add node to global symbol table (or to nearest class if there is one)."""
    @abstractmethod
    def qualified_name(self, n: str) -> str:
        """Make qualified name using current module and enclosing class (if any)."""
    @abstractmethod
    def defer(self) -> None:
        """Call this to defer the processing of the current node.

        This will request an additional iteration of semantic analysis.
        """
    @property
    @abstractmethod
    def final_iteration(self) -> bool:
        """Is this the final iteration of semantic analysis?"""
    @property
    @abstractmethod
    def is_stub_file(self) -> bool: ...
    @abstractmethod
    def analyze_simple_literal_type(self, rvalue: Expression, is_final: bool) -> Type | None: ...

class ReportConfigContext(NamedTuple):
    id: str
    path: str
    is_check: bool

class FunctionSigContext(NamedTuple):
    args: list[list[Expression]]
    default_signature: CallableType
    context: Context
    api: CheckerPluginInterface

class FunctionContext(NamedTuple):
    arg_types: list[list[Type]]
    arg_kinds: list[list[ArgKind]]
    callee_arg_names: list[str | None]
    arg_names: list[list[str | None]]
    default_return_type: Type
    args: list[list[Expression]]
    context: Context
    api: CheckerPluginInterface

class MethodSigContext(NamedTuple):
    type: ProperType
    args: list[list[Expression]]
    default_signature: CallableType
    context: Context
    api: CheckerPluginInterface

class MethodContext(NamedTuple):
    type: ProperType
    arg_types: list[list[Type]]
    arg_kinds: list[list[ArgKind]]
    callee_arg_names: list[str | None]
    arg_names: list[list[str | None]]
    default_return_type: Type
    args: list[list[Expression]]
    context: Context
    api: CheckerPluginInterface

class AttributeContext(NamedTuple):
    type: ProperType
    default_attr_type: Type
    context: Context
    api: CheckerPluginInterface

class ClassDefContext(NamedTuple):
    cls: ClassDef
    reason: Expression
    api: SemanticAnalyzerPluginInterface

class DynamicClassDefContext(NamedTuple):
    call: CallExpr
    name: str
    api: SemanticAnalyzerPluginInterface

class Plugin(CommonPluginApi):
    """Base class of all type checker plugins.

    This defines a no-op plugin.  Subclasses can override some methods to
    provide some actual functionality.

    All get_ methods are treated as pure functions (you should assume that
    results might be cached). A plugin should return None from a get_ method
    to give way to other plugins.

    Look at the comments of various *Context objects for additional information on
    various hooks.
    """
    options: Incomplete
    python_version: Incomplete
    def __init__(self, options: Options) -> None: ...
    def set_modules(self, modules: dict[str, MypyFile]) -> None: ...
    def lookup_fully_qualified(self, fullname: str) -> SymbolTableNode | None: ...
    def report_config_data(self, ctx: ReportConfigContext) -> Any:
        """Get representation of configuration data for a module.

        The data must be encodable as JSON and will be stored in the
        cache metadata for the module. A mismatch between the cached
        values and the returned will result in that module's cache
        being invalidated and the module being rechecked.

        This can be called twice for each module, once after loading
        the cache to check if it is valid and once while writing new
        cache information.

        If is_check in the context is true, then the return of this
        call will be checked against the cached version. Otherwise the
        call is being made to determine what to put in the cache. This
        can be used to allow consulting extra cache files in certain
        complex situations.

        This can be used to incorporate external configuration information
        that might require changes to typechecking.
        """
    def get_additional_deps(self, file: MypyFile) -> list[tuple[int, str, int]]:
        """Customize dependencies for a module.

        This hook allows adding in new dependencies for a module. It
        is called after parsing a file but before analysis. This can
        be useful if a library has dependencies that are dynamic based
        on configuration information, for example.

        Returns a list of (priority, module name, line number) tuples.

        The line number can be -1 when there is not a known real line number.

        Priorities are defined in mypy.build (but maybe shouldn't be).
        10 is a good choice for priority.
        """
    def get_type_analyze_hook(self, fullname: str) -> Callable[[AnalyzeTypeContext], Type] | None:
        """Customize behaviour of the type analyzer for given full names.

        This method is called during the semantic analysis pass whenever mypy sees an
        unbound type. For example, while analysing this code:

            from lib import Special, Other

            var: Special
            def func(x: Other[int]) -> None:
                ...

        this method will be called with 'lib.Special', and then with 'lib.Other'.
        The callback returned by plugin must return an analyzed type,
        i.e. an instance of `mypy.types.Type`.
        """
    def get_function_signature_hook(self, fullname: str) -> Callable[[FunctionSigContext], FunctionLike] | None:
        """Adjust the signature of a function.

        This method is called before type checking a function call. Plugin
        may infer a better type for the function.

            from lib import Class, do_stuff

            do_stuff(42)
            Class()

        This method will be called with 'lib.do_stuff' and then with 'lib.Class'.
        """
    def get_function_hook(self, fullname: str) -> Callable[[FunctionContext], Type] | None:
        """Adjust the return type of a function call.

        This method is called after type checking a call. Plugin may adjust the return
        type inferred by mypy, and/or emit some error messages. Note, this hook is also
        called for class instantiation calls, so that in this example:

            from lib import Class, do_stuff

            do_stuff(42)
            Class()

        This method will be called with 'lib.do_stuff' and then with 'lib.Class'.
        """
    def get_method_signature_hook(self, fullname: str) -> Callable[[MethodSigContext], FunctionLike] | None:
        """Adjust the signature of a method.

        This method is called before type checking a method call. Plugin
        may infer a better type for the method. The hook is also called for special
        Python dunder methods except __init__ and __new__ (use get_function_hook to customize
        class instantiation). This function is called with the method full name using
        the class where it was _defined_. For example, in this code:

            from lib import Special

            class Base:
                def method(self, arg: Any) -> Any:
                    ...
            class Derived(Base):
                ...

            var: Derived
            var.method(42)

            x: Special
            y = x[0]

        this method is called with '__main__.Base.method', and then with
        'lib.Special.__getitem__'.
        """
    def get_method_hook(self, fullname: str) -> Callable[[MethodContext], Type] | None:
        """Adjust return type of a method call.

        This is the same as get_function_hook(), but is called with the
        method full name (again, using the class where the method is defined).
        """
    def get_attribute_hook(self, fullname: str) -> Callable[[AttributeContext], Type] | None:
        """Adjust type of an instance attribute.

        This method is called with attribute full name using the class of the instance where
        the attribute was defined (or Var.info.fullname for generated attributes).

        For classes without __getattr__ or __getattribute__, this hook is only called for
        names of fields/properties (but not methods) that exist in the instance MRO.

        For classes that implement __getattr__ or __getattribute__, this hook is called
        for all fields/properties, including nonexistent ones (but still not methods).

        For example:

            class Base:
                x: Any
                def __getattr__(self, attr: str) -> Any: ...

            class Derived(Base):
                ...

            var: Derived
            var.x
            var.y

        get_attribute_hook is called with '__main__.Base.x' and '__main__.Base.y'.
        However, if we had not implemented __getattr__ on Base, you would only get
        the callback for 'var.x'; 'var.y' would produce an error without calling the hook.
        """
    def get_class_attribute_hook(self, fullname: str) -> Callable[[AttributeContext], Type] | None:
        """
        Adjust type of a class attribute.

        This method is called with attribute full name using the class where the attribute was
        defined (or Var.info.fullname for generated attributes).

        For example:

            class Cls:
                x: Any

            Cls.x

        get_class_attribute_hook is called with '__main__.Cls.x' as fullname.
        """
    def get_class_decorator_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None:
        """Update class definition for given class decorators.

        The plugin can modify a TypeInfo _in place_ (for example add some generated
        methods to the symbol table). This hook is called after the class body was
        semantically analyzed, but *there may still be placeholders* (typically
        caused by forward references).

        NOTE: Usually get_class_decorator_hook_2 is the better option, since it
              guarantees that there are no placeholders.

        The hook is called with full names of all class decorators.

        The hook can be called multiple times per class, so it must be
        idempotent.
        """
    def get_class_decorator_hook_2(self, fullname: str) -> Callable[[ClassDefContext], bool] | None:
        """Update class definition for given class decorators.

        Similar to get_class_decorator_hook, but this runs in a later pass when
        placeholders have been resolved.

        The hook can return False if some base class hasn't been
        processed yet using class hooks. It causes all class hooks
        (that are run in this same pass) to be invoked another time for
        the file(s) currently being processed.

        The hook can be called multiple times per class, so it must be
        idempotent.
        """
    def get_metaclass_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None:
        """Update class definition for given declared metaclasses.

        Same as get_class_decorator_hook() but for metaclasses. Note:
        this hook will be only called for explicit metaclasses, not for
        inherited ones.

        TODO: probably it should also be called on inherited metaclasses.
        """
    def get_base_class_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None:
        """Update class definition for given base classes.

        Same as get_class_decorator_hook() but for base classes. Base classes
        don't need to refer to TypeInfos, if a base class refers to a variable with
        Any type, this hook will still be called.
        """
    def get_customize_class_mro_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None:
        """Customize MRO for given classes.

        The plugin can modify the class MRO _in place_. This method is called
        with the class full name before its body was semantically analyzed.
        """
    def get_dynamic_class_hook(self, fullname: str) -> Callable[[DynamicClassDefContext], None] | None:
        """Semantically analyze a dynamic class definition.

        This plugin hook allows one to semantically analyze dynamic class definitions like:

            from lib import dynamic_class

            X = dynamic_class('X', [])

        For such definition, this hook will be called with 'lib.dynamic_class'.
        The plugin should create the corresponding TypeInfo, and place it into a relevant
        symbol table, e.g. using ctx.api.add_symbol_table_node().
        """
T = TypeVar('T')

class ChainedPlugin(Plugin):
    """A plugin that represents a sequence of chained plugins.

    Each lookup method returns the hook for the first plugin that
    reports a match.

    This class should not be subclassed -- use Plugin as the base class
    for all plugins.
    """
    def __init__(self, options: Options, plugins: list[Plugin]) -> None:
        """Initialize chained plugin.

        Assume that the child plugins aren't mutated (results may be cached).
        """
    def set_modules(self, modules: dict[str, MypyFile]) -> None: ...
    def report_config_data(self, ctx: ReportConfigContext) -> Any: ...
    def get_additional_deps(self, file: MypyFile) -> list[tuple[int, str, int]]: ...
    def get_type_analyze_hook(self, fullname: str) -> Callable[[AnalyzeTypeContext], Type] | None: ...
    def get_function_signature_hook(self, fullname: str) -> Callable[[FunctionSigContext], FunctionLike] | None: ...
    def get_function_hook(self, fullname: str) -> Callable[[FunctionContext], Type] | None: ...
    def get_method_signature_hook(self, fullname: str) -> Callable[[MethodSigContext], FunctionLike] | None: ...
    def get_method_hook(self, fullname: str) -> Callable[[MethodContext], Type] | None: ...
    def get_attribute_hook(self, fullname: str) -> Callable[[AttributeContext], Type] | None: ...
    def get_class_attribute_hook(self, fullname: str) -> Callable[[AttributeContext], Type] | None: ...
    def get_class_decorator_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None: ...
    def get_class_decorator_hook_2(self, fullname: str) -> Callable[[ClassDefContext], bool] | None: ...
    def get_metaclass_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None: ...
    def get_base_class_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None: ...
    def get_customize_class_mro_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None: ...
    def get_dynamic_class_hook(self, fullname: str) -> Callable[[DynamicClassDefContext], None] | None: ...
