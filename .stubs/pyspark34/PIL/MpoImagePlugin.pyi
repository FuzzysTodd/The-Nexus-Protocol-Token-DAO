from . import ExifTags as ExifTags, Image as Image, ImageFile as ImageFile, ImageSequence as ImageSequence, JpegImagePlugin as JpegImagePlugin, TiffImagePlugin as TiffImagePlugin
from ._binary import o32le as o32le
from _typeshed import Incomplete

class MpoImageFile(JpegImagePlugin.JpegImageFile):
    format: str
    format_description: str
    def load_seek(self, pos) -> None: ...
    fp: Incomplete
    offset: Incomplete
    tile: Incomplete
    def seek(self, frame) -> None: ...
    def tell(self): ...
    @staticmethod
    def adopt(jpeg_instance, mpheader: Incomplete | None = None):
        """
        Transform the instance of JpegImageFile into
        an instance of MpoImageFile.
        After the call, the JpegImageFile is extended
        to be an MpoImageFile.

        This is essentially useful when opening a JPEG
        file that reveals itself as an MPO, to avoid
        double call to _open.
        """
