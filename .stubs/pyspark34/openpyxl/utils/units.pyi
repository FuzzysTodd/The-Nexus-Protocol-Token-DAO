from _typeshed import Incomplete

DEFAULT_ROW_HEIGHT: float
BASE_COL_WIDTH: int
DEFAULT_COLUMN_WIDTH: Incomplete
DEFAULT_LEFT_MARGIN: float
DEFAULT_TOP_MARGIN: float
DEFAULT_HEADER: float

def inch_to_dxa(value):
    """1 inch = 72 * 20 dxa"""
def dxa_to_inch(value): ...
def dxa_to_cm(value): ...
def cm_to_dxa(value): ...
def pixels_to_EMU(value):
    """1 pixel = 9525 EMUs"""
def EMU_to_pixels(value): ...
def cm_to_EMU(value):
    """1 cm = 360000 EMUs"""
def EMU_to_cm(value): ...
def inch_to_EMU(value):
    """1 inch = 914400 EMUs"""
def EMU_to_inch(value): ...
def pixels_to_points(value, dpi: int = 96):
    """96 dpi, 72i"""
def points_to_pixels(value, dpi: int = 96): ...
def degrees_to_angle(value):
    """1 degree = 60000 angles"""
def angle_to_degrees(value): ...
def short_color(color):
    """ format a color to its short size """
