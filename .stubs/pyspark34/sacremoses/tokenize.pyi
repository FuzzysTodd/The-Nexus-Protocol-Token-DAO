from _typeshed import Incomplete

__all__ = ['MosesTokenizer', 'MosesDetokenizer']

class MosesTokenizer:
    """
    This is a Python port of the Moses Tokenizer from
    https://github.com/moses-smt/mosesdecoder/blob/master/scripts/tokenizer/tokenizer.perl
    """
    IsN: Incomplete
    IsAlnum: Incomplete
    IsSc: Incomplete
    IsSo: Incomplete
    IsAlpha: Incomplete
    IsLower: Incomplete
    DEDUPLICATE_SPACE: Incomplete
    ASCII_JUNK: Incomplete
    MID_STRIP: Incomplete
    LEFT_STRIP: Incomplete
    RIGHT_STRIP: Incomplete
    PAD_NOT_ISALNUM: Incomplete
    AGGRESSIVE_HYPHEN_SPLIT: Incomplete
    REPLACE_DOT_WITH_LITERALSTRING_1: Incomplete
    REPLACE_DOT_WITH_LITERALSTRING_2: Incomplete
    REPLACE_DOT_WITH_LITERALSTRING_3: Incomplete
    COMMA_SEPARATE_1: Incomplete
    COMMA_SEPARATE_2: Incomplete
    COMMA_SEPARATE_3: Incomplete
    DIRECTIONAL_QUOTE_1: Incomplete
    DIRECTIONAL_QUOTE_2: Incomplete
    DIRECTIONAL_QUOTE_3: Incomplete
    DIRECTIONAL_QUOTE_4: Incomplete
    DIRECTIONAL_QUOTE_5: Incomplete
    DIRECTIONAL_QUOTE_6: Incomplete
    DIRECTIONAL_QUOTE_7: Incomplete
    DIRECTIONAL_QUOTE_8: Incomplete
    REPLACE_ELLIPSIS: Incomplete
    RESTORE_ELLIPSIS: Incomplete
    COMMA_1: Incomplete
    COMMA_2: Incomplete
    COMMA_3: Incomplete
    SYMBOLS: Incomplete
    INTRATOKEN_SLASHES: Incomplete
    FINAL_PERIOD: Incomplete
    PAD_QUESTION_EXCLAMATION_MARK: Incomplete
    PAD_PARENTHESIS: Incomplete
    CONVERT_PARENTHESIS_1: Incomplete
    CONVERT_PARENTHESIS_2: Incomplete
    CONVERT_PARENTHESIS_3: Incomplete
    CONVERT_PARENTHESIS_4: Incomplete
    CONVERT_PARENTHESIS_5: Incomplete
    CONVERT_PARENTHESIS_6: Incomplete
    PAD_DOUBLE_DASHES: Incomplete
    PAD_START_OF_STR: Incomplete
    PAD_END_OF_STR: Incomplete
    CONVERT_DOUBLE_TO_SINGLE_QUOTES: Incomplete
    HANDLES_SINGLE_QUOTES: Incomplete
    APOSTROPHE: Incomplete
    CONTRACTION_1: Incomplete
    CONTRACTION_2: Incomplete
    CONTRACTION_3: Incomplete
    CONTRACTION_4: Incomplete
    CONTRACTION_5: Incomplete
    CONTRACTION_6: Incomplete
    CONTRACTION_7: Incomplete
    CONTRACTION_8: Incomplete
    CONTRACTION_9: Incomplete
    CONTRACTION_10: Incomplete
    CONTRACTION_11: Incomplete
    CONTRACTION_12: Incomplete
    CONTRACTION_13: Incomplete
    CONTRACTION_14: Incomplete
    CONTRACTION_15: Incomplete
    CONTRACTION_16: Incomplete
    CONTRACTION_17: Incomplete
    CONTRACTION_18: Incomplete
    CONTRACTION_19: Incomplete
    CLEAN_EXTRA_SPACE_1: Incomplete
    CLEAN_EXTRA_SPACE_2: Incomplete
    CLEAN_EXTRA_SPACE_3: Incomplete
    ESCAPE_AMPERSAND: Incomplete
    ESCAPE_PIPE: Incomplete
    ESCAPE_LEFT_ANGLE_BRACKET: Incomplete
    ESCAPE_RIGHT_ANGLE_BRACKET: Incomplete
    ESCAPE_SINGLE_QUOTE: Incomplete
    ESCAPE_DOUBLE_QUOTE: Incomplete
    ESCAPE_LEFT_SQUARE_BRACKET: Incomplete
    ESCAPE_RIGHT_SQUARE_BRACKET: Incomplete
    EN_SPECIFIC_1: Incomplete
    EN_SPECIFIC_2: Incomplete
    EN_SPECIFIC_3: Incomplete
    EN_SPECIFIC_4: Incomplete
    EN_SPECIFIC_5: Incomplete
    ENGLISH_SPECIFIC_APOSTROPHE: Incomplete
    FR_IT_SPECIFIC_1: Incomplete
    FR_IT_SPECIFIC_2: Incomplete
    FR_IT_SPECIFIC_3: Incomplete
    FR_IT_SPECIFIC_4: Incomplete
    FR_IT_SPECIFIC_APOSTROPHE: Incomplete
    NON_SPECIFIC_APOSTROPHE: Incomplete
    TRAILING_DOT_APOSTROPHE: Incomplete
    BASIC_PROTECTED_PATTERN_1: str
    BASIC_PROTECTED_PATTERN_2: str
    BASIC_PROTECTED_PATTERN_3: str
    BASIC_PROTECTED_PATTERN_4: str
    BASIC_PROTECTED_PATTERN_5: str
    MOSES_PENN_REGEXES_1: Incomplete
    MOSES_PENN_REGEXES_2: Incomplete
    MOSES_ESCAPE_XML_REGEXES: Incomplete
    BASIC_PROTECTED_PATTERNS: Incomplete
    WEB_PROTECTED_PATTERNS: Incomplete
    lang: Incomplete
    NONBREAKING_PREFIXES: Incomplete
    NUMERIC_ONLY_PREFIXES: Incomplete
    def __init__(self, lang: str = 'en', custom_nonbreaking_prefixes_file: Incomplete | None = None) -> None: ...
    def replace_multidots(self, text): ...
    def restore_multidots(self, text): ...
    def islower(self, text): ...
    def isanyalpha(self, text): ...
    def has_numeric_only(self, text): ...
    def handles_nonbreaking_prefixes(self, text): ...
    def escape_xml(self, text): ...
    def penn_tokenize(self, text, return_str: bool = False):
        """
        This is a Python port of the Penn treebank tokenizer adapted by the Moses
        machine translation community.
        """
    def tokenize(self, text, aggressive_dash_splits: bool = False, return_str: bool = False, escape: bool = True, protected_patterns: Incomplete | None = None):
        """
        Python port of the Moses tokenizer.

            :param tokens: A single string, i.e. sentence text.
            :type tokens: str
            :param aggressive_dash_splits: Option to trigger dash split rules .
            :type aggressive_dash_splits: bool
        """

