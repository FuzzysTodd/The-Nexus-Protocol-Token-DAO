from .interactiveshell import TerminalInteractiveShell as TerminalInteractiveShell
from IPython.core import release as release, usage as usage
from IPython.core.application import BaseIPythonApplication as BaseIPythonApplication, ProfileDir as ProfileDir, base_aliases as base_aliases, base_flags as base_flags
from IPython.core.completer import IPCompleter as IPCompleter
from IPython.core.crashhandler import CrashHandler as CrashHandler
from IPython.core.formatters import PlainTextFormatter as PlainTextFormatter
from IPython.core.history import HistoryManager as HistoryManager
from IPython.core.magic import MagicsManager as MagicsManager
from IPython.core.magics import LoggingMagics as LoggingMagics, ScriptMagics as ScriptMagics
from IPython.core.shellapp import InteractiveShellApp as InteractiveShellApp, shell_aliases as shell_aliases, shell_flags as shell_flags
from IPython.extensions.storemagic import StoreMagics as StoreMagics
from IPython.paths import get_ipython_dir as get_ipython_dir
from _typeshed import Incomplete

class IPAppCrashHandler(CrashHandler):
    """sys.excepthook for IPython itself, leaves a detailed report on disk."""
    def __init__(self, app) -> None: ...
    def make_report(self, traceback):
        """Return a string containing a crash report."""

flags: Incomplete
frontend_flags: Incomplete
addflag: Incomplete
classic_config: Incomplete
aliases: Incomplete

class LocateIPythonApp(BaseIPythonApplication):
    description: str
    subcommands: Incomplete
    def start(self): ...

class TerminalIPythonApp(BaseIPythonApplication, InteractiveShellApp):
    name: str
    description: Incomplete
    crash_handler_class = IPAppCrashHandler
    examples: Incomplete
    flags = flags
    aliases = aliases
    classes: Incomplete
    interactive_shell_class: Incomplete
    subcommands: Incomplete
    auto_create: Incomplete
    quick: Incomplete
    display_banner: Incomplete
    force_interact: Incomplete
    something_to_run: Incomplete
    file_to_run: Incomplete
    def initialize(self, argv: Incomplete | None = None) -> None:
        """Do actions after construct, but before starting the app."""
    shell: Incomplete
    def init_shell(self) -> None:
        """initialize the InteractiveShell instance"""
    def init_banner(self) -> None:
        """optionally display the banner"""
    def start(self): ...

def load_default_config(ipython_dir: Incomplete | None = None):
    """Load the default config file from the default ipython_dir.

    This is useful for embedded shells.
    """

launch_new_instance: Incomplete
