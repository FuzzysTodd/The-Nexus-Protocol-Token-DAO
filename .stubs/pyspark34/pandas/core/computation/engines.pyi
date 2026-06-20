import abc
from _typeshed import Incomplete
from pandas.core.computation.align import align_terms as align_terms, reconstruct_object as reconstruct_object
from pandas.core.computation.expr import Expr as Expr
from pandas.core.computation.ops import MATHOPS as MATHOPS, REDUCTIONS as REDUCTIONS
from pandas.errors import NumExprClobberingError as NumExprClobberingError
from pandas.io.formats import printing as printing

class AbstractEngine(metaclass=abc.ABCMeta):
    """Object serving as a base class for all engines."""
    has_neg_frac: bool
    expr: Incomplete
    aligned_axes: Incomplete
    result_type: Incomplete
    def __init__(self, expr) -> None: ...
    def convert(self) -> str:
        """
        Convert an expression for evaluation.

        Defaults to return the expression as a string.
        """
    def evaluate(self) -> object:
        """
        Run the engine on the expression.

        This method performs alignment which is necessary no matter what engine
        is being used, thus its implementation is in the base class.

        Returns
        -------
        object
            The result of the passed expression.
        """

class NumExprEngine(AbstractEngine):
    """NumExpr engine class"""
    has_neg_frac: bool

class PythonEngine(AbstractEngine):
    """
    Evaluate an expression in Python space.

    Mostly for testing purposes.
    """
    has_neg_frac: bool
    def evaluate(self): ...

ENGINES: dict[str, type[AbstractEngine]]
