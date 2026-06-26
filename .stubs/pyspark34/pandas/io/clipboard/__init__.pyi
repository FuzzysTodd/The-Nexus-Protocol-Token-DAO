from _typeshed import Incomplete

__all__ = ['copy', 'paste', 'set_clipboard', 'determine_clipboard']

class CheckedCall:
    def __init__(self, f) -> None: ...
    def __call__(self, *args): ...
    def __setattr__(self, key, value) -> None: ...

def determine_clipboard():
    """
    Determine the OS/platform and set the copy() and paste() functions
    accordingly.
    """
def set_clipboard(clipboard) -> None:
    '''
    Explicitly sets the clipboard mechanism. The "clipboard mechanism" is how
    the copy() and paste() functions interact with the operating system to
    implement the copy/paste feature. The clipboard parameter must be one of:
        - pbcopy
        - pyobjc (default on macOS)
        - qt
        - xclip
        - xsel
        - klipper
        - windows (default on Windows)
        - no (this is what is set when no clipboard mechanism can be found)
    '''

copy: Incomplete
paste: Incomplete
clipboard_get = paste
clipboard_set = copy
