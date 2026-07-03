from nltk.chunk.api import ChunkParserI as ChunkParserI
from nltk.chunk.regexp import RegexpChunkParser as RegexpChunkParser, RegexpParser as RegexpParser
from nltk.chunk.util import ChunkScore as ChunkScore, accuracy as accuracy, conllstr2tree as conllstr2tree, conlltags2tree as conlltags2tree, ieerstr2tree as ieerstr2tree, tagstr2tree as tagstr2tree, tree2conllstr as tree2conllstr, tree2conlltags as tree2conlltags
from nltk.data import load as load

def ne_chunk(tagged_tokens, binary: bool = False):
    """
    Use NLTK's currently recommended named entity chunker to
    chunk the given list of tagged tokens.
    """
def ne_chunk_sents(tagged_sentences, binary: bool = False):
    """
    Use NLTK's currently recommended named entity chunker to chunk the
    given list of tagged sentences, each consisting of a list of tagged tokens.
    """
