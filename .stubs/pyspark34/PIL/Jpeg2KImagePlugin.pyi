from . import Image as Image, ImageFile as ImageFile
from _typeshed import Incomplete

class BoxReader:
    """
    A small helper class to read fields stored in JPEG2000 header boxes
    and to easily step into and read sub-boxes.
    """
    fp: Incomplete
    has_length: Incomplete
    length: Incomplete
    remaining_in_box: int
    def __init__(self, fp, length: int = -1) -> None: ...
    def read_fields(self, field_format): ...
    def read_boxes(self): ...
    def has_next_box(self): ...
    def next_box_type(self): ...

class Jpeg2KImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    @property
    def reduce(self): ...
    @reduce.setter
    def reduce(self, value) -> None: ...
    tile: Incomplete
    def load(self): ...
