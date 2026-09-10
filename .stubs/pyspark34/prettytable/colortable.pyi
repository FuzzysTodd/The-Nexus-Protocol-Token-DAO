from .prettytable import PrettyTable as PrettyTable
from _typeshed import Incomplete

RESET_CODE: str

class Theme:
    default_color: Incomplete
    vertical_char: Incomplete
    vertical_color: Incomplete
    horizontal_char: Incomplete
    horizontal_color: Incomplete
    junction_char: Incomplete
    junction_color: Incomplete
    def __init__(self, default_color: str = '', vertical_char: str = '|', vertical_color: str = '', horizontal_char: str = '-', horizontal_color: str = '', junction_char: str = '+', junction_color: str = '') -> None: ...
    @staticmethod
    def format_code(s: str) -> str:
        """Takes string and intelligently puts it into an ANSI escape sequence"""

class Themes:
    DEFAULT: Incomplete
    OCEAN: Incomplete

class ColorTable(PrettyTable):
    def __init__(self, field_names: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def theme(self) -> Theme: ...
    @theme.setter
    def theme(self, value: Theme): ...
    def update_theme(self) -> None: ...
    def get_string(self, **kwargs) -> str: ...
