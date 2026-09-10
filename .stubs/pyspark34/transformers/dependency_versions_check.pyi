from .dependency_versions_table import deps as deps
from .utils import is_tokenizers_available as is_tokenizers_available
from .utils.versions import require_version as require_version, require_version_core as require_version_core
from _typeshed import Incomplete

pkgs_to_check_at_runtime: Incomplete

def dep_version_check(pkg, hint: Incomplete | None = None) -> None: ...
