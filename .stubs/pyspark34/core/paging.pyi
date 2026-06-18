from .exceptions import AzureError as AzureError
from _typeshed import Incomplete
from typing import Any, Callable, Iterable, Iterator, Tuple, TypeVar

ReturnType = TypeVar('ReturnType')
ResponseType = TypeVar('ResponseType')

class PageIterator(Iterator[Iterator[ReturnType]]):
    continuation_token: Incomplete
    def __init__(self, get_next: Callable[[str | None], ResponseType], extract_data: Callable[[ResponseType], Tuple[str, Iterable[ReturnType]]], continuation_token: str | None = None) -> None:
        """Return an iterator of pages.

        :param get_next: Callable that take the continuation token and return a HTTP response
        :param extract_data: Callable that take an HTTP response and return a tuple continuation token,
         list of ReturnType
        :param str continuation_token: The continuation token needed by get_next
        """
    def __iter__(self) -> Iterator[Iterator[ReturnType]]: ...
    def __next__(self) -> Iterator[ReturnType]: ...
    next = __next__

class ItemPaged(Iterator[ReturnType]):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Return an iterator of items.

        args and kwargs will be passed to the PageIterator constructor directly,
        except page_iterator_class
        """
    def by_page(self, continuation_token: str | None = None) -> Iterator[Iterator[ReturnType]]:
        """Get an iterator of pages of objects, instead of an iterator of objects.

        :param str continuation_token:
            An opaque continuation token. This value can be retrieved from the
            continuation_token field of a previous generator object. If specified,
            this generator will begin returning results from this point.
        :returns: An iterator of pages (themselves iterator of objects)
        :rtype: iterator[iterator[ReturnType]]
        """
    def __iter__(self) -> Iterator[ReturnType]: ...
    def __next__(self) -> ReturnType: ...
    next = __next__
