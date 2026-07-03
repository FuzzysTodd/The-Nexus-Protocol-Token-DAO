from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Literal as Literal, Name as Name, Number as Number, Operator as Operator, String as String, Text as Text, Token as Token

RED_2: str
RED_3: str
RED_9: str
ORANGE_2: str
ORANGE_3: str
GREEN_1: str
GREEN_2: str
GREEN_7: str
BLUE_1: str
BLUE_2: str
PURPLE_2: str
GRAY_3: str
GRAY_4: str
FG_SUBTLE: str
FG_DEFAULT: str
BG_DEFAULT: str
DANGER_FG: str

class GhDarkStyle(Style):
    """
    Github's Dark-Colorscheme based theme for Pygments
    """
    background_color = BG_DEFAULT
    highlight_color = GRAY_4
    line_number_special_color = FG_DEFAULT
    line_number_special_background_color = FG_SUBTLE
    line_number_color = GRAY_4
    line_number_background_color = BG_DEFAULT
    styles: Incomplete
