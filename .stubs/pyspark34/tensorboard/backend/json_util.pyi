def Cleanse(obj, encoding: str = 'utf-8'):
    """Makes Python object appropriate for JSON serialization.

    - Replaces instances of Infinity/-Infinity/NaN with strings.
    - Turns byte strings into unicode strings.
    - Turns sets into sorted lists.
    - Turns tuples into lists.

    Args:
      obj: Python data structure.
      encoding: Charset used to decode byte strings.

    Returns:
      Unicode JSON data structure.
    """
