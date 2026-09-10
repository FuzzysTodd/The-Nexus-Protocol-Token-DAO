__all__ = ['accept_key', 'apply_mask']

def accept_key(key: str) -> str:
    """
    Compute the value of the Sec-WebSocket-Accept header.

    Args:
        key: value of the Sec-WebSocket-Key header.

    """
def apply_mask(data: bytes, mask: bytes) -> bytes:
    """
    Apply masking to the data of a WebSocket message.

    Args:
        data: data to mask.
        mask: 4-bytes mask.

    """
