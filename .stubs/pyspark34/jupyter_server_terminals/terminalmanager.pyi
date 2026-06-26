from _typeshed import Incomplete
from terminado.management import NamedTermManager
from traitlets.config import LoggingConfigurable

RUNNING_TOTAL: Incomplete

class TerminalManager(LoggingConfigurable, NamedTermManager):
    """A MultiTerminalManager for use in the notebook webserver"""
    cull_inactive_timeout: Incomplete
    cull_interval_default: int
    cull_interval: Incomplete
    def create(self, **kwargs):
        """Create a new terminal."""
    def get(self, name):
        """Get terminal 'name'."""
    def list(self):
        """Get a list of all running terminals."""
    async def terminate(self, name, force: bool = False) -> None:
        """Terminate terminal 'name'."""
    async def terminate_all(self) -> None:
        """Terminate all terminals."""
    def get_terminal_model(self, name):
        """Return a JSON-safe dict representing a terminal.
        For use in representing terminals in the JSON APIs.
        """
    def pre_pty_read_hook(self, ptywclients) -> None:
        """The pre-pty read hook."""
