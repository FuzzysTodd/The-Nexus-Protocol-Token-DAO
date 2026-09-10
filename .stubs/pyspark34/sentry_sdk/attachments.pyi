from _typeshed import Incomplete
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.envelope import Item as Item, PayloadRef as PayloadRef
from typing import Callable

class Attachment:
    bytes: Incomplete
    filename: Incomplete
    path: Incomplete
    content_type: Incomplete
    add_to_transactions: Incomplete
    def __init__(self, bytes: None | bytes | Callable[[], bytes] = None, filename: str | None = None, path: str | None = None, content_type: str | None = None, add_to_transactions: bool = False) -> None: ...
    def to_envelope_item(self) -> Item:
        """Returns an envelope item for this attachment."""
