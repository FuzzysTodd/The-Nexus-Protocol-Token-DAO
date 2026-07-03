from .. import dir_util as dir_util
from .._log import log as log
from ..cmd import Command as Command
from _typeshed import Incomplete

class install_egg_info(Command):
    """Install an .egg-info file for the package"""
    description: str
    user_options: Incomplete
    install_dir: Incomplete
    def initialize_options(self) -> None: ...
    @property
    def basename(self):
        """
        Allow basename to be overridden by child class.
        Ref pypa/distutils#2.
        """
    target: Incomplete
    outputs: Incomplete
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_outputs(self): ...

def safe_name(name):
    """Convert an arbitrary string to a standard distribution name

    Any runs of non-alphanumeric/. characters are replaced with a single '-'.
    """
def safe_version(version):
    """Convert an arbitrary string to a standard version string

    Spaces become dots, and all other non-alphanumeric characters become
    dashes, with runs of multiple dashes condensed to a single dash.
    """
def to_filename(name):
    """Convert a project or version name to its filename-escaped form

    Any '-' characters are currently replaced with '_'.
    """
