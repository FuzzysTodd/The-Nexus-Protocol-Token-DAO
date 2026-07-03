from .client import NotebookClient as NotebookClient
from _typeshed import Incomplete
from jupyter_core.application import JupyterApp
from nbclient import __version__ as __version__

nbclient_aliases: dict
nbclient_flags: dict

class NbClientApp(JupyterApp):
    """
    An application used to execute notebook files (``*.ipynb``)
    """
    version: Incomplete
    name: str
    aliases = nbclient_aliases
    flags = nbclient_flags
    description: str
    notebooks: Incomplete
    timeout: int
    startup_timeout: int
    allow_errors: bool
    skip_cells_with_tag: str
    kernel_name: str
    def initialize(self, argv: Incomplete | None = None) -> None:
        """Initialize the app."""
    def get_notebooks(self):
        """Get the notebooks for the app."""
    def run_notebook(self, notebook_path) -> None:
        """Run a notebook by path."""

main: Incomplete
