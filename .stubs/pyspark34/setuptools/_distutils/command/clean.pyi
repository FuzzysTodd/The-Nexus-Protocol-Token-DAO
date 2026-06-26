from ..core import Command as Command
from ..dir_util import remove_tree as remove_tree
from _typeshed import Incomplete

class clean(Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    build_base: Incomplete
    build_lib: Incomplete
    build_temp: Incomplete
    build_scripts: Incomplete
    bdist_base: Incomplete
    all: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
