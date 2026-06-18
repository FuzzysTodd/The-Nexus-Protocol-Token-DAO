from ... import InputExample as InputExample
from _typeshed import Incomplete
from typing import List

logger: Incomplete

class CECorrelationEvaluator:
    """
    This evaluator can be used with the CrossEncoder class. Given sentence pairs and continuous scores,
    it compute the pearson & spearman correlation between the predicted score for the sentence pair
    and the gold score.
    """
    sentence_pairs: Incomplete
    scores: Incomplete
    name: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    write_csv: Incomplete
    def __init__(self, sentence_pairs: List[List[str]], scores: List[float], name: str = '', write_csv: bool = True) -> None: ...
    @classmethod
    def from_input_examples(cls, examples: List[InputExample], **kwargs): ...
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float: ...
