from _typeshed import Incomplete
from nltk.stem.api import StemmerI as StemmerI

class ARLSTem2(StemmerI):
    """
    Return a stemmed Arabic word after removing affixes. This an improved
    version of the previous algorithm, which reduces under-stemming errors.
    Typically used in Arabic search engine, information retrieval and NLP.

        >>> from nltk.stem import arlstem2
        >>> stemmer = ARLSTem2()
        >>> word = stemmer.stem('يعمل')
        >>> print(word)
        عمل

    :param token: The input Arabic word (unicode) to be stemmed
    :type token: unicode
    :return: A unicode Arabic word
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
    is_verb: bool
    def stem1(self, token):
        """
        call this function to get the first stem
        """
    def stem(self, token): ...
    def norm(self, token):
        """
        normalize the word by removing diacritics, replace hamzated Alif
        with Alif bare, replace AlifMaqsura with Yaa and remove Waaw at the
        beginning.
        """
    def pref(self, token):
        """
        remove prefixes from the words' beginning.
        """
    def adjective(self, token):
        """
        remove the infixes from adjectives
        """
    def suff(self, token):
        """
        remove the suffixes from the word's ending.
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
        stem the present tense co-occurred prefixes and suffixes
        """
    def verb_t2(self, token):
        """
        stem the future tense co-occurred prefixes and suffixes
        """
    def verb_t3(self, token):
        """
        stem the present tense suffixes
        """
    def verb_t4(self, token):
        """
        stem the present tense prefixes
        """
    def verb_t5(self, token):
        """
        stem the future tense prefixes
        """
    def verb_t6(self, token):
        """
        stem the imperative tense prefixes
        """
