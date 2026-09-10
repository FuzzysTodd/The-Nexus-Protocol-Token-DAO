from _typeshed import Incomplete
from nltk.translate import AlignedSent as AlignedSent, Alignment as Alignment, IBMModel as IBMModel, IBMModel2 as IBMModel2
from nltk.translate.ibm_model import Counts as Counts

class IBMModel3(IBMModel):
    """
    Translation model that considers how a word can be aligned to
    multiple words in another language

    >>> bitext = []
    >>> bitext.append(AlignedSent(['klein', 'ist', 'das', 'haus'], ['the', 'house', 'is', 'small']))
    >>> bitext.append(AlignedSent(['das', 'haus', 'war', 'ja', 'groß'], ['the', 'house', 'was', 'big']))
    >>> bitext.append(AlignedSent(['das', 'buch', 'ist', 'ja', 'klein'], ['the', 'book', 'is', 'small']))
    >>> bitext.append(AlignedSent(['ein', 'haus', 'ist', 'klein'], ['a', 'house', 'is', 'small']))
    >>> bitext.append(AlignedSent(['das', 'haus'], ['the', 'house']))
    >>> bitext.append(AlignedSent(['das', 'buch'], ['the', 'book']))
    >>> bitext.append(AlignedSent(['ein', 'buch'], ['a', 'book']))
    >>> bitext.append(AlignedSent(['ich', 'fasse', 'das', 'buch', 'zusammen'], ['i', 'summarize', 'the', 'book']))
    >>> bitext.append(AlignedSent(['fasse', 'zusammen'], ['summarize']))

    >>> ibm3 = IBMModel3(bitext, 5)

    >>> print(round(ibm3.translation_table['buch']['book'], 3))
    1.0
    >>> print(round(ibm3.translation_table['das']['book'], 3))
    0.0
    >>> print(round(ibm3.translation_table['ja'][None], 3))
    1.0

    >>> print(round(ibm3.distortion_table[1][1][2][2], 3))
    1.0
    >>> print(round(ibm3.distortion_table[1][2][2][2], 3))
    0.0
    >>> print(round(ibm3.distortion_table[2][2][4][5], 3))
    0.75

    >>> print(round(ibm3.fertility_table[2]['summarize'], 3))
    1.0
    >>> print(round(ibm3.fertility_table[1]['book'], 3))
    1.0

    >>> print(round(ibm3.p1, 3))
    0.054

    >>> test_sentence = bitext[2]
    >>> test_sentence.words
    ['das', 'buch', 'ist', 'ja', 'klein']
    >>> test_sentence.mots
    ['the', 'book', 'is', 'small']
    >>> test_sentence.alignment
    Alignment([(0, 0), (1, 1), (2, 2), (3, None), (4, 3)])

    """
    translation_table: Incomplete
    alignment_table: Incomplete
    fertility_table: Incomplete
    p1: Incomplete
    distortion_table: Incomplete
    def __init__(self, sentence_aligned_corpus, iterations, probability_tables: Incomplete | None = None) -> None:
        """
        Train on ``sentence_aligned_corpus`` and create a lexical
        translation model, a distortion model, a fertility model, and a
        model for generating NULL-aligned words.

        Translation direction is from ``AlignedSent.mots`` to
        ``AlignedSent.words``.

        :param sentence_aligned_corpus: Sentence-aligned parallel corpus
        :type sentence_aligned_corpus: list(AlignedSent)

        :param iterations: Number of iterations to run training algorithm
        :type iterations: int

        :param probability_tables: Optional. Use this to pass in custom
            probability values. If not specified, probabilities will be
            set to a uniform distribution, or some other sensible value.
            If specified, all the following entries must be present:
            ``translation_table``, ``alignment_table``,
            ``fertility_table``, ``p1``, ``distortion_table``.
            See ``IBMModel`` for the type and purpose of these tables.
        :type probability_tables: dict[str]: object
        """
    def reset_probabilities(self): ...
    def set_uniform_probabilities(self, sentence_aligned_corpus): ...
    def train(self, parallel_corpus) -> None: ...
    def maximize_distortion_probabilities(self, counts) -> None: ...
    def prob_t_a_given_s(self, alignment_info):
        """
        Probability of target sentence and an alignment given the
        source sentence
        """

class Model3Counts(Counts):
    """
    Data object to store counts of various parameters during training.
    Includes counts for distortion.
    """
    distortion: Incomplete
    distortion_for_any_j: Incomplete
    def __init__(self) -> None: ...
    def update_distortion(self, count, alignment_info, j, l, m) -> None: ...
