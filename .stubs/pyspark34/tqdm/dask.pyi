from _typeshed import Incomplete
from dask.callbacks import Callback

__all__ = ['TqdmCallback']

class TqdmCallback(Callback):
    """Dask callback for task progress."""
    tqdm_class: Incomplete
    def __init__(self, start: Incomplete | None = None, pretask: Incomplete | None = None, tqdm_class=..., **tqdm_kwargs) -> None:
        """
        Parameters
        ----------
        tqdm_class  : optional
            `tqdm` class to use for bars [default: `tqdm.auto.tqdm`].
        tqdm_kwargs  : optional
            Any other arguments used for all bars.
        """
    def display(self) -> None:
        """Displays in the current cell in Notebooks."""
