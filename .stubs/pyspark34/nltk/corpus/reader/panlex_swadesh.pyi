from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from _typeshed import Incomplete
from collections.abc import Generator
from nltk.corpus.reader.wordlist import WordListCorpusReader as WordListCorpusReader
from nltk.tokenize import line_tokenize as line_tokenize
from typing import NamedTuple

class PanlexLanguage(NamedTuple):
    panlex_uid: Incomplete
    iso639: Incomplete
    iso639_type: Incomplete
    script: Incomplete
    name: Incomplete
    langvar_uid: Incomplete

class PanlexSwadeshCorpusReader(WordListCorpusReader):
    """
    This is a class to read the PanLex Swadesh list from

    David Kamholz, Jonathan Pool, and Susan M. Colowick (2014).
    PanLex: Building a Resource for Panlingual Lexical Translation.
    In LREC. http://www.lrec-conf.org/proceedings/lrec2014/pdf/1029_Paper.pdf

    License: CC0 1.0 Universal
    https://creativecommons.org/publicdomain/zero/1.0/legalcode
    """
    swadesh_size: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def license(self): ...
    def language_codes(self): ...
    def get_languages(self) -> Generator[Incomplete, None, None]: ...
    def get_macrolanguages(self): ...
    def words_by_lang(self, lang_code):
        """
        :return: a list of list(str)
        """
    def words_by_iso639(self, iso63_code):
        """
        :return: a list of list(str)
        """
    def entries(self, fileids: Incomplete | None = None):
        """
        :return: a tuple of words for the specified fileids.
        """
