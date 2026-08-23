from . import Image as Image, ImageFile as ImageFile
from .JpegPresets import presets as presets
from ._binary import o8 as o8
from _typeshed import Incomplete

def Skip(self, marker) -> None: ...
def APP(self, marker) -> None: ...
def COM(self, marker) -> None: ...
def SOF(self, marker) -> None: ...
def DQT(self, marker) -> None: ...

MARKER: Incomplete

class JpegImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    def load_read(self, read_bytes):
        """
        internal: read more image data
        For premature EOF and LOAD_TRUNCATED_IMAGES adds EOI marker
        so libjpeg can finish decoding
        """
    mode: Incomplete
    tile: Incomplete
    decoderconfig: Incomplete
    def draft(self, mode, size): ...
    im: Incomplete
    def load_djpeg(self) -> None: ...
    def getxmp(self):
        """
        Returns a dictionary containing the XMP tags.
        Requires defusedxml to be installed.

        :returns: XMP tags in a dictionary.
        """

RAWMODE: Incomplete
zigzag_index: Incomplete
samplings: Incomplete

def get_sampling(im): ...
def jpeg_factory(fp: Incomplete | None = None, filename: Incomplete | None = None): ...
