from _typeshed import Incomplete
from tokenizers import NormalizedString as NormalizedString, PreTokenizedString as PreTokenizedString
from typing import List

class JiebaPreTokenizer:
    vocab: Incomplete
    normalizers: Incomplete
    jieba: Incomplete
    def __init__(self, vocab) -> None: ...
    def jieba_split(self, i: int, normalized_string: NormalizedString) -> List[NormalizedString]: ...
    def pre_tokenize(self, pretok: PreTokenizedString): ...
