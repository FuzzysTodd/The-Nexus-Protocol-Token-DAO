from ..core import Command as Command
from ..errors import DistutilsOptionError as DistutilsOptionError, DistutilsPlatformError as DistutilsPlatformError
from ..util import get_platform as get_platform
from _typeshed import Incomplete

def show_formats() -> None:
    '''Print list of available formats (arguments to "--format" option).'''

class ListCompat(dict):
    def append(self, item) -> None: ...

class bdist(Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    help_options: Incomplete
    no_format_option: Incomplete
    default_format: Incomplete
    format_commands: Incomplete
    format_command = format_commands
    bdist_base: Incomplete
    plat_name: Incomplete
    formats: Incomplete
    dist_dir: Incomplete
    skip_build: int
    group: Incomplete
    owner: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
