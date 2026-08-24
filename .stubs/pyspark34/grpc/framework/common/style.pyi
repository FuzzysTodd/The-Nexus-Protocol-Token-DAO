import enum

class Service(enum.Enum):
    """Describes the control flow style of RPC method implementation."""
    INLINE: str
    EVENT: str
