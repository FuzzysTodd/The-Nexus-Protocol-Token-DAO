from .base import Button
from _typeshed import Incomplete
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.layout.containers import AnyContainer
from prompt_toolkit.layout.dimension import AnyDimension
from typing import Sequence

__all__ = ['Dialog']

class Dialog:
    """
    Simple dialog window. This is the base for input dialogs, message dialogs
    and confirmation dialogs.

    Changing the title and body of the dialog is possible at runtime by
    assigning to the `body` and `title` attributes of this class.

    :param body: Child container object.
    :param title: Text to be displayed in the heading of the dialog.
    :param buttons: A list of `Button` widgets, displayed at the bottom.
    """
    body: Incomplete
    title: Incomplete
    container: Incomplete
    def __init__(self, body: AnyContainer, title: AnyFormattedText = '', buttons: Sequence[Button] | None = None, modal: bool = True, width: AnyDimension = None, with_background: bool = False) -> None: ...
    def __pt_container__(self) -> AnyContainer: ...
