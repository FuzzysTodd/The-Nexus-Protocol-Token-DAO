from IPython.core.application import BaseIPythonApplication as BaseIPythonApplication, base_flags as base_flags
from IPython.core.profiledir import ProfileDir as ProfileDir
from IPython.paths import get_ipython_dir as get_ipython_dir, get_ipython_package_dir as get_ipython_package_dir
from IPython.utils.importstring import import_item as import_item
from _typeshed import Incomplete
from traitlets.config.application import Application

create_help: str
list_help: str
profile_help: str

def list_profiles_in(path):
    """list profiles in a given root directory"""
def list_bundled_profiles():
    """list profiles that are bundled with IPython."""

class ProfileLocate(BaseIPythonApplication):
    description: str
    profile: Incomplete
    def parse_command_line(self, argv: Incomplete | None = None) -> None: ...
    def start(self) -> None: ...

class ProfileList(Application):
    name: str
    description = list_help
    examples: Incomplete
    aliases: Incomplete
    flags: Incomplete
    ipython_dir: Incomplete
    def list_profile_dirs(self) -> None: ...
    def start(self) -> None: ...

create_flags: Incomplete

class ProfileCreate(BaseIPythonApplication):
    name: str
    description = create_help
    examples: Incomplete
    auto_create: Incomplete
    parallel: Incomplete
    profile: Incomplete
    def parse_command_line(self, argv) -> None: ...
    flags: Incomplete
    classes: Incomplete
    def init_config_files(self) -> None: ...
    def stage_default_config_file(self) -> None: ...

class ProfileApp(Application):
    name: str
    description = profile_help
    examples: Incomplete
    subcommands: Incomplete
    def start(self): ...
