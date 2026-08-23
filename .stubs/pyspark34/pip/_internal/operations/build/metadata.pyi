from pip._internal.build_env import BuildEnvironment as BuildEnvironment
from pip._internal.exceptions import InstallationSubprocessError as InstallationSubprocessError, MetadataGenerationFailed as MetadataGenerationFailed
from pip._internal.utils.subprocess import runner_with_spinner_message as runner_with_spinner_message
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory
from pip._vendor.pyproject_hooks import BuildBackendHookCaller as BuildBackendHookCaller

def generate_metadata(build_env: BuildEnvironment, backend: BuildBackendHookCaller, details: str) -> str:
    """Generate metadata using mechanisms described in PEP 517.

    Returns the generated metadata directory.
    """
