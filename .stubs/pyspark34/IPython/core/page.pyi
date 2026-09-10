from IPython import get_ipython as get_ipython
from IPython.core.error import TryNext as TryNext
from IPython.display import display as display
from IPython.utils import py3compat as py3compat
from IPython.utils.data import chop as chop
from IPython.utils.process import system as system
from IPython.utils.terminal import get_terminal_size as get_terminal_size
from _typeshed import Incomplete

def display_page(strng, start: int = 0, screen_lines: int = 25) -> None:
    """Just display, no paging. screen_lines is ignored."""
def as_hook(page_func):
    """Wrap a pager func to strip the `self` arg

    so it can be called as a hook.
    """

esc_re: Incomplete

def page_dumb(strng, start: int = 0, screen_lines: int = 25) -> None:
    """Very dumb 'pager' in Python, for when nothing else works.

    Only moves forward, same interface as page(), except for pager_cmd and
    mode.
    """
def pager_page(strng, start: int = 0, screen_lines: int = 0, pager_cmd: Incomplete | None = None) -> None:
    """Display a string, piping through a pager after a certain length.

    strng can be a mime-bundle dict, supplying multiple representations,
    keyed by mime-type.

    The screen_lines parameter specifies the number of *usable* lines of your
    terminal screen (total lines minus lines you need to reserve to show other
    information).

    If you set screen_lines to a number <=0, page() will try to auto-determine
    your screen size and will only use up to (screen_size+screen_lines) for
    printing, paging after that. That is, if you want auto-detection but need
    to reserve the bottom 3 lines of the screen, use screen_lines = -3, and for
    auto-detection without any lines reserved simply use screen_lines = 0.

    If a string won't fit in the allowed lines, it is sent through the
    specified pager command. If none given, look for PAGER in the environment,
    and ultimately default to less.

    If no system pager works, the string is sent through a 'dumb pager'
    written in python, very simplistic.
    """
def page(data, start: int = 0, screen_lines: int = 0, pager_cmd: Incomplete | None = None):
    """Display content in a pager, piping through a pager after a certain length.

    data can be a mime-bundle dict, supplying multiple representations,
    keyed by mime-type, or text.

    Pager is dispatched via the `show_in_pager` IPython hook.
    If no hook is registered, `pager_page` will be used.
    """
def page_file(fname, start: int = 0, pager_cmd: Incomplete | None = None) -> None:
    """Page a file, using an optional pager command and starting line.
    """
def get_pager_cmd(pager_cmd: Incomplete | None = None):
    """Return a pager command.

    Makes some attempts at finding an OS-correct one.
    """
def get_pager_start(pager, start):
    """Return the string for paging files with an offset.

    This is the '+N' argument which less and more (under Unix) accept.
    """
def page_more():
    """ Smart pausing between pages

        @return:    True if need print more lines, False if quit
        """
