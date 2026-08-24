from _typeshed import Incomplete
from openpyxl import LXML as LXML
from openpyxl.cell.rich_text import TextBlock as TextBlock
from openpyxl.compat import safe_string as safe_string
from openpyxl.utils.datetime import to_ISO8601 as to_ISO8601, to_excel as to_excel
from openpyxl.worksheet.formula import ArrayFormula as ArrayFormula, DataTableFormula as DataTableFormula
from openpyxl.xml.functions import Element as Element, REL_NS as REL_NS, SubElement as SubElement, XML_NS as XML_NS, whitespace as whitespace

def etree_write_cell(xf, worksheet, cell, styled: Incomplete | None = None) -> None: ...
def lxml_write_cell(xf, worksheet, cell, styled: bool = False) -> None: ...
write_cell = lxml_write_cell
write_cell = etree_write_cell
