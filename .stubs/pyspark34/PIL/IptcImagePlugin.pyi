from . import Image as Image, ImageFile as ImageFile
from ._binary import i8 as i8, o8 as o8
from _typeshed import Incomplete

COMPRESSION: Incomplete
PAD: Incomplete

def i(c): ...
def dump(c) -> None: ...

class IptcImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    def getint(self, key): ...
    def field(self): ...
    im: Incomplete
    def load(self): ...

def getiptcinfo(im):
    """
    Get IPTC information from TIFF, JPEG, or IPTC file.

    :param im: An image containing IPTC data.
    :returns: A dictionary containing IPTC information, or None if
        no IPTC information block was found.
    """
