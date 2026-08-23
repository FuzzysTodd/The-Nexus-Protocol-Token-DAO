from .compat import StreamTextType as StreamTextType, binary_type as binary_type, text_type as text_type
from _typeshed import Incomplete
from typing import Any

class LazyEval:
    """
    Lightweight wrapper around lazily evaluated func(*args, **kwargs).

    func is only evaluated when any attribute of its return value is accessed.
    Every attribute access is passed through to the wrapped value.
    (This only excludes special cases like method-wrappers, e.g., __hash__.)
    The sole additional attribute is the lazy_self function which holds the
    return value (or, prior to evaluation, func and arguments), in its closure.
    """
    def __init__(self, func: Any, *args: Any, **kwargs: Any) -> None: ...
    def __getattribute__(self, name: Any) -> Any: ...
    def __setattr__(self, name: Any, value: Any) -> None: ...

RegExp: Incomplete

def load_yaml_guess_indent(stream: StreamTextType, **kw: Any) -> Any:
    """guess the indent and block sequence indent of yaml stream/string

    returns round_trip_loaded stream, indent level, block sequence indent
    - block sequence indent is the number of spaces before a dash relative to previous indent
    - if there are no block sequences, indent is taken from nested mappings, block sequence
      indent is unset (None) in that case
    """
def configobj_walker(cfg: Any) -> Any:
    """
    walks over a ConfigObj (INI file with comments) generating
    corresponding YAML output (including comments
    """
