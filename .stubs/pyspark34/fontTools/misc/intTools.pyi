from _typeshed import Incomplete

__all__ = ['popCount', 'bit_count', 'bit_indices']

bit_count: Incomplete
popCount = bit_count

def bit_indices(v):
    """Return list of indices where bits are set, 0 being the index of the least significant bit.

    >>> bit_indices(0b101)
    [0, 2]
    """
