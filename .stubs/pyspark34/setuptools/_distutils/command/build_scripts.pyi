from ..core import Command as Command
from ..dep_util import newer as newer
from ..util import convert_path as convert_path
from _typeshed import Incomplete

shebang_pattern: Incomplete
first_line_re = shebang_pattern

class build_scripts(Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    build_dir: Incomplete
    scripts: Incomplete
    force: Incomplete
    executable: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def get_source_files(self): ...
    def run(self) -> None: ...
    def copy_scripts(self):
        '''
        Copy each script listed in ``self.scripts``.

        If a script is marked as a Python script (first line matches
        \'shebang_pattern\', i.e. starts with ``#!`` and contains
        "python"), then adjust in the copy the first line to refer to
        the current Python interpreter.
        '''
