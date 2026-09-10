from torch.nn.utils.rnn import PackedSequence as PackedSequence
from torch.utils._mode_utils import no_dispatch as no_dispatch
from typing import Any

def p_assert(cond: Any, s: str, raise_assertion_error: bool = True) -> None:
    """This is used as an alternate to ``assert`` when in the backward context
    to print the error message ``s`` since otherwise, it is swallowed."""
