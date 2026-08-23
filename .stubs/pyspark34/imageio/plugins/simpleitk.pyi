from ..core import Format as Format, has_module as has_module
from _typeshed import Incomplete

def load_lib(): ...

ITK_FORMATS: Incomplete
ALL_FORMATS: Incomplete

class ItkFormat(Format):
    """See :mod:`imageio.plugins.simpleitk`"""
    class Reader(Format.Reader): ...
    class Writer(Format.Writer):
        def set_meta_data(self, meta) -> None: ...
