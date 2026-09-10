import click
from _typeshed import Incomplete
from rich.console import RenderableType as RenderableType
from rich.highlighter import RegexHighlighter
from typing import Literal

STYLE_OPTION: str
STYLE_SWITCH: str
STYLE_NEGATIVE_OPTION: str
STYLE_NEGATIVE_SWITCH: str
STYLE_METAVAR: str
STYLE_METAVAR_SEPARATOR: str
STYLE_USAGE: str
STYLE_USAGE_COMMAND: str
STYLE_DEPRECATED: str
STYLE_DEPRECATED_COMMAND: str
STYLE_HELPTEXT_FIRST_LINE: str
STYLE_HELPTEXT: str
STYLE_OPTION_HELP: str
STYLE_OPTION_DEFAULT: str
STYLE_OPTION_ENVVAR: str
STYLE_REQUIRED_SHORT: str
STYLE_REQUIRED_LONG: str
STYLE_OPTIONS_PANEL_BORDER: str
ALIGN_OPTIONS_PANEL: Literal['left', 'center', 'right']
STYLE_OPTIONS_TABLE_SHOW_LINES: bool
STYLE_OPTIONS_TABLE_LEADING: int
STYLE_OPTIONS_TABLE_PAD_EDGE: bool
STYLE_OPTIONS_TABLE_PADDING: Incomplete
STYLE_OPTIONS_TABLE_BOX: str
STYLE_OPTIONS_TABLE_ROW_STYLES: Incomplete
STYLE_OPTIONS_TABLE_BORDER_STYLE: Incomplete
STYLE_COMMANDS_PANEL_BORDER: str
ALIGN_COMMANDS_PANEL: Literal['left', 'center', 'right']
STYLE_COMMANDS_TABLE_SHOW_LINES: bool
STYLE_COMMANDS_TABLE_LEADING: int
STYLE_COMMANDS_TABLE_PAD_EDGE: bool
STYLE_COMMANDS_TABLE_PADDING: Incomplete
STYLE_COMMANDS_TABLE_BOX: str
STYLE_COMMANDS_TABLE_ROW_STYLES: Incomplete
STYLE_COMMANDS_TABLE_BORDER_STYLE: Incomplete
STYLE_ERRORS_PANEL_BORDER: str
ALIGN_ERRORS_PANEL: Literal['left', 'center', 'right']
STYLE_ERRORS_SUGGESTION: str
STYLE_ABORTED: str
MAX_WIDTH: Incomplete
COLOR_SYSTEM: Literal['auto', 'standard', '256', 'truecolor', 'windows'] | None
FORCE_TERMINAL: Incomplete
DEPRECATED_STRING: str
DEFAULT_STRING: str
ENVVAR_STRING: str
REQUIRED_SHORT_STRING: str
REQUIRED_LONG_STRING: str
RANGE_STRING: str
ARGUMENTS_PANEL_TITLE: str
OPTIONS_PANEL_TITLE: str
COMMANDS_PANEL_TITLE: str
ERRORS_PANEL_TITLE: str
ABORTED_TEXT: str
MARKUP_MODE_MARKDOWN: str
MARKUP_MODE_RICH: str
MarkupMode: Incomplete

class OptionHighlighter(RegexHighlighter):
    """Highlights our special options."""
    highlights: Incomplete

class NegativeOptionHighlighter(RegexHighlighter):
    highlights: Incomplete

highlighter: Incomplete
negative_highlighter: Incomplete

def rich_format_help(*, obj: click.Command | click.Group, ctx: click.Context, markup_mode: MarkupMode) -> None:
    """Print nicely formatted help text using rich.

    Based on original code from rich-cli, by @willmcgugan.
    https://github.com/Textualize/rich-cli/blob/8a2767c7a340715fc6fbf4930ace717b9b2fc5e5/src/rich_cli/__main__.py#L162-L236

    Replacement for the click function format_help().
    Takes a command or group and builds the help text output.
    """
def rich_format_error(self) -> None:
    """Print richly formatted click errors.

    Called by custom exception handler to print richly formatted click errors.
    Mimics original click.ClickException.echo() function but with rich formatting.
    """
def rich_abort_error() -> None:
    """Print richly formatted abort error."""
