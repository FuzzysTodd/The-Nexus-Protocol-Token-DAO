from _typeshed import Incomplete
from ctypes.wintypes import HANDLE as HANDLE
from enum import Enum

class RlType(Enum):
    """Readline library types we recognize"""
    GNU: int
    PYREADLINE: int
    NONE: int

rl_type: Incomplete
vt100_support: bool

def enable_win_vt100(handle: HANDLE) -> bool:
    """
            Enables VT100 character sequences in a Windows console
            This only works on Windows 10 and up
            :param handle: the handle on which to enable vt100
            :return: True if vt100 characters are enabled for the handle
            """

STD_OUT_HANDLE: int
STD_ERROR_HANDLE: int
vt100_stdout_support: Incomplete
vt100_stderr_support: Incomplete

def pyreadline_remove_history_item(pos: int) -> None:
    """
            An implementation of remove_history_item() for pyreadline3
            :param pos: The 0-based position in history to remove
            """

readline_lib: Incomplete
rl_warning: Incomplete

def rl_force_redisplay() -> None:
    """
    Causes readline to display the prompt and input text wherever the cursor is and start
    reading input from this location. This is the proper way to restore the input line after
    printing to the screen
    """
def rl_get_point() -> int:
    """
    Returns the offset of the current cursor position in rl_line_buffer
    """
def rl_get_prompt() -> str:
    """Gets Readline's current prompt"""
def rl_set_prompt(prompt: str) -> None:
    """
    Sets Readline's prompt
    :param prompt: the new prompt value
    """
def rl_escape_prompt(prompt: str) -> str:
    """Overcome bug in GNU Readline in relation to calculation of prompt length in presence of ANSI escape codes

    :param prompt: original prompt
    :return: prompt safe to pass to GNU Readline
    """
def rl_unescape_prompt(prompt: str) -> str:
    """Remove escape characters from a Readline prompt"""
