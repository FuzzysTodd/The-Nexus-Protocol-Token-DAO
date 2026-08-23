import enum

class Cardinality(enum.Enum):
    """Describes the streaming semantics of an RPC method."""
    UNARY_UNARY: str
    UNARY_STREAM: str
    STREAM_UNARY: str
    STREAM_STREAM: str
