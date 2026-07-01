from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Whitespace as Whitespace

class FriendlyGrayscaleStyle(Style):
    """
    A modern grayscale style based on the friendly style.

    .. versionadded:: 2.11
    """
    background_color: str
    styles: Incomplete
