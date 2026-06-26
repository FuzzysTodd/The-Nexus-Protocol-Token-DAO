from _typeshed import Incomplete
from typing import Any, Iterable

def __getattr__(name: str) -> list[str]: ...

ATTRIBUTES: Incomplete
HIGHLIGHTS: Incomplete
COLORS: Incomplete
RESET: str

def colored(text: str, color: str | None = None, on_color: str | None = None, attrs: Iterable[str] | None = None, *, no_color: bool | None = None, force_color: bool | None = None) -> str:
    """Colorize text.

    Available text colors:
        black, red, green, yellow, blue, magenta, cyan, white,
        light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
        light_magenta, light_cyan.

    Available text highlights:
        on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white,
        on_light_grey, on_dark_grey, on_light_red, on_light_green, on_light_yellow,
        on_light_blue, on_light_magenta, on_light_cyan.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.

    Example:
        colored('Hello, World!', 'red', 'on_black', ['bold', 'blink'])
        colored('Hello, World!', 'green')
    """
def cprint(text: str, color: str | None = None, on_color: str | None = None, attrs: Iterable[str] | None = None, *, no_color: bool | None = None, force_color: bool | None = None, **kwargs: Any) -> None:
    """Print colorized text.

    It accepts arguments of print function.
    """
