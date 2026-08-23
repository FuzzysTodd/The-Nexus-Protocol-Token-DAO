from ..core import PyPIRCCommand as PyPIRCCommand
from ..errors import DistutilsError as DistutilsError, DistutilsOptionError as DistutilsOptionError
from ..spawn import spawn as spawn
from _typeshed import Incomplete

class upload(PyPIRCCommand):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    username: str
    password: str
    show_response: int
    sign: bool
    identity: Incomplete
    def initialize_options(self) -> None: ...
    repository: Incomplete
    realm: Incomplete
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def upload_file(self, command, pyversion, filename) -> None: ...
