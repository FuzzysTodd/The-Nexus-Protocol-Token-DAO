from _typeshed import Incomplete
from pip._internal.build_env import BuildEnvironment as BuildEnvironment
from pip._internal.utils.logging import indent_log as indent_log
from pip._internal.utils.setuptools_build import make_setuptools_develop_args as make_setuptools_develop_args
from pip._internal.utils.subprocess import call_subprocess as call_subprocess
from typing import Sequence

logger: Incomplete

def install_editable(*, global_options: Sequence[str], prefix: str | None, home: str | None, use_user_site: bool, name: str, setup_py_path: str, isolated: bool, build_env: BuildEnvironment, unpacked_source_directory: str) -> None:
    """Install a package in editable mode. Most arguments are pass-through
    to setuptools.
    """
