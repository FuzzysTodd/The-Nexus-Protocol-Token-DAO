from _typeshed import Incomplete
from nltk.util import trigrams as trigrams

class TextCat:
    fingerprints: Incomplete
    last_distances: Incomplete
    def __init__(self) -> None: ...
    def remove_punctuation(self, text):
        """Get rid of punctuation except apostrophes"""
    def profile(self, text):
        """Create FreqDist of trigrams within text"""
    def calc_dist(self, lang, trigram, text_profile):
        '''Calculate the "out-of-place" measure between the
        text and language profile for a single trigram'''
    def lang_dists(self, text):
        '''Calculate the "out-of-place" measure between
        the text and all languages'''
    def guess_language(self, text):
        """Find the language with the min distance
        to the text and return its ISO 639-3 code"""

def demo() -> None: ...
