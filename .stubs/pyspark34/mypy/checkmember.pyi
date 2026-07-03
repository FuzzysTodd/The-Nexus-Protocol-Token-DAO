import mypy.checker
from _typeshed import Incomplete
from mypy import meet as meet, message_registry as message_registry, state as state, subtypes as subtypes
from mypy.erasetype import erase_typevars as erase_typevars
from mypy.expandtype import expand_self_type as expand_self_type, expand_type_by_instance as expand_type_by_instance, freshen_all_functions_type_vars as freshen_all_functions_type_vars
from mypy.maptype import map_instance_to_supertype as map_instance_to_supertype
from mypy.messages import MessageBuilder as MessageBuilder
from mypy.nodes import ARG_POS as ARG_POS, ARG_STAR as ARG_STAR, ARG_STAR2 as ARG_STAR2, Context as Context, Decorator as Decorator, FuncBase as FuncBase, FuncDef as FuncDef, IndexExpr as IndexExpr, MypyFile as MypyFile, OverloadedFuncDef as OverloadedFuncDef, SYMBOL_FUNCBASE_TYPES as SYMBOL_FUNCBASE_TYPES, SymbolNode as SymbolNode, SymbolTable as SymbolTable, TempNode as TempNode, TypeAlias as TypeAlias, TypeInfo as TypeInfo, TypeVarExpr as TypeVarExpr, Var as Var, is_final_node as is_final_node
from mypy.plugin import AttributeContext as AttributeContext
from mypy.typeops import bind_self as bind_self, class_callable as class_callable, erase_to_bound as erase_to_bound, function_type as function_type, get_type_vars as get_type_vars, make_simplified_union as make_simplified_union, supported_self_type as supported_self_type, tuple_fallback as tuple_fallback, type_object_type_from_function as type_object_type_from_function
from mypy.types import AnyType as AnyType, CallableType as CallableType, DeletedType as DeletedType, ENUM_REMOVED_PROPS as ENUM_REMOVED_PROPS, FunctionLike as FunctionLike, Instance as Instance, LiteralType as LiteralType, NoneType as NoneType, Overloaded as Overloaded, ParamSpecType as ParamSpecType, PartialType as PartialType, ProperType as ProperType, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, TypeType as TypeType, TypeVarLikeType as TypeVarLikeType, TypeVarTupleType as TypeVarTupleType, TypeVarType as TypeVarType, TypedDictType as TypedDictType, UnionType as UnionType, get_proper_type as get_proper_type
from mypy.typetraverser import TypeTraverserVisitor as TypeTraverserVisitor
from typing import Callable, Sequence

class MemberContext:
    """Information and objects needed to type check attribute access.

    Look at the docstring of analyze_member_access for more information.
    """
    is_lvalue: Incomplete
    is_super: Incomplete
    is_operator: Incomplete
    original_type: Incomplete
    self_type: Incomplete
    context: Incomplete
    msg: Incomplete
    chk: Incomplete
    module_symbol_table: Incomplete
    no_deferral: Incomplete
    is_self: Incomplete
    def __init__(self, is_lvalue: bool, is_super: bool, is_operator: bool, original_type: Type, context: Context, msg: MessageBuilder, chk: mypy.checker.TypeChecker, self_type: Type | None, module_symbol_table: SymbolTable | None = None, no_deferral: bool = False, is_self: bool = False) -> None: ...
    def named_type(self, name: str) -> Instance: ...
    def not_ready_callback(self, name: str, context: Context) -> None: ...
    def copy_modified(self, *, messages: MessageBuilder | None = None, self_type: Type | None = None, is_lvalue: bool | None = None) -> MemberContext: ...

def analyze_member_access(name: str, typ: Type, context: Context, is_lvalue: bool, is_super: bool, is_operator: bool, msg: MessageBuilder, *, original_type: Type, chk: mypy.checker.TypeChecker, override_info: TypeInfo | None = None, in_literal_context: bool = False, self_type: Type | None = None, module_symbol_table: SymbolTable | None = None, no_deferral: bool = False, is_self: bool = False) -> Type:
    """Return the type of attribute 'name' of 'typ'.

    The actual implementation is in '_analyze_member_access' and this docstring
    also applies to it.

    This is a general operation that supports various different variations:

      1. lvalue or non-lvalue access (setter or getter access)
      2. supertype access when using super() (is_super == True and
         'override_info' should refer to the supertype)

    'original_type' is the most precise inferred or declared type of the base object
    that we have available. When looking for an attribute of 'typ', we may perform
    recursive calls targeting the fallback type, and 'typ' may become some supertype
    of 'original_type'. 'original_type' is always preserved as the 'typ' type used in
    the initial, non-recursive call. The 'self_type' is a component of 'original_type'
    to which generic self should be bound (a narrower type that has a fallback to instance).
    Currently this is used only for union types.

    'module_symbol_table' is passed to this function if 'typ' is actually a module
    and we want to keep track of the available attributes of the module (since they
    are not available via the type object directly)
    """
def may_be_awaitable_attribute(name: str, typ: Type, mx: MemberContext, override_info: TypeInfo | None = None) -> bool:
    """Check if the given type has the attribute when awaited."""
