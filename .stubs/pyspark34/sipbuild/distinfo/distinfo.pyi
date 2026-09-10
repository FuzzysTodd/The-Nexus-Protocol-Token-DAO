from ..exceptions import UserException as UserException
from ..pyproject import PyProject as PyProject
from ..version import SIP_VERSION_STR as SIP_VERSION_STR
from _typeshed import Incomplete

WHEEL_VERSION: str

def distinfo(name, console_scripts, gui_scripts, generator, generator_version, inventory, metadata_overrides, prefix, project_root, requires_dists, wheel_tag) -> None:
    """ Create and populate a .dist-info directory from an inventory file. """
def create_distinfo(distinfo_dir, wheel_tag, installed, metadata, requires_dists, project_root, console_scripts, gui_scripts, prefix_dir: str = '', generator: Incomplete | None = None, generator_version: Incomplete | None = None) -> None:
    """ Create and populate a .dist-info directory. """
def write_metadata(metadata, requires_dists, metadata_fn, project_root, prefix_dir: str = '') -> None:
    """ Write the meta-data, with additional requirements to a file. """
