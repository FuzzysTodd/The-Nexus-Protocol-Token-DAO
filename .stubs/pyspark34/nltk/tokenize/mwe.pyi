from _typeshed import Incomplete
from nltk.tokenize.api import TokenizerI as TokenizerI
from nltk.util import Trie as Trie

class MWETokenizer(TokenizerI):
    """A tokenizer that processes tokenized text and merges multi-word expressions
    into single tokens.
    """
    def __init__(self, mwes: Incomplete | None = None, separator: str = '_') -> None:
        """Initialize the multi-word tokenizer with a list of expressions and a
        separator

        :type mwes: list(list(str))
        :param mwes: A sequence of multi-word expressions to be merged, where
            each MWE is a sequence of strings.
        :type separator: str
        :param separator: String that should be inserted between words in a multi-word
            expression token. (Default is '_')

        """
    def add_mwe(self, mwe) -> None:
        """Add a multi-word expression to the lexicon (stored as a word trie)

        We use ``util.Trie`` to represent the trie. Its form is a dict of dicts.
        The key True marks the end of a valid MWE.

        :param mwe: The multi-word expression we're adding into the word trie
        :type mwe: tuple(str) or list(str)

        :Example:

        >>> tokenizer = MWETokenizer()
        >>> tokenizer.add_mwe(('a', 'b'))
        >>> tokenizer.add_mwe(('a', 'b', 'c'))
        >>> tokenizer.add_mwe(('a', 'x'))
        >>> expected = {'a': {'x': {True: None}, 'b': {True: None, 'c': {True: None}}}}
        >>> tokenizer._mwes == expected
        True

        """
    def tokenize(self, text):
        '''

        :param text: A list containing tokenized text
        :type text: list(str)
        :return: A list of the tokenized text with multi-words merged together
        :rtype: list(str)

        :Example:

        >>> tokenizer = MWETokenizer([(\'hors\', "d\'oeuvre")], separator=\'+\')
        >>> tokenizer.tokenize("An hors d\'oeuvre tonight, sir?".split())
        [\'An\', "hors+d\'oeuvre", \'tonight,\', \'sir?\']

        '''
