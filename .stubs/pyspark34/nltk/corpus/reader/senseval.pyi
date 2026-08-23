from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.tokenize import *
from _typeshed import Incomplete

class SensevalInstance:
    word: Incomplete
    senses: Incomplete
    position: Incomplete
    context: Incomplete
    def __init__(self, word, position, context, senses) -> None: ...

class SensevalCorpusReader(CorpusReader):
    def instances(self, fileids: Incomplete | None = None): ...

class SensevalCorpusView(StreamBackedCorpusView):
    def __init__(self, fileid, encoding) -> None: ...
    def read_block(self, stream): ...
