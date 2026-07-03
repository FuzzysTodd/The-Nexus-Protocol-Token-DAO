from . import Image as Image, ImageFile as ImageFile

class McIdasImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
