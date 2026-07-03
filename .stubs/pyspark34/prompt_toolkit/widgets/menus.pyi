from _typeshed import Incomplete
from prompt_toolkit.key_binding.key_bindings import KeyBindingsBase
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout.containers import AnyContainer, Container, Float
from typing import Callable, Sequence

__all__ = ['MenuContainer', 'MenuItem']

E = KeyPressEvent

class MenuContainer:
    """
    :param floats: List of extra Float objects to display.
    :param menu_items: List of `MenuItem` objects.
    """
    body: Incomplete
    menu_items: Incomplete
    selected_menu: Incomplete
    control: Incomplete
    window: Incomplete
    container: Incomplete
    def __init__(self, body: AnyContainer, menu_items: list[MenuItem], floats: list[Float] | None = None, key_bindings: KeyBindingsBase | None = None) -> None: ...
    @property
    def floats(self) -> list[Float] | None: ...
    def __pt_container__(self) -> Container: ...

class MenuItem:
    text: Incomplete
    handler: Incomplete
    children: Incomplete
    shortcut: Incomplete
    disabled: Incomplete
    selected_item: int
    def __init__(self, text: str = '', handler: Callable[[], None] | None = None, children: list[MenuItem] | None = None, shortcut: Sequence[Keys | str] | None = None, disabled: bool = False) -> None: ...
    @property
    def width(self) -> int: ...
