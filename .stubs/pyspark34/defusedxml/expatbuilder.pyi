from .common import DTDForbidden as DTDForbidden, EntitiesForbidden as EntitiesForbidden, ExternalReferenceForbidden as ExternalReferenceForbidden
from _typeshed import Incomplete
from xml.dom.expatbuilder import ExpatBuilder as _ExpatBuilder, Namespaces as _Namespaces

__origin__: str

class DefusedExpatBuilder(_ExpatBuilder):
    """Defused document builder"""
    forbid_dtd: Incomplete
    forbid_entities: Incomplete
    forbid_external: Incomplete
    def __init__(self, options: Incomplete | None = None, forbid_dtd: bool = False, forbid_entities: bool = True, forbid_external: bool = True) -> None: ...
    def defused_start_doctype_decl(self, name, sysid, pubid, has_internal_subset) -> None: ...
    def defused_entity_decl(self, name, is_parameter_entity, value, base, sysid, pubid, notation_name) -> None: ...
    def defused_unparsed_entity_decl(self, name, base, sysid, pubid, notation_name) -> None: ...
    def defused_external_entity_ref_handler(self, context, base, sysid, pubid) -> None: ...
    def install(self, parser) -> None: ...

class DefusedExpatBuilderNS(_Namespaces, DefusedExpatBuilder):
    """Defused document builder that supports namespaces."""
    def install(self, parser) -> None: ...
    def reset(self) -> None: ...

def parse(file, namespaces: bool = True, forbid_dtd: bool = False, forbid_entities: bool = True, forbid_external: bool = True):
    """Parse a document, returning the resulting Document node.

    'file' may be either a file name or an open file object.
    """
def parseString(string, namespaces: bool = True, forbid_dtd: bool = False, forbid_entities: bool = True, forbid_external: bool = True):
    """Parse a document from a string, returning the resulting
    Document node.
    """
