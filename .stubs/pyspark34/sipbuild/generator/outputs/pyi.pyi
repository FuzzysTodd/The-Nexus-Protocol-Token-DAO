from ...version import SIP_VERSION_STR as SIP_VERSION_STR
from ..python_slots import is_number_slot as is_number_slot, reflected_slot as reflected_slot
from ..specification import AccessSpecifier as AccessSpecifier, ArgumentType as ArgumentType, ArrayArgument as ArrayArgument, EnumBaseType as EnumBaseType, IfaceFileType as IfaceFileType, PyQtMethodSpecifier as PyQtMethodSpecifier, PySlot as PySlot, Signature as Signature
from ..utils import append_iface_file as append_iface_file, find_method as find_method
from .formatters import ArgumentFormatter as ArgumentFormatter, ClassFormatter as ClassFormatter, format_copying as format_copying, format_scoped_py_name as format_scoped_py_name

def output_pyi(spec, project, pyi_filename) -> None:
    """ Output a .pyi file. """
