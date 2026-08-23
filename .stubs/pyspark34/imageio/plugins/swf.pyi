from ..core import Format as Format, image_as_uint as image_as_uint, read_n_bytes as read_n_bytes
from _typeshed import Incomplete

logger: Incomplete

def load_lib(): ...

class SWFFormat(Format):
    """See :mod:`imageio.plugins.swf`"""
    class Reader(Format.Reader): ...
    class Writer(Format.Writer):
        def set_meta_data(self, meta) -> None: ...

HTML: str
