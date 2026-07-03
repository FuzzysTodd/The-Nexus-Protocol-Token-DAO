import docutils.utils
from ..core import Command as Command
from ..errors import DistutilsSetupError as DistutilsSetupError
from _typeshed import Incomplete

class SilentReporter(docutils.utils.Reporter):
    messages: Incomplete
    def __init__(self, source, report_level, halt_level, stream: Incomplete | None = None, debug: int = 0, encoding: str = 'ascii', error_handler: str = 'replace') -> None: ...
    def system_message(self, level, message, *children, **kwargs): ...

class check(Command):
    """This command checks the meta-data of the package."""
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    restructuredtext: int
    metadata: int
    strict: int
    def initialize_options(self) -> None:
        """Sets default values for options."""
    def finalize_options(self) -> None: ...
    def warn(self, msg):
        """Counts the number of warnings that occurs."""
    def run(self) -> None:
        """Runs the command."""
    def check_metadata(self) -> None:
        """Ensures that all required elements of meta-data are supplied.

        Required fields:
            name, version

        Warns if any are missing.
        """
    def check_restructuredtext(self) -> None:
        """Checks if the long string fields are reST-compliant."""
