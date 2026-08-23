from ._importlib import metadata as metadata
from ._itertools import ensure_unique as ensure_unique
from .errors import OptionError as OptionError
from .extern.jaraco.functools import pass_none as pass_none
from .extern.jaraco.text import yield_lines as yield_lines
from .extern.more_itertools import consume as consume

def ensure_valid(ep) -> None:
    """
    Exercise one of the dynamic properties to trigger
    the pattern match.
    """
def load_group(value, group):
    """
    Given a value of an entry point or series of entry points,
    return each as an EntryPoint.
    """
def by_group_and_name(ep): ...
def validate(eps: metadata.EntryPoints):
    """
    Ensure entry points are unique by group and name and validate each.
    """
def load(eps):
    """
    Given a Distribution.entry_points, produce EntryPoints.
    """
def _(eps):
    """
    >>> ep, = load('[console_scripts]\\nfoo=bar')
    >>> ep.group
    'console_scripts'
    >>> ep.name
    'foo'
    >>> ep.value
    'bar'
    """
def render(eps: metadata.EntryPoints): ...
def render_items(eps): ...
