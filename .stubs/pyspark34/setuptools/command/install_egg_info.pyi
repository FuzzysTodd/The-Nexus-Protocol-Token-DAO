from .._path import ensure_directory as ensure_directory
from _typeshed import Incomplete
from setuptools import Command as Command, namespaces as namespaces
from setuptools.archive_util import unpack_archive as unpack_archive

class install_egg_info(namespaces.Installer, Command):
    """Install an .egg-info directory for the package"""
    description: str
    user_options: Incomplete
    install_dir: Incomplete
    def initialize_options(self) -> None: ...
    source: Incomplete
    target: Incomplete
    outputs: Incomplete
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_outputs(self): ...
    def copytree(self): ...
