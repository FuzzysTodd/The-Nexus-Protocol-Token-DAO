from . import SentenceEvaluator as SentenceEvaluator, SimilarityFunction as SimilarityFunction
from ..readers import InputExample as InputExample
from _typeshed import Incomplete
from typing import List

logger: Incomplete

class EmbeddingSimilarityEvaluator(SentenceEvaluator):
    """
    Evaluate a model based on the similarity of the embeddings by calculating the Spearman and Pearson rank correlation
    in comparison to the gold standard labels.
    The metrics are the cosine similarity as well as euclidean and Manhattan distance
    The returned score is the Spearman correlation with a specified metric.

    The results are written in a CSV. If a CSV already exists, then values are appended.
    """
    sentences1: Incomplete
    sentences2: Incomplete
    scores: Incomplete
    write_csv: Incomplete
    main_similarity: Incomplete
    name: Incomplete
    batch_size: Incomplete
    show_progress_bar: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    def __init__(self, sentences1: List[str], sentences2: List[str], scores: List[float], batch_size: int = 16, main_similarity: SimilarityFunction = None, name: str = '', show_progress_bar: bool = False, write_csv: bool = True) -> None:
        """
        Constructs an evaluator based for the dataset

        The labels need to indicate the similarity between the sentences.

        :param sentences1:  List with the first sentence in a pair
        :param sentences2: List with the second sentence in a pair
        :param scores: Similarity score between sentences1[i] and sentences2[i]
        :param write_csv: Write results to a CSV file
        """
    @classmethod
    def from_input_examples(cls, examples: List[InputExample], **kwargs): ...
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float: ...
