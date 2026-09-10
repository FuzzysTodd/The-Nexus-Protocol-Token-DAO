from typing import AsyncGenerator, Callable, Iterable

__all__ = ['aclosing', 'generator_to_async_generator']

async def aclosing(thing: _T_Generator) -> AsyncGenerator[_T_Generator, None]:
    """Similar to `contextlib.aclosing`, in Python 3.10."""

class _Done: ...

async def generator_to_async_generator(get_iterable: Callable[[], Iterable[_T]], buffer_size: int = ...) -> AsyncGenerator[_T, None]:
    """
    Turn a generator or iterable into an async generator.

    This works by running the generator in a background thread.

    :param get_iterable: Function that returns a generator or iterable when
        called.
    :param buffer_size: Size of the queue between the async consumer and the
        synchronous generator that produces items.
    """
