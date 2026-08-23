from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Keyword as Keyword, Name as Name, String as String, Token as Token

class RrtStyle(Style):
    '''
    Minimalistic "rrt" theme, based on Zap and Emacs defaults.
    '''
    background_color: str
    highlight_color: str
    styles: Incomplete
