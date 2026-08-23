from _typeshed import Incomplete
from statsmodels.tsa.tsatools import freq_to_period as freq_to_period

def pandas_wrapper(func, trim_head: Incomplete | None = None, trim_tail: Incomplete | None = None, names: Incomplete | None = None, *args, **kwargs): ...
def pandas_wrapper_bunch(func, trim_head: Incomplete | None = None, trim_tail: Incomplete | None = None, names: Incomplete | None = None, *args, **kwargs): ...
def pandas_wrapper_predict(func, trim_head: Incomplete | None = None, trim_tail: Incomplete | None = None, columns: Incomplete | None = None, *args, **kwargs) -> None: ...
def pandas_wrapper_freq(func, trim_head: Incomplete | None = None, trim_tail: Incomplete | None = None, freq_kw: str = 'freq', columns: Incomplete | None = None, *args, **kwargs):
    """
    Return a new function that catches the incoming X, checks if it's pandas,
    calls the functions as is. Then wraps the results in the incoming index.

    Deals with frequencies. Expects that the function returns a tuple,
    a Bunch object, or a pandas-object.
    """
