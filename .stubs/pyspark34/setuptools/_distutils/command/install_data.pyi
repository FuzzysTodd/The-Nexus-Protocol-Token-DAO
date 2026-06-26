from ..core import Command as Command
from ..util import change_root as change_root, convert_path as convert_path
from _typeshed import Incomplete

class install_data(Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    install_dir: Incomplete
    outfiles: Incomplete
    root: Incomplete
    force: int
    data_files: Incomplete
    warn_dir: int
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_inputs(self): ...
    def get_outputs(self): ...
