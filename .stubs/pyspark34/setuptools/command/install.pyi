import distutils.command.install as orig
from ..warnings import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning, SetuptoolsWarning as SetuptoolsWarning
from _typeshed import Incomplete

class install(orig.install):
    """Use easy_install to install the package, w/dependencies"""
    user_options: Incomplete
    boolean_options: Incomplete
    new_commands: Incomplete
    old_and_unmanageable: Incomplete
    single_version_externally_managed: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    path_file: Incomplete
    extra_dirs: str
    def handle_extra_path(self): ...
    def run(self): ...
    def do_egg_install(self) -> None: ...
