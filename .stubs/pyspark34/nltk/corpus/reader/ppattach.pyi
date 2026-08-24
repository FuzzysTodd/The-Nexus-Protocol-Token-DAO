from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from _typeshed import Incomplete

class PPAttachment:
    sent: Incomplete
    verb: Incomplete
    noun1: Incomplete
    prep: Incomplete
    noun2: Incomplete
    attachment: Incomplete
    def __init__(self, sent, verb, noun1, prep, noun2, attachment) -> None: ...

class PPAttachmentCorpusReader(CorpusReader):
    """
    sentence_id verb noun1 preposition noun2 attachment
    """
    def attachments(self, fileids): ...
    def tuples(self, fileids): ...
