from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Token as Token, Whitespace as Whitespace

class NativeStyle(Style):
    '''
    Pygments version of the "native" vim theme.
    '''
    background_color: str
    highlight_color: str
    line_number_color: str
    styles: Incomplete
