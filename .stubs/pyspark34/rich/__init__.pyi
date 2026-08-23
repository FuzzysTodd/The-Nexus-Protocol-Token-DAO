from .console import Console
from typing import Any, Callable, IO

__all__ = ['get_console', 'reconfigure', 'print', 'inspect', 'print_json']

def get_console() -> Console:
    """Get a global :class:`~rich.console.Console` instance. This function is used when Rich requires a Console,
    and hasn't been explicitly given one.

    Returns:
        Console: A console instance.
    """
def reconfigure(*args: Any, **kwargs: Any) -> None:
    """Reconfigures the global console by replacing it with another.

    Args:
        *args (Any): Positional arguments for the replacement :class:`~rich.console.Console`.
        **kwargs (Any): Keyword arguments for the replacement :class:`~rich.console.Console`.
    """
def print(*objects: Any, sep: str = ' ', end: str = '\n', file: IO[str] | None = None, flush: bool = False) -> None:
    '''Print object(s) supplied via positional arguments.
    This function has an identical signature to the built-in print.
    For more advanced features, see the :class:`~rich.console.Console` class.

    Args:
        sep (str, optional): Separator between printed objects. Defaults to " ".
        end (str, optional): Character to write at end of output. Defaults to "\\\\n".
        file (IO[str], optional): File to write to, or None for stdout. Defaults to None.
        flush (bool, optional): Has no effect as Rich always flushes output. Defaults to False.

    '''
def print_json(json: str | None = None, *, data: Any = None, indent: None | int | str = 2, highlight: bool = True, skip_keys: bool = False, ensure_ascii: bool = False, check_circular: bool = True, allow_nan: bool = True, default: Callable[[Any], Any] | None = None, sort_keys: bool = False) -> None:
    """Pretty prints JSON. Output will be valid JSON.

    Args:
        json (str): A string containing JSON.
        data (Any): If json is not supplied, then encode this data.
        indent (int, optional): Number of spaces to indent. Defaults to 2.
        highlight (bool, optional): Enable highlighting of output: Defaults to True.
        skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
        ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
        check_circular (bool, optional): Check for circular references. Defaults to True.
        allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
        default (Callable, optional): A callable that converts values that can not be encoded
            in to something that can be JSON encoded. Defaults to None.
        sort_keys (bool, optional): Sort dictionary keys. Defaults to False.
    """
def inspect(obj: Any, *, console: Console | None = None, title: str | None = None, help: bool = False, methods: bool = False, docs: bool = True, private: bool = False, dunder: bool = False, sort: bool = True, all: bool = False, value: bool = True) -> None:
    """Inspect any Python object.

    * inspect(<OBJECT>) to see summarized info.
    * inspect(<OBJECT>, methods=True) to see methods.
    * inspect(<OBJECT>, help=True) to see full (non-abbreviated) help.
    * inspect(<OBJECT>, private=True) to see private attributes (single underscore).
    * inspect(<OBJECT>, dunder=True) to see attributes beginning with double underscore.
    * inspect(<OBJECT>, all=True) to see all attributes.

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
        value (bool, optional): Pretty print value. Defaults to True.
    """
