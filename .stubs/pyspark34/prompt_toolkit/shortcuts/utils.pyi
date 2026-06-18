from prompt_toolkit.layout.containers import AnyContainer
from prompt_toolkit.output import ColorDepth, Output
from prompt_toolkit.styles import BaseStyle, StyleTransformation
from typing import Any, TextIO

__all__ = ['print_formatted_text', 'print_container', 'clear', 'set_title', 'clear_title']

def print_formatted_text(*values: Any, sep: str = ' ', end: str = '\n', file: TextIO | None = None, flush: bool = False, style: BaseStyle | None = None, output: Output | None = None, color_depth: ColorDepth | None = None, style_transformation: StyleTransformation | None = None, include_default_pygments_style: bool = True) -> None:
    """
    ::

        print_formatted_text(*values, sep=' ', end='\\n', file=None, flush=False, style=None, output=None)

    Print text to stdout. This is supposed to be compatible with Python's print
    function, but supports printing of formatted text. You can pass a
    :class:`~prompt_toolkit.formatted_text.FormattedText`,
    :class:`~prompt_toolkit.formatted_text.HTML` or
    :class:`~prompt_toolkit.formatted_text.ANSI` object to print formatted
    text.

    * Print HTML as follows::

        print_formatted_text(HTML('<i>Some italic text</i> <ansired>This is red!</ansired>'))

        style = Style.from_dict({
            'hello': '#ff0066',
            'world': '#884444 italic',
        })
        print_formatted_text(HTML('<hello>Hello</hello> <world>world</world>!'), style=style)

    * Print a list of (style_str, text) tuples in the given style to the
      output.  E.g.::

        style = Style.from_dict({
            'hello': '#ff0066',
            'world': '#884444 italic',
        })
        fragments = FormattedText([
            ('class:hello', 'Hello'),
            ('class:world', 'World'),
        ])
        print_formatted_text(fragments, style=style)

    If you want to print a list of Pygments tokens, wrap it in
    :class:`~prompt_toolkit.formatted_text.PygmentsTokens` to do the
    conversion.

    If a prompt_toolkit `Application` is currently running, this will always
    print above the application or prompt (similar to `patch_stdout`). So,
    `print_formatted_text` will erase the current application, print the text,
    and render the application again.

    :param values: Any kind of printable object, or formatted string.
    :param sep: String inserted between values, default a space.
    :param end: String appended after the last value, default a newline.
    :param style: :class:`.Style` instance for the color scheme.
    :param include_default_pygments_style: `bool`. Include the default Pygments
        style when set to `True` (the default).
    """
def print_container(container: AnyContainer, file: TextIO | None = None, style: BaseStyle | None = None, include_default_pygments_style: bool = True) -> None:
    """
    Print any layout to the output in a non-interactive way.

    Example usage::

        from prompt_toolkit.widgets import Frame, TextArea
        print_container(
            Frame(TextArea(text='Hello world!')))
    """
def clear() -> None:
    """
    Clear the screen.
    """
def set_title(text: str) -> None:
    """
    Set the terminal title.
    """
def clear_title() -> None:
    """
    Erase the current title.
    """
