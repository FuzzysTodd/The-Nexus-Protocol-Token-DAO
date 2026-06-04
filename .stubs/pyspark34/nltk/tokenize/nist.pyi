from _typeshed import Incomplete
from nltk.corpus import perluniprops as perluniprops
from nltk.tokenize.api import TokenizerI as TokenizerI
from nltk.tokenize.util import xml_unescape as xml_unescape

class NISTTokenizer(TokenizerI):
    '''
    This NIST tokenizer is sentence-based instead of the original
    paragraph-based tokenization from mteval-14.pl; The sentence-based
    tokenization is consistent with the other tokenizers available in NLTK.

    >>> from nltk.tokenize.nist import NISTTokenizer
    >>> nist = NISTTokenizer()
    >>> s = "Good muffins cost $3.88 in New York."
    >>> expected_lower = [u\'good\', u\'muffins\', u\'cost\', u\'$\', u\'3.88\', u\'in\', u\'new\', u\'york\', u\'.\']
    >>> expected_cased = [u\'Good\', u\'muffins\', u\'cost\', u\'$\', u\'3.88\', u\'in\', u\'New\', u\'York\', u\'.\']
    >>> nist.tokenize(s, lowercase=False) == expected_cased
    True
    >>> nist.tokenize(s, lowercase=True) == expected_lower  # Lowercased.
    True

    The international_tokenize() is the preferred function when tokenizing
    non-european text, e.g.

    >>> from nltk.tokenize.nist import NISTTokenizer
    >>> nist = NISTTokenizer()

    # Input strings.
    >>> albb = u\'Alibaba Group Holding Limited (Chinese: 阿里巴巴集团控股 有限公司) us a Chinese e-commerce company...\'
    >>> amz = u\'Amazon.com, Inc. (/ˈæməzɒn/) is an American electronic commerce...\'
    >>> rkt = u\'Rakuten, Inc. (楽天株式会社 Rakuten Kabushiki-gaisha) is a Japanese electronic commerce and Internet company based in Tokyo.\'

    # Expected tokens.
    >>> expected_albb = [u\'Alibaba\', u\'Group\', u\'Holding\', u\'Limited\', u\'(\', u\'Chinese\', u\':\', u\'阿里巴巴集团控股\', u\'有限公司\', u\')\']
    >>> expected_amz = [u\'Amazon\', u\'.\', u\'com\', u\',\', u\'Inc\', u\'.\', u\'(\', u\'/\', u\'ˈæ\', u\'m\']
    >>> expected_rkt = [u\'Rakuten\', u\',\', u\'Inc\', u\'.\', u\'(\', u\'楽天株式会社\', u\'Rakuten\', u\'Kabushiki\', u\'-\', u\'gaisha\']

    >>> nist.international_tokenize(albb)[:10] == expected_albb
    True
    >>> nist.international_tokenize(amz)[:10] == expected_amz
    True
    >>> nist.international_tokenize(rkt)[:10] == expected_rkt
    True

    # Doctest for patching issue #1926
    >>> sent = u\'this is a foo☄sentence.\'
    >>> expected_sent = [u\'this\', u\'is\', u\'a\', u\'foo\', u\'☄\', u\'sentence\', u\'.\']
    >>> nist.international_tokenize(sent) == expected_sent
    True
    '''
    STRIP_SKIP: Incomplete
    STRIP_EOL_HYPHEN: Incomplete
    PUNCT: Incomplete
    PERIOD_COMMA_PRECEED: Incomplete
    PERIOD_COMMA_FOLLOW: Incomplete
    DASH_PRECEED_DIGIT: Incomplete
    LANG_DEPENDENT_REGEXES: Incomplete
    pup_number: Incomplete
    pup_punct: Incomplete
    pup_symbol: Incomplete
    number_regex: Incomplete
    punct_regex: Incomplete
    symbol_regex: Incomplete
    NONASCII: Incomplete
    PUNCT_1: Incomplete
    PUNCT_2: Incomplete
    SYMBOLS: Incomplete
    INTERNATIONAL_REGEXES: Incomplete
    def lang_independent_sub(self, text):
        """Performs the language independent string substituitions."""
    def tokenize(self, text, lowercase: bool = False, western_lang: bool = True, return_str: bool = False): ...
    def international_tokenize(self, text, lowercase: bool = False, split_non_ascii: bool = True, return_str: bool = False): ...
