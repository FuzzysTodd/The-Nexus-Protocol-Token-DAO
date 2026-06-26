from _typeshed import Incomplete
from typing import Any, AsyncIterator, Awaitable, Callable, Iterable, Tuple, TypeVar

__all__ = ['AsyncPageIterator', 'AsyncItemPaged']

ReturnType = TypeVar('ReturnType')
ResponseType = TypeVar('ResponseType')

class AsyncList(AsyncIterator[ReturnType]):
    def __init__(self, iterable: Iterable[ReturnType]) -> None:
        """Change an iterable into a fake async iterator.

        Could be useful to fill the async iterator contract when you get a list.

        :param iterable: A sync iterable of T
        """
    async def __anext__(self) -> ReturnType: ...

class AsyncPageIterator(AsyncIterator[AsyncIterator[ReturnType]]):
    continuation_token: Incomplete
    def __init__(self, get_next: Callable[[str | None], Awaitable[ResponseType]], extract_data: Callable[[ResponseType], Awaitable[Tuple[str, AsyncIterator[ReturnType]]]], continuation_token: str | None = None) -> None:
        """Return an async iterator of pages.

        :param get_next: Callable that take the continuation token and return a HTTP response
        :param extract_data: Callable that take an HTTP response and return a tuple continuation token,
         list of ReturnType
        :param str continuation_token: The continuation token needed by get_next
        """
    async def __anext__(self) -> AsyncIterator[ReturnType]: ...

class AsyncItemPaged(AsyncIterator[ReturnType]):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Return an async iterator of items.

        args and kwargs will be passed to the AsyncPageIterator constructor directly,
        except page_iterator_class
        """
    def by_page(self, continuation_token: str | None = None) -> AsyncIterator[AsyncIterator[ReturnType]]:
        """Get an async iterator of pages of objects, instead of an async iterator of objects.

        :param str continuation_token:
            An opaque continuation token. This value can be retrieved from the
            continuation_token field of a previous generator object. If specified,
            this generator will begin returning results from this point.
        :returns: An async iterator of pages (themselves async iterator of objects)
        :rtype: AsyncIterator[AsyncIterator[ReturnType]]
        """
    async def __anext__(self) -> ReturnType: ...
