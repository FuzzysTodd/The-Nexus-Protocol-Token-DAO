from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['MosesTruecaser', 'MosesDetruecaser']

class MosesTruecaser:
    """
    This is a Python port of the Moses Truecaser from
    https://github.com/moses-smt/mosesdecoder/blob/master/scripts/recaser/train-truecaser.perl
    https://github.com/moses-smt/mosesdecoder/blob/master/scripts/recaser/truecase.perl
    """
    Lowercase_Letter: Incomplete
    Uppercase_Letter: Incomplete
    Titlecase_Letter: Incomplete
    SKIP_LETTERS_REGEX: Incomplete
    XML_SPLIT_REGX: Incomplete
    SENT_END: Incomplete
    DELAYED_SENT_START: Incomplete
    encoding: Incomplete
    is_asr: Incomplete
    model: Incomplete
    def __init__(self, load_from: Incomplete | None = None, is_asr: Incomplete | None = None, encoding: str = 'utf8') -> None:
        """
        :param load_from:
        :type load_from:

        :param is_asr: A flag to indicate that model is for ASR. ASR input has
            no case, make sure it is lowercase, and make sure known are cased
            eg. 'i' to be uppercased even if i is known.
        :type is_asr: bool
        """
    def learn_truecase_weights(self, tokens, possibly_use_first_token: bool = False):
        """
        This function checks through each tokens in a sentence and returns the
        appropriate weight of each surface token form.
        """
    def train(self, documents, save_to: Incomplete | None = None, possibly_use_first_token: bool = False, processes: int = 1, progress_bar: bool = False):
        """
        Default duck-type of _train(), accepts list(list(str)) as input documents.
        """
    def train_from_file(self, filename, save_to: Incomplete | None = None, possibly_use_first_token: bool = False, processes: int = 1, progress_bar: bool = False):
        """
        Duck-type of _train(), accepts a filename to read as a `iter(list(str))`
        object.
        """
    def train_from_file_object(self, file_object, save_to: Incomplete | None = None, possibly_use_first_token: bool = False, processes: int = 1, progress_bar: bool = False):
        """
        Duck-type of _train(), accepts a file object to read as a `iter(list(str))`
        object.
        """
    def truecase(self, text, return_str: bool = False, use_known: bool = False):
        """
        Truecase a single sentence / line of text.

        :param text: A single string, i.e. sentence text.
        :type text: str

        :param use_known: Use the known case if a word is a known word but not the first word.
        :type use_known: bool
        """
    def truecase_file(self, filename, return_str: bool = True) -> Generator[Incomplete, None, None]: ...
    @staticmethod
    def split_xml(line):
        """
        Python port of split_xml function in Moses' truecaser:
        https://github.com/moses-smt/mosesdecoder/blob/master/scripts/recaser/truecaser.perl

        :param line: Input string, should be tokenized, separated by space.
        :type line: str
        """
    def save_model(self, filename) -> None: ...

class MosesDetruecaser:
    SENT_END: Incomplete
    DELAYED_SENT_START: Incomplete
    ALWAYS_LOWER: Incomplete
    def __init__(self) -> None: ...
    def detruecase(self, text, is_headline: bool = False, return_str: bool = False):
        """
        Detruecase the translated files from a model that learnt from truecased
        tokens.

        :param text: A single string, i.e. sentence text.
        :type text: str
        """
