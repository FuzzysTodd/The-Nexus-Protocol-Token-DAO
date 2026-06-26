from _typeshed import Incomplete
from setuptools.command.setopt import config_file as config_file, edit_config as edit_config, option_base as option_base

def shquote(arg):
    """Quote an argument for later parsing by shlex.split()"""

class alias(option_base):
    """Define a shortcut that invokes one or more commands"""
    description: str
    command_consumes_arguments: bool
    user_options: Incomplete
    boolean_options: Incomplete
    args: Incomplete
    remove: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...

def format_alias(name, aliases): ...
