from _typeshed import Incomplete
from pure_eval.utils import CannotEval as CannotEval, of_type as of_type

def getattr_static(obj, attr):
    """Retrieve attributes without triggering dynamic lookup via the
       descriptor protocol,  __getattr__ or __getattribute__.

       Note: this function may not be able to retrieve all attributes
       that getattr can fetch (like dynamically created attributes)
       and may find attributes that getattr can't (like descriptors
       that raise AttributeError). It can also return descriptor objects
       instead of instance members in some cases. See the
       documentation for details.
    """

class _foo:
    method: Incomplete

slot_descriptor: Incomplete
wrapper_descriptor: Incomplete
method_descriptor: Incomplete
user_method_descriptor: Incomplete
safe_descriptors_raw: Incomplete
safe_descriptor_types: Incomplete
