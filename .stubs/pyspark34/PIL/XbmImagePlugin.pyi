from . import Image as Image, ImageFile as ImageFile
from _typeshed import Incomplete

xbm_head: Incomplete

class XbmImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
