from typing import List, Tuple

def intranges_from_list(list_: List[int]) -> Tuple[int, ...]:
    """Represent a list of integers as a sequence of ranges:
    ((start_0, end_0), (start_1, end_1), ...), such that the original
    integers are exactly those x such that start_i <= x < end_i for some i.

    Ranges are encoded as single integers (start << 32 | end), not as tuples.
    """
def intranges_contain(int_: int, ranges: Tuple[int, ...]) -> bool:
    """Determine if `int_` falls into one of the ranges in `ranges`."""
