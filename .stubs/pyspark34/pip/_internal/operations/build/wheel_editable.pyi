from _typeshed import Incomplete
from pip._internal.utils.subprocess import runner_with_spinner_message as runner_with_spinner_message
from pip._vendor.pyproject_hooks import BuildBackendHookCaller as BuildBackendHookCaller, HookMissing as HookMissing

logger: Incomplete

def build_wheel_editable(name: str, backend: BuildBackendHookCaller, metadata_directory: str, tempd: str) -> str | None:
    """Build one InstallRequirement using the PEP 660 build process.

    Returns path to wheel if successfully built. Otherwise, returns None.
    """
