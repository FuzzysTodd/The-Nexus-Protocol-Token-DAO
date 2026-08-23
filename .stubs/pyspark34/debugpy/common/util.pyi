from _typeshed import Incomplete

def evaluate(code, path=..., mode: str = 'eval'): ...

class Observable:
    """An object with change notifications."""
    observers: Incomplete
    def __init__(self) -> None: ...
    def __setattr__(self, name, value): ...

class Env(dict):
    """A dict for environment variables."""
    @staticmethod
    def snapshot():
        """Returns a snapshot of the current environment."""
    def copy(self, updated_from: Incomplete | None = None): ...
    def prepend_to(self, key, entry) -> None:
        """Prepends a new entry to a PATH-style environment variable, creating
        it if it doesn't exist already.
        """

def force_str(s, encoding, errors: str = 'strict'):
    """Converts s to str, using the provided encoding. If s is already str,
    it is returned as is.
    """
def force_bytes(s, encoding, errors: str = 'strict'):
    '''Converts s to bytes, using the provided encoding. If s is already bytes,
    it is returned as is.

    If errors="strict" and s is bytes, its encoding is verified by decoding it;
    UnicodeError is raised if it cannot be decoded.
    '''
def force_ascii(s, errors: str = 'strict'):
    '''Same as force_bytes(s, "ascii", errors)'''
def force_utf8(s, errors: str = 'strict'):
    '''Same as force_bytes(s, "utf8", errors)'''
def nameof(obj, quote: bool = False):
    """Returns the most descriptive name of a Python module, class, or function,
    as a Unicode string

    If quote=True, name is quoted with repr().

    Best-effort, but guaranteed to not fail - always returns something.
    """
def srcnameof(obj):
    """Returns the most descriptive name of a Python module, class, or function,
    including source information (filename and linenumber), if available.

    Best-effort, but guaranteed to not fail - always returns something.
    """
def hide_debugpy_internals():
    """Returns True if the caller should hide something from debugpy."""
def hide_thread_from_debugger(thread) -> None:
    """Disables tracing for the given thread if DEBUGPY_TRACE_DEBUGPY is not set.
    DEBUGPY_TRACE_DEBUGPY is used to debug debugpy with debugpy
    """
