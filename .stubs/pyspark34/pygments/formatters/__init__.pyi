import types
from _typeshed import Incomplete
from collections.abc import Generator
from pygments.formatters._mapping import FORMATTERS as FORMATTERS
from pygments.plugin import find_plugin_formatters as find_plugin_formatters
from pygments.util import ClassNotFound as ClassNotFound

def get_all_formatters() -> Generator[Incomplete, None, None]:
    """Return a generator for all formatter classes."""
def find_formatter_class(alias):
    """Lookup a formatter by alias.

    Returns None if not found.
    """
def get_formatter_by_name(_alias, **options):
    """
    Return an instance of a :class:`.Formatter` subclass that has `alias` in its
    aliases list. The formatter is given the `options` at its instantiation.

    Will raise :exc:`pygments.util.ClassNotFound` if no formatter with that
    alias is found.
    """
def load_formatter_from_file(filename, formattername: str = 'CustomFormatter', **options):
    """
    Return a `Formatter` subclass instance loaded from the provided file, relative
    to the current directory.

    The file is expected to contain a Formatter class named ``formattername``
    (by default, CustomFormatter). Users should be very careful with the input, because
    this method is equivalent to running ``eval()`` on the input file. The formatter is
    given the `options` at its instantiation.

    :exc:`pygments.util.ClassNotFound` is raised if there are any errors loading
    the formatter.

    .. versionadded:: 2.2
    """
def get_formatter_for_filename(fn, **options):
    """
    Return a :class:`.Formatter` subclass instance that has a filename pattern
    matching `fn`. The formatter is given the `options` at its instantiation.

    Will raise :exc:`pygments.util.ClassNotFound` if no formatter for that filename
    is found.
    """

class _automodule(types.ModuleType):
    """Automatically import formatters."""
    def __getattr__(self, name): ...

oldmod: Incomplete
newmod: Incomplete
