from . import SentenceEvaluator as SentenceEvaluator
from _typeshed import Incomplete
from typing import Iterable

class SequentialEvaluator(SentenceEvaluator):
    """
    This evaluator allows that multiple sub-evaluators are passed. When the model is evaluated,
    the data is passed sequentially to all sub-evaluators.

    All scores are passed to 'main_score_function', which derives one final score value
    """
    evaluators: Incomplete
    main_score_function: Incomplete
    def __init__(self, evaluators: Iterable[SentenceEvaluator], main_score_function=...) -> None: ...
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float: ...
