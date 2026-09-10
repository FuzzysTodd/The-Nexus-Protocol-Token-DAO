import abc
from abc import ABC, abstractmethod
from argparse import _SubParsersAction

class BaseHuggingfaceCLICommand(ABC, metaclass=abc.ABCMeta):
    @staticmethod
    @abstractmethod
    def register_subcommand(parser: _SubParsersAction): ...
    @abstractmethod
    def run(self): ...
