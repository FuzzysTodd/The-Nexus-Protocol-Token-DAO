from _typeshed import Incomplete
from nltk.stem.api import StemmerI as StemmerI

class ISRIStemmer(StemmerI):
    """
    ISRI Arabic stemmer based on algorithm: Arabic Stemming without a root dictionary.
    Information Science Research Institute. University of Nevada, Las Vegas, USA.

    A few minor modifications have been made to ISRI basic algorithm.
    See the source code of this module for more information.

    isri.stem(token) returns Arabic root for the given token.

    The ISRI Stemmer requires that all tokens have Unicode string types.
    If you use Python IDLE on Arabic Windows you have to decode text first
    using Arabic '1256' coding.
    """
    p3: Incomplete
    p2: Incomplete
    p1: Incomplete
    s3: Incomplete
    s2: Incomplete
    s1: Incomplete
    pr4: Incomplete
    pr53: Incomplete
    re_short_vowels: Incomplete
    re_hamza: Incomplete
    re_initial_hamza: Incomplete
    stop_words: Incomplete
    def __init__(self) -> None: ...
    def stem(self, token):
        """
        Stemming a word token using the ISRI stemmer.
        """
    def norm(self, word, num: int = 3):
        """
        normalization:
        num=1  normalize diacritics
        num=2  normalize initial hamza
        num=3  both 1&2
        """
    def pre32(self, word):
        """remove length three and length two prefixes in this order"""
    def suf32(self, word):
        """remove length three and length two suffixes in this order"""
    def waw(self, word):
        """remove connective ‘و’ if it precedes a word beginning with ‘و’"""
    def pro_w4(self, word):
        """process length four patterns and extract length three roots"""
    def pro_w53(self, word):
        """process length five patterns and extract length three roots"""
    def pro_w54(self, word):
        """process length five patterns and extract length four roots"""
    def end_w5(self, word):
        """ending step (word of length five)"""
    def pro_w6(self, word):
        """process length six patterns and extract length three roots"""
    def pro_w64(self, word):
        """process length six patterns and extract length four roots"""
    def end_w6(self, word):
        """ending step (word of length six)"""
    def suf1(self, word):
        """normalize short sufix"""
    def pre1(self, word):
        """normalize short prefix"""
