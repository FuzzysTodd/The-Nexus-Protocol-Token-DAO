from .scoped_name import ScopedName as ScopedName
from .specification import ArgumentType as ArgumentType, IfaceFileType as IfaceFileType
from .utils import append_iface_file as append_iface_file, argument_as_str as argument_as_str, same_base_type as same_base_type
from _typeshed import Incomplete

def encoded_template_name(template):
    """ Return the encoded name of a template. """
def same_template_signature(sig1, sig2, deep: bool = False):
    """ Return True if the template signatures are the same.  A deep comparison
    is used for mapped type templates where we want to recurse into any nested
    templates.
    """
def template_code(spec, used, proto_code, expansions):
    """ Return a copy of an optional CodeBlock object with sub-strings replaced
    by corresponding values.
    """
def template_code_blocks(spec, used, proto_code_blocks, expansions):
    """ Return a copy of a list of CodeBlock objects with sub-strings replaced
    by corresponding values.
    """
def template_expansions(template_names, instantiation_values, declared_names: Incomplete | None = None):
    """ Return a dict of expansions to be applied when instantiating mapped
    type of class templates (including handwritten code).  The key is the
    symbolic name of a template argument and the value is the replacement to be
    used in a particular instantiation.
    """
def template_string(proto_str, expansions, scope_replacement: Incomplete | None = None):
    """ Return a copy of a string with sub-strings replaced by corresponding
    values.
    """
