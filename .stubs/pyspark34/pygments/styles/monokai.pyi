from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Literal as Literal, Name as Name, Number as Number, Operator as Operator, Other as Other, Punctuation as Punctuation, String as String, Token as Token, Whitespace as Whitespace

class MonokaiStyle(Style):
    """
    This style mimics the Monokai color scheme.
    """
    background_color: str
    highlight_color: str
    styles: Incomplete
