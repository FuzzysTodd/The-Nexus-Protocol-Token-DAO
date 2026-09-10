from . import Image as Image, ImageFile as ImageFile
from _typeshed import Incomplete

SUPPORTED: bool

class WebPImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    def getxmp(self):
        """
        Returns a dictionary containing the XMP tags.
        Requires defusedxml to be installed.

        :returns: XMP tags in a dictionary.
        """
    def seek(self, frame) -> None: ...
    fp: Incomplete
    tile: Incomplete
    def load(self): ...
    def tell(self): ...
