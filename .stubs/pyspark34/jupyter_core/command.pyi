import argparse
from . import paths as paths
from .version import __version__ as __version__
from subprocess import Popen as Popen
from typing import Any

class JupyterParser(argparse.ArgumentParser):
    """A Jupyter argument parser."""
    @property
    def epilog(self) -> str | None:
        """Add subcommands to epilog on request

        Avoids searching PATH for subcommands unless help output is requested.
        """
    @epilog.setter
    def epilog(self, x: Any) -> None:
        """Ignore epilog set in Parser.__init__"""
    def argcomplete(self) -> None:
        """Trigger auto-completion, if enabled"""

def jupyter_parser() -> JupyterParser:
    """Create a jupyter parser object."""
def list_subcommands() -> list[str]:
    """List all jupyter subcommands

    searches PATH for `jupyter-name`

    Returns a list of jupyter's subcommand names, without the `jupyter-` prefix.
    Nested children (e.g. jupyter-sub-subsub) are not included.
    """
def main() -> None:
    """The command entry point."""
