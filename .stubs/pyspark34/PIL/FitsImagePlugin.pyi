from . import Image as Image, ImageFile as ImageFile

class FitsImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
