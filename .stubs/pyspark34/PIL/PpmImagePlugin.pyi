from . import Image as Image, ImageFile as ImageFile
from ._binary import o8 as o8
from _typeshed import Incomplete

b_whitespace: bytes
MODES: Incomplete

class PpmImageFile(ImageFile.ImageFile):
    format: str
    format_description: str

class PpmPlainDecoder(ImageFile.PyDecoder):
    def decode(self, buffer): ...

class PpmDecoder(ImageFile.PyDecoder):
    def decode(self, buffer): ...
