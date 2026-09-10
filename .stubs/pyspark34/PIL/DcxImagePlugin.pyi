from . import Image as Image
from .PcxImagePlugin import PcxImageFile as PcxImageFile
from _typeshed import Incomplete

MAGIC: int

class DcxImageFile(PcxImageFile):
    format: str
    format_description: str
    frame: Incomplete
    fp: Incomplete
    def seek(self, frame) -> None: ...
    def tell(self): ...
