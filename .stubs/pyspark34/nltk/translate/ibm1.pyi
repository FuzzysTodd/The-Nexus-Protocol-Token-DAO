from _typeshed import Incomplete
from nltk.translate import AlignedSent as AlignedSent, Alignment as Alignment, IBMModel as IBMModel
from nltk.translate.ibm_model import Counts as Counts

class IBMModel1(IBMModel):
    """
    Lexical translation model that ignores word order

    >>> bitext = []
    >>> bitext.append(AlignedSent(['klein', 'ist', 'das', 'haus'], ['the', 'house', 'is', 'small']))
    >>> bitext.append(AlignedSent(['das', 'haus', 'ist', 'ja', 'groß'], ['the', 'house', 'is', 'big']))
    >>> bitext.append(AlignedSent(['das', 'buch', 'ist', 'ja', 'klein'], ['the', 'book', 'is', 'small']))
    >>> bitext.append(AlignedSent(['das', 'haus'], ['the', 'house']))
    >>> bitext.append(AlignedSent(['das', 'buch'], ['the', 'book']))
    >>> bitext.append(AlignedSent(['ein', 'buch'], ['a', 'book']))

    >>> ibm1 = IBMModel1(bitext, 5)

    >>> print(round(ibm1.translation_table['buch']['book'], 3))
    0.889
    >>> print(round(ibm1.translation_table['das']['book'], 3))
    0.062
    >>> print(round(ibm1.translation_table['buch'][None], 3))
    0.113
    >>> print(round(ibm1.translation_table['ja'][None], 3))
    0.073

    >>> test_sentence = bitext[2]
    >>> test_sentence.words
    ['das', 'buch', 'ist', 'ja', 'klein']
    >>> test_sentence.mots
    ['the', 'book', 'is', 'small']
    >>> test_sentence.alignment
    Alignment([(0, 0), (1, 1), (2, 2), (3, 2), (4, 3)])

    """
    translation_table: Incomplete
    def __init__(self, sentence_aligned_corpus, iterations, probability_tables: Incomplete | None = None) -> None:
        """
        Train on ``sentence_aligned_corpus`` and create a lexical
        translation model.

        Translation direction is from ``AlignedSent.mots`` to
        ``AlignedSent.words``.

        :param sentence_aligned_corpus: Sentence-aligned parallel corpus
        :type sentence_aligned_corpus: list(AlignedSent)

        :param iterations: Number of iterations to run training algorithm
        :type iterations: int

        :param probability_tables: Optional. Use this to pass in custom
            probability values. If not specified, probabilities will be
            set to a uniform distribution, or some other sensible value.
            If specified, the following entry must be present:
            ``translation_table``.
            See ``IBMModel`` for the type and purpose of this table.
        :type probability_tables: dict[str]: object
        """
    def set_uniform_probabilities(self, sentence_aligned_corpus): ...
    def train(self, parallel_corpus) -> None: ...
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
    def prob_alignment_point(self, s, t):
        """
        Probability that word ``t`` in the target sentence is aligned to
        word ``s`` in the source sentence
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
