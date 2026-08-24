from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Literal as Literal, Name as Name, Number as Number, Operator as Operator, Punctuation as Punctuation, String as String, Token as Token

class ZenburnStyle(Style):
    """
    Low contrast Zenburn style.
    """
    background_color: str
    highlight_color: str
    line_number_color: str
    line_number_background_color: str
    line_number_special_color: str
    line_number_special_background_color: str
    styles: Incomplete
