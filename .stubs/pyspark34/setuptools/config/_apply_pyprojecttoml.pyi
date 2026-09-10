from ..warnings import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning, SetuptoolsWarning as SetuptoolsWarning
from _typeshed import Incomplete
from collections.abc import Mapping
from setuptools._importlib import metadata as metadata
from setuptools.dist import Distribution as Distribution
from typing import Dict

EMPTY: Mapping

def apply(dist: Distribution, config: dict, filename: _Path) -> Distribution:
    """Apply configuration dict read with :func:`read_configuration`"""
def json_compatible_key(key: str) -> str:
    """As defined in :pep:`566#json-compatible-metadata`"""

PYPROJECT_CORRESPONDENCE: Dict[str, _Correspondence]
TOOL_TABLE_RENAMES: Incomplete
TOOL_TABLE_DEPRECATIONS: Incomplete
SETUPTOOLS_PATCHES: Incomplete

class _WouldIgnoreField(SetuptoolsDeprecationWarning): ...