class MosesDetokenizer:
    """
    This is a Python port of the Moses Detokenizer from
    https://github.com/moses-smt/mosesdecoder/blob/master/scripts/tokenizer/detokenizer.perl

    """
    IsAlnum: Incomplete
    IsAlpha: Incomplete
    IsSc: Incomplete
    AGGRESSIVE_HYPHEN_SPLIT: Incomplete
    ONE_SPACE: Incomplete
    UNESCAPE_FACTOR_SEPARATOR: Incomplete
    UNESCAPE_LEFT_ANGLE_BRACKET: Incomplete
    UNESCAPE_RIGHT_ANGLE_BRACKET: Incomplete
    UNESCAPE_DOUBLE_QUOTE: Incomplete
    UNESCAPE_SINGLE_QUOTE: Incomplete
    UNESCAPE_SYNTAX_NONTERMINAL_LEFT: Incomplete
    UNESCAPE_SYNTAX_NONTERMINAL_RIGHT: Incomplete
    UNESCAPE_AMPERSAND: Incomplete
    UNESCAPE_FACTOR_SEPARATOR_LEGACY: Incomplete
    UNESCAPE_SYNTAX_NONTERMINAL_LEFT_LEGACY: Incomplete
    UNESCAPE_SYNTAX_NONTERMINAL_RIGHT_LEGACY: Incomplete
    MOSES_UNESCAPE_XML_REGEXES: Incomplete
    FINNISH_MORPHSET_1: Incomplete
    FINNISH_MORPHSET_2: Incomplete
    FINNISH_MORPHSET_3: Incomplete
    FINNISH_REGEX: Incomplete
    lang: Incomplete
    def __init__(self, lang: str = 'en') -> None: ...
    def unescape_xml(self, text): ...
    def tokenize(self, tokens, return_str: bool = True, unescape: bool = True):
        """
        Python port of the Moses detokenizer.
        :param tokens: A list of strings, i.e. tokenized text.
        :type tokens: list(str)
        :return: str
        """
    def detokenize(self, tokens, return_str: bool = True, unescape: bool = True):
        """Duck-typing the abstract *tokenize()*."""
