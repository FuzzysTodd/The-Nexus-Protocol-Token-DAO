from _typeshed import Incomplete
from nltk.tokenize.api import TokenizerI as TokenizerI

class SExprTokenizer(TokenizerI):
    """
    A tokenizer that divides strings into s-expressions.
    An s-expresion can be either:

      - a parenthesized expression, including any nested parenthesized
        expressions, or
      - a sequence of non-whitespace non-parenthesis characters.

    For example, the string ``(a (b c)) d e (f)`` consists of four
    s-expressions: ``(a (b c))``, ``d``, ``e``, and ``(f)``.

    By default, the characters ``(`` and ``)`` are treated as open and
    close parentheses, but alternative strings may be specified.

    :param parens: A two-element sequence specifying the open and close parentheses
        that should be used to find sexprs.  This will typically be either a
        two-character string, or a list of two strings.
    :type parens: str or list
    :param strict: If true, then raise an exception when tokenizing an ill-formed sexpr.
    """
    def __init__(self, parens: str = '()', strict: bool = True) -> None: ...
    def tokenize(self, text):
        """
        Return a list of s-expressions extracted from *text*.
        For example:

            >>> SExprTokenizer().tokenize('(a b (c d)) e f (g)')
            ['(a b (c d))', 'e', 'f', '(g)']

        All parentheses are assumed to mark s-expressions.
        (No special processing is done to exclude parentheses that occur
        inside strings, or following backslash characters.)

        If the given expression contains non-matching parentheses,
        then the behavior of the tokenizer depends on the ``strict``
        parameter to the constructor.  If ``strict`` is ``True``, then
        raise a ``ValueError``.  If ``strict`` is ``False``, then any
        unmatched close parentheses will be listed as their own
        s-expression; and the last partial s-expression with unmatched open
        parentheses will be listed as its own s-expression:

            >>> SExprTokenizer(strict=False).tokenize('c) d) e (f (g')
            ['c', ')', 'd', ')', 'e', '(f (g']

        :param text: the string to be tokenized
        :type text: str or iter(str)
        :rtype: iter(str)
        """

sexpr_tokenize: Incomplete
