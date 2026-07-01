from . import Image as Image, ImageFile as ImageFile

class PixarImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
