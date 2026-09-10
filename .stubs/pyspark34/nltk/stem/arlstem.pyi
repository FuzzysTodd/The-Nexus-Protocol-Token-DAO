from _typeshed import Incomplete
from nltk.stem.api import StemmerI as StemmerI

class ARLSTem(StemmerI):
    """
    ARLSTem stemmer : a light Arabic Stemming algorithm without any dictionary.
    Department of Telecommunication & Information Processing. USTHB University,
    Algiers, Algeria.
    ARLSTem.stem(token) returns the Arabic stem for the input token.
    The ARLSTem Stemmer requires that all tokens are encoded using Unicode
    encoding.
    """
    re_hamzated_alif: Incomplete
    re_alifMaqsura: Incomplete
    re_diacritics: Incomplete
    pr2: Incomplete
    pr3: Incomplete
    pr32: Incomplete
    pr4: Incomplete
    su2: Incomplete
    su22: Incomplete
    su3: Incomplete
    su32: Incomplete
    pl_si2: Incomplete
    pl_si3: Incomplete
    verb_su2: Incomplete
    verb_pr2: Incomplete
    verb_pr22: Incomplete
    verb_pr33: Incomplete
    verb_suf3: Incomplete
    verb_suf2: Incomplete
    verb_suf1: Incomplete
    def __init__(self) -> None: ...
    def stem(self, token):
        """
        call this function to get the word's stem based on ARLSTem .
        """
    def norm(self, token):
        """
        normalize the word by removing diacritics, replacing hamzated Alif
        with Alif replacing AlifMaqsura with Yaa and removing Waaw at the
        beginning.
        """
    def pref(self, token):
        """
        remove prefixes from the words' beginning.
        """
    def suff(self, token):
        """
        remove suffixes from the word's end.
        """
    def fem2masc(self, token):
        """
        transform the word from the feminine form to the masculine form.
        """
    def plur2sing(self, token):
        """
        transform the word from the plural form to the singular form.
        """
    def verb(self, token):
        """
        stem the verb prefixes and suffixes or both
        """
    def verb_t1(self, token):
        """
        stem the present prefixes and suffixes
        """
    def verb_t2(self, token):
        """
        stem the future prefixes and suffixes
        """
    def verb_t3(self, token):
        """
        stem the present suffixes
        """
    def verb_t4(self, token):
        """
        stem the present prefixes
        """
    def verb_t5(self, token):
        """
        stem the future prefixes
        """
    def verb_t6(self, token):
        """
        stem the order prefixes
        """
