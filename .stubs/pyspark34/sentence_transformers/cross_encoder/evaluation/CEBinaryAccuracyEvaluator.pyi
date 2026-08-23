from ... import InputExample as InputExample
from _typeshed import Incomplete
from typing import List

logger: Incomplete

class CEBinaryAccuracyEvaluator:
    """
    This evaluator can be used with the CrossEncoder class.

    It is designed for CrossEncoders with 1 outputs. It measure the
    accuracy of the predict class vs. the gold labels. It uses a fixed threshold to determine the label (0 vs 1).

    See CEBinaryClassificationEvaluator for an evaluator that determines automatically the optimal threshold.
    """
    sentence_pairs: Incomplete
    labels: Incomplete
    name: Incomplete
    threshold: Incomplete
    csv_file: Incomplete
    csv_headers: Incomplete
    write_csv: Incomplete
    def __init__(self, sentence_pairs: List[List[str]], labels: List[int], name: str = '', threshold: float = 0.5, write_csv: bool = True) -> None: ...
    @classmethod
    def from_input_examples(cls, examples: List[InputExample], **kwargs): ...
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float: ...
