from . import BmpImagePlugin as BmpImagePlugin, Image as Image

class CurImageFile(BmpImagePlugin.BmpImageFile):
    format: str
    format_description: str
