import re
from ..common.html_blocks import block_names as block_names
from ..common.html_re import HTML_OPEN_CLOSE_TAG_STR as HTML_OPEN_CLOSE_TAG_STR
from .state_block import StateBlock as StateBlock
from _typeshed import Incomplete

LOGGER: Incomplete
HTML_SEQUENCES: list[tuple[re.Pattern[str], re.Pattern[str], bool]]

def html_block(state: StateBlock, startLine: int, endLine: int, silent: bool) -> bool: ...
