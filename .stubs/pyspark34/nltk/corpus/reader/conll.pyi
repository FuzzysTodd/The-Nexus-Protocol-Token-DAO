from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from _typeshed import Incomplete
from nltk.tag import map_tag as map_tag
from nltk.tree import Tree as Tree
from nltk.util import LazyConcatenation as LazyConcatenation, LazyMap as LazyMap

class ConllCorpusReader(CorpusReader):
    '''
    A corpus reader for CoNLL-style files.  These files consist of a
    series of sentences, separated by blank lines.  Each sentence is
    encoded using a table (or "grid") of values, where each line
    corresponds to a single word, and each column corresponds to an
    annotation type.  The set of columns used by CoNLL-style files can
    vary from corpus to corpus; the ``ConllCorpusReader`` constructor
    therefore takes an argument, ``columntypes``, which is used to
    specify the columns that are used by a given corpus. By default
    columns are split by consecutive whitespaces, with the
    ``separator`` argument you can set a string to split by (e.g.
    ``\'\t\'``).


    @todo: Add support for reading from corpora where different
        parallel files contain different columns.
    @todo: Possibly add caching of the grid corpus view?  This would
        allow the same grid view to be used by different data access
        methods (eg words() and parsed_sents() could both share the
        same grid corpus view object).
    @todo: Better support for -DOCSTART-.  Currently, we just ignore
        it, but it could be used to define methods that retrieve a
        document at a time (eg parsed_documents()).
    '''
    WORDS: str
    POS: str
    TREE: str
    CHUNK: str
    NE: str
    SRL: str
    IGNORE: str
    COLUMN_TYPES: Incomplete
    sep: Incomplete
    def __init__(self, root, fileids, columntypes, chunk_types: Incomplete | None = None, root_label: str = 'S', pos_in_tree: bool = False, srl_includes_roleset: bool = True, encoding: str = 'utf8', tree_class=..., tagset: Incomplete | None = None, separator: Incomplete | None = None) -> None: ...
    def words(self, fileids: Incomplete | None = None): ...
    def sents(self, fileids: Incomplete | None = None): ...
    def tagged_words(self, fileids: Incomplete | None = None, tagset: Incomplete | None = None): ...
    def tagged_sents(self, fileids: Incomplete | None = None, tagset: Incomplete | None = None): ...
    def chunked_words(self, fileids: Incomplete | None = None, chunk_types: Incomplete | None = None, tagset: Incomplete | None = None): ...
    def chunked_sents(self, fileids: Incomplete | None = None, chunk_types: Incomplete | None = None, tagset: Incomplete | None = None): ...
    def parsed_sents(self, fileids: Incomplete | None = None, pos_in_tree: Incomplete | None = None, tagset: Incomplete | None = None): ...
    def srl_spans(self, fileids: Incomplete | None = None): ...
    def srl_instances(self, fileids: Incomplete | None = None, pos_in_tree: Incomplete | None = None, flatten: bool = True): ...
    def iob_words(self, fileids: Incomplete | None = None, tagset: Incomplete | None = None):
        """
        :return: a list of word/tag/IOB tuples
        :rtype: list(tuple)
        :param fileids: the list of fileids that make up this corpus
        :type fileids: None or str or list
        """
    def iob_sents(self, fileids: Incomplete | None = None, tagset: Incomplete | None = None):
        """
        :return: a list of lists of word/tag/IOB tuples
        :rtype: list(list)
        :param fileids: the list of fileids that make up this corpus
        :type fileids: None or str or list
        """

class ConllSRLInstance:
    """
    An SRL instance from a CoNLL corpus, which identifies and
    providing labels for the arguments of a single verb.
    """
    verb: Incomplete
    verb_head: Incomplete
    verb_stem: Incomplete
    roleset: Incomplete
    arguments: Incomplete
    tagged_spans: Incomplete
    tree: Incomplete
    words: Incomplete
    def __init__(self, tree, verb_head, verb_stem, roleset, tagged_spans) -> None: ...
    def pprint(self): ...

class ConllSRLInstanceList(list):
    """
    Set of instances for a single sentence
    """
    tree: Incomplete
    def __init__(self, tree, instances=()) -> None: ...
    def pprint(self, include_tree: bool = False): ...

class ConllChunkCorpusReader(ConllCorpusReader):
    """
    A ConllCorpusReader whose data file contains three columns: words,
    pos, and chunk.
    """
    def __init__(self, root, fileids, chunk_types, encoding: str = 'utf8', tagset: Incomplete | None = None, separator: Incomplete | None = None) -> None: ...
