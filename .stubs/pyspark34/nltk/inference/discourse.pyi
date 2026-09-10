from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from nltk.data import show_cfg as show_cfg
from nltk.inference.mace import MaceCommand as MaceCommand
from nltk.inference.prover9 import Prover9Command as Prover9Command
from nltk.parse import load_parser as load_parser
from nltk.parse.malt import MaltParser as MaltParser
from nltk.sem.drt import AnaphoraResolutionException as AnaphoraResolutionException, resolve_anaphora as resolve_anaphora
from nltk.sem.glue import DrtGlue as DrtGlue
from nltk.sem.logic import Expression as Expression
from nltk.tag import RegexpTagger as RegexpTagger

class ReadingCommand(metaclass=ABCMeta):
    @abstractmethod
    def parse_to_readings(self, sentence):
        """
        :param sentence: the sentence to read
        :type sentence: str
        """
    def process_thread(self, sentence_readings):
        """
        This method should be used to handle dependencies between readings such
        as resolving anaphora.

        :param sentence_readings: readings to process
        :type sentence_readings: list(Expression)
        :return: the list of readings after processing
        :rtype: list(Expression)
        """
    @abstractmethod
    def combine_readings(self, readings):
        """
        :param readings: readings to combine
        :type readings: list(Expression)
        :return: one combined reading
        :rtype: Expression
        """
    @abstractmethod
    def to_fol(self, expression):
        """
        Convert this expression into a First-Order Logic expression.

        :param expression: an expression
        :type expression: Expression
        :return: a FOL version of the input expression
        :rtype: Expression
        """

class CfgReadingCommand(ReadingCommand):
    def __init__(self, gramfile: Incomplete | None = None) -> None:
        """
        :param gramfile: name of file where grammar can be loaded
        :type gramfile: str
        """
    def parse_to_readings(self, sentence):
        """:see: ReadingCommand.parse_to_readings()"""
    def combine_readings(self, readings):
        """:see: ReadingCommand.combine_readings()"""
    def to_fol(self, expression):
        """:see: ReadingCommand.to_fol()"""

class DrtGlueReadingCommand(ReadingCommand):
    def __init__(self, semtype_file: Incomplete | None = None, remove_duplicates: bool = False, depparser: Incomplete | None = None) -> None:
        """
        :param semtype_file: name of file where grammar can be loaded
        :param remove_duplicates: should duplicates be removed?
        :param depparser: the dependency parser
        """
    def parse_to_readings(self, sentence):
        """:see: ReadingCommand.parse_to_readings()"""
    def process_thread(self, sentence_readings):
        """:see: ReadingCommand.process_thread()"""
    def combine_readings(self, readings):
        """:see: ReadingCommand.combine_readings()"""
    def to_fol(self, expression):
        """:see: ReadingCommand.to_fol()"""

class DiscourseTester:
    """
    Check properties of an ongoing discourse.
    """
    def __init__(self, input, reading_command: Incomplete | None = None, background: Incomplete | None = None) -> None:
        """
        Initialize a ``DiscourseTester``.

        :param input: the discourse sentences
        :type input: list of str
        :param background: Formulas which express background assumptions
        :type background: list(Expression)
        """
    def sentences(self) -> None:
        """
        Display the list of sentences in the current discourse.
        """
    def add_sentence(self, sentence, informchk: bool = False, consistchk: bool = False) -> None:
        """
        Add a sentence to the current discourse.

        Updates ``self._input`` and ``self._sentences``.
        :param sentence: An input sentence
        :type sentence: str
        :param informchk: if ``True``, check that the result of adding the sentence is thread-informative. Updates ``self._readings``.
        :param consistchk: if ``True``, check that the result of adding the sentence is thread-consistent. Updates ``self._readings``.

        """
    def retract_sentence(self, sentence, verbose: bool = True) -> None:
        """
        Remove a sentence from the current discourse.

        Updates ``self._input``, ``self._sentences`` and ``self._readings``.
        :param sentence: An input sentence
        :type sentence: str
        :param verbose: If ``True``,  report on the updated list of sentences.
        """
    def grammar(self) -> None:
        """
        Print out the grammar in use for parsing input sentences
        """
    def readings(self, sentence: Incomplete | None = None, threaded: bool = False, verbose: bool = True, filter: bool = False, show_thread_readings: bool = False) -> None:
        """
        Construct and show the readings of the discourse (or of a single sentence).

        :param sentence: test just this sentence
        :type sentence: str
        :param threaded: if ``True``, print out each thread ID and the corresponding thread.
        :param filter: if ``True``, only print out consistent thread IDs and threads.
        """
    def expand_threads(self, thread_id, threads: Incomplete | None = None):
        """
        Given a thread ID, find the list of ``logic.Expression`` objects corresponding to the reading IDs in that thread.

        :param thread_id: thread ID
        :type thread_id: str
        :param threads: a mapping from thread IDs to lists of reading IDs
        :type threads: dict
        :return: A list of pairs ``(rid, reading)`` where reading is the ``logic.Expression`` associated with a reading ID
        :rtype: list of tuple
        """
    def models(self, thread_id: Incomplete | None = None, show: bool = True, verbose: bool = False) -> None:
        """
        Call Mace4 to build a model for each current discourse thread.

        :param thread_id: thread ID
        :type thread_id: str
        :param show: If ``True``, display the model that has been found.
        """
    def add_background(self, background, verbose: bool = False) -> None:
        """
        Add a list of background assumptions for reasoning about the discourse.

        When called,  this method also updates the discourse model's set of readings and threads.
        :param background: Formulas which contain background information
        :type background: list(Expression)
        """
    def background(self) -> None:
        """
        Show the current background assumptions.
        """
    @staticmethod
    def multiply(discourse, readings):
        """
        Multiply every thread in ``discourse`` by every reading in ``readings``.

        Given discourse = [['A'], ['B']], readings = ['a', 'b', 'c'] , returns
        [['A', 'a'], ['A', 'b'], ['A', 'c'], ['B', 'a'], ['B', 'b'], ['B', 'c']]

        :param discourse: the current list of readings
        :type discourse: list of lists
        :param readings: an additional list of readings
        :type readings: list(Expression)
        :rtype: A list of lists
        """

def load_fol(s):
    """
    Temporarily duplicated from ``nltk.sem.util``.
    Convert a  file of first order formulas into a list of ``Expression`` objects.

    :param s: the contents of the file
    :type s: str
    :return: a list of parsed formulas.
    :rtype: list(Expression)
    """
def discourse_demo(reading_command: Incomplete | None = None) -> None:
    """
    Illustrate the various methods of ``DiscourseTester``
    """
def drt_discourse_demo(reading_command: Incomplete | None = None) -> None:
    """
    Illustrate the various methods of ``DiscourseTester``
    """
def spacer(num: int = 30) -> None: ...
def demo() -> None: ...
