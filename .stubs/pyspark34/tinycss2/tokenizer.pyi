from .ast import AtKeywordToken as AtKeywordToken, Comment as Comment, CurlyBracketsBlock as CurlyBracketsBlock, DimensionToken as DimensionToken, FunctionBlock as FunctionBlock, HashToken as HashToken, IdentToken as IdentToken, LiteralToken as LiteralToken, NumberToken as NumberToken, ParenthesesBlock as ParenthesesBlock, ParseError as ParseError, PercentageToken as PercentageToken, SquareBracketsBlock as SquareBracketsBlock, StringToken as StringToken, URLToken as URLToken, UnicodeRangeToken as UnicodeRangeToken, WhitespaceToken as WhitespaceToken
from .serializer import serialize_string_value as serialize_string_value, serialize_url as serialize_url

def parse_component_value_list(css, skip_comments: bool = False):
    """Parse a list of component values.

    :type css: :obj:`str`
    :param css: A CSS string.
    :type skip_comments: :obj:`bool`
    :param skip_comments:
        Ignore CSS comments.
        The return values (and recursively its blocks and functions)
        will not contain any :class:`~tinycss2.ast.Comment` object.
    :returns: A list of :term:`component values`.

    """
