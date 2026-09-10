from .std import tqdm as std_tqdm
from _typeshed import Incomplete

__all__ = ['tqdm_gui', 'tgrange', 'tqdm', 'trange']

class tqdm_gui(std_tqdm):
    """Experimental Matplotlib GUI version of tqdm!"""
    mpl: Incomplete
    plt: Incomplete
    toolbar: Incomplete
    mininterval: Incomplete
    xdata: Incomplete
    ydata: Incomplete
    zdata: Incomplete
    hspan: Incomplete
    wasion: Incomplete
    ax: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    disable: bool
    def close(self) -> None: ...
    def clear(self, *_, **__) -> None: ...
    def display(self, *_, **__) -> None: ...

def tgrange(*args, **kwargs):
    """Shortcut for `tqdm.gui.tqdm(range(*args), **kwargs)`."""
tqdm = tqdm_gui
trange = tgrange
