from prompt_toolkit.key_binding.key_processor import KeyPressEvent

__all__ = ['abort_search', 'accept_search', 'start_reverse_incremental_search', 'start_forward_incremental_search', 'reverse_incremental_search', 'forward_incremental_search', 'accept_search_and_accept_input']

E = KeyPressEvent

def abort_search(event: E) -> None:
    """
    Abort an incremental search and restore the original
    line.
    (Usually bound to ControlG/ControlC.)
    """
def accept_search(event: E) -> None:
    """
    When enter pressed in isearch, quit isearch mode. (Multiline
    isearch would be too complicated.)
    (Usually bound to Enter.)
    """
def start_reverse_incremental_search(event: E) -> None:
    """
    Enter reverse incremental search.
    (Usually ControlR.)
    """
def start_forward_incremental_search(event: E) -> None:
    """
    Enter forward incremental search.
    (Usually ControlS.)
    """
def reverse_incremental_search(event: E) -> None:
    """
    Apply reverse incremental search, but keep search buffer focused.
    """
def forward_incremental_search(event: E) -> None:
    """
    Apply forward incremental search, but keep search buffer focused.
    """
def accept_search_and_accept_input(event: E) -> None:
    """
    Accept the search operation first, then accept the input.
    """
