from _typeshed import Incomplete
from mypyc.codegen.emit import Emitter as Emitter, HeaderDeclaration as HeaderDeclaration, ReturnHandler as ReturnHandler
from mypyc.codegen.emitfunc import native_function_header as native_function_header
from mypyc.codegen.emitwrapper import generate_bin_op_wrapper as generate_bin_op_wrapper, generate_bool_wrapper as generate_bool_wrapper, generate_contains_wrapper as generate_contains_wrapper, generate_dunder_wrapper as generate_dunder_wrapper, generate_get_wrapper as generate_get_wrapper, generate_hash_wrapper as generate_hash_wrapper, generate_ipow_wrapper as generate_ipow_wrapper, generate_len_wrapper as generate_len_wrapper, generate_richcompare_wrapper as generate_richcompare_wrapper, generate_set_del_item_wrapper as generate_set_del_item_wrapper
from mypyc.common import BITMAP_BITS as BITMAP_BITS, BITMAP_TYPE as BITMAP_TYPE, NATIVE_PREFIX as NATIVE_PREFIX, PREFIX as PREFIX, REG_PREFIX as REG_PREFIX
from mypyc.ir.class_ir import ClassIR as ClassIR, VTableEntries as VTableEntries
from mypyc.ir.func_ir import FUNC_CLASSMETHOD as FUNC_CLASSMETHOD, FUNC_STATICMETHOD as FUNC_STATICMETHOD, FuncDecl as FuncDecl, FuncIR as FuncIR
from mypyc.ir.rtypes import RTuple as RTuple, RType as RType, object_rprimitive as object_rprimitive
from mypyc.namegen import NameGenerator as NameGenerator
from mypyc.sametype import is_same_type as is_same_type
from typing import Callable, Mapping, Tuple

def native_slot(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str: ...
def wrapper_slot(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str: ...
SlotGenerator = Callable[[ClassIR, FuncIR, Emitter], str]
SlotTable = Mapping[str, Tuple[str, SlotGenerator]]
SLOT_DEFS: SlotTable
AS_MAPPING_SLOT_DEFS: SlotTable
AS_SEQUENCE_SLOT_DEFS: SlotTable
AS_NUMBER_SLOT_DEFS: SlotTable
AS_ASYNC_SLOT_DEFS: SlotTable
SIDE_TABLES: Incomplete
ALWAYS_FILL: Incomplete

def generate_call_wrapper(cl: ClassIR, fn: FuncIR, emitter: Emitter) -> str: ...
def slot_key(attr: str) -> str:
    """Map dunder method name to sort key.

    Sort reverse operator methods and __delitem__ after others ('x' > '_').
    """
def generate_slots(cl: ClassIR, table: SlotTable, emitter: Emitter) -> dict[str, str]: ...
def generate_class_type_decl(cl: ClassIR, c_emitter: Emitter, external_emitter: Emitter, emitter: Emitter) -> None: ...
def generate_class(cl: ClassIR, module: str, emitter: Emitter) -> None:
    """Generate C code for a class.

    This is the main entry point to the module.
    """
def getter_name(cl: ClassIR, attribute: str, names: NameGenerator) -> str: ...
def setter_name(cl: ClassIR, attribute: str, names: NameGenerator) -> str: ...
def generate_object_struct(cl: ClassIR, emitter: Emitter) -> None: ...
def generate_vtables(base: ClassIR, vtable_setup_name: str, vtable_name: str, emitter: Emitter, shadow: bool) -> str:
    '''Emit the vtables and vtable setup functions for a class.

    This includes both the primary vtable and any trait implementation vtables.
    The trait vtables go before the main vtable, and have the following layout:
        {
            CPyType_T1,         // pointer to type object
            C_T1_trait_vtable,  // pointer to array of method pointers
            C_T1_offset_table,  // pointer to array of attribute offsets
            CPyType_T2,
            C_T2_trait_vtable,
            C_T2_offset_table,
            ...
        }
    The method implementations are calculated at the end of IR pass, attribute
    offsets are {offsetof(native__C, _x1), offsetof(native__C, _y1), ...}.

    To account for both dynamic loading and dynamic class creation,
    vtables are populated dynamically at class creation time, so we
    emit empty array definitions to store the vtables and a function to
    populate them.

    If shadow is True, generate "shadow vtables" that point to the
    shadow glue methods (which should dispatch via the Python C-API).

    Returns the expression to use to refer to the vtable, which might be
    different than the name, if there are trait vtables.
    '''
def generate_offset_table(trait_offset_table_name: str, emitter: Emitter, trait: ClassIR, cl: ClassIR) -> None:
    """Generate attribute offset row of a trait vtable."""
def generate_vtable(entries: VTableEntries, vtable_name: str, emitter: Emitter, subtables: list[tuple[ClassIR, str, str]], shadow: bool) -> None: ...
def generate_setup_for_class(cl: ClassIR, func_name: str, defaults_fn: FuncIR | None, vtable_name: str, shadow_vtable_name: str | None, emitter: Emitter) -> None:
    """Generate a native function that allocates an instance of a class."""
def generate_constructor_for_class(cl: ClassIR, fn: FuncDecl, init_fn: FuncIR | None, setup_name: str, vtable_name: str, emitter: Emitter) -> None:
    """Generate a native function that allocates and initializes an instance of a class."""
def generate_init_for_class(cl: ClassIR, init_fn: FuncIR, emitter: Emitter) -> str:
    """Generate an init function suitable for use as tp_init.

    tp_init needs to be a function that returns an int, and our
    __init__ methods return a PyObject. Translate NULL to -1,
    everything else to 0.
    """
def generate_new_for_class(cl: ClassIR, func_name: str, vtable_name: str, setup_name: str, init_fn: FuncIR | None, emitter: Emitter) -> None: ...
def generate_new_for_trait(cl: ClassIR, func_name: str, emitter: Emitter) -> None: ...
def generate_traverse_for_class(cl: ClassIR, func_name: str, emitter: Emitter) -> None:
    """Emit function that performs cycle GC traversal of an instance."""
def generate_clear_for_class(cl: ClassIR, func_name: str, emitter: Emitter) -> None: ...
def generate_dealloc_for_class(cl: ClassIR, dealloc_func_name: str, clear_func_name: str, emitter: Emitter) -> None: ...
def generate_methods_table(cl: ClassIR, name: str, emitter: Emitter) -> None: ...
def generate_side_table_for_class(cl: ClassIR, name: str, type: str, slots: dict[str, str], emitter: Emitter) -> str | None: ...
def generate_getseter_declarations(cl: ClassIR, emitter: Emitter) -> None: ...
def generate_getseters_table(cl: ClassIR, name: str, emitter: Emitter) -> None: ...
def generate_getseters(cl: ClassIR, emitter: Emitter) -> None: ...
def generate_getter(cl: ClassIR, attr: str, rtype: RType, emitter: Emitter) -> None: ...
def generate_setter(cl: ClassIR, attr: str, rtype: RType, emitter: Emitter) -> None: ...
def generate_readonly_getter(cl: ClassIR, attr: str, rtype: RType, func_ir: FuncIR, emitter: Emitter) -> None: ...
def generate_property_setter(cl: ClassIR, attr: str, arg_type: RType, func_ir: FuncIR, emitter: Emitter) -> None: ...
def has_managed_dict(cl: ClassIR, emitter: Emitter) -> bool:
    """Should the class get the Py_TPFLAGS_MANAGED_DICT flag?"""
