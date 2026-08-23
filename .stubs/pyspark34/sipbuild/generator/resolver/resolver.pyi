from ..error_log import ErrorLog as ErrorLog
from ..instantiations import instantiate_type_hints as instantiate_type_hints
from ..python_slots import is_hash_return_slot as is_hash_return_slot, is_inplace_number_slot as is_inplace_number_slot, is_int_return_slot as is_int_return_slot, is_rich_compare_slot as is_rich_compare_slot, is_ssize_return_slot as is_ssize_return_slot, is_void_return_slot as is_void_return_slot, is_zero_arg_slot as is_zero_arg_slot
from ..scoped_name import ScopedName as ScopedName
from ..specification import AccessSpecifier as AccessSpecifier, Argument as Argument, ArgumentType as ArgumentType, ClassKey as ClassKey, Constructor as Constructor, IfaceFileType as IfaceFileType, MappedType as MappedType, Member as Member, PyQtMethodSpecifier as PyQtMethodSpecifier, PySlot as PySlot, Signature as Signature, Transfer as Transfer, ValueType as ValueType, VirtualHandler as VirtualHandler, VirtualOverload as VirtualOverload, VisibleMember as VisibleMember, WrappedClass as WrappedClass
from ..templates import encoded_template_name as encoded_template_name, same_template_signature as same_template_signature, template_code as template_code, template_code_blocks as template_code_blocks, template_expansions as template_expansions
from ..utils import append_iface_file as append_iface_file, argument_as_str as argument_as_str, cached_name as cached_name, find_iface_file as find_iface_file, find_method as find_method, same_argument_type as same_argument_type, same_base_type as same_base_type, same_signature as same_signature, search_typedefs as search_typedefs

def resolve(spec, modules):
    """ Resolve all types of a parsed specification and create additional views
    so that code can be generated.
    """
