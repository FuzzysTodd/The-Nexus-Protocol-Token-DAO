from .compat import is_posix as is_posix
from .exc import CommandError as CommandError
from typing import Dict

def open_in_editor(filename: str, environ: Dict[str, str] | None = None) -> None:
    """
    Opens the given file in a text editor. If the environment variable
    ``EDITOR`` is set, this is taken as preference.

    Otherwise, a list of commonly installed editors is tried.

    If no editor matches, an :py:exc:`OSError` is raised.

    :param filename: The filename to open. Will be passed  verbatim to the
        editor command.
    :param environ: An optional drop-in replacement for ``os.environ``. Used
        mainly for testing.
    """
