from .console import Group as Group, RenderableType as RenderableType
from .control import escape_control_codes as escape_control_codes
from .highlighter import ReprHighlighter as ReprHighlighter
from .jupyter import JupyterMixin as JupyterMixin
from .panel import Panel as Panel
from .pretty import Pretty as Pretty
from .table import Table as Table
from .text import Text as Text, TextType as TextType
from _typeshed import Incomplete
from typing import Any, Collection, Tuple, Type

class Inspect(JupyterMixin):
    """A renderable to inspect any Python Object.

    Args:
        obj (Any): An object to inspect.
        title (str, optional): Title to display over inspect result, or None use type. Defaults to None.
        help (bool, optional): Show full help text rather than just first paragraph. Defaults to False.
        methods (bool, optional): Enable inspection of callables. Defaults to False.
        docs (bool, optional): Also render doc strings. Defaults to True.
        private (bool, optional): Show private attributes (beginning with underscore). Defaults to False.
        dunder (bool, optional): Show attributes starting with double underscore. Defaults to False.
        sort (bool, optional): Sort attributes alphabetically. Defaults to True.
        all (bool, optional): Show all attributes. Defaults to False.
        value (bool, optional): Pretty print value of object. Defaults to True.
    """
    highlighter: Incomplete
    obj: Incomplete
    title: Incomplete
    help: Incomplete
    methods: Incomplete
    docs: Incomplete
    private: Incomplete
    dunder: Incomplete
    sort: Incomplete
    value: Incomplete
    def __init__(self, obj: Any, *, title: TextType | None = None, help: bool = False, methods: bool = False, docs: bool = True, private: bool = False, dunder: bool = False, sort: bool = True, all: bool = True, value: bool = True) -> None: ...
    def __rich__(self) -> Panel: ...

def get_object_types_mro(obj: object | Type[Any]) -> Tuple[type, ...]:
    """Returns the MRO of an object's class, or of the object itself if it's a class."""
def get_object_types_mro_as_strings(obj: object) -> Collection[str]:
    """
    Returns the MRO of an object's class as full qualified names, or of the object itself if it's a class.

    Examples:
        `object_types_mro_as_strings(JSONDecoder)` will return `['json.decoder.JSONDecoder', 'builtins.object']`
    """
def is_object_one_of_types(obj: object, fully_qualified_types_names: Collection[str]) -> bool:
    """
    Returns `True` if the given object's class (or the object itself, if it's a class) has one of the
    fully qualified names in its MRO.
    """
