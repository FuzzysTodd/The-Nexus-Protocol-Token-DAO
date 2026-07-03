def calc_chunk_sizes(chunk_size: int | tuple[int, int] | None, chunk_count: int | tuple[int, int] | None, total_chunk_count: int | None, ny: int, nx: int) -> tuple[int, int]:
    """Calculate chunk sizes.

    Args:
        chunk_size (int or tuple(int, int), optional): Chunk size in (y, x) directions, or the same
            size in both directions if only one is specified. Cannot be negative.
        chunk_count (int or tuple(int, int), optional): Chunk count in (y, x) directions, or the
            same count in both directions if only one is specified. If less than 1, set to 1.
        total_chunk_count (int, optional): Total number of chunks. If less than 1, set to 1.
        ny (int): Number of grid points in y-direction.
        nx (int): Number of grid points in x-direction.

    Return:
        tuple(int, int): Chunk sizes (y_chunk_size, x_chunk_size).

    Note:
        Zero or one of ``chunk_size``, ``chunk_count`` and ``total_chunk_count`` should be
        specified.
    """
def two_factors(n: int) -> tuple[int, int]:
    """Split an integer into two integer factors.

    The two factors will be as close as possible to the sqrt of n, and are returned in decreasing
    order.  Worst case returns (n, 1).

    Args:
        n (int): The integer to factorize, must be positive.

    Return:
        tuple(int, int): The two factors of n, in decreasing order.
    """
