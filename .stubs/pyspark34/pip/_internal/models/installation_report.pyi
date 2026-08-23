from pip import __version__ as __version__
from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._vendor.packaging.markers import default_environment as default_environment
from typing import Any, Dict, Sequence

class InstallationReport:
    def __init__(self, install_requirements: Sequence[InstallRequirement]) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
