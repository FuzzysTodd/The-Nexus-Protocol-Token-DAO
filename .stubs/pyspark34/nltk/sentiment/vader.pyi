from _typeshed import Incomplete
from nltk.util import pairwise as pairwise

class VaderConstants:
    """
    A class to keep the Vader lists and constants.
    """
    B_INCR: float
    B_DECR: float
    C_INCR: float
    N_SCALAR: float
    NEGATE: Incomplete
    BOOSTER_DICT: Incomplete
    SPECIAL_CASE_IDIOMS: Incomplete
    REGEX_REMOVE_PUNCTUATION: Incomplete
    PUNC_LIST: Incomplete
    def __init__(self) -> None: ...
    def negated(self, input_words, include_nt: bool = True):
        """
        Determine if input contains negation words
        """
    def normalize(self, score, alpha: int = 15):
        """
        Normalize the score to be between -1 and 1 using an alpha that
        approximates the max expected value
        """
    def scalar_inc_dec(self, word, valence, is_cap_diff):
        """
        Check if the preceding words increase, decrease, or negate/nullify the
        valence
        """

class SentiText:
    """
    Identify sentiment-relevant string-level properties of input text.
    """
    text: Incomplete
    PUNC_LIST: Incomplete
    REGEX_REMOVE_PUNCTUATION: Incomplete
    words_and_emoticons: Incomplete
    is_cap_diff: Incomplete
    def __init__(self, text, punc_list, regex_remove_punctuation) -> None: ...
    def allcap_differential(self, words):
        """
        Check whether just some words in the input are ALL CAPS

        :param list words: The words to inspect
        :returns: `True` if some but not all items in `words` are ALL CAPS
        """

class SentimentIntensityAnalyzer:
    """
    Give a sentiment intensity score to sentences.
    """
    lexicon_file: Incomplete
    lexicon: Incomplete
    constants: Incomplete
    def __init__(self, lexicon_file: str = 'sentiment/vader_lexicon.zip/vader_lexicon/vader_lexicon.txt') -> None: ...
    def make_lex_dict(self):
        """
        Convert lexicon file to a dictionary
        """
    def polarity_scores(self, text):
        """
        Return a float for sentiment strength based on the input text.
        Positive values are positive valence, negative value are negative
        valence.

        :note: Hashtags are not taken into consideration (e.g. #BAD is neutral). If you
            are interested in processing the text in the hashtags too, then we recommend
            preprocessing your data to remove the #, after which the hashtag text may be
            matched as if it was a normal word in the sentence.
        """
    def sentiment_valence(self, valence, sentitext, item, i, sentiments): ...
    def score_valence(self, sentiments, text): ...
