from _typeshed import Incomplete
from pygments.token import STANDARD_TYPES as STANDARD_TYPES, Token as Token

ansicolors: Incomplete

class StyleMeta(type):
    def __new__(mcs, name, bases, dct): ...
    def style_for_token(cls, token): ...
    def list_styles(cls): ...
    def styles_token(cls, ttype): ...
    def __iter__(cls): ...
    def __len__(cls) -> int: ...

class Style(metaclass=StyleMeta):
    background_color: str
    highlight_color: str
    line_number_color: str
    line_number_background_color: str
    line_number_special_color: str
    line_number_special_background_color: str
    styles: Incomplete
    web_style_gallery_exclude: bool
