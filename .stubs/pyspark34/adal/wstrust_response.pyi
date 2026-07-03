from . import log as log, xmlutil as xmlutil
from .adal_error import AdalError as AdalError
from .constants import WSTrustVersion as WSTrustVersion
from _typeshed import Incomplete

def scrub_rstr_log_message(response_str): ...
def findall_content(xml_string, tag):
    '''
    Given a tag name without any prefix,
    this function returns a list of the raw content inside this tag as-is.

    >>> findall_content("<ns0:foo> what <bar> ever </bar> content </ns0:foo>", "foo")
    [" what <bar> ever </bar> content "]

    Motivation:

    Usually we would use XML parser to extract the data by xpath.
    However the ElementTree in Python will implicitly normalize the output
    by "hoisting" the inner inline namespaces into the outmost element.
    The result will be a semantically equivalent XML snippet,
    but not fully identical to the original one.
    While this effect shouldn\'t become a problem in all other cases,
    it does not seem to fully comply with Exclusive XML Canonicalization spec
    (https://www.w3.org/TR/xml-exc-c14n/), and void the SAML token signature.
    SAML signature algo needs the "XML -> C14N(XML) -> Signed(C14N(Xml))" order.

    The binary extention lxml is probably the canonical way to solve this
    (https://stackoverflow.com/questions/22959577/python-exclusive-xml-canonicalization-xml-exc-c14n)
    but here we use this workaround, based on Regex, to return raw content as-is.
    '''

class WSTrustResponse:
    error_code: Incomplete
    fault_message: Incomplete
    token_type: Incomplete
    token: Incomplete
    def __init__(self, call_context, response, wstrust_version) -> None: ...
    def parse(self) -> None: ...
