from _typeshed import Incomplete
from nltk.tokenize.api import TokenizerI as TokenizerI

class LegalitySyllableTokenizer(TokenizerI):
    '''
    Syllabifies words based on the Legality Principle and Onset Maximization.

        >>> from nltk.tokenize import LegalitySyllableTokenizer
        >>> from nltk import word_tokenize
        >>> from nltk.corpus import words
        >>> text = "This is a wonderful sentence."
        >>> text_words = word_tokenize(text)
        >>> LP = LegalitySyllableTokenizer(words.words())
        >>> [LP.tokenize(word) for word in text_words]
        [[\'This\'], [\'is\'], [\'a\'], [\'won\', \'der\', \'ful\'], [\'sen\', \'ten\', \'ce\'], [\'.\']]
    '''
    legal_frequency_threshold: Incomplete
    vowels: Incomplete
    legal_onsets: Incomplete
    def __init__(self, tokenized_source_text, vowels: str = 'aeiouy', legal_frequency_threshold: float = 0.001) -> None:
        """
        :param tokenized_source_text: List of valid tokens in the language
        :type tokenized_source_text: list(str)
        :param vowels: Valid vowels in language or IPA representation
        :type vowels: str
        :param legal_frequency_threshold: Lowest frequency of all onsets to be considered a legal onset
        :type legal_frequency_threshold: float
        """
    def find_legal_onsets(self, words):
        """
        Gathers all onsets and then return only those above the frequency threshold

        :param words: List of words in a language
        :type words: list(str)
        :return: Set of legal onsets
        :rtype: set(str)
        """
    def onset(self, word):
        """
        Returns consonant cluster of word, i.e. all characters until the first vowel.

        :param word: Single word or token
        :type word: str
        :return: String of characters of onset
        :rtype: str
        """
    def tokenize(self, token):
        """
        Apply the Legality Principle in combination with
        Onset Maximization to return a list of syllables.

        :param token: Single word or token
        :type token: str
        :return syllable_list: Single word or token broken up into syllables.
        :rtype: list(str)
        """
