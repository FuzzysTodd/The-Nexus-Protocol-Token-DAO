from _typeshed import Incomplete
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.layout.containers import Container, Window
from prompt_toolkit.layout.controls import UIContent, UIControl
from typing import Any

__all__ = ['ArgToolbar', 'CompletionsToolbar', 'FormattedTextToolbar', 'SearchToolbar', 'SystemToolbar', 'ValidationToolbar']

E = KeyPressEvent

class FormattedTextToolbar(Window):
    def __init__(self, text: AnyFormattedText, style: str = '', **kw: Any) -> None: ...

class SystemToolbar:
    """
    Toolbar for a system prompt.

    :param prompt: Prompt to be displayed to the user.
    """
    prompt: Incomplete
    enable_global_bindings: Incomplete
    system_buffer: Incomplete
    buffer_control: Incomplete
    window: Incomplete
    container: Incomplete
    def __init__(self, prompt: AnyFormattedText = 'Shell command: ', enable_global_bindings: FilterOrBool = True) -> None: ...
    def __pt_container__(self) -> Container: ...

class ArgToolbar:
    window: Incomplete
    container: Incomplete
    def __init__(self) -> None: ...
    def __pt_container__(self) -> Container: ...

class SearchToolbar:
    """
    :param vi_mode: Display '/' and '?' instead of I-search.
    :param ignore_case: Search case insensitive.
    """
    search_buffer: Incomplete
    control: Incomplete
    container: Incomplete
    def __init__(self, search_buffer: Buffer | None = None, vi_mode: bool = False, text_if_not_searching: AnyFormattedText = '', forward_search_prompt: AnyFormattedText = 'I-search: ', backward_search_prompt: AnyFormattedText = 'I-search backward: ', ignore_case: FilterOrBool = False) -> None: ...
    def __pt_container__(self) -> Container: ...

class _CompletionsToolbarControl(UIControl):
    def create_content(self, width: int, height: int) -> UIContent: ...

class CompletionsToolbar:
    container: Incomplete
    def __init__(self) -> None: ...
    def __pt_container__(self) -> Container: ...

class ValidationToolbar:
    control: Incomplete
    container: Incomplete
    def __init__(self, show_position: bool = False) -> None: ...
    def __pt_container__(self) -> Container: ...