def report_missing_attribute(original_type: Type, typ: Type, name: str, mx: MemberContext, override_info: TypeInfo | None = None) -> Type: ...
def analyze_instance_member_access(name: str, typ: Instance, mx: MemberContext, override_info: TypeInfo | None) -> Type: ...
def validate_super_call(node: FuncBase, mx: MemberContext) -> None: ...
def analyze_type_callable_member_access(name: str, typ: FunctionLike, mx: MemberContext) -> Type: ...
def analyze_type_type_member_access(name: str, typ: TypeType, mx: MemberContext, override_info: TypeInfo | None) -> Type: ...
def analyze_union_member_access(name: str, typ: UnionType, mx: MemberContext) -> Type: ...
def analyze_none_member_access(name: str, typ: None, mx: MemberContext) -> Type: ...
def analyze_member_var_access(name: str, itype: Instance, info: TypeInfo, mx: MemberContext) -> Type:
    """Analyse attribute access that does not target a method.

    This is logically part of analyze_member_access and the arguments are similar.

    original_type is the type of E in the expression E.var
    """
def check_final_member(name: str, info: TypeInfo, msg: MessageBuilder, ctx: Context) -> None:
    """Give an error if the name being assigned was declared as final."""
def analyze_descriptor_access(descriptor_type: Type, mx: MemberContext) -> Type:
    """Type check descriptor access.

    Arguments:
        descriptor_type: The type of the descriptor attribute being accessed
            (the type of ``f`` in ``a.f`` when ``f`` is a descriptor).
        mx: The current member access context.
    Return:
        The return type of the appropriate ``__get__`` overload for the descriptor.
    """
def is_instance_var(var: Var) -> bool:
    """Return if var is an instance variable according to PEP 526."""
def analyze_var(name: str, var: Var, itype: Instance, info: TypeInfo, mx: MemberContext, *, implicit: bool = False) -> Type:
    """Analyze access to an attribute via a Var node.

    This is conceptually part of analyze_member_access and the arguments are similar.

    itype is the class object in which var is defined
    original_type is the type of E in the expression E.var
    if implicit is True, the original Var was created as an assignment to self
    """
def freeze_all_type_vars(member_type: Type) -> None: ...

class FreezeTypeVarsVisitor(TypeTraverserVisitor):
    def visit_callable_type(self, t: CallableType) -> None: ...

def lookup_member_var_or_accessor(info: TypeInfo, name: str, is_lvalue: bool) -> SymbolNode | None:
    """Find the attribute/accessor node that refers to a member of a type."""
def check_self_arg(functype: FunctionLike, dispatched_arg_type: Type, is_classmethod: bool, context: Context, name: str, msg: MessageBuilder) -> FunctionLike:
    """Check that an instance has a valid type for a method with annotated 'self'.

    For example if the method is defined as:
        class A:
            def f(self: S) -> T: ...
    then for 'x.f' we check that meet(type(x), A) <: S. If the method is overloaded, we
    select only overloads items that satisfy this requirement. If there are no matching
    overloads, an error is generated.

    Note: dispatched_arg_type uses a meet to select a relevant item in case if the
    original type of 'x' is a union. This is done because several special methods
    treat union types in ad-hoc manner, so we can't use MemberContext.self_type yet.
    """
def analyze_class_attribute_access(itype: Instance, name: str, mx: MemberContext, override_info: TypeInfo | None = None, original_vars: Sequence[TypeVarLikeType] | None = None) -> Type | None:
    """Analyze access to an attribute on a class object.

    itype is the return type of the class object callable, original_type is the type
    of E in the expression E.var, original_vars are type variables of the class callable
    (for generic classes).
    """
def apply_class_attr_hook(mx: MemberContext, hook: Callable[[AttributeContext], Type] | None, result: Type) -> Type | None: ...
def analyze_enum_class_attribute_access(itype: Instance, name: str, mx: MemberContext) -> Type | None: ...
def analyze_typeddict_access(name: str, typ: TypedDictType, mx: MemberContext, override_info: TypeInfo | None) -> Type: ...
def add_class_tvars(t: ProperType, isuper: Instance | None, is_classmethod: bool, original_type: Type, original_vars: Sequence[TypeVarLikeType] | None = None) -> Type:
    """Instantiate type variables during analyze_class_attribute_access,
    e.g T and Q in the following:

    class A(Generic[T]):
        @classmethod
        def foo(cls: Type[Q]) -> Tuple[T, Q]: ...

    class B(A[str]): pass
    B.foo()

    Args:
        t: Declared type of the method (or property)
        isuper: Current instance mapped to the superclass where method was defined, this
            is usually done by map_instance_to_supertype()
        is_classmethod: True if this method is decorated with @classmethod
        original_type: The value of the type B in the expression B.foo() or the corresponding
            component in case of a union (this is used to bind the self-types)
        original_vars: Type variables of the class callable on which the method was accessed
    Returns:
        Expanded method type with added type variables (when needed).
    """
def type_object_type(info: TypeInfo, named_type: Callable[[str], Instance]) -> ProperType:
    """Return the type of a type object.

    For a generic type G with type variables T and S the type is generally of form

      Callable[..., G[T, S]]

    where ... are argument types for the __init__/__new__ method (without the self
    argument). Also, the fallback type will be 'type' instead of 'function'.
    """
def analyze_decorator_or_funcbase_access(defn: Decorator | FuncBase, itype: Instance, info: TypeInfo, self_type: Type | None, name: str, mx: MemberContext) -> Type:
    """Analyzes the type behind method access.

    The function itself can possibly be decorated.
    See: https://github.com/python/mypy/issues/10409
    """
def is_valid_constructor(n: SymbolNode | None) -> bool:
    """Does this node represents a valid constructor method?

    This includes normal functions, overloaded functions, and decorators
    that return a callable type.
    """
