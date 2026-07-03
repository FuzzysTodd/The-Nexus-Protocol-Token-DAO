from ._emoji_codes import EMOJI as EMOJI
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .jupyter import JupyterMixin as JupyterMixin
from .segment import Segment as Segment
from .style import Style as Style
from _typeshed import Incomplete

EmojiVariant: Incomplete

class NoEmoji(Exception):
    """No emoji by that name."""

class Emoji(JupyterMixin):
    VARIANTS: Incomplete
    name: Incomplete
    style: Incomplete
    variant: Incomplete
    def __init__(self, name: str, style: str | Style = 'none', variant: EmojiVariant | None = None) -> None:
        """A single emoji character.

        Args:
            name (str): Name of emoji.
            style (Union[str, Style], optional): Optional style. Defaults to None.

        Raises:
            NoEmoji: If the emoji doesn't exist.
        """
    @classmethod
    def replace(cls, text: str) -> str:
        '''Replace emoji markup with corresponding unicode characters.

        Args:
            text (str): A string with emojis codes, e.g. "Hello :smiley:!"

        Returns:
            str: A string with emoji codes replaces with actual emoji.
        '''
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
