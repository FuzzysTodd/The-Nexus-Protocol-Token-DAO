from _typeshed import Incomplete
from nltk.tokenize.api import TokenizerI as TokenizerI

class ToktokTokenizer(TokenizerI):
    """
    This is a Python port of the tok-tok.pl from
    https://github.com/jonsafari/tok-tok/blob/master/tok-tok.pl

    >>> toktok = ToktokTokenizer()
    >>> text = u'Is 9.5 or 525,600 my favorite number?'
    >>> print(toktok.tokenize(text, return_str=True))
    Is 9.5 or 525,600 my favorite number ?
    >>> text = u'The https://github.com/jonsafari/tok-tok/blob/master/tok-tok.pl is a website with/and/or slashes and sort of weird : things'
    >>> print(toktok.tokenize(text, return_str=True))
    The https://github.com/jonsafari/tok-tok/blob/master/tok-tok.pl is a website with/and/or slashes and sort of weird : things
    >>> text = u'¡This, is a sentence with weird» symbols… appearing everywhere¿'
    >>> expected = u'¡ This , is a sentence with weird » symbols … appearing everywhere ¿'
    >>> assert toktok.tokenize(text, return_str=True) == expected
    >>> toktok.tokenize(text) == [u'¡', u'This', u',', u'is', u'a', u'sentence', u'with', u'weird', u'»', u'symbols', u'…', u'appearing', u'everywhere', u'¿']
    True
    """
    NON_BREAKING: Incomplete
    FUNKY_PUNCT_1: Incomplete
    FUNKY_PUNCT_2: Incomplete
    EN_EM_DASHES: Incomplete
    AMPERCENT: Incomplete
    TAB: Incomplete
    PIPE: Incomplete
    COMMA_IN_NUM: Incomplete
    PROB_SINGLE_QUOTES: Incomplete
    STUPID_QUOTES_1: Incomplete
    STUPID_QUOTES_2: Incomplete
    FINAL_PERIOD_1: Incomplete
    FINAL_PERIOD_2: Incomplete
    MULTI_COMMAS: Incomplete
    MULTI_DASHES: Incomplete
    MULTI_DOTS: Incomplete
    OPEN_PUNCT: Incomplete
    CLOSE_PUNCT: Incomplete
    CURRENCY_SYM: Incomplete
    OPEN_PUNCT_RE: Incomplete
    CLOSE_PUNCT_RE: Incomplete
    CURRENCY_SYM_RE: Incomplete
    URL_FOE_1: Incomplete
    URL_FOE_2: Incomplete
    URL_FOE_3: Incomplete
    URL_FOE_4: Incomplete
    LSTRIP: Incomplete
    RSTRIP: Incomplete
    ONE_SPACE: Incomplete
    TOKTOK_REGEXES: Incomplete
    def tokenize(self, text, return_str: bool = False): ...
