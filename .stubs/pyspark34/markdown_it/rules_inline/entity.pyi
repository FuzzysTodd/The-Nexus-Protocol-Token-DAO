from ..common.entities import entities as entities
from ..common.utils import fromCodePoint as fromCodePoint, isValidEntityCode as isValidEntityCode
from .state_inline import StateInline as StateInline
from _typeshed import Incomplete

DIGITAL_RE: Incomplete
NAMED_RE: Incomplete

def entity(state: StateInline, silent: bool) -> bool: ...
