from _typeshed import Incomplete
from typing import Any, Dict

def unicode_std_stream(stream: str = 'stdout'):
    """Get a wrapper to write unicode to stdout/stderr as UTF-8.

    This ignores environment variables and default encodings, to reliably write
    unicode to stdout or stderr.

    ::

        unicode_std_stream().write(u'ł@e¶ŧ←')
    """
def unicode_stdin_stream():
    """Get a wrapper to read unicode from stdin as UTF-8.

    This ignores environment variables and default encodings, to reliably read unicode from stdin.

    ::

        totreat = unicode_stdin_stream().read()
    """

class FormatSafeDict(Dict[Any, Any]):
    """Format a dictionary safely."""
    def __missing__(self, key):
        """Handle missing value."""

ENOLINK: Incomplete

def link(src, dst):
    """Hard links ``src`` to ``dst``, returning 0 or errno.

    Note that the special errno ``ENOLINK`` will be returned if ``os.link`` isn't
    supported by the operating system.
    """
def link_or_copy(src, dst) -> None:
    """Attempts to hardlink ``src`` to ``dst``, copying if the link fails.

    Attempts to maintain the semantics of ``shutil.copy``.

    Because ``os.link`` does not overwrite files, a unique temporary file
    will be used if the target already exists, then that file will be moved
    into place.
    """
