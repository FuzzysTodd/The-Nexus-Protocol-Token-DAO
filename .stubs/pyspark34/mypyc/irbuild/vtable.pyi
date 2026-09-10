from mypyc.ir.class_ir import ClassIR as ClassIR, VTableEntries as VTableEntries, VTableMethod as VTableMethod
from mypyc.sametype import is_same_method_signature as is_same_method_signature

def compute_vtable(cls) -> None:
    """Compute the vtable structure for a class."""
def specialize_parent_vtable(cls, parent: ClassIR) -> VTableEntries:
    """Generate the part of a vtable corresponding to a parent class or trait"""
