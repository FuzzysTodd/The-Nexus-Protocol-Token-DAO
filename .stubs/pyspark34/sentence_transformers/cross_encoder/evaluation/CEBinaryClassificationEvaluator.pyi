from ... import InputExample as InputExample
from ...evaluation import BinaryClassificationEvaluator as BinaryClassificationEvaluator
from _typeshed import Incomplete
from typing import List

logger: Incomplete

class CEBinaryClassificationEvaluator:
    """
    This evaluator can be used with the CrossEncoder class. Given sentence pairs and binary labels (0 and 1),
    it compute the average precision and the best possible f1 score
    """
    sentence_pairs: Incomplete
    labels: Incomplete
    name: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    write_csv: Incomplete
    def __init__(self, sentence_pairs: List[List[str]], labels: List[int], name: str = '', write_csv: bool = True) -> None: ...
    @classmethod
    def from_input_examples(cls, examples: List[InputExample], **kwargs): ...
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float: ...
