from .std import tqdm as std_tqdm
from _typeshed import Incomplete

__all__ = ['tqdm_tk', 'ttkrange', 'tqdm', 'trange']

class tqdm_tk(std_tqdm):
    """
    Experimental Tkinter GUI version of tqdm!

    Note: Window interactivity suffers if `tqdm_tk` is not running within
    a Tkinter mainloop and values are generated infrequently. In this case,
    consider calling `tqdm_tk.refresh()` frequently in the Tk thread.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        This class accepts the following parameters *in addition* to
        the parameters accepted by `tqdm`.

        Parameters
        ----------
        grab  : bool, optional
            Grab the input across all windows of the process.
        tk_parent  : `tkinter.Wm`, optional
            Parent Tk window.
        cancel_callback  : Callable, optional
            Create a cancel button and set `cancel_callback` to be called
            when the cancel or window close button is clicked.
        """
    disable: bool
    def close(self) -> None: ...
    def clear(self, *_, **__) -> None: ...
    def display(self, *_, **__) -> None: ...
    def set_description(self, desc: Incomplete | None = None, refresh: bool = True) -> None: ...
    desc: Incomplete
    def set_description_str(self, desc: Incomplete | None = None, refresh: bool = True) -> None: ...
    def cancel(self) -> None:
        """
        `cancel_callback()` followed by `close()`
        when close/cancel buttons clicked.
        """
    def reset(self, total: Incomplete | None = None) -> None:
        """
        Resets to 0 iterations for repeated use.

        Parameters
        ----------
        total  : int or float, optional. Total to use for the new bar.
        """

def ttkrange(*args, **kwargs):
    """Shortcut for `tqdm.tk.tqdm(range(*args), **kwargs)`."""
tqdm = tqdm_tk
trange = ttkrange
