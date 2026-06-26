from .._utils import compute_md5 as compute_md5, job as job, run_command_with_process as run_command_with_process
from _typeshed import Incomplete

logger: Incomplete

class BuildProcess:
    logger: Incomplete
    main: Incomplete
    build_folder: Incomplete
    deps_info: Incomplete
    npm_modules: Incomplete
    package_lock: Incomplete
    package: Incomplete
    asset_paths: Incomplete
    def __init__(self, main, deps_info) -> None: ...
    def clean(self) -> None: ...
    def npm(self) -> None:
        """Job to install npm packages."""
    def watch(self) -> None: ...
    def build(self, build: Incomplete | None = None) -> None: ...
    def digest(self) -> None: ...
    def bundles(self, build: Incomplete | None = None) -> None: ...

class Renderer(BuildProcess):
    def __init__(self) -> None:
        """dash-renderer's path is binding with the dash folder hierarchy."""

def renderer() -> None: ...
