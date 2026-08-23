import abc
from _typeshed import Incomplete
from collections.abc import Generator
from nltk.tokenize.api import StringTokenizer as StringTokenizer, TokenizerI as TokenizerI
from nltk.tokenize.util import regexp_span_tokenize as regexp_span_tokenize, string_span_tokenize as string_span_tokenize

class SpaceTokenizer(StringTokenizer):
    '''Tokenize a string using the space character as a delimiter,
    which is the same as ``s.split(\' \')``.

        >>> from nltk.tokenize import SpaceTokenizer
        >>> s = "Good muffins cost $3.88\\nin New York.  Please buy me\\ntwo of them.\\n\\nThanks."
        >>> SpaceTokenizer().tokenize(s) # doctest: +NORMALIZE_WHITESPACE
        [\'Good\', \'muffins\', \'cost\', \'$3.88\\nin\', \'New\', \'York.\', \'\',
        \'Please\', \'buy\', \'me\\ntwo\', \'of\', \'them.\\n\\nThanks.\']
    '''
class TabTokenizer(StringTokenizer):
    """Tokenize a string use the tab character as a delimiter,
    the same as ``s.split('\\t')``.

        >>> from nltk.tokenize import TabTokenizer
        >>> TabTokenizer().tokenize('a\\tb c\\n\\t d')
        ['a', 'b c\\n', ' d']
    """

class CharTokenizer(StringTokenizer, metaclass=abc.ABCMeta):
    """Tokenize a string into individual characters.  If this functionality
    is ever required directly, use ``for char in string``.
    """
    def tokenize(self, s): ...
    def span_tokenize(self, s) -> Generator[Incomplete, Incomplete, None]: ...

class LineTokenizer(TokenizerI):
    '''Tokenize a string into its lines, optionally discarding blank lines.
    This is similar to ``s.split(\'\\n\')``.

        >>> from nltk.tokenize import LineTokenizer
        >>> s = "Good muffins cost $3.88\\nin New York.  Please buy me\\ntwo of them.\\n\\nThanks."
        >>> LineTokenizer(blanklines=\'keep\').tokenize(s) # doctest: +NORMALIZE_WHITESPACE
        [\'Good muffins cost $3.88\', \'in New York.  Please buy me\',
        \'two of them.\', \'\', \'Thanks.\']
        >>> # same as [l for l in s.split(\'\\n\') if l.strip()]:
        >>> LineTokenizer(blanklines=\'discard\').tokenize(s) # doctest: +NORMALIZE_WHITESPACE
        [\'Good muffins cost $3.88\', \'in New York.  Please buy me\',
        \'two of them.\', \'Thanks.\']

    :param blanklines: Indicates how blank lines should be handled.  Valid values are:

        - ``discard``: strip blank lines out of the token list before returning it.
           A line is considered blank if it contains only whitespace characters.
        - ``keep``: leave all blank lines in the token list.
        - ``discard-eof``: if the string ends with a newline, then do not generate
           a corresponding token ``\'\'`` after that newline.
    '''
    def __init__(self, blanklines: str = 'discard') -> None: ...
    def tokenize(self, s): ...
    def span_tokenize(self, s) -> Generator[Incomplete, Incomplete, None]: ...

def line_tokenize(text, blanklines: str = 'discard'): ...
