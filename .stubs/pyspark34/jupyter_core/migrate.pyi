from .application import JupyterApp as JupyterApp
from .paths import jupyter_config_dir as jupyter_config_dir, jupyter_data_dir as jupyter_data_dir
from .utils import ensure_dir_exists as ensure_dir_exists
from _typeshed import Incomplete
from typing import Any

pjoin: Incomplete
migrations: Incomplete
custom_src_t: Incomplete
custom_dst_t: Incomplete
src: Incomplete
dst: Incomplete
config_migrations: Incomplete
regex: Incomplete
config_substitutions: Incomplete

def get_ipython_dir() -> str:
    """Return the IPython directory location.

    Not imported from IPython because the IPython implementation
    ensures that a writable directory exists,
    creating a temporary directory if not.
    We don't want to trigger that when checking if migration should happen.

    We only need to support the IPython < 4 behavior for migration,
    so importing for forward-compatibility and edge cases is not important.
    """
def migrate_dir(src: str, dst: str) -> bool:
    """Migrate a directory from src to dst"""
def migrate_file(src: str, dst: str, substitutions: Any = None) -> bool:
    """Migrate a single file from src to dst

    substitutions is an optional dict of {regex: replacement} for performing replacements on the file.
    """
def migrate_one(src: str, dst: str) -> bool:
    """Migrate one item

    dispatches to migrate_dir/_file
    """
def migrate_static_custom(src: str, dst: str) -> bool:
    """Migrate non-empty custom.js,css from src to dst

    src, dst are 'custom' directories containing custom.{js,css}
    """
def migrate_config(name: str, env: Any) -> list[Any]:
    """Migrate a config file.

    Includes substitutions for updated configurable names.
    """
def migrate() -> bool:
    """Migrate IPython configuration to Jupyter"""

class JupyterMigrate(JupyterApp):
    """A Jupyter Migration App."""
    name: str
    description: str
    def start(self) -> None:
        """Start the application."""

main: Incomplete
