from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Whitespace as Whitespace

class PerldocStyle(Style):
    """
    Style similar to the style used in the perldoc code blocks.
    """
    background_color: str
    styles: Incomplete
