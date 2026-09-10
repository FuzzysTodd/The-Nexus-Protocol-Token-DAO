from _typeshed import Incomplete
from pip._internal.models.link import Link as Link
from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory
from types import TracebackType
from typing import Generator, Type

logger: Incomplete

def update_env_context_manager(**changes: str) -> Generator[None, None, None]: ...
def get_build_tracker() -> Generator['BuildTracker', None, None]: ...

class TrackerId(str):
    """Uniquely identifying string provided to the build tracker."""

class BuildTracker:
    """Ensure that an sdist cannot request itself as a setup requirement.

    When an sdist is prepared, it identifies its setup requirements in the
    context of ``BuildTracker.track()``. If a requirement shows up recursively, this
    raises an exception.

    This stops fork bombs embedded in malicious packages."""
    def __init__(self, root: str) -> None: ...
    def __enter__(self) -> BuildTracker: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    def add(self, req: InstallRequirement, key: TrackerId) -> None:
        """Add an InstallRequirement to build tracking."""
    def remove(self, req: InstallRequirement, key: TrackerId) -> None:
        """Remove an InstallRequirement from build tracking."""
    def cleanup(self) -> None: ...
    def track(self, req: InstallRequirement, key: str) -> Generator[None, None, None]:
        """Ensure that `key` cannot install itself as a setup requirement.

        :raises LookupError: If `key` was already provided in a parent invocation of
                             the context introduced by this method."""
