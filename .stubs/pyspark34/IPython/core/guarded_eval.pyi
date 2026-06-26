import ast
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Callable, Literal, NamedTuple, Set, Tuple
from typing_extensions import Protocol

__all__ = ['guarded_eval', 'eval_node', 'GuardRejection', 'EvaluationContext', '_unbind_method']

class HasGetItem(Protocol):
    def __getitem__(self, key) -> None: ...

class InstancesHaveGetItem(Protocol):
    def __call__(self, *args, **kwargs) -> HasGetItem: ...

class HasGetAttr(Protocol):
    def __getattr__(self, key) -> None: ...

class DoesNotHaveGetAttr(Protocol): ...
MayHaveGetattr = HasGetAttr | DoesNotHaveGetAttr

def _unbind_method(func: Callable) -> Callable | None:
    """Get unbound method for given bound method.

    Returns None if cannot get unbound method, or method is already unbound.
    """

@dataclass
class EvaluationPolicy:
    """Definition of evaluation policy."""
    allow_locals_access: bool = ...
    allow_globals_access: bool = ...
    allow_item_access: bool = ...
    allow_attr_access: bool = ...
    allow_builtins_access: bool = ...
    allow_all_operations: bool = ...
    allow_any_calls: bool = ...
    allowed_calls: Set[Callable] = ...
    def can_get_item(self, value, item): ...
    def can_get_attr(self, value, attr): ...
    def can_operate(self, dunders: Tuple[str, ...], a, b: Incomplete | None = None): ...
    def can_call(self, func): ...
    def __init__(self, allow_locals_access, allow_globals_access, allow_item_access, allow_attr_access, allow_builtins_access, allow_all_operations, allow_any_calls, allowed_calls) -> None: ...

@dataclass
class SelectivePolicy(EvaluationPolicy):
    allowed_getitem: Set[InstancesHaveGetItem] = ...
    allowed_getitem_external: Set[Tuple[str, ...]] = ...
    allowed_getattr: Set[MayHaveGetattr] = ...
    allowed_getattr_external: Set[Tuple[str, ...]] = ...
    allowed_operations: Set = ...
    allowed_operations_external: Set[Tuple[str, ...]] = ...
    def can_get_attr(self, value, attr): ...
    def can_get_item(self, value, item):
        """Allow accessing `__getiitem__` of allow-listed instances unless it was not modified."""
    def can_operate(self, dunders: Tuple[str, ...], a, b: Incomplete | None = None): ...
    def __init__(self, allow_locals_access, allow_globals_access, allow_item_access, allow_attr_access, allow_builtins_access, allow_all_operations, allow_any_calls, allowed_calls, allowed_getitem, allowed_getitem_external, allowed_getattr, allowed_getattr_external, allowed_operations, allowed_operations_external) -> None: ...

class _DummyNamedTuple(NamedTuple):
    """Used internally to retrieve methods of named tuple instance."""

class EvaluationContext(NamedTuple):
    locals: dict
    globals: dict
    evaluation: Literal['forbidden', 'minimal', 'limited', 'unsafe', 'dangerous'] = ...
    in_subscript: bool = ...

class _IdentitySubscript:
    """Returns the key itself when item is requested via subscript."""
    def __getitem__(self, key): ...

class GuardRejection(Exception):
    """Exception raised when guard rejects evaluation attempt."""

def guarded_eval(code: str, context: EvaluationContext):
    """Evaluate provided code in the evaluation context.

    If evaluation policy given by context is set to ``forbidden``
    no evaluation will be performed; if it is set to ``dangerous``
    standard :func:`eval` will be used; finally, for any other,
    policy :func:`eval_node` will be called on parsed AST.
    """
def eval_node(node: ast.AST | None, context: EvaluationContext):
    """Evaluate AST node in provided context.

    Applies evaluation restrictions defined in the context. Currently does not support evaluation of functions with keyword arguments.

    Does not evaluate actions that always have side effects:

    - class definitions (``class sth: ...``)
    - function definitions (``def sth: ...``)
    - variable assignments (``x = 1``)
    - augmented assignments (``x += 1``)
    - deletions (``del x``)

    Does not evaluate operations which do not return values:

    - assertions (``assert x``)
    - pass (``pass``)
    - imports (``import x``)
    - control flow:

        - conditionals (``if x:``) except for ternary IfExp (``a if x else b``)
        - loops (``for`` and `while``)
        - exception handling

    The purpose of this function is to guard against unwanted side-effects;
    it does not give guarantees on protection from malicious code execution.
    """
