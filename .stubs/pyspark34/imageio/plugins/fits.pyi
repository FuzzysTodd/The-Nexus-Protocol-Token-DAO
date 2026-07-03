from ..core import Format as Format

def load_lib(): ...

class FitsFormat(Format):
    """See :mod:`imageio.plugins.fits`"""
    class Reader(Format.Reader): ...
