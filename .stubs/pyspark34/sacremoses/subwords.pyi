from _typeshed import Incomplete
from sacremoses.util import pairwise as pairwise

class SubwordTokenizer:
    """
    This is a Python port of the Subword NMT from
    https://github.com/rsennrich/subword-nmt
    """
    vocab: Incomplete
    big_stats: Incomplete
    def __init__(self, filename) -> None: ...
    def get_vocabulary(self, filename, is_dict: bool = False): ...
    def get_pair_statistics(self):
        """Count frequency of all symbol pairs, and create index"""
    def modify_token(self, token, pair):
        """
        From https://stackoverflow.com/a/40367074/610569
            >>> modify_token(('s', 'h', 'e', 'r', 'l', 'o', 'c', 'k'), ('h', 'e'))
            ('S', 'he', 'r', 'l', 'o', 'c', 'k')
        """
    def replace_pair(self, pair):
        """Replace all occurrences of a symbol pair ('A', 'B') with a new symbol 'AB'"""
    def update_pair_statistics(self, pair, changed) -> None:
        """
        Minimally update the indices and frequency of symbol pairs
        if we merge a pair of symbols, only pairs that overlap with occurrences
        of this pair are affected, and need to be updated.
        """
    def learn(self, num_symbols, min_freq: int = 2, jump: int = 1, is_dict: Incomplete | None = None) -> None: ...
