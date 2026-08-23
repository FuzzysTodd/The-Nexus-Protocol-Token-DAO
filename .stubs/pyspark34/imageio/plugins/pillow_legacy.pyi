from ..core import Format as Format, image_as_uint as image_as_uint
from ..core.request import URI_BYTES as URI_BYTES, URI_FILE as URI_FILE
from .pillowmulti import GIFFormat as GIFFormat, TIFFFormat as TIFFFormat
from _typeshed import Incomplete

logger: Incomplete
GENERIC_DOCS: str

class PillowFormat(Format):
    """
    Base format class for Pillow formats.
    """
    def __init__(self, *args, plugin_id: str = None, **kwargs) -> None: ...
    @property
    def plugin_id(self):
        """The PIL plugin id."""
    class Reader(Format.Reader): ...
    class Writer(Format.Writer):
        def set_meta_data(self, meta) -> None: ...

class PNGFormat(PillowFormat):
    """See :mod:`imageio.plugins.pillow_legacy`"""
    class Reader(PillowFormat.Reader): ...
    class Writer(PillowFormat.Writer): ...

class JPEGFormat(PillowFormat):
    """See :mod:`imageio.plugins.pillow_legacy`"""
    class Reader(PillowFormat.Reader): ...
    class Writer(PillowFormat.Writer): ...

class JPEG2000Format(PillowFormat):
    """See :mod:`imageio.plugins.pillow_legacy`"""
    class Reader(PillowFormat.Reader): ...
    class Writer(PillowFormat.Writer): ...

def save_pillow_close(im) -> None: ...
def pil_try_read(im) -> None: ...
def pil_get_frame(im, is_gray: Incomplete | None = None, as_gray: Incomplete | None = None, mode: Incomplete | None = None, dtype: Incomplete | None = None):
    """
    is_gray: Whether the image *is* gray (by inspecting its palette).
    as_gray: Whether the resulting image must be converted to gaey.
    mode: The mode to convert to.
    """
def ndarray_to_pil(arr, format_str: Incomplete | None = None, prefer_uint8: bool = True): ...
