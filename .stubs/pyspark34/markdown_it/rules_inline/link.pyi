from ..common.utils import isStrSpace as isStrSpace, normalizeReference as normalizeReference
from .state_inline import StateInline as StateInline

def link(state: StateInline, silent: bool) -> bool: ...
