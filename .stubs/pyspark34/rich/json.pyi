from .highlighter import JSONHighlighter as JSONHighlighter, NullHighlighter as NullHighlighter
from .text import Text as Text
from _typeshed import Incomplete
from typing import Any, Callable

class JSON:
    """A renderable which pretty prints JSON.

    Args:
        json (str): JSON encoded data.
        indent (Union[None, int, str], optional): Number of characters to indent by. Defaults to 2.
        highlight (bool, optional): Enable highlighting. Defaults to True.
        skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
        ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
        check_circular (bool, optional): Check for circular references. Defaults to True.
        allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
        default (Callable, optional): A callable that converts values that can not be encoded
            in to something that can be JSON encoded. Defaults to None.
        sort_keys (bool, optional): Sort dictionary keys. Defaults to False.
    """
    text: Incomplete
    def __init__(self, json: str, indent: None | int | str = 2, highlight: bool = True, skip_keys: bool = False, ensure_ascii: bool = False, check_circular: bool = True, allow_nan: bool = True, default: Callable[[Any], Any] | None = None, sort_keys: bool = False) -> None: ...
    @classmethod
    def from_data(cls, data: Any, indent: None | int | str = 2, highlight: bool = True, skip_keys: bool = False, ensure_ascii: bool = False, check_circular: bool = True, allow_nan: bool = True, default: Callable[[Any], Any] | None = None, sort_keys: bool = False) -> JSON:
        """Encodes a JSON object from arbitrary data.

        Args:
            data (Any): An object that may be encoded in to JSON
            indent (Union[None, int, str], optional): Number of characters to indent by. Defaults to 2.
            highlight (bool, optional): Enable highlighting. Defaults to True.
            default (Callable, optional): Optional callable which will be called for objects that cannot be serialized. Defaults to None.
            skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
            ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
            check_circular (bool, optional): Check for circular references. Defaults to True.
            allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
            default (Callable, optional): A callable that converts values that can not be encoded
                in to something that can be JSON encoded. Defaults to None.
            sort_keys (bool, optional): Sort dictionary keys. Defaults to False.

        Returns:
            JSON: New JSON object from the given data.
        """
    def __rich__(self) -> Text: ...
