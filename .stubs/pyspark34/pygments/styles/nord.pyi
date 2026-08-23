from _typeshed import Incomplete
from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, Punctuation as Punctuation, String as String, Text as Text, Token as Token, Whitespace as Whitespace

class NordStyle(Style):
    '''
    Pygments version of the "nord" theme by Arctic Ice Studio.
    '''
    line_number_color: str
    line_number_background_color: str
    line_number_special_color: str
    line_number_special_background_color: str
    background_color: str
    highlight_color: str
    styles: Incomplete

class NordDarkerStyle(Style):
    '''
    Pygments version of a darker "nord" theme by Arctic Ice Studio
    '''
    line_number_color: str
    line_number_background_color: str
    line_number_special_color: str
    line_number_special_background_color: str
    background_color: str
    highlight_color: str
    styles: Incomplete
