from _typeshed import Incomplete
from mypy.nodes import ParamSpecExpr as ParamSpecExpr, SymbolTableNode as SymbolTableNode, TypeVarExpr as TypeVarExpr, TypeVarLikeExpr as TypeVarLikeExpr, TypeVarTupleExpr as TypeVarTupleExpr
from mypy.types import ParamSpecFlavor as ParamSpecFlavor, ParamSpecType as ParamSpecType, TypeVarId as TypeVarId, TypeVarLikeType as TypeVarLikeType, TypeVarTupleType as TypeVarTupleType, TypeVarType as TypeVarType

class TypeVarLikeScope:
    """Scope that holds bindings for type variables and parameter specifications.

    Node fullname -> TypeVarLikeType.
    """
    scope: Incomplete
    parent: Incomplete
    func_id: int
    class_id: int
    is_class_scope: Incomplete
    prohibited: Incomplete
    namespace: Incomplete
    def __init__(self, parent: TypeVarLikeScope | None = None, is_class_scope: bool = False, prohibited: TypeVarLikeScope | None = None, namespace: str = '') -> None:
        """Initializer for TypeVarLikeScope

        Parameters:
          parent: the outer scope for this scope
          is_class_scope: True if this represents a generic class
          prohibited: Type variables that aren't strictly in scope exactly,
                      but can't be bound because they're part of an outer class's scope.
        """
    def get_function_scope(self) -> TypeVarLikeScope | None:
        """Get the nearest parent that's a function scope, not a class scope"""
    def allow_binding(self, fullname: str) -> bool: ...
    def method_frame(self) -> TypeVarLikeScope:
        """A new scope frame for binding a method"""
    def class_frame(self, namespace: str) -> TypeVarLikeScope:
        """A new scope frame for binding a class. Prohibits *this* class's tvars"""
    def new_unique_func_id(self) -> int:
        """Used by plugin-like code that needs to make synthetic generic functions."""
    def bind_new(self, name: str, tvar_expr: TypeVarLikeExpr) -> TypeVarLikeType: ...
    def bind_existing(self, tvar_def: TypeVarLikeType) -> None: ...
    def get_binding(self, item: str | SymbolTableNode) -> TypeVarLikeType | None: ...
