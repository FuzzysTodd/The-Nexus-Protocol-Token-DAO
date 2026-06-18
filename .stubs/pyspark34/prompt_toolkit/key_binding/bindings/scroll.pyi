from prompt_toolkit.key_binding.key_processor import KeyPressEvent

__all__ = ['scroll_forward', 'scroll_backward', 'scroll_half_page_up', 'scroll_half_page_down', 'scroll_one_line_up', 'scroll_one_line_down']

E = KeyPressEvent

def scroll_forward(event: E, half: bool = False) -> None:
    """
    Scroll window down.
    """
def scroll_backward(event: E, half: bool = False) -> None:
    """
    Scroll window up.
    """
def scroll_half_page_down(event: E) -> None:
    """
    Same as ControlF, but only scroll half a page.
    """
def scroll_half_page_up(event: E) -> None:
    """
    Same as ControlB, but only scroll half a page.
    """
def scroll_one_line_down(event: E) -> None:
    """
    scroll_offset += 1
    """
def scroll_one_line_up(event: E) -> None:
    """
    scroll_offset -= 1
    """
