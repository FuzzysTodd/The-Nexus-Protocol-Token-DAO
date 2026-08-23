from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli import cmdoptions as cmdoptions
from pip._internal.cli.cmdoptions import make_target_python as make_target_python
from pip._internal.cli.req_command import RequirementCommand as RequirementCommand, with_cleanup as with_cleanup
from pip._internal.cli.status_codes import SUCCESS as SUCCESS
from pip._internal.operations.build.build_tracker import get_build_tracker as get_build_tracker
from pip._internal.req.req_install import check_legacy_setup_py_options as check_legacy_setup_py_options
from pip._internal.utils.misc import ensure_dir as ensure_dir, normalize_path as normalize_path, write_output as write_output
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory
from typing import List

logger: Incomplete

class DownloadCommand(RequirementCommand):
    '''
    Download packages from:

    - PyPI (and other indexes) using requirement specifiers.
    - VCS project urls.
    - Local project directories.
    - Local or remote source archives.

    pip also supports downloading from "requirements files", which provide
    an easy way to specify a whole environment to be downloaded.
    '''
    usage: str
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...
