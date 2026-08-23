from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Whitespace as Whitespace

class DefaultStyle(Style):
    """
    The default style (inspired by Emacs 22).
    """
    background_color: str
    styles: Incomplete
