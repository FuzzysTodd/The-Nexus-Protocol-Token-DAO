from typing import Any, overload

@overload
def get_nested_attr(__o: object, __name: str) -> Any: ...
@overload
def get_nested_attr(__o: object, __name: str, __default: Any) -> Any: ...
def set_nested_attr(__obj: object, __name: str, __value: Any):
    """
    Set the nested named attribute on the given object to the specified value by a `.` separated name.
    set_nested_attr(x, 'y.z', v) is equivalent to setattr(getattr(x, 'y'), 'z', v) x.y.z = v.
    """
