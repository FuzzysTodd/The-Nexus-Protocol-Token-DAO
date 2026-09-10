from .std import tqdm as std_tqdm
from IPython.html.widgets import ContainerWidget as HBox
from _typeshed import Incomplete

__all__ = ['tqdm_notebook', 'tnrange', 'tqdm', 'trange']

HBox = object

class TqdmHBox(HBox):
    """`ipywidgets.HBox` with a pretty representation"""

class tqdm_notebook(std_tqdm):
    """
    Experimental IPython/Jupyter Notebook widget using tqdm!
    """
    @staticmethod
    def status_printer(_, total: Incomplete | None = None, desc: Incomplete | None = None, ncols: Incomplete | None = None):
        """
        Manage the printing of an IPython/Jupyter Notebook progress bar widget.
        """
    displayed: bool
    def display(self, msg: Incomplete | None = None, pos: Incomplete | None = None, close: bool = False, bar_style: Incomplete | None = None, check_delay: bool = True) -> None: ...
    @property
    def colour(self): ...
    @colour.setter
    def colour(self, bar_color) -> None: ...
    disp: Incomplete
    ncols: Incomplete
    container: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """
        Supports the usual `tqdm.tqdm` parameters as well as those listed below.

        Parameters
        ----------
        display  : Whether to call `display(self.container)` immediately
            [default: True].
        """
    def __iter__(self): ...
    def update(self, n: int = 1): ...
    def close(self) -> None: ...
    def clear(self, *_, **__) -> None: ...
    def reset(self, total: Incomplete | None = None):
        """
        Resets to 0 iterations for repeated use.

        Consider combining with `leave=True`.

        Parameters
        ----------
        total  : int or float, optional. Total to use for the new bar.
        """

def tnrange(*args, **kwargs):
    """Shortcut for `tqdm.notebook.tqdm(range(*args), **kwargs)`."""
tqdm = tqdm_notebook
trange = tnrange
