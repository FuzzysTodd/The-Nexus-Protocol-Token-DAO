from requests import PreparedRequest as PreparedRequest
from responses import BaseResponse as BaseResponse
from typing import List, Tuple

class FirstMatchRegistry:
    def __init__(self) -> None: ...
    @property
    def registered(self) -> List['BaseResponse']: ...
    def reset(self) -> None: ...
    def find(self, request: PreparedRequest) -> Tuple[BaseResponse | None, List[str]]: ...
    def add(self, response: BaseResponse) -> BaseResponse: ...
    def remove(self, response: BaseResponse) -> List['BaseResponse']: ...
    def replace(self, response: BaseResponse) -> BaseResponse: ...

class OrderedRegistry(FirstMatchRegistry):
    """Registry where `Response` objects are dependent on the insertion order and invocation index.

    OrderedRegistry applies the rule of first in - first out. Responses should be invoked in
    the same order in which they were added to the registry. Otherwise, an error is returned.
    """
    def find(self, request: PreparedRequest) -> Tuple[BaseResponse | None, List[str]]:
        '''Find the next registered `Response` and check if it matches the request.

        Search is performed by taking the first element of the registered responses list
        and removing this object (popping from the list).

        Parameters
        ----------
        request : PreparedRequest
            Request that was caught by the custom adapter.

        Returns
        -------
        Tuple[Optional["BaseResponse"], List[str]]
            Matched `Response` object and empty list in case of match.
            Otherwise, None and a list with reasons for not finding a match.

        '''
