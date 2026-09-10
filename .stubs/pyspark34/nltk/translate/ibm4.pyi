from _typeshed import Incomplete
from nltk.translate import AlignedSent as AlignedSent, Alignment as Alignment, IBMModel as IBMModel, IBMModel3 as IBMModel3
from nltk.translate.ibm_model import Counts as Counts, longest_target_sentence_length as longest_target_sentence_length

class IBMModel4(IBMModel):
    """
    Translation model that reorders output words based on their type and
    their distance from other related words in the output sentence

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
    >>> src_classes = {'the': 0, 'a': 0, 'small': 1, 'big': 1, 'house': 2, 'book': 2, 'is': 3, 'was': 3, 'i': 4, 'summarize': 5 }
    >>> trg_classes = {'das': 0, 'ein': 0, 'haus': 1, 'buch': 1, 'klein': 2, 'groß': 2, 'ist': 3, 'war': 3, 'ja': 4, 'ich': 5, 'fasse': 6, 'zusammen': 6 }

    >>> ibm4 = IBMModel4(bitext, 5, src_classes, trg_classes)

    >>> print(round(ibm4.translation_table['buch']['book'], 3))
    1.0
    >>> print(round(ibm4.translation_table['das']['book'], 3))
    0.0
    >>> print(round(ibm4.translation_table['ja'][None], 3))
    1.0

    >>> print(round(ibm4.head_distortion_table[1][0][1], 3))
    1.0
    >>> print(round(ibm4.head_distortion_table[2][0][1], 3))
    0.0
    >>> print(round(ibm4.non_head_distortion_table[3][6], 3))
    0.5

    >>> print(round(ibm4.fertility_table[2]['summarize'], 3))
    1.0
    >>> print(round(ibm4.fertility_table[1]['book'], 3))
    1.0

    >>> print(round(ibm4.p1, 3))
    0.033

    >>> test_sentence = bitext[2]
    >>> test_sentence.words
    ['das', 'buch', 'ist', 'ja', 'klein']
    >>> test_sentence.mots
    ['the', 'book', 'is', 'small']
    >>> test_sentence.alignment
    Alignment([(0, 0), (1, 1), (2, 2), (3, None), (4, 3)])

    """
    src_classes: Incomplete
    trg_classes: Incomplete
    translation_table: Incomplete
    alignment_table: Incomplete
    fertility_table: Incomplete
    p1: Incomplete
    head_distortion_table: Incomplete
    non_head_distortion_table: Incomplete
    def __init__(self, sentence_aligned_corpus, iterations, source_word_classes, target_word_classes, probability_tables: Incomplete | None = None) -> None:
        """
        Train on ``sentence_aligned_corpus`` and create a lexical
        translation model, distortion models, a fertility model, and a
        model for generating NULL-aligned words.

        Translation direction is from ``AlignedSent.mots`` to
        ``AlignedSent.words``.

        :param sentence_aligned_corpus: Sentence-aligned parallel corpus
        :type sentence_aligned_corpus: list(AlignedSent)

        :param iterations: Number of iterations to run training algorithm
        :type iterations: int

        :param source_word_classes: Lookup table that maps a source word
            to its word class, the latter represented by an integer id
        :type source_word_classes: dict[str]: int

        :param target_word_classes: Lookup table that maps a target word
            to its word class, the latter represented by an integer id
        :type target_word_classes: dict[str]: int

        :param probability_tables: Optional. Use this to pass in custom
            probability values. If not specified, probabilities will be
            set to a uniform distribution, or some other sensible value.
            If specified, all the following entries must be present:
            ``translation_table``, ``alignment_table``,
            ``fertility_table``, ``p1``, ``head_distortion_table``,
            ``non_head_distortion_table``. See ``IBMModel`` and
            ``IBMModel4`` for the type and purpose of these tables.
        :type probability_tables: dict[str]: object
        """
    def reset_probabilities(self): ...
    def set_uniform_probabilities(self, sentence_aligned_corpus):
        """
        Set distortion probabilities uniformly to
        1 / cardinality of displacement values
        """
    def train(self, parallel_corpus) -> None: ...
    def maximize_distortion_probabilities(self, counts) -> None: ...
    def prob_t_a_given_s(self, alignment_info):
        """
        Probability of target sentence and an alignment given the
        source sentence
        """
    @staticmethod
    def model4_prob_t_a_given_s(alignment_info, ibm_model): ...

class Model4Counts(Counts):
    """
    Data object to store counts of various parameters during training.
    Includes counts for distortion.
    """
    head_distortion: Incomplete
    head_distortion_for_any_dj: Incomplete
    non_head_distortion: Incomplete
    non_head_distortion_for_any_dj: Incomplete
    def __init__(self) -> None: ...
    def update_distortion(self, count, alignment_info, j, src_classes, trg_classes) -> None: ...
