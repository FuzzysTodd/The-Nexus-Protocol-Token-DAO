from _typeshed import Incomplete
from typing import Iterable

class TablePlotter:
    """
    Layout some DataFrames in vertical/horizontal layout for explanation.
    Used in merging.rst
    """
    cell_width: Incomplete
    cell_height: Incomplete
    font_size: Incomplete
    def __init__(self, cell_width: float = 0.37, cell_height: float = 0.25, font_size: float = 7.5) -> None: ...
    def plot(self, left, right, labels: Iterable[str] = (), vertical: bool = True):
        """
        Plot left / right DataFrames in specified layout.

        Parameters
        ----------
        left : list of DataFrames before operation is applied
        right : DataFrame of operation result
        labels : list of str to be drawn as titles of left DataFrames
        vertical : bool, default True
            If True, use vertical layout. If False, use horizontal layout.
        """

def main() -> None: ...
