from .align import AlignMethod as AlignMethod
from .cells import cell_len as cell_len, set_cell_size as set_cell_size
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .style import Style as Style
from .text import Text as Text
from _typeshed import Incomplete

class Rule(JupyterMixin):
    '''A console renderable to draw a horizontal rule (line).

    Args:
        title (Union[str, Text], optional): Text to render in the rule. Defaults to "".
        characters (str, optional): Character(s) used to draw the line. Defaults to "─".
        style (StyleType, optional): Style of Rule. Defaults to "rule.line".
        end (str, optional): Character at end of Rule. defaults to "\\\\n"
        align (str, optional): How to align the title, one of "left", "center", or "right". Defaults to "center".
    '''
    title: Incomplete
    characters: Incomplete
    style: Incomplete
    end: Incomplete
    align: Incomplete
    def __init__(self, title: str | Text = '', *, characters: str = '─', style: str | Style = 'rule.line', end: str = '\n', align: AlignMethod = 'center') -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
