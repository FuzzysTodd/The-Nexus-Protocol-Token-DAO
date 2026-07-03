from . import Image as Image, ImageFile as ImageFile
from ._binary import o8 as o8

class QoiImageFile(ImageFile.ImageFile):
    format: str
    format_description: str

class QoiDecoder(ImageFile.PyDecoder):
    def decode(self, buffer): ...
