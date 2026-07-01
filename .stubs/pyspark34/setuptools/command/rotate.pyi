from _typeshed import Incomplete
from setuptools import Command as Command

class rotate(Command):
    """Delete older distributions"""
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    match: Incomplete
    dist_dir: Incomplete
    keep: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
