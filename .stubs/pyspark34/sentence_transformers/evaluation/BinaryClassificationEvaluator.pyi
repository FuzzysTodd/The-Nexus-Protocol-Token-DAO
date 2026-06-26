from . import SentenceEvaluator as SentenceEvaluator
from ..readers import InputExample as InputExample
from _typeshed import Incomplete
from typing import List

logger: Incomplete

class BinaryClassificationEvaluator(SentenceEvaluator):
    """
    Evaluate a model based on the similarity of the embeddings by calculating the accuracy of identifying similar and
    dissimilar sentences.
    The metrics are the cosine similarity as well as euclidean and Manhattan distance
    The returned score is the accuracy with a specified metric.

    The results are written in a CSV. If a CSV already exists, then values are appended.

    The labels need to be 0 for dissimilar pairs and 1 for similar pairs.

    :param sentences1: The first column of sentences
    :param sentences2: The second column of sentences
    :param labels: labels[i] is the label for the pair (sentences1[i], sentences2[i]). Must be 0 or 1
    :param name: Name for the output
    :param batch_size: Batch size used to compute embeddings
    :param show_progress_bar: If true, prints a progress bar
    :param write_csv: Write results to a CSV file
    """
    sentences1: Incomplete
    sentences2: Incomplete
    labels: Incomplete
    write_csv: Incomplete
    name: Incomplete
    batch_size: Incomplete
    show_progress_bar: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    def __init__(self, sentences1: List[str], sentences2: List[str], labels: List[int], name: str = '', batch_size: int = 32, show_progress_bar: bool = False, write_csv: bool = True) -> None: ...
    @classmethod
    def from_input_examples(cls, examples: List[InputExample], **kwargs): ...
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float: ...
    def compute_metrices(self, model): ...
    @staticmethod
    def find_best_acc_and_threshold(scores, labels, high_score_more_similar: bool): ...
    @staticmethod
    def find_best_f1_and_threshold(scores, labels, high_score_more_similar: bool): ...
