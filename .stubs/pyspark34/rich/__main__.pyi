from rich import box as box
from rich.color import Color as Color
from rich.console import Console as Console, ConsoleOptions as ConsoleOptions, Group as Group, RenderResult as RenderResult, RenderableType as RenderableType
from rich.markdown import Markdown as Markdown
from rich.measure import Measurement as Measurement
from rich.pretty import Pretty as Pretty
from rich.segment import Segment as Segment
from rich.style import Style as Style
from rich.syntax import Syntax as Syntax
from rich.table import Table as Table
from rich.text import Text as Text

class ColorBox:
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...

def make_test_card() -> Table:
    """Get a renderable that demonstrates a number of features."""
