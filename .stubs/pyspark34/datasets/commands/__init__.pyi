import abc
from abc import ABC, abstractmethod
from argparse import ArgumentParser

class BaseDatasetsCLICommand(ABC, metaclass=abc.ABCMeta):
    @staticmethod
    @abstractmethod
    def register_subcommand(parser: ArgumentParser): ...
    @abstractmethod
    def run(self): ...
