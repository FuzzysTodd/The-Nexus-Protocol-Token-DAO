import abc
from . import BaseTransformersCLICommand as BaseTransformersCLICommand
from _typeshed import Incomplete
from argparse import ArgumentParser
from typing import List, Union

class UserCommands(BaseTransformersCLICommand, metaclass=abc.ABCMeta):
    @staticmethod
    def register_subcommand(parser: ArgumentParser): ...

class ANSI:
    """
    Helper for en.wikipedia.org/wiki/ANSI_escape_code
    """
    @classmethod
    def bold(cls, s): ...
    @classmethod
    def red(cls, s): ...
    @classmethod
    def gray(cls, s): ...

def tabulate(rows: List[List[Union[str, int]]], headers: List[str]) -> str:
    """
    Inspired by:

    - stackoverflow.com/a/8356620/593036
    - stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
    """

class BaseUserCommand:
    args: Incomplete
    def __init__(self, args) -> None: ...

class LoginCommand(BaseUserCommand):
    def run(self) -> None: ...

class WhoamiCommand(BaseUserCommand):
    def run(self) -> None: ...

class LogoutCommand(BaseUserCommand):
    def run(self) -> None: ...

class RepoCreateCommand(BaseUserCommand):
    def run(self) -> None: ...
