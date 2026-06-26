from typing import List

__all__ = ['solve']

def solve(sequence: List[int], partitions: int = 1) -> List[List[int]]:
    """Splits a sequence into several partitions to minimize variance for each
    partition.

    The result might not be optimal. However, it can be done only in O(kn³),
    where k is the number of partitions and n is the length of the sequence.

    """
