from _typeshed import Incomplete
from distutils import cmd

logger: Incomplete

class TestrReal(cmd.Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    testr_args: Incomplete
    coverage: Incomplete
    omit: str
    slowest: Incomplete
    coverage_package_name: Incomplete
    no_parallel: Incomplete
    log_level: str
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None:
        """Set up testr repo, then run testr."""

class TestrFake(cmd.Command):
    description: str
    user_options: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...

have_testr: bool
Testr = TestrReal
Testr = TestrFake
