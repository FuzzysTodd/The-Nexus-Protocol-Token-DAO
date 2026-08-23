from . import api_handlers as api_handlers, handlers as handlers
from .terminalmanager import TerminalManager as TerminalManager
from _typeshed import Incomplete
from jupyter_server.extension.application import ExtensionApp

class TerminalsExtensionApp(ExtensionApp):
    """A terminals extension app."""
    name: str
    terminal_manager_class: Incomplete
    terminals_available: bool
    def initialize_settings(self) -> None:
        """Initialize settings."""
    terminal_manager: Incomplete
    def initialize_configurables(self) -> None:
        """Initialize configurables."""
    def initialize_handlers(self) -> None:
        """Initialize handlers."""
    def current_activity(self):
        """Get current activity info."""
    async def cleanup_terminals(self) -> None:
        """Shutdown all terminals.

        The terminals will shutdown themselves when this process no longer exists,
        but explicit shutdown allows the TerminalManager to cleanup.
        """
    async def stop_extension(self) -> None:
        """Stop the extension."""
