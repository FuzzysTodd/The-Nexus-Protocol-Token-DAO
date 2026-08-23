from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.util import Index as Index

class CMUDictCorpusReader(CorpusReader):
    def entries(self):
        """
        :return: the cmudict lexicon as a list of entries
            containing (word, transcriptions) tuples.
        """
    def words(self):
        """
        :return: a list of all words defined in the cmudict lexicon.
        """
    def dict(self):
        """
        :return: the cmudict lexicon as a dictionary, whose keys are
            lowercase words and whose values are lists of pronunciations.
        """

def read_cmudict_block(stream): ...
