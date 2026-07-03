from ..common.utils import isStrSpace as isStrSpace
from .state_inline import StateInline as StateInline

def escape(state: StateInline, silent: bool) -> bool:
    """Process escaped chars and hardbreaks."""
