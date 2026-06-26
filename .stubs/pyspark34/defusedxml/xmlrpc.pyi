from .common import DTDForbidden as DTDForbidden, EntitiesForbidden as EntitiesForbidden, ExternalReferenceForbidden as ExternalReferenceForbidden, PY3 as PY3
from _typeshed import Incomplete
from xmlrpc.client import ExpatParser

__origin__: str
MAX_DATA: Incomplete

def defused_gzip_decode(data, limit: Incomplete | None = None):
    """gzip encoded data -> unencoded data

    Decode data using the gzip content encoding as described in RFC 1952
    """

class DefusedGzipDecodedResponse:
    """a file-like object to decode a response encoded with the gzip
    method, as described in RFC 1952.
    """
    limit: Incomplete
    readlength: Incomplete
    stringio: Incomplete
    def __init__(self, response, limit: Incomplete | None = None) -> None: ...
    def read(self, n): ...
    def close(self) -> None: ...

class DefusedExpatParser(ExpatParser):
    forbid_dtd: Incomplete
    forbid_entities: Incomplete
    forbid_external: Incomplete
    def __init__(self, target, forbid_dtd: bool = False, forbid_entities: bool = True, forbid_external: bool = True) -> None: ...
    def defused_start_doctype_decl(self, name, sysid, pubid, has_internal_subset) -> None: ...
    def defused_entity_decl(self, name, is_parameter_entity, value, base, sysid, pubid, notation_name) -> None: ...
    def defused_unparsed_entity_decl(self, name, base, sysid, pubid, notation_name) -> None: ...
    def defused_external_entity_ref_handler(self, context, base, sysid, pubid) -> None: ...

def monkey_patch() -> None: ...
def unmonkey_patch() -> None: ...
