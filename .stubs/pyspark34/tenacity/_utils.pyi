import typing
from _typeshed import Incomplete

MAX_WAIT: Incomplete

def find_ordinal(pos_num: int) -> str: ...
def to_ordinal(pos_num: int) -> str: ...
def get_callback_name(cb: typing.Callable[..., typing.Any]) -> str:
    """Get a callback fully-qualified name.

    If no name can be produced ``repr(cb)`` is called and returned.
    """

time_unit_type: Incomplete

def to_seconds(time_unit: time_unit_type) -> float: ...
