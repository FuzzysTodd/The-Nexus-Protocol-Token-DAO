import regex
from _typeshed import Incomplete
from nltk.tokenize.api import TokenizerI as TokenizerI
from typing import List

EMOTICONS: str
URLS: str
FLAGS: str
PHONE_REGEX: str
REGEXPS: Incomplete
REGEXPS_PHONE: Incomplete
HANG_RE: Incomplete
EMOTICON_RE: Incomplete
ENT_RE: Incomplete
HANDLES_RE: Incomplete

class TweetTokenizer(TokenizerI):
    '''
    Tokenizer for tweets.

        >>> from nltk.tokenize import TweetTokenizer
        >>> tknzr = TweetTokenizer()
        >>> s0 = "This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <--"
        >>> tknzr.tokenize(s0) # doctest: +NORMALIZE_WHITESPACE
        [\'This\', \'is\', \'a\', \'cooool\', \'#dummysmiley\', \':\', \':-)\', \':-P\', \'<3\', \'and\', \'some\', \'arrows\', \'<\', \'>\', \'->\',
         \'<--\']

    Examples using `strip_handles` and `reduce_len parameters`:

        >>> tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
        >>> s1 = \'@remy: This is waaaaayyyy too much for you!!!!!!\'
        >>> tknzr.tokenize(s1)
        [\':\', \'This\', \'is\', \'waaayyy\', \'too\', \'much\', \'for\', \'you\', \'!\', \'!\', \'!\']
    '''
    preserve_case: Incomplete
    reduce_len: Incomplete
    strip_handles: Incomplete
    match_phone_numbers: Incomplete
    def __init__(self, preserve_case: bool = True, reduce_len: bool = False, strip_handles: bool = False, match_phone_numbers: bool = True) -> None:
        """
        Create a `TweetTokenizer` instance with settings for use in the `tokenize` method.

        :param preserve_case: Flag indicating whether to preserve the casing (capitalisation)
            of text used in the `tokenize` method. Defaults to True.
        :type preserve_case: bool
        :param reduce_len: Flag indicating whether to replace repeated character sequences
            of length 3 or greater with sequences of length 3. Defaults to False.
        :type reduce_len: bool
        :param strip_handles: Flag indicating whether to remove Twitter handles of text used
            in the `tokenize` method. Defaults to False.
        :type strip_handles: bool
        :param match_phone_numbers: Flag indicating whether the `tokenize` method should look
            for phone numbers. Defaults to True.
        :type match_phone_numbers: bool
        """
    def tokenize(self, text: str) -> List[str]:
        """Tokenize the input text.

        :param text: str
        :rtype: list(str)
        :return: a tokenized list of strings; joining this list returns        the original string if `preserve_case=False`.
        """
    @property
    def WORD_RE(self) -> regex.Pattern:
        """Core TweetTokenizer regex"""
    @property
    def PHONE_WORD_RE(self) -> regex.Pattern:
        """Secondary core TweetTokenizer regex"""

def reduce_lengthening(text):
    """
    Replace repeated character sequences of length 3 or greater with sequences
    of length 3.
    """
def remove_handles(text):
    """
    Remove Twitter username handles from text.
    """
def casual_tokenize(text, preserve_case: bool = True, reduce_len: bool = False, strip_handles: bool = False, match_phone_numbers: bool = True):
    """
    Convenience function for wrapping the tokenizer.
    """
