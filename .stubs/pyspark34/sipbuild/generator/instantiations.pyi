from .scoped_name import ScopedName as ScopedName
from .specification import Argument as Argument, ArgumentType as ArgumentType, FunctionCall as FunctionCall, IfaceFileType as IfaceFileType, KwArgs as KwArgs, Signature as Signature, TypeHints as TypeHints, Value as Value, ValueType as ValueType
from .templates import template_code as template_code, template_code_blocks as template_code_blocks, template_expansions as template_expansions, template_string as template_string
from .utils import append_iface_file as append_iface_file, cached_name as cached_name, normalised_scoped_name as normalised_scoped_name

def instantiate_class(p, symbol, fq_cpp_name, tmpl_names, proto_class, template, py_name, no_type_name, docstring, pm) -> None:
    """ Instantiate a class template. """
def instantiate_type_hints(spec, proto_type_hints, expansions):
    """ Return an instantiated TypeHints object. """
