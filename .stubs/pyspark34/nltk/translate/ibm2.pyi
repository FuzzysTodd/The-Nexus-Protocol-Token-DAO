from _typeshed import Incomplete
from nltk.translate import AlignedSent as AlignedSent, Alignment as Alignment, IBMModel as IBMModel, IBMModel1 as IBMModel1
from nltk.translate.ibm_model import Counts as Counts

class IBMModel2(IBMModel):
    """
    Lexical translation model that considers word order

    >>> bitext = []
    >>> bitext.append(AlignedSent(['klein', 'ist', 'das', 'haus'], ['the', 'house', 'is', 'small']))
    >>> bitext.append(AlignedSent(['das', 'haus', 'ist', 'ja', 'groß'], ['the', 'house', 'is', 'big']))
    >>> bitext.append(AlignedSent(['das', 'buch', 'ist', 'ja', 'klein'], ['the', 'book', 'is', 'small']))
    >>> bitext.append(AlignedSent(['das', 'haus'], ['the', 'house']))
    >>> bitext.append(AlignedSent(['das', 'buch'], ['the', 'book']))
    >>> bitext.append(AlignedSent(['ein', 'buch'], ['a', 'book']))

    >>> ibm2 = IBMModel2(bitext, 5)

    >>> print(round(ibm2.translation_table['buch']['book'], 3))
    1.0
    >>> print(round(ibm2.translation_table['das']['book'], 3))
    0.0
    >>> print(round(ibm2.translation_table['buch'][None], 3))
    0.0
    >>> print(round(ibm2.translation_table['ja'][None], 3))
    0.0

    >>> print(round(ibm2.alignment_table[1][1][2][2], 3))
    0.939
    >>> print(round(ibm2.alignment_table[1][2][2][2], 3))
    0.0
    >>> print(round(ibm2.alignment_table[2][2][4][5], 3))
    1.0

    >>> test_sentence = bitext[2]
    >>> test_sentence.words
    ['das', 'buch', 'ist', 'ja', 'klein']
    >>> test_sentence.mots
    ['the', 'book', 'is', 'small']
    >>> test_sentence.alignment
    Alignment([(0, 0), (1, 1), (2, 2), (3, 2), (4, 3)])

    """
    translation_table: Incomplete
    alignment_table: Incomplete
    def __init__(self, sentence_aligned_corpus, iterations, probability_tables: Incomplete | None = None) -> None:
        """
        Train on ``sentence_aligned_corpus`` and create a lexical
        translation model and an alignment model.

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
            ``translation_table``, ``alignment_table``.
            See ``IBMModel`` for the type and purpose of these tables.
        :type probability_tables: dict[str]: object
        """
    def set_uniform_probabilities(self, sentence_aligned_corpus) -> None: ...
    def train(self, parallel_corpus) -> None: ...
    def maximize_alignment_probabilities(self, counts) -> None: ...
    def prob_all_alignments(self, src_sentence, trg_sentence):
        """
        Computes the probability of all possible word alignments,
        expressed as a marginal distribution over target words t

        Each entry in the return value represents the contribution to
        the total alignment probability by the target word t.

        To obtain probability(alignment | src_sentence, trg_sentence),
        simply sum the entries in the return value.

        :return: Probability of t for all s in ``src_sentence``
        :rtype: dict(str): float
        """
    def prob_alignment_point(self, i, j, src_sentence, trg_sentence):
        """
        Probability that position j in ``trg_sentence`` is aligned to
        position i in the ``src_sentence``
        """
    def prob_t_a_given_s(self, alignment_info):
        """
        Probability of target sentence and an alignment given the
        source sentence
        """
    def align_all(self, parallel_corpus) -> None: ...
    def align(self, sentence_pair) -> None:
        """
        Determines the best word alignment for one sentence pair from
        the corpus that the model was trained on.

        The best alignment will be set in ``sentence_pair`` when the
        method returns. In contrast with the internal implementation of
        IBM models, the word indices in the ``Alignment`` are zero-
        indexed, not one-indexed.

        :param sentence_pair: A sentence in the source language and its
            counterpart sentence in the target language
        :type sentence_pair: AlignedSent
        """

class Model2Counts(Counts):
    """
    Data object to store counts of various parameters during training.
    Includes counts for alignment.
    """
    alignment: Incomplete
    alignment_for_any_i: Incomplete
    def __init__(self) -> None: ...
    def update_lexical_translation(self, count, s, t) -> None: ...
    def update_alignment(self, count, i, j, l, m) -> None: ...
