from .cmd import Command as Command
from _typeshed import Incomplete

DEFAULT_PYPIRC: str

class PyPIRCCommand(Command):
    """Base command that knows how to handle the .pypirc file"""
    DEFAULT_REPOSITORY: str
    DEFAULT_REALM: str
    repository: Incomplete
    realm: Incomplete
    user_options: Incomplete
    boolean_options: Incomplete
    show_response: int
    def initialize_options(self) -> None:
        """Initialize options."""
    def finalize_options(self) -> None:
        """Finalizes options."""
