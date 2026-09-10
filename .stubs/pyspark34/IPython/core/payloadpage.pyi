from IPython.core.getipython import get_ipython as get_ipython
from _typeshed import Incomplete

def page(strng, start: int = 0, screen_lines: int = 0, pager_cmd: Incomplete | None = None) -> None:
    """Print a string, piping through a pager.

    This version ignores the screen_lines and pager_cmd arguments and uses
    IPython's payload system instead.

    Parameters
    ----------
    strng : str or mime-dict
        Text to page, or a mime-type keyed dict of already formatted data.
    start : int
        Starting line at which to place the display.
    """
def install_payload_page() -> None:
    """DEPRECATED, use show_in_pager hook

    Install this version of page as IPython.core.page.page.
    """
