from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Literal as Literal, Name as Name, Number as Number, Operator as Operator, Other as Other, Punctuation as Punctuation, String as String, Text as Text, Whitespace as Whitespace

class DraculaStyle(Style):
    background_color: str
    highlight_color: str
    line_number_color: str
    line_number_background_color: str
    line_number_special_color: str
    line_number_special_background_color: str
    styles: Incomplete
