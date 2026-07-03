from .evaluator import Evaluator as Evaluator
from _typeshed import Incomplete

class FunctionalEvaluator(Evaluator):
    """
    Functional evaluator that directly takes a function and thus should be general.

    Attributes
    ----------
    function
        The full name of the function.
    arguments
        Keyword arguments for the function other than model.
    """
    function: Incomplete
    arguments: Incomplete
    def __init__(self, function, **kwargs) -> None: ...
    def __eq__(self, other): ...
