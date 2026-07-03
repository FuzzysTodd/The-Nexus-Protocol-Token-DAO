from _typeshed import Incomplete
from openpyxl.utils import coordinate_to_tuple as coordinate_to_tuple
from openpyxl.xml.functions import Element as Element, SubElement as SubElement, tostring as tostring

vmlns: str
officens: str
excelns: str

class ShapeWriter:
    """
    Create VML for comments
    """
    vml: Incomplete
    vml_path: Incomplete
    comments: Incomplete
    def __init__(self, comments) -> None: ...
    def add_comment_shapetype(self, root) -> None: ...
    def add_comment_shape(self, root, idx, coord, height, width) -> None: ...
    def write(self, root): ...
