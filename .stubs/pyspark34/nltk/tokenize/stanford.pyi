from _typeshed import Incomplete
from nltk.internals import config_java as config_java, find_jar as find_jar, java as java
from nltk.parse.corenlp import CoreNLPParser as CoreNLPParser
from nltk.tokenize.api import TokenizerI as TokenizerI

class StanfordTokenizer(TokenizerI):
    '''
    Interface to the Stanford Tokenizer

    >>> from nltk.tokenize.stanford import StanfordTokenizer
    >>> s = "Good muffins cost $3.88\\nin New York.  Please buy me\\ntwo of them.\\nThanks."
    >>> StanfordTokenizer().tokenize(s) # doctest: +SKIP
    [\'Good\', \'muffins\', \'cost\', \'$\', \'3.88\', \'in\', \'New\', \'York\', \'.\', \'Please\', \'buy\', \'me\', \'two\', \'of\', \'them\', \'.\', \'Thanks\', \'.\']
    >>> s = "The colour of the wall is blue."
    >>> StanfordTokenizer(options={"americanize": True}).tokenize(s) # doctest: +SKIP
    [\'The\', \'color\', \'of\', \'the\', \'wall\', \'is\', \'blue\', \'.\']
    '''
    java_options: Incomplete
    def __init__(self, path_to_jar: Incomplete | None = None, encoding: str = 'utf8', options: Incomplete | None = None, verbose: bool = False, java_options: str = '-mx1000m') -> None: ...
    def tokenize(self, s):
        """
        Use stanford tokenizer's PTBTokenizer to tokenize multiple sentences.
        """
