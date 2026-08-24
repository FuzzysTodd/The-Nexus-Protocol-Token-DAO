import typing as t
from .paths import allow_insecure_writes as allow_insecure_writes, issue_insecure_write_warning as issue_insecure_write_warning, jupyter_config_dir as jupyter_config_dir, jupyter_config_path as jupyter_config_path, jupyter_data_dir as jupyter_data_dir, jupyter_path as jupyter_path, jupyter_runtime_dir as jupyter_runtime_dir
from .utils import ensure_dir_exists as ensure_dir_exists
from _typeshed import Incomplete
from traitlets import List
from traitlets.config.application import Application

base_aliases: dict[str, t.Any]
base_flags: dict[str, t.Any]

class NoStart(Exception):
    """Exception to raise when an application shouldn't start"""

class JupyterApp(Application):
    """Base class for Jupyter applications"""
    name: str
    description: str
    aliases = base_aliases
    flags = base_flags
    jupyter_path: list[str] | List
    config_dir: Incomplete
    @property
    def config_file_paths(self) -> list[str]: ...
    data_dir: Incomplete
    runtime_dir: Incomplete
    generate_config: Incomplete
    config_file_name: Incomplete
    config_file: Incomplete
    answer_yes: Incomplete
    def write_default_config(self) -> None:
        """Write our default config to a .py config file"""
    def migrate_config(self) -> None:
        """Migrate config/data from IPython 3"""
    def load_config_file(self, suppress_errors: bool = True) -> None:
        """Load the config file.

        By default, errors in loading config are handled, and a warning
        printed on screen. For testing, the suppress_errors option is set
        to False, so errors will make tests fail.
        """
    subcommand: Incomplete
    argv: Incomplete
    def initialize(self, argv: t.Any = None) -> None:
        """Initialize the application."""
    def start(self) -> None:
        """Start the whole thing"""
    @classmethod
    def launch_instance(cls, argv: t.Any = None, **kwargs: t.Any) -> None:
        """Launch an instance of a Jupyter Application"""
