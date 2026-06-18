import distutils.command.install_scripts as orig
from .._path import ensure_directory as ensure_directory
from _typeshed import Incomplete

class install_scripts(orig.install_scripts):
    """Do normal script install, plus any egg_info wrapper scripts"""
    no_ep: bool
    def initialize_options(self) -> None: ...
    outfiles: Incomplete
    def run(self) -> None: ...
    def write_script(self, script_name, contents, mode: str = 't', *ignored) -> None:
        """Write an executable file to the scripts directory"""
