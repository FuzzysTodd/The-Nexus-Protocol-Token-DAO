from ..keys import Keys
from _typeshed import Incomplete

__all__ = ['ANSI_SEQUENCES', 'REVERSE_ANSI_SEQUENCES']

ANSI_SEQUENCES: dict[str, Keys | tuple[Keys, ...]]
REVERSE_ANSI_SEQUENCES: Incomplete
