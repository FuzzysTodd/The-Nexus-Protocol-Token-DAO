from ..common.utils import isStrSpace as isStrSpace, normalizeReference as normalizeReference
from ..token import Token as Token
from .state_inline import StateInline as StateInline

def image(state: StateInline, silent: bool) -> bool: ...
