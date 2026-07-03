from _typeshed import Incomplete
from mypyc.common import JsonDict as JsonDict, PROPSET_PREFIX as PROPSET_PREFIX
from mypyc.ir.func_ir import FuncDecl as FuncDecl, FuncIR as FuncIR, FuncSignature as FuncSignature
from mypyc.ir.ops import DeserMaps as DeserMaps, Value as Value
from mypyc.ir.rtypes import RInstance as RInstance, RType as RType, deserialize_type as deserialize_type
from mypyc.namegen import NameGenerator as NameGenerator, exported_name as exported_name
from typing import List, NamedTuple

class VTableMethod(NamedTuple):
    cls: ClassIR
    name: str
    method: FuncIR
    shadow_method: FuncIR | None
VTableEntries = List[VTableMethod]

class ClassIR:
    """Intermediate representation of a class.

    This also describes the runtime structure of native instances.
    """
    name: Incomplete
    module_name: Incomplete
    is_trait: Incomplete
    is_generated: Incomplete
    is_abstract: Incomplete
    is_ext_class: Incomplete
    is_augmented: bool
    inherits_python: bool
    has_dict: bool
    allow_interpreted_subclasses: bool
    needs_getseters: bool
    builtin_base: Incomplete
    ctor: Incomplete
    attributes: Incomplete
    deletable: Incomplete
    method_decls: Incomplete
    methods: Incomplete
    glue_methods: Incomplete
    properties: Incomplete
    property_types: Incomplete
    vtable: Incomplete
    vtable_entries: Incomplete
    trait_vtables: Incomplete
    base: Incomplete
    traits: Incomplete
    mro: Incomplete
    base_mro: Incomplete
    children: Incomplete
    attrs_with_defaults: Incomplete
    init_self_leak: bool
    bitmap_attrs: Incomplete
    def __init__(self, name: str, module_name: str, is_trait: bool = False, is_generated: bool = False, is_abstract: bool = False, is_ext_class: bool = True) -> None: ...
    @property
    def fullname(self) -> str: ...
    def real_base(self) -> ClassIR | None:
        """Return the actual concrete base class, if there is one."""
    def vtable_entry(self, name: str) -> int: ...
    def attr_details(self, name: str) -> tuple[RType, ClassIR]: ...
    def attr_type(self, name: str) -> RType: ...
    def method_decl(self, name: str) -> FuncDecl: ...
    def method_sig(self, name: str) -> FuncSignature: ...
    def has_method(self, name: str) -> bool: ...
    def is_method_final(self, name: str) -> bool: ...
    def has_attr(self, name: str) -> bool: ...
    def is_deletable(self, name: str) -> bool: ...
    def is_always_defined(self, name: str) -> bool: ...
    def name_prefix(self, names: NameGenerator) -> str: ...
    def struct_name(self, names: NameGenerator) -> str: ...
    def get_method_and_class(self, name: str, *, prefer_method: bool = False) -> tuple[FuncIR, ClassIR] | None: ...
    def get_method(self, name: str, *, prefer_method: bool = False) -> FuncIR | None: ...
    def has_method_decl(self, name: str) -> bool: ...
    def has_no_subclasses(self) -> bool: ...
    def subclasses(self) -> set[ClassIR] | None:
        """Return all subclasses of this class, both direct and indirect.

        Return None if it is impossible to identify all subclasses, for example
        because we are performing separate compilation.
        """
    def concrete_subclasses(self) -> list[ClassIR] | None:
        """Return all concrete (i.e. non-trait and non-abstract) subclasses.

        Include both direct and indirect subclasses. Place classes with no children first.
        """
    def is_serializable(self) -> bool: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict, ctx: DeserMaps) -> ClassIR: ...

class NonExtClassInfo:
    """Information needed to construct a non-extension class (Python class).

    Includes the class dictionary, a tuple of base classes,
    the class annotations dictionary, and the metaclass.
    """
    dict: Incomplete
    bases: Incomplete
    anns: Incomplete
    metaclass: Incomplete
    def __init__(self, dict: Value, bases: Value, anns: Value, metaclass: Value) -> None: ...

def serialize_vtable_entry(entry: VTableMethod) -> JsonDict: ...
def serialize_vtable(vtable: VTableEntries) -> list[JsonDict]: ...
def deserialize_vtable_entry(data: JsonDict, ctx: DeserMaps) -> VTableMethod: ...
def deserialize_vtable(data: list[JsonDict], ctx: DeserMaps) -> VTableEntries: ...
def all_concrete_classes(class_ir: ClassIR) -> list[ClassIR] | None:
    """Return all concrete classes among the class itself and its subclasses."""
