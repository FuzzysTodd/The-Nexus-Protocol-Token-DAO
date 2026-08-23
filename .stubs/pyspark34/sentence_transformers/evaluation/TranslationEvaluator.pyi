from . import SentenceEvaluator as SentenceEvaluator
from ..util import pytorch_cos_sim as pytorch_cos_sim
from _typeshed import Incomplete
from typing import List

logger: Incomplete

class TranslationEvaluator(SentenceEvaluator):
    """
    Given two sets of sentences in different languages, e.g. (en_1, en_2, en_3...) and (fr_1, fr_2, fr_3, ...),
    and assuming that fr_i is the translation of en_i.
    Checks if vec(en_i) has the highest similarity to vec(fr_i). Computes the accurarcy in both directions
    """
    source_sentences: Incomplete
    target_sentences: Incomplete
    name: Incomplete
    batch_size: Incomplete
    show_progress_bar: Incomplete
    print_wrong_matches: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    write_csv: Incomplete
    def __init__(self, source_sentences: List[str], target_sentences: List[str], show_progress_bar: bool = False, batch_size: int = 16, name: str = '', print_wrong_matches: bool = False, write_csv: bool = True) -> None:
        """
        Constructs an evaluator based for the dataset

        The labels need to indicate the similarity between the sentences.

        :param source_sentences:
            List of sentences in source language
        :param target_sentences:
            List of sentences in target language
        :param print_wrong_matches:
            Prints incorrect matches
        :param write_csv:
            Write results to CSV file
        """
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float: ...
