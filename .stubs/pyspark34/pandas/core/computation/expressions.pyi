from _typeshed import Incomplete
from pandas._config import get_option as get_option
from pandas._typing import FuncType as FuncType
from pandas.core.computation.check import NUMEXPR_INSTALLED as NUMEXPR_INSTALLED
from pandas.core.ops import roperator as roperator
from pandas.util._exceptions import find_stack_level as find_stack_level

USE_NUMEXPR = NUMEXPR_INSTALLED

def set_use_numexpr(v: bool = True) -> None: ...
def set_numexpr_threads(n: Incomplete | None = None) -> None: ...
def evaluate(op, a, b, use_numexpr: bool = True):
    """
    Evaluate and return the expression of the op on a and b.

    Parameters
    ----------
    op : the actual operand
    a : left operand
    b : right operand
    use_numexpr : bool, default True
        Whether to try to use numexpr.
    """
def where(cond, a, b, use_numexpr: bool = True):
    """
    Evaluate the where condition cond on a and b.

    Parameters
    ----------
    cond : np.ndarray[bool]
    a : return if cond is True
    b : return if cond is False
    use_numexpr : bool, default True
        Whether to try to use numexpr.
    """
def set_test_mode(v: bool = True) -> None:
    """
    Keeps track of whether numexpr was used.

    Stores an additional ``True`` for every successful use of evaluate with
    numexpr since the last ``get_test_result``.
    """
def get_test_result() -> list[bool]:
    """
    Get test result and reset test_results.
    """
