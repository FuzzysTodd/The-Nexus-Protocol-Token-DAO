from ..core import Format as Format, has_module as has_module
from _typeshed import Incomplete

def load_lib(): ...

GDAL_FORMATS: Incomplete

class GdalFormat(Format):
    """See :mod:`imageio.plugins.gdal`"""
    class Reader(Format.Reader): ...
