from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.corpus.reader.xmldocs import *
from _typeshed import Incomplete

def norm(value_string):
    """
    Normalize the string value in an RTE pair's ``value`` or ``entailment``
    attribute as an integer (1, 0).

    :param value_string: the label used to classify a text/hypothesis pair
    :type value_string: str
    :rtype: int
    """

class RTEPair:
    """
    Container for RTE text-hypothesis pairs.

    The entailment relation is signalled by the ``value`` attribute in RTE1, and by
    ``entailment`` in RTE2 and RTE3. These both get mapped on to the ``entailment``
    attribute of this class.
    """
    challenge: Incomplete
    id: Incomplete
    gid: Incomplete
    text: Incomplete
    hyp: Incomplete
    value: Incomplete
    task: Incomplete
    length: Incomplete
    def __init__(self, pair, challenge: Incomplete | None = None, id: Incomplete | None = None, text: Incomplete | None = None, hyp: Incomplete | None = None, value: Incomplete | None = None, task: Incomplete | None = None, length: Incomplete | None = None) -> None:
        """
        :param challenge: version of the RTE challenge (i.e., RTE1, RTE2 or RTE3)
        :param id: identifier for the pair
        :param text: the text component of the pair
        :param hyp: the hypothesis component of the pair
        :param value: classification label for the pair
        :param task: attribute for the particular NLP task that the data was drawn from
        :param length: attribute for the length of the text of the pair
        """

class RTECorpusReader(XMLCorpusReader):
    """
    Corpus reader for corpora in RTE challenges.

    This is just a wrapper around the XMLCorpusReader. See module docstring above for the expected
    structure of input documents.
    """
    def pairs(self, fileids):
        """
        Build a list of RTEPairs from a RTE corpus.

        :param fileids: a list of RTE corpus fileids
        :type: list
        :rtype: list(RTEPair)
        """
