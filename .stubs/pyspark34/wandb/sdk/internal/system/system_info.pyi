from .assets.interfaces import Interface as Interface
from _typeshed import Incomplete
from typing import Any, Dict
from wandb.sdk.internal.settings_static import SettingsStatic as SettingsStatic
from wandb.sdk.lib import filesystem as filesystem
from wandb.sdk.lib.filenames import CONDA_ENVIRONMENTS_FNAME as CONDA_ENVIRONMENTS_FNAME, DIFF_FNAME as DIFF_FNAME, METADATA_FNAME as METADATA_FNAME, REQUIREMENTS_FNAME as REQUIREMENTS_FNAME
from wandb.sdk.lib.gitlib import GitRepo as GitRepo

logger: Incomplete

class SystemInfo:
    settings: Incomplete
    metadata_file_name: Incomplete
    backend_interface: Incomplete
    git: Incomplete
    saved_program: Incomplete
    saved_patches: Incomplete
    def __init__(self, settings: SettingsStatic, interface: Interface) -> None: ...
    def probe(self) -> Dict[str, Any]:
        """Probe the system for information about the current environment."""
    def publish(self, system_info: dict) -> None: ...
