from .specification import PySlot as PySlot
from _typeshed import Incomplete

slot_type_name_map: Incomplete
slot_name_detail_map: Incomplete

def invalid_global_slot(slot):
    """ Return True if a slot cannot be specified as a global (ie. module
    level) slot.
    """
def is_hash_return_slot(slot):
    """ Return True if a slot returns a Py_hash_t. """
def is_inplace_number_slot(slot):
    """ Return True if a slot is an inplace binary numeric slot. """
def is_int_return_slot(slot):
    """ Return True if a slot returns an int. """
def is_number_slot(slot):
    """ Return True if a slot is a binary numeric slot. """
def is_rich_compare_slot(slot):
    """ Return True if a slot is a rich comparision slot. """
def is_ssize_return_slot(slot):
    """ Return True if a slot returns a Py_ssize_t. """
def is_void_return_slot(slot):
    """ Return True if a slot returns a void. """
def is_zero_arg_slot(slot):
    """ Return True if a slot takes zero arguments. """
def reflected_slot(slot):
    """ Return the name of the reflected version of a slot or None if it
    doesn't have one.
    """
