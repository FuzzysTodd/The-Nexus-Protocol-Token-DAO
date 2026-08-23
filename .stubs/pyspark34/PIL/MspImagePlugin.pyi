from . import Image as Image, ImageFile as ImageFile

class MspImageFile(ImageFile.ImageFile):
    format: str
    format_description: str

class MspDecoder(ImageFile.PyDecoder):
    def decode(self, buffer): ...
