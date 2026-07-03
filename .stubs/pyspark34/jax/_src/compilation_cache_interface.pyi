import abc
from abc import ABC, abstractmethod

class CacheInterface(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get(self, key: str): ...
    @abstractmethod
    def put(self, key: str, value: bytes): ...
