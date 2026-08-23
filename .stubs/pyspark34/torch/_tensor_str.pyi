from _typeshed import Incomplete
from torch import inf as inf

class __PrinterOptions:
    precision: int
    threshold: float
    edgeitems: int
    linewidth: int
    sci_mode: bool | None

PRINT_OPTS: Incomplete

def set_printoptions(precision: Incomplete | None = None, threshold: Incomplete | None = None, edgeitems: Incomplete | None = None, linewidth: Incomplete | None = None, profile: Incomplete | None = None, sci_mode: Incomplete | None = None) -> None:
    """Set options for printing. Items shamelessly taken from NumPy

    Args:
        precision: Number of digits of precision for floating point output
            (default = 4).
        threshold: Total number of array elements which trigger summarization
            rather than full `repr` (default = 1000).
        edgeitems: Number of array items in summary at beginning and end of
            each dimension (default = 3).
        linewidth: The number of characters per line for the purpose of
            inserting line breaks (default = 80). Thresholded matrices will
            ignore this parameter.
        profile: Sane defaults for pretty printing. Can override with any of
            the above options. (any one of `default`, `short`, `full`)
        sci_mode: Enable (True) or disable (False) scientific notation. If
            None (default) is specified, the value is defined by
            `torch._tensor_str._Formatter`. This value is automatically chosen
            by the framework.

    Example::

        >>> # Limit the precision of elements
        >>> torch.set_printoptions(precision=2)
        >>> torch.tensor([1.12345])
        tensor([1.12])
        >>> # Limit the number of elements shown
        >>> torch.set_printoptions(threshold=5)
        >>> torch.arange(10)
        tensor([0, 1, 2, ..., 7, 8, 9])
        >>> # Restore defaults
        >>> torch.set_printoptions(profile='default')
        >>> torch.tensor([1.12345])
        tensor([1.1235])
        >>> torch.arange(10)
        tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    """
def tensor_totype(t): ...

class _Formatter:
    floating_dtype: Incomplete
    int_mode: bool
    sci_mode: bool
    max_width: int
    def __init__(self, tensor) -> None: ...
    def width(self): ...
    def format(self, value): ...

def get_summarized_data(self): ...
