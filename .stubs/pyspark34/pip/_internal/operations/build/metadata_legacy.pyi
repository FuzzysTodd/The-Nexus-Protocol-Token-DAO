from _typeshed import Incomplete
from pip._internal.build_env import BuildEnvironment as BuildEnvironment
from pip._internal.cli.spinners import open_spinner as open_spinner
from pip._internal.exceptions import InstallationError as InstallationError, InstallationSubprocessError as InstallationSubprocessError, MetadataGenerationFailed as MetadataGenerationFailed
from pip._internal.utils.setuptools_build import make_setuptools_egg_info_args as make_setuptools_egg_info_args
from pip._internal.utils.subprocess import call_subprocess as call_subprocess
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory

logger: Incomplete

def generate_metadata(build_env: BuildEnvironment, setup_py_path: str, source_dir: str, isolated: bool, details: str) -> str:
    """Generate metadata using setup.py-based defacto mechanisms.

    Returns the generated metadata directory.
    """
