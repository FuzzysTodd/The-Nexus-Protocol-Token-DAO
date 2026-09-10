import abc
from abc import ABC, abstractmethod
from chromadb.config import Settings as Settings

class Server(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def __init__(self, settings: Settings): ...
