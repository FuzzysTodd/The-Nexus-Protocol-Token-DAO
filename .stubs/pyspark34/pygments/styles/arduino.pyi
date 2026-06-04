from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Whitespace as Whitespace

class ArduinoStyle(Style):
    """
    The Arduino® language style. This style is designed to highlight the
    Arduino source code, so expect the best results with it.
    """
    background_color: str
    styles: Incomplete
