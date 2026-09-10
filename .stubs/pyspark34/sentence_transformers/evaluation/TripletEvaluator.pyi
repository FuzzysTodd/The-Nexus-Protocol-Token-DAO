from . import SentenceEvaluator as SentenceEvaluator, SimilarityFunction as SimilarityFunction
from ..readers import InputExample as InputExample
from _typeshed import Incomplete
from typing import List

logger: Incomplete

class TripletEvaluator(SentenceEvaluator):
    """
    Evaluate a model based on a triplet: (sentence, positive_example, negative_example). Checks if distance(sentence,positive_example) < distance(sentence, negative_example).
    """
    anchors: Incomplete
    positives: Incomplete
    negatives: Incomplete
    name: Incomplete
    main_distance_function: Incomplete
    batch_size: Incomplete
    show_progress_bar: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    write_csv: Incomplete
    def __init__(self, anchors: List[str], positives: List[str], negatives: List[str], main_distance_function: SimilarityFunction = None, name: str = '', batch_size: int = 16, show_progress_bar: bool = False, write_csv: bool = True) -> None:
        """
        Constructs an evaluator based for the dataset


        :param dataloader:
            the data for the evaluation
        :param main_similarity:
            the similarity metric that will be used for the returned score

        """
    @classmethod
    def from_input_examples(cls, examples: List[InputExample], **kwargs): ...
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float: ...
