from _typeshed import Incomplete
from nltk.corpus.reader import CorpusReader as CorpusReader
from nltk.data import ZipFilePathPointer as ZipFilePathPointer
from nltk.probability import FreqDist as FreqDist

class CrubadanCorpusReader(CorpusReader):
    """
    A corpus reader used to access language An Crubadan n-gram files.
    """
    def __init__(self, root, fileids, encoding: str = 'utf8', tagset: Incomplete | None = None) -> None: ...
    def lang_freq(self, lang):
        """Return n-gram FreqDist for a specific language
        given ISO 639-3 language code"""
    def langs(self):
        """Return a list of supported languages as ISO 639-3 codes"""
    def iso_to_crubadan(self, lang):
        """Return internal Crubadan code based on ISO 639-3 code"""
    def crubadan_to_iso(self, lang):
        """Return ISO 639-3 code given internal Crubadan code"""
