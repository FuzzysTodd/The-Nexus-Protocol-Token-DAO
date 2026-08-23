from _typeshed import Incomplete
from xml.etree.ElementTree import ParseError as ParseError, tostring as tostring

__all__ = ['ParseError', 'XML', 'XMLParse', 'XMLParser', 'XMLTreeBuilder', 'fromstring', 'iterparse', 'parse', 'tostring']

class DefusedXMLParser(_XMLParser):
    forbid_dtd: Incomplete
    forbid_entities: Incomplete
    forbid_external: Incomplete
    def __init__(self, html=..., target: Incomplete | None = None, encoding: Incomplete | None = None, forbid_dtd: bool = False, forbid_entities: bool = True, forbid_external: bool = True) -> None: ...
    def defused_start_doctype_decl(self, name, sysid, pubid, has_internal_subset) -> None: ...
    def defused_entity_decl(self, name, is_parameter_entity, value, base, sysid, pubid, notation_name) -> None: ...
    def defused_unparsed_entity_decl(self, name, base, sysid, pubid, notation_name) -> None: ...
    def defused_external_entity_ref_handler(self, context, base, sysid, pubid) -> None: ...
XMLTreeBuilder = DefusedXMLParser
XMLParse = DefusedXMLParser
XMLParser = DefusedXMLParser
parse: Incomplete
iterparse: Incomplete
fromstring: Incomplete
XML = fromstring
