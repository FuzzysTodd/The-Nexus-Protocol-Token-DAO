from _typeshed import Incomplete
from mypy.nodes import FuncBase as FuncBase, TypeInfo as TypeInfo
from typing import Iterator
from typing_extensions import TypeAlias as _TypeAlias

SavedScope: _TypeAlias

class Scope:
    """Track which target we are processing at any given time."""
    module: Incomplete
    classes: Incomplete
    function: Incomplete
    functions: Incomplete
    ignored: int
    def __init__(self) -> None: ...
    def current_module_id(self) -> str: ...
    def current_target(self) -> str:
        """Return the current target (non-class; for a class return enclosing module)."""
    def current_full_target(self) -> str:
        """Return the current target (may be a class)."""
    def current_type_name(self) -> str | None:
        """Return the current type's short name if it exists"""
    def current_function_name(self) -> str | None:
        """Return the current function's short name if it exists"""
    def module_scope(self, prefix: str) -> Iterator[None]: ...
    def function_scope(self, fdef: FuncBase) -> Iterator[None]: ...
    def outer_functions(self) -> list[FuncBase]: ...
    def enter_class(self, info: TypeInfo) -> None:
        """Enter a class target scope."""
    def leave_class(self) -> None:
        """Leave a class target scope."""
    def class_scope(self, info: TypeInfo) -> Iterator[None]: ...
    def save(self) -> SavedScope:
        """Produce a saved scope that can be entered with saved_scope()"""
    def saved_scope(self, saved: SavedScope) -> Iterator[None]: ...
