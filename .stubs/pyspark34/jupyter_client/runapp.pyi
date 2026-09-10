import typing as t
from . import __version__ as __version__
from .consoleapp import JupyterConsoleApp as JupyterConsoleApp, app_aliases as app_aliases, app_flags as app_flags
from _typeshed import Incomplete
from jupyter_core.application import JupyterApp

OUTPUT_TIMEOUT: int
flags: Incomplete
frontend_flags_dict: Incomplete
aliases: Incomplete
frontend_aliases_dict: Incomplete
frontend_aliases: Incomplete
frontend_flags: Incomplete

class RunApp(JupyterApp, JupyterConsoleApp):
    """An Jupyter Console app to run files."""
    version = __version__
    name: str
    description: str
    flags: Incomplete
    aliases: Incomplete
    frontend_aliases: Incomplete
    frontend_flags: Incomplete
    kernel_timeout: Incomplete
    filenames_to_run: Incomplete
    def parse_command_line(self, argv: list[str] | None = None) -> None:
        """Parse the command line arguments."""
    def initialize(self, argv: list[str] | None = None) -> None:
        """Initialize the app."""
    def handle_sigint(self, *args: t.Any) -> None:
        """Handle SIGINT."""
    kernel_info: Incomplete
    def init_kernel_info(self) -> None:
        """Wait for a kernel to be ready, and store kernel info"""
    def start(self) -> None:
        """Start the application."""

main: Incomplete

launch_new_instance: Incomplete
