from _typeshed import Incomplete
from dataclasses import dataclass
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from typing import Any, Callable, List

__all__ = ['create_ipython_shortcuts']

@dataclass
class BaseBinding:
    command: Callable[[KeyPressEvent], Any]
    keys: List[str]
    def __init__(self, command, keys) -> None: ...

@dataclass
class RuntimeBinding(BaseBinding):
    filter: Condition
    def __init__(self, command, keys, filter) -> None: ...

@dataclass
class Binding(BaseBinding):
    condition: str | None = ...
    filter = ...
    def __post_init__(self) -> None: ...
    def __init__(self, command, keys, condition) -> None: ...

def create_ipython_shortcuts(shell, skip: Incomplete | None = None) -> KeyBindings:
    """Set up the prompt_toolkit keyboard shortcuts for IPython.

    Parameters
    ----------
    shell: InteractiveShell
        The current IPython shell Instance
    skip: List[Binding]
        Bindings to skip.

    Returns
    -------
    KeyBindings
        the keybinding instance for prompt toolkit.

    """
