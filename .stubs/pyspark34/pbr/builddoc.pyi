from _typeshed import Incomplete
from pbr import git as git, options as options, version as version
from sphinx import setup_command

apidoc_use_padding: bool

class LocalBuildDoc(setup_command.BuildDoc):
    builders: Incomplete
    command_name: str
    sphinx_initialized: bool
    def generate_autoindex(self, excluded_modules: Incomplete | None = None): ...
    builder: Incomplete
    def run(self): ...
    autodoc_tree_excludes: Incomplete
    def initialize_options(self) -> None: ...
    project: Incomplete
    version: Incomplete
    release: Incomplete
    warning_is_error: bool
    def finalize_options(self) -> None: ...
