from _typeshed import Incomplete

class MosesPunctNormalizer:
    """
    This is a Python port of the Moses punctuation normalizer from
    https://github.com/moses-smt/mosesdecoder/blob/master/scripts/tokenizer/normalize-punctuation.perl
    """
    EXTRA_WHITESPACE: Incomplete
    NORMALIZE_UNICODE_IF_NOT_PENN: Incomplete
    NORMALIZE_UNICODE: Incomplete
    FRENCH_QUOTES: Incomplete
    HANDLE_PSEUDO_SPACES: Incomplete
    EN_QUOTATION_FOLLOWED_BY_COMMA: Incomplete
    DE_ES_FR_QUOTATION_FOLLOWED_BY_COMMA: Incomplete
    DE_ES_CZ_CS_FR: Incomplete
    OTHER: Incomplete
    REPLACE_UNICODE_PUNCTUATION: Incomplete
    substitutions: Incomplete
    pre_replace_unicode_punct: Incomplete
    post_remove_control_chars: Incomplete
    def __init__(self, lang: str = 'en', penn: bool = True, norm_quote_commas: bool = True, norm_numbers: bool = True, pre_replace_unicode_punct: bool = False, post_remove_control_chars: bool = False) -> None:
        """
        :param language: The two-letter language code.
        :type lang: str
        :param penn: Normalize Penn Treebank style quotations.
        :type penn: bool
        :param norm_quote_commas: Normalize quotations and commas
        :type norm_quote_commas: bool
        :param norm_numbers: Normalize numbers
        :type norm_numbers: bool
        """
    def normalize(self, text):
        """
        Returns a string with normalized punctuation.
        """
    def replace_unicode_punct(self, text): ...
    def remove_control_chars(self, text): ...
