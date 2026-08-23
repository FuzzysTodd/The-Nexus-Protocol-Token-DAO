import abc
from abc import abstractmethod
from overrides import EnforceOverrides
from typing import Dict, Type

class ChromaError(Exception, EnforceOverrides, metaclass=abc.ABCMeta):
    def code(self) -> int:
        """Return an appropriate HTTP response code for this error"""
    def message(self) -> str: ...
    @classmethod
    @abstractmethod
    def name(self) -> str:
        """Return the error name"""

class InvalidDimensionException(ChromaError):
    @classmethod
    def name(cls) -> str: ...

class InvalidCollectionException(ChromaError):
    @classmethod
    def name(cls) -> str: ...

class IDAlreadyExistsError(ChromaError):
    def code(self) -> int: ...
    @classmethod
    def name(cls) -> str: ...

class DuplicateIDError(ChromaError):
    @classmethod
    def name(cls) -> str: ...

class InvalidUUIDError(ChromaError):
    @classmethod
    def name(cls) -> str: ...

error_types: Dict[str, Type[ChromaError]]
