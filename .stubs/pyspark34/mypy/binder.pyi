from _typeshed import Incomplete
from mypy.erasetype import remove_instance_last_known_values as remove_instance_last_known_values
from mypy.join import join_simple as join_simple
from mypy.literals import Key as Key, literal as literal, literal_hash as literal_hash, subkeys as subkeys
from mypy.nodes import Expression as Expression, IndexExpr as IndexExpr, MemberExpr as MemberExpr, NameExpr as NameExpr, RefExpr as RefExpr, TypeInfo as TypeInfo, Var as Var
from mypy.subtypes import is_same_type as is_same_type, is_subtype as is_subtype
from mypy.types import AnyType as AnyType, NoneType as NoneType, PartialType as PartialType, Type as Type, TypeOfAny as TypeOfAny, TypeType as TypeType, UnionType as UnionType, get_proper_type as get_proper_type
from mypy.typevars import fill_typevars_with_any as fill_typevars_with_any
from typing import DefaultDict, Iterator, List, Optional, Tuple
from typing_extensions import TypeAlias as _TypeAlias

BindableExpression: _TypeAlias

class Frame:
    """A Frame represents a specific point in the execution of a program.
    It carries information about the current types of expressions at
    that point, arising either from assignments to those expressions
    or the result of isinstance checks. It also records whether it is
    possible to reach that point at all.

    This information is not copied into a new Frame when it is pushed
    onto the stack, so a given Frame only has information about types
    that were assigned in that frame.
    """
    id: Incomplete
    types: Incomplete
    unreachable: bool
    conditional_frame: Incomplete
    suppress_unreachable_warnings: bool
    def __init__(self, id: int, conditional_frame: bool = False) -> None: ...
Assigns = DefaultDict[Expression, List[Tuple[Type, Optional[Type]]]]

class ConditionalTypeBinder:
    """Keep track of conditional types of variables.

    NB: Variables are tracked by literal expression, so it is possible
    to confuse the binder; for example,

    ```
    class A:
        a: Union[int, str] = None
    x = A()
    lst = [x]
    reveal_type(x.a)      # Union[int, str]
    x.a = 1
    reveal_type(x.a)      # int
    reveal_type(lst[0].a) # Union[int, str]
    lst[0].a = 'a'
    reveal_type(x.a)      # int
    reveal_type(lst[0].a) # str
    ```
    """
    type_assignments: Assigns | None
    next_id: int
    frames: Incomplete
    options_on_return: Incomplete
    declarations: Incomplete
    dependencies: Incomplete
    last_pop_changed: bool
    try_frames: Incomplete
    break_frames: Incomplete
    continue_frames: Incomplete
    def __init__(self) -> None: ...
    def push_frame(self, conditional_frame: bool = False) -> Frame:
        """Push a new frame into the binder."""
    def put(self, expr: Expression, typ: Type) -> None: ...
    def unreachable(self) -> None: ...
    def suppress_unreachable_warnings(self) -> None: ...
    def get(self, expr: Expression) -> Type | None: ...
    def is_unreachable(self) -> bool: ...
    def is_unreachable_warning_suppressed(self) -> bool: ...
    def cleanse(self, expr: Expression) -> None:
        """Remove all references to a Node from the binder."""
    def update_from_options(self, frames: list[Frame]) -> bool:
        """Update the frame to reflect that each key will be updated
        as in one of the frames.  Return whether any item changes.

        If a key is declared as AnyType, only update it if all the
        options are the same.
        """
    def pop_frame(self, can_skip: bool, fall_through: int) -> Frame:
        """Pop a frame and return it.

        See frame_context() for documentation of fall_through.
        """
    def accumulate_type_assignments(self) -> Iterator[Assigns]:
        """Push a new map to collect assigned types in multiassign from union.

        If this map is not None, actual binding is deferred until all items in
        the union are processed (a union of collected items is later bound
        manually by the caller).
        """
    def assign_type(self, expr: Expression, type: Type, declared_type: Type | None, restrict_any: bool = False) -> None: ...
    def invalidate_dependencies(self, expr: BindableExpression) -> None:
        """Invalidate knowledge of types that include expr, but not expr itself.

        For example, when expr is foo.bar, invalidate foo.bar.baz.

        It is overly conservative: it invalidates globally, including
        in code paths unreachable from here.
        """
    def most_recent_enclosing_type(self, expr: BindableExpression, type: Type) -> Type | None: ...
    def allow_jump(self, index: int) -> None: ...
    def handle_break(self) -> None: ...
    def handle_continue(self) -> None: ...
    def frame_context(self, *, can_skip: bool, fall_through: int = 1, break_frame: int = 0, continue_frame: int = 0, conditional_frame: bool = False, try_frame: bool = False) -> Iterator[Frame]:
        """Return a context manager that pushes/pops frames on enter/exit.

        If can_skip is True, control flow is allowed to bypass the
        newly-created frame.

        If fall_through > 0, then it will allow control flow that
        falls off the end of the frame to escape to its ancestor
        `fall_through` levels higher. Otherwise control flow ends
        at the end of the frame.

        If break_frame > 0, then 'break' statements within this frame
        will jump out to the frame break_frame levels higher than the
        frame created by this call to frame_context. Similarly for
        continue_frame and 'continue' statements.

        If try_frame is true, then execution is allowed to jump at any
        point within the newly created frame (or its descendants) to
        its parent (i.e., to the frame that was on top before this
        call to frame_context).

        After the context manager exits, self.last_pop_changed indicates
        whether any types changed in the newly-topmost frame as a result
        of popping this frame.
        """
    def top_frame_context(self) -> Iterator[Frame]:
        """A variant of frame_context for use at the top level of
        a namespace (module, function, or class).
        """

def get_declaration(expr: BindableExpression) -> Type | None: ...
