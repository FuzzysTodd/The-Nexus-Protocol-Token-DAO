from . import Image as Image, ImageFile as ImageFile
from ._binary import i8 as i8
from _typeshed import Incomplete

class BitStream:
    fp: Incomplete
    bits: int
    bitbuffer: int
    def __init__(self, fp) -> None: ...
    def next(self): ...
    def peek(self, bits): ...
    def skip(self, bits) -> None: ...
    def read(self, bits): ...

class MpegImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
