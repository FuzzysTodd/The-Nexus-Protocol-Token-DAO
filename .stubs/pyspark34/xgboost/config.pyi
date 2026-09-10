from ._typing import _F
from .core import c_str as c_str, py_str as py_str
from typing import Any, Callable, Dict, Iterator

def config_doc(*, header: str | None = None, extra_note: str | None = None, parameters: str | None = None, returns: str | None = None, see_also: str | None = None) -> Callable[[_F], _F]:
    """Decorator to format docstring for config functions.

    Parameters
    ----------
    header: str
        An introducion to the function
    extra_note: str
        Additional notes
    parameters: str
        Parameters of the function
    returns: str
        Return value
    see_also: str
        Related functions
    """
def set_config(**new_config: Any) -> None: ...
def get_config() -> Dict[str, Any]: ...
def config_context(**new_config: Any) -> Iterator[None]: ...
