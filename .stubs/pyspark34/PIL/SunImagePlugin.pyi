from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette

class SunImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
