from _typeshed import Incomplete
from collections.abc import Generator

def expo(base: int = 2, factor: int = 1, max_value: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Generator for exponential decay.

    Args:
        base: The mathematical base of the exponentiation operation
        factor: Factor to multiply the exponentiation by.
        max_value: The maximum value to yield. Once the value in the
             true exponential sequence exceeds this, the value
             of max_value will forever after be yielded.
    """
def fibo(max_value: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Generator for fibonaccial decay.

    Args:
        max_value: The maximum value to yield. Once the value in the
             true fibonacci sequence exceeds this, the value
             of max_value will forever after be yielded.
    """
def constant(interval: int = 1) -> Generator[Incomplete, None, None]:
    """Generator for constant intervals.

    Args:
        interval: A constant value to yield or an iterable of such values.
    """
