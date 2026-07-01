from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, String as String, Token as Token, Whitespace as Whitespace

class FruityStyle(Style):
    '''
    Pygments version of the "native" vim theme.
    '''
    background_color: str
    highlight_color: str
    styles: Incomplete
