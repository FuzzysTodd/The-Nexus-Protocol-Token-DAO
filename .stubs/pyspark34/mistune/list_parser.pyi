import re
from .core import BlockState as BlockState
from .util import expand_leading_tab as expand_leading_tab, expand_tab as expand_tab, strip_end as strip_end

LIST_PATTERN: str

def parse_list(block, m: re.Match, state: BlockState) -> int:
    """Parse tokens for ordered and unordered list."""
