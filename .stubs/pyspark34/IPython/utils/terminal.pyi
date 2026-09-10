from _typeshed import Incomplete

ignore_termtitle: bool

def toggle_set_term_title(val) -> None:
    """Control whether set_term_title is active or not.

    set_term_title() allows writing to the console titlebar.  In embedded
    widgets this can cause problems, so this call can be used to toggle it on
    or off as needed.

    The default state of the module is for the function to be disabled.

    Parameters
    ----------
    val : bool
        If True, set_term_title() actually writes to the terminal (using the
        appropriate platform-specific module).  If False, it is a no-op.
    """

TERM: Incomplete

def set_term_title(title) -> None:
    """Set terminal title using the necessary platform-dependent calls."""
def restore_term_title() -> None:
    """Restore, if possible, terminal title to the original state"""
def freeze_term_title() -> None: ...
def get_terminal_size(defaultx: int = 80, defaulty: int = 25): ...
