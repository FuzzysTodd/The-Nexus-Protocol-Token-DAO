from .std import tqdm as std_tqdm
from _typeshed import Incomplete
from rich.progress import ProgressColumn

__all__ = ['tqdm_rich', 'trrange', 'tqdm', 'trange']

class FractionColumn(ProgressColumn):
    """Renders completed/total, e.g. '0.5/2.3 G'."""
    unit_scale: Incomplete
    unit_divisor: Incomplete
    def __init__(self, unit_scale: bool = False, unit_divisor: int = 1000) -> None: ...
    def render(self, task):
        """Calculate common unit for completed and total."""

class RateColumn(ProgressColumn):
    """Renders human readable transfer speed."""
    unit: Incomplete
    unit_scale: Incomplete
    unit_divisor: Incomplete
    def __init__(self, unit: str = '', unit_scale: bool = False, unit_divisor: int = 1000) -> None: ...
    def render(self, task):
        """Show data transfer speed."""

class tqdm_rich(std_tqdm):
    """Experimental rich.progress GUI version of tqdm!"""
    def __init__(self, *args, **kwargs) -> None:
        """
        This class accepts the following parameters *in addition* to
        the parameters accepted by `tqdm`.

        Parameters
        ----------
        progress  : tuple, optional
            arguments for `rich.progress.Progress()`.
        options  : dict, optional
            keyword arguments for `rich.progress.Progress()`.
        """
    def close(self) -> None: ...
    def clear(self, *_, **__) -> None: ...
    def display(self, *_, **__) -> None: ...
    def reset(self, total: Incomplete | None = None) -> None:
        """
        Resets to 0 iterations for repeated use.

        Parameters
        ----------
        total  : int or float, optional. Total to use for the new bar.
        """

def trrange(*args, **kwargs):
    """Shortcut for `tqdm.rich.tqdm(range(*args), **kwargs)`."""
tqdm = tqdm_rich
trange = trrange
