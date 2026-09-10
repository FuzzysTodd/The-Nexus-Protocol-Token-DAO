from _typeshed import Incomplete
from email.message import Message
from typing import Any, Dict

METADATA_FIELDS: Incomplete

def json_name(field: str) -> str: ...
def msg_to_json(msg: Message) -> Dict[str, Any]:
    """Convert a Message object into a JSON-compatible dictionary."""
