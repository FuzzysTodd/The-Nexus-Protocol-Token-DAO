from _typeshed import Incomplete
from openpyxl.utils.units import pixels_to_EMU as pixels_to_EMU

class Drawing:
    """ a drawing object - eg container for shapes or charts
        we assume user specifies dimensions in pixels; units are
        converted to EMU in the drawing part
    """
    count: int
    name: str
    description: str
    coordinates: Incomplete
    left: int
    top: int
    resize_proportional: bool
    rotation: int
    anchortype: str
    anchorcol: int
    anchorrow: int
    def __init__(self) -> None: ...
    @property
    def width(self): ...
    @width.setter
    def width(self, w) -> None: ...
    @property
    def height(self): ...
    @height.setter
    def height(self, h) -> None: ...
    def set_dimension(self, w: int = 0, h: int = 0) -> None: ...
    @property
    def anchor(self): ...
