from ..core import BaseProgressIndicator as BaseProgressIndicator, Format as Format, StdoutProgressIndicator as StdoutProgressIndicator, read_n_bytes as read_n_bytes
from _typeshed import Incomplete

logger: Incomplete

def load_lib(): ...

sys_is_little_endian: Incomplete

def get_dcmdjpeg_exe(): ...
def get_gdcmconv_exe(): ...

class DicomFormat(Format):
    """See :mod:`imageio.plugins.dicom`"""
    class Reader(Format.Reader):
        @property
        def series(self): ...
