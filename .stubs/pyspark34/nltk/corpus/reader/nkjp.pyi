from _typeshed import Incomplete
from nltk.corpus.reader.util import concat as concat
from nltk.corpus.reader.xmldocs import XMLCorpusReader as XMLCorpusReader, XMLCorpusView as XMLCorpusView

class NKJPCorpusReader(XMLCorpusReader):
    WORDS_MODE: int
    SENTS_MODE: int
    HEADER_MODE: int
    RAW_MODE: int
    def __init__(self, root, fileids: str = '.*') -> None:
        """
        Corpus reader designed to work with National Corpus of Polish.
        See http://nkjp.pl/ for more details about NKJP.
        use example:
        import nltk
        import nkjp
        from nkjp import NKJPCorpusReader
        x = NKJPCorpusReader(root='/home/USER/nltk_data/corpora/nkjp/', fileids='') # obtain the whole corpus
        x.header()
        x.raw()
        x.words()
        x.tagged_words(tags=['subst', 'comp'])  #Link to find more tags: nkjp.pl/poliqarp/help/ense2.html
        x.sents()
        x = NKJPCorpusReader(root='/home/USER/nltk_data/corpora/nkjp/', fileids='Wilk*') # obtain particular file(s)
        x.header(fileids=['WilkDom', '/home/USER/nltk_data/corpora/nkjp/WilkWilczy'])
        x.tagged_words(fileids=['WilkDom', '/home/USER/nltk_data/corpora/nkjp/WilkWilczy'], tags=['subst', 'comp'])
        """
    def get_paths(self): ...
    def fileids(self):
        """
        Returns a list of file identifiers for the fileids that make up
        this corpus.
        """
    def add_root(self, fileid):
        """
        Add root if necessary to specified fileid.
        """
    def header(self, fileids: Incomplete | None = None, **kwargs):
        """
        Returns header(s) of specified fileids.
        """
    def sents(self, fileids: Incomplete | None = None, **kwargs):
        """
        Returns sentences in specified fileids.
        """
    def words(self, fileids: Incomplete | None = None, **kwargs):
        """
        Returns words in specified fileids.
        """
    def tagged_words(self, fileids: Incomplete | None = None, **kwargs):
        """
        Call with specified tags as a list, e.g. tags=['subst', 'comp'].
        Returns tagged words in specified fileids.
        """
    def raw(self, fileids: Incomplete | None = None, **kwargs):
        """
        Returns words in specified fileids.
        """

class NKJPCorpus_Header_View(XMLCorpusView):
    tagspec: str
    def __init__(self, filename, **kwargs) -> None:
        """
        HEADER_MODE
        A stream backed corpus view specialized for use with
        header.xml files in NKJP corpus.
        """
    def handle_query(self): ...
    def handle_elt(self, elt, context): ...

class XML_Tool:
    """
    Helper class creating xml file to one without references to nkjp: namespace.
    That's needed because the XMLCorpusView assumes that one can find short substrings
    of XML that are valid XML, which is not true if a namespace is declared at top level
    """
    read_file: Incomplete
    write_file: Incomplete
    def __init__(self, root, filename) -> None: ...
    def build_preprocessed_file(self): ...
    def remove_preprocessed_file(self) -> None: ...

class NKJPCorpus_Segmentation_View(XMLCorpusView):
    """
    A stream backed corpus view specialized for use with
    ann_segmentation.xml files in NKJP corpus.
    """
    tagspec: str
    text_view: Incomplete
    xml_tool: Incomplete
    def __init__(self, filename, **kwargs) -> None: ...
    def get_segm_id(self, example_word): ...
    def get_sent_beg(self, beg_word): ...
    def get_sent_end(self, end_word): ...
    def get_sentences(self, sent_segm): ...
    def remove_choice(self, segm): ...
    def handle_query(self): ...
    def handle_elt(self, elt, context): ...

class NKJPCorpus_Text_View(XMLCorpusView):
    """
    A stream backed corpus view specialized for use with
    text.xml files in NKJP corpus.
    """
    SENTS_MODE: int
    RAW_MODE: int
    mode: Incomplete
    tagspec: str
    segm_dict: Incomplete
    xml_tool: Incomplete
    def __init__(self, filename, **kwargs) -> None: ...
    def handle_query(self): ...
    def read_block(self, stream, tagspec: Incomplete | None = None, elt_handler: Incomplete | None = None):
        """
        Returns text as a list of sentences.
        """
    def get_segm_id(self, elt): ...
    def handle_elt(self, elt, context): ...

class NKJPCorpus_Morph_View(XMLCorpusView):
    """
    A stream backed corpus view specialized for use with
    ann_morphosyntax.xml files in NKJP corpus.
    """
    tags: Incomplete
    tagspec: str
    xml_tool: Incomplete
    def __init__(self, filename, **kwargs) -> None: ...
    def handle_query(self): ...
    def handle_elt(self, elt, context): ...
