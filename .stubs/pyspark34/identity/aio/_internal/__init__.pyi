import abc
from .aad_client import AadClient as AadClient
from .decorators import wrap_exceptions as wrap_exceptions

__all__ = ['AadClient', 'AsyncContextManager', 'wrap_exceptions']

class AsyncContextManager(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def close(self): ...
    async def __aenter__(self): ...
    async def __aexit__(self, *args) -> None: ...
