__all__ = ['get_filetype_from_buffer']

def get_filetype_from_buffer(buf, max_lines: int = 5):
    """
    Scan the buffer for modelines and return filetype if one is found.
    """
