import distutils.command.sdist as orig
from .._importlib import metadata as metadata
from _typeshed import Incomplete
from collections.abc import Generator

def walk_revctrl(dirname: str = '') -> Generator[Incomplete, None, None]:
    """Find all files under revision control"""

class sdist(orig.sdist):
    """Smart sdist that finds anything supported by revision control"""
    user_options: Incomplete
    negative_opt: Incomplete
    README_EXTENSIONS: Incomplete
    READMES: Incomplete
    filelist: Incomplete
    def run(self) -> None: ...
    def initialize_options(self) -> None: ...
    def make_distribution(self) -> None:
        """
        Workaround for #516
        """
    def add_defaults(self) -> None: ...
    def check_readme(self) -> None: ...
    def make_release_tree(self, base_dir, files) -> None: ...
    def read_manifest(self) -> None:
        """Read the manifest file (named by 'self.manifest') and use it to
        fill in 'self.filelist', the list of files to include in the source
        distribution.
        """
