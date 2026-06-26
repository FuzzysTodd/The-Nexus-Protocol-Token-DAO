def escape(value):
    """
    Convert ASCII < 31 to OOXML: \\n == _x + hex(ord(\\n)) + _
    """
def unescape(value):
    """
    Convert escaped strings to ASCIII: _x000a_ == \\n
    """
