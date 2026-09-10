from _typeshed import Incomplete
from collections.abc import Generator
from setuptools.command.egg_info import write_requirements as write_requirements
from setuptools.extern.packaging.tags import sys_tags as sys_tags
from setuptools.extern.packaging.utils import canonicalize_name as canonicalize_name

WHEEL_NAME: Incomplete
NAMESPACE_PACKAGE_INIT: str

def unpack(src_dir, dst_dir) -> None:
    """Move everything under `src_dir` to `dst_dir`, and delete the former."""
def disable_info_traces() -> Generator[None, None, None]:
    """
    Temporarily disable info traces.
    """

class Wheel:
    filename: Incomplete
    def __init__(self, filename) -> None: ...
    def tags(self):
        """List tags (py_version, abi, platform) supported by this wheel."""
    def is_compatible(self):
        """Is the wheel compatible with the current platform?"""
    def egg_name(self): ...
    def get_dist_info(self, zf): ...
    def install_as_egg(self, destination_eggdir) -> None:
        """Install wheel as an egg directory."""
