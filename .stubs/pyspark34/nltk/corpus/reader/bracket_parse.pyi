from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from _typeshed import Incomplete
from nltk.tag import map_tag as map_tag
from nltk.tree import Tree as Tree

SORTTAGWRD: Incomplete
TAGWORD: Incomplete
WORD: Incomplete
EMPTY_BRACKETS: Incomplete

class BracketParseCorpusReader(SyntaxCorpusReader):
    '''
    Reader for corpora that consist of parenthesis-delineated parse trees,
    like those found in the "combined" section of the Penn Treebank,
    e.g. "(S (NP (DT the) (JJ little) (NN dog)) (VP (VBD barked)))".

    '''
    def __init__(self, root, fileids, comment_char: Incomplete | None = None, detect_blocks: str = 'unindented_paren', encoding: str = 'utf8', tagset: Incomplete | None = None) -> None:
        """
        :param root: The root directory for this corpus.
        :param fileids: A list or regexp specifying the fileids in this corpus.
        :param comment_char: The character which can appear at the start of
            a line to indicate that the rest of the line is a comment.
        :param detect_blocks: The method that is used to find blocks
            in the corpus; can be 'unindented_paren' (every unindented
            parenthesis starts a new parse) or 'sexpr' (brackets are
            matched).
        :param tagset: The name of the tagset used by this corpus, to be used
            for normalizing or converting the POS tags returned by the
            ``tagged_...()`` methods.
        """

class CategorizedBracketParseCorpusReader(CategorizedCorpusReader, BracketParseCorpusReader):
    """
    A reader for parsed corpora whose documents are
    divided into categories based on their file identifiers.
    @author: Nathan Schneider <nschneid@cs.cmu.edu>
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the corpus reader.  Categorization arguments
        (C{cat_pattern}, C{cat_map}, and C{cat_file}) are passed to
        the L{CategorizedCorpusReader constructor
        <CategorizedCorpusReader.__init__>}.  The remaining arguments
        are passed to the L{BracketParseCorpusReader constructor
        <BracketParseCorpusReader.__init__>}.
        """
    def tagged_words(self, fileids: Incomplete | None = None, categories: Incomplete | None = None, tagset: Incomplete | None = None): ...
    def tagged_sents(self, fileids: Incomplete | None = None, categories: Incomplete | None = None, tagset: Incomplete | None = None): ...
    def tagged_paras(self, fileids: Incomplete | None = None, categories: Incomplete | None = None, tagset: Incomplete | None = None): ...
    def parsed_words(self, fileids: Incomplete | None = None, categories: Incomplete | None = None): ...
    def parsed_sents(self, fileids: Incomplete | None = None, categories: Incomplete | None = None): ...
    def parsed_paras(self, fileids: Incomplete | None = None, categories: Incomplete | None = None): ...

class AlpinoCorpusReader(BracketParseCorpusReader):
    """
    Reader for the Alpino Dutch Treebank.
    This corpus has a lexical breakdown structure embedded, as read by `_parse`
    Unfortunately this puts punctuation and some other words out of the sentence
    order in the xml element tree. This is no good for `tag_` and `word_`
    `_tag` and `_word` will be overridden to use a non-default new parameter 'ordered'
    to the overridden _normalize function. The _parse function can then remain
    untouched.
    """
    def __init__(self, root, encoding: str = 'ISO-8859-1', tagset: Incomplete | None = None) -> None: ...
