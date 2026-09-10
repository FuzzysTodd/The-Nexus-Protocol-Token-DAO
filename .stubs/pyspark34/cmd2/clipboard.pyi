from _typeshed import Incomplete

_: Incomplete
can_clip: bool

def get_paste_buffer() -> str:
    """Get the contents of the clipboard / paste buffer.

    :return: contents of the clipboard
    """
def write_to_paste_buffer(txt: str) -> None:
    """Copy text to the clipboard / paste buffer.

    :param txt: text to copy to the clipboard
    """
