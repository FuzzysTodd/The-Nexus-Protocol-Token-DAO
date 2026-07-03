from _typeshed import Incomplete
from collections.abc import Generator
from pygments.plugin import find_plugin_styles as find_plugin_styles
from pygments.util import ClassNotFound as ClassNotFound

STYLE_MAP: Incomplete

def get_style_by_name(name):
    """
    Return a style class by its short name. The names of the builtin styles
    are listed in :data:`pygments.styles.STYLE_MAP`.

    Will raise :exc:`pygments.util.ClassNotFound` if no style of that name is
    found.
    """
def get_all_styles() -> Generator[Incomplete, Incomplete, None]:
    """Return a generator for all styles by name, both builtin and plugin."""
