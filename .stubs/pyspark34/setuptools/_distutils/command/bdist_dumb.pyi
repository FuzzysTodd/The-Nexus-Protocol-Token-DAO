from ..core import Command as Command
from ..dir_util import ensure_relative as ensure_relative, remove_tree as remove_tree
from ..errors import DistutilsPlatformError as DistutilsPlatformError
from ..sysconfig import get_python_version as get_python_version
from ..util import get_platform as get_platform
from _typeshed import Incomplete

class bdist_dumb(Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    default_format: Incomplete
    bdist_dir: Incomplete
    plat_name: Incomplete
    format: Incomplete
    keep_temp: int
    dist_dir: Incomplete
    skip_build: Incomplete
    relative: int
    owner: Incomplete
    group: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
