from ..warnings import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning
from _typeshed import Incomplete
from distutils.core import Command

class dist_info(Command):
    """
    This command is private and reserved for internal use of setuptools,
    users should rely on ``setuptools.build_meta`` APIs.
    """
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    negative_opt: Incomplete
    egg_base: Incomplete
    output_dir: Incomplete
    name: Incomplete
    dist_info_dir: Incomplete
    tag_date: Incomplete
    tag_build: Incomplete
    keep_egg_info: bool
    def initialize_options(self) -> None: ...
    egg_info: Incomplete
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
