from .std import tqdm as std_tqdm
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['tqdm_asyncio', 'tarange', 'tqdm', 'trange']

class tqdm_asyncio(std_tqdm):
    """
    Asynchronous-friendly version of tqdm.
    """
    iterable_awaitable: bool
    iterable_next: Incomplete
    iterable_iterator: Incomplete
    def __init__(self, iterable: Incomplete | None = None, *args, **kwargs) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self): ...
    def send(self, *args, **kwargs): ...
    @classmethod
    def as_completed(cls, fs, *, loop: Incomplete | None = None, timeout: Incomplete | None = None, total: Incomplete | None = None, **tqdm_kwargs) -> Generator[Incomplete, Incomplete, None]:
        """
        Wrapper for `asyncio.as_completed`.
        """
    @classmethod
    async def gather(cls, *fs, loop: Incomplete | None = None, timeout: Incomplete | None = None, total: Incomplete | None = None, **tqdm_kwargs):
        """
        Wrapper for `asyncio.gather`.
        """

def tarange(*args, **kwargs):
    """
    A shortcut for `tqdm.asyncio.tqdm(range(*args), **kwargs)`.
    """
tqdm = tqdm_asyncio
trange = tarange
