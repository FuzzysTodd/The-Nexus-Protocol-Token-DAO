from . import Image as Image, ImageFile as ImageFile
from enum import IntEnum

class Format(IntEnum):
    JPEG: int

class Encoding(IntEnum):
    UNCOMPRESSED: int
    DXT: int
    UNCOMPRESSED_RAW_BGRA: int

class AlphaEncoding(IntEnum):
    DXT1: int
    DXT3: int
    DXT5: int

def unpack_565(i): ...
def decode_dxt1(data, alpha: bool = False):
    '''
    input: one "row" of data (i.e. will produce 4*width pixels)
    '''
def decode_dxt3(data):
    '''
    input: one "row" of data (i.e. will produce 4*width pixels)
    '''
def decode_dxt5(data):
    '''
    input: one "row" of data (i.e. will produce 4 * width pixels)
    '''

class BLPFormatError(NotImplementedError): ...

class BlpImageFile(ImageFile.ImageFile):
    """
    Blizzard Mipmap Format
    """
    format: str
    format_description: str

class _BLPBaseDecoder(ImageFile.PyDecoder):
    def decode(self, buffer): ...

class BLP1Decoder(_BLPBaseDecoder): ...
class BLP2Decoder(_BLPBaseDecoder): ...

class BLPEncoder(ImageFile.PyEncoder):
    def encode(self, bufsize): ...
