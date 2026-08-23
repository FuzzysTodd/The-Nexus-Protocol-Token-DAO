from _typeshed import Incomplete
from typing import Dict, NamedTuple, Tuple

class Message(NamedTuple):
    id: str
    name: str
    message: str
    reason: str
    def to_dict(self) -> Dict[str, Tuple[str, str, str]]: ...

def to_msgs(*messages: Message) -> Dict[str, Tuple[str, str, str]]: ...

PYTEST_RAISES_WITHOUT_MATCH: Incomplete
UNITTEST_PYTEST_RAISES: Incomplete
LAZY_BUILTIN_IMPORT: Incomplete
USELESS_ASSIGNMENT: Incomplete
