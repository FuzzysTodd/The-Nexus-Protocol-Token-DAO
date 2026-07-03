from _typeshed import Incomplete
from nltk.tokenize.api import TokenizerI as TokenizerI
from nltk.util import ngrams as ngrams

class SyllableTokenizer(TokenizerI):
    '''
    Syllabifies words based on the Sonority Sequencing Principle (SSP).

        >>> from nltk.tokenize import SyllableTokenizer
        >>> from nltk import word_tokenize
        >>> SSP = SyllableTokenizer()
        >>> SSP.tokenize(\'justification\')
        [\'jus\', \'ti\', \'fi\', \'ca\', \'tion\']
        >>> text = "This is a foobar-like sentence."
        >>> [SSP.tokenize(token) for token in word_tokenize(text)]
        [[\'This\'], [\'is\'], [\'a\'], [\'foo\', \'bar\', \'-\', \'li\', \'ke\'], [\'sen\', \'ten\', \'ce\'], [\'.\']]
    '''
    vowels: Incomplete
    phoneme_map: Incomplete
    def __init__(self, lang: str = 'en', sonority_hierarchy: bool = False) -> None:
        """
        :param lang: Language parameter, default is English, 'en'
        :type lang: str
        :param sonority_hierarchy: Sonority hierarchy according to the
                                   Sonority Sequencing Principle.
        :type sonority_hierarchy: list(str)
        """
    def assign_values(self, token):
        """
        Assigns each phoneme its value from the sonority hierarchy.
        Note: Sentence/text has to be tokenized first.

        :param token: Single word or token
        :type token: str
        :return: List of tuples, first element is character/phoneme and
                 second is the soronity value.
        :rtype: list(tuple(str, int))
        """
    def validate_syllables(self, syllable_list):
        """
        Ensures each syllable has at least one vowel.
        If the following syllable doesn't have vowel, add it to the current one.

        :param syllable_list: Single word or token broken up into syllables.
        :type syllable_list: list(str)
        :return: Single word or token broken up into syllables
                 (with added syllables if necessary)
        :rtype: list(str)
        """
    def tokenize(self, token):
        """
        Apply the SSP to return a list of syllables.
        Note: Sentence/text has to be tokenized first.

        :param token: Single word or token
        :type token: str
        :return syllable_list: Single word or token broken up into syllables.
        :rtype: list(str)
        """
