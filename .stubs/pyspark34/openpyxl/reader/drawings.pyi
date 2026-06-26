from openpyxl.chart.chartspace import ChartSpace as ChartSpace
from openpyxl.chart.reader import read_chart as read_chart
from openpyxl.drawing.image import Image as Image, PILImage as PILImage
from openpyxl.drawing.spreadsheet_drawing import SpreadsheetDrawing as SpreadsheetDrawing
from openpyxl.packaging.relationship import get_dependents as get_dependents, get_rel as get_rel, get_rels_path as get_rels_path
from openpyxl.xml.constants import IMAGE_NS as IMAGE_NS
from openpyxl.xml.functions import fromstring as fromstring

def find_images(archive, path):
    """
    Given the path to a drawing file extract charts and images

    Ignore errors due to unsupported parts of DrawingML
    """
