from ..python_slots import is_number_slot as is_number_slot, reflected_slot as reflected_slot
from ..scoped_name import STRIP_GLOBAL as STRIP_GLOBAL, ScopedName as ScopedName
from ..specification import AccessSpecifier as AccessSpecifier, ArgumentType as ArgumentType, ArrayArgument as ArrayArgument, IfaceFileType as IfaceFileType, KwArgs as KwArgs, PyQtMethodSpecifier as PyQtMethodSpecifier, PySlot as PySlot, Transfer as Transfer
from .formatters import ArgumentFormatter as ArgumentFormatter, ClassFormatter as ClassFormatter, EnumFormatter as EnumFormatter, SignatureFormatter as SignatureFormatter, ValueListFormatter as ValueListFormatter, VariableFormatter as VariableFormatter, format_scoped_py_name as format_scoped_py_name

def output_xml(spec, module_name):
    """ Return the root Module element of the XML for a module. """
