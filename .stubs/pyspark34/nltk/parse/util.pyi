from _typeshed import Incomplete
from collections.abc import Generator
from nltk.data import load as load
from nltk.grammar import CFG as CFG, FeatureGrammar as FeatureGrammar, PCFG as PCFG
from nltk.parse.chart import Chart as Chart, ChartParser as ChartParser
from nltk.parse.featurechart import FeatureChart as FeatureChart, FeatureChartParser as FeatureChartParser
from nltk.parse.pchart import InsideChartParser as InsideChartParser

def load_parser(grammar_url, trace: int = 0, parser: Incomplete | None = None, chart_class: Incomplete | None = None, beam_size: int = 0, **load_args):
    '''
    Load a grammar from a file, and build a parser based on that grammar.
    The parser depends on the grammar format, and might also depend
    on properties of the grammar itself.

    The following grammar formats are currently supported:
      - ``\'cfg\'``  (CFGs: ``CFG``)
      - ``\'pcfg\'`` (probabilistic CFGs: ``PCFG``)
      - ``\'fcfg\'`` (feature-based CFGs: ``FeatureGrammar``)

    :type grammar_url: str
    :param grammar_url: A URL specifying where the grammar is located.
        The default protocol is ``"nltk:"``, which searches for the file
        in the the NLTK data package.
    :type trace: int
    :param trace: The level of tracing that should be used when
        parsing a text.  ``0`` will generate no tracing output;
        and higher numbers will produce more verbose tracing output.
    :param parser: The class used for parsing; should be ``ChartParser``
        or a subclass.
        If None, the class depends on the grammar format.
    :param chart_class: The class used for storing the chart;
        should be ``Chart`` or a subclass.
        Only used for CFGs and feature CFGs.
        If None, the chart class depends on the grammar format.
    :type beam_size: int
    :param beam_size: The maximum length for the parser\'s edge queue.
        Only used for probabilistic CFGs.
    :param load_args: Keyword parameters used when loading the grammar.
        See ``data.load`` for more information.
    '''
def taggedsent_to_conll(sentence) -> Generator[Incomplete, None, None]:
    '''
    A module to convert a single POS tagged sentence into CONLL format.

    >>> from nltk import word_tokenize, pos_tag
    >>> text = "This is a foobar sentence."
    >>> for line in taggedsent_to_conll(pos_tag(word_tokenize(text))): # doctest: +NORMALIZE_WHITESPACE
    ... \tprint(line, end="")
        1\tThis\t_\tDT\tDT\t_\t0\ta\t_\t_
        2\tis\t_\tVBZ\tVBZ\t_\t0\ta\t_\t_
        3\ta\t_\tDT\tDT\t_\t0\ta\t_\t_
        4\tfoobar\t_\tJJ\tJJ\t_\t0\ta\t_\t_
        5\tsentence\t_\tNN\tNN\t_\t0\ta\t_\t_
        6\t.\t\t_\t.\t.\t_\t0\ta\t_\t_

    :param sentence: A single input sentence to parse
    :type sentence: list(tuple(str, str))
    :rtype: iter(str)
    :return: a generator yielding a single sentence in CONLL format.
    '''
def taggedsents_to_conll(sentences) -> Generator[Incomplete, Incomplete, None]:
    '''
    A module to convert the a POS tagged document stream
    (i.e. list of list of tuples, a list of sentences) and yield lines
    in CONLL format. This module yields one line per word and two newlines
    for end of sentence.

    >>> from nltk import word_tokenize, sent_tokenize, pos_tag
    >>> text = "This is a foobar sentence. Is that right?"
    >>> sentences = [pos_tag(word_tokenize(sent)) for sent in sent_tokenize(text)]
    >>> for line in taggedsents_to_conll(sentences): # doctest: +NORMALIZE_WHITESPACE
    ...     if line:
    ...         print(line, end="")
    1\tThis\t_\tDT\tDT\t_\t0\ta\t_\t_
    2\tis\t_\tVBZ\tVBZ\t_\t0\ta\t_\t_
    3\ta\t_\tDT\tDT\t_\t0\ta\t_\t_
    4\tfoobar\t_\tJJ\tJJ\t_\t0\ta\t_\t_
    5\tsentence\t_\tNN\tNN\t_\t0\ta\t_\t_
    6\t.\t\t_\t.\t.\t_\t0\ta\t_\t_
    <BLANKLINE>
    <BLANKLINE>
    1\tIs\t_\tVBZ\tVBZ\t_\t0\ta\t_\t_
    2\tthat\t_\tIN\tIN\t_\t0\ta\t_\t_
    3\tright\t_\tNN\tNN\t_\t0\ta\t_\t_
    4\t?\t_\t.\t.\t_\t0\ta\t_\t_
    <BLANKLINE>
    <BLANKLINE>

    :param sentences: Input sentences to parse
    :type sentence: list(list(tuple(str, str)))
    :rtype: iter(str)
    :return: a generator yielding sentences in CONLL format.
    '''

class TestGrammar:
    """
    Unit tests for  CFG.
    """
    test_grammar: Incomplete
    cp: Incomplete
    suite: Incomplete
    def __init__(self, grammar, suite, accept: Incomplete | None = None, reject: Incomplete | None = None) -> None: ...
    def run(self, show_trees: bool = False) -> None:
        """
        Sentences in the test suite are divided into two classes:

        - grammatical (``accept``) and
        - ungrammatical (``reject``).

        If a sentence should parse according to the grammar, the value of
        ``trees`` will be a non-empty list. If a sentence should be rejected
        according to the grammar, then the value of ``trees`` will be None.
        """

def extract_test_sentences(string, comment_chars: str = '#%;', encoding: Incomplete | None = None):
    """
    Parses a string with one test sentence per line.
    Lines can optionally begin with:

    - a bool, saying if the sentence is grammatical or not, or
    - an int, giving the number of parse trees is should have,

    The result information is followed by a colon, and then the sentence.
    Empty lines and lines beginning with a comment char are ignored.

    :return: a list of tuple of sentences and expected results,
        where a sentence is a list of str,
        and a result is None, or bool, or int

    :param comment_chars: ``str`` of possible comment characters.
    :param encoding: the encoding of the string, if it is binary
    """
