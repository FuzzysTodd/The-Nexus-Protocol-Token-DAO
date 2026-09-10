from _typeshed import Incomplete
from defusedxml.ElementTree import iterparse as iterparse
from et_xmlfile import xmlfile as xmlfile
from openpyxl import DEFUSEDXML as DEFUSEDXML, LXML as LXML
from openpyxl.xml.constants import CHART_DRAWING_NS as CHART_DRAWING_NS, CHART_NS as CHART_NS, COREPROPS_NS as COREPROPS_NS, CUSTPROPS_NS as CUSTPROPS_NS, DCTERMS_NS as DCTERMS_NS, DCTERMS_PREFIX as DCTERMS_PREFIX, DRAWING_NS as DRAWING_NS, REL_NS as REL_NS, SHEET_DRAWING_NS as SHEET_DRAWING_NS, SHEET_MAIN_NS as SHEET_MAIN_NS, VTYPES_NS as VTYPES_NS, XML_NS as XML_NS

safe_parser: Incomplete
NS_REGEX: Incomplete

def localname(node): ...
def whitespace(node) -> None: ...
