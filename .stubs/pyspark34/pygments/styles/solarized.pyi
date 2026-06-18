from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Token as Token

def make_style(colors): ...

DARK_COLORS: Incomplete
LIGHT_COLORS: Incomplete

class SolarizedDarkStyle(Style):
    """
    The solarized style, dark.
    """
    styles: Incomplete
    background_color: Incomplete
    highlight_color: Incomplete
    line_number_color: Incomplete
    line_number_background_color: Incomplete

class SolarizedLightStyle(SolarizedDarkStyle):
    """
    The solarized style, light.
    """
    styles: Incomplete
    background_color: Incomplete
    highlight_color: Incomplete
    line_number_color: Incomplete
    line_number_background_color: Incomplete
