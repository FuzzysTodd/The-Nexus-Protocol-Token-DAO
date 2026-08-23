def i8(c): ...
def o8(i): ...
def i16le(c, o: int = 0):
    """
    Converts a 2-bytes (16 bits) string to an unsigned integer.

    :param c: string containing bytes to convert
    :param o: offset of bytes to convert in string
    """
def si16le(c, o: int = 0):
    """
    Converts a 2-bytes (16 bits) string to a signed integer.

    :param c: string containing bytes to convert
    :param o: offset of bytes to convert in string
    """
def si16be(c, o: int = 0):
    """
    Converts a 2-bytes (16 bits) string to a signed integer, big endian.

    :param c: string containing bytes to convert
    :param o: offset of bytes to convert in string
    """
def i32le(c, o: int = 0):
    """
    Converts a 4-bytes (32 bits) string to an unsigned integer.

    :param c: string containing bytes to convert
    :param o: offset of bytes to convert in string
    """
def si32le(c, o: int = 0):
    """
    Converts a 4-bytes (32 bits) string to a signed integer.

    :param c: string containing bytes to convert
    :param o: offset of bytes to convert in string
    """
def i16be(c, o: int = 0): ...
def i32be(c, o: int = 0): ...
def o16le(i): ...
def o32le(i): ...
def o16be(i): ...
def o32be(i): ...
