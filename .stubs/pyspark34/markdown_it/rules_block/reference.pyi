from ..common.utils import charCodeAt as charCodeAt, isSpace as isSpace, normalizeReference as normalizeReference
from .state_block import StateBlock as StateBlock
from _typeshed import Incomplete

LOGGER: Incomplete

def reference(state: StateBlock, startLine: int, _endLine: int, silent: bool) -> bool: ...
