def pylong_join(count, digits_ptr: str = 'digits', join_type: str = 'unsigned long'):
    """
    Generate an unrolled shift-then-or loop over the first 'count' digits.
    Assumes that they fit into 'join_type'.

    (((d[2] << n) | d[1]) << n) | d[0]
    """
