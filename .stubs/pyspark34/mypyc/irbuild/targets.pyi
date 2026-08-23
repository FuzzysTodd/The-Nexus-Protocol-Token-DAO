from _typeshed import Incomplete
from mypyc.ir.ops import Register as Register, Value as Value
from mypyc.ir.rtypes import RInstance as RInstance, RType as RType, object_rprimitive as object_rprimitive

class AssignmentTarget:
    """Abstract base class for assignment targets during IR building."""
    type: RType

class AssignmentTargetRegister(AssignmentTarget):
    """Register as an assignment target.

    This is used for local variables and some temporaries.
    """
    register: Incomplete
    type: Incomplete
    def __init__(self, register: Register) -> None: ...

class AssignmentTargetIndex(AssignmentTarget):
    """base[index] as assignment target"""
    base: Incomplete
    index: Incomplete
    type: Incomplete
    def __init__(self, base: Value, index: Value) -> None: ...

class AssignmentTargetAttr(AssignmentTarget):
    """obj.attr as assignment target"""
    obj: Incomplete
    attr: Incomplete
    can_borrow: Incomplete
    obj_type: Incomplete
    type: Incomplete
    def __init__(self, obj: Value, attr: str, can_borrow: bool = False) -> None: ...

class AssignmentTargetTuple(AssignmentTarget):
    """x, ..., y as assignment target"""
    items: Incomplete
    star_idx: Incomplete
    def __init__(self, items: list[AssignmentTarget], star_idx: int | None = None) -> None: ...
