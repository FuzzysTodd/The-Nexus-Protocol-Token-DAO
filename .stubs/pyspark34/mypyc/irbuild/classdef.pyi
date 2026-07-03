import abc
from _typeshed import Incomplete
from abc import abstractmethod
from mypy.nodes import AssignmentStmt, ClassDef as ClassDef, FuncDef, Lvalue as Lvalue, NameExpr, TypeInfo
from mypyc.common import PROPSET_PREFIX as PROPSET_PREFIX
from mypyc.ir.class_ir import ClassIR as ClassIR, NonExtClassInfo as NonExtClassInfo
from mypyc.ir.func_ir import FuncDecl as FuncDecl, FuncSignature as FuncSignature
from mypyc.ir.ops import BasicBlock as BasicBlock, Branch as Branch, Call as Call, InitStatic as InitStatic, LoadAddress as LoadAddress, LoadErrorValue as LoadErrorValue, LoadStatic as LoadStatic, MethodCall as MethodCall, NAMESPACE_TYPE as NAMESPACE_TYPE, Register as Register, Return as Return, SetAttr as SetAttr, TupleSet as TupleSet, Value as Value
from mypyc.ir.rtypes import RType as RType, bool_rprimitive as bool_rprimitive, dict_rprimitive as dict_rprimitive, is_none_rprimitive as is_none_rprimitive, is_object_rprimitive as is_object_rprimitive, is_optional_type as is_optional_type, object_rprimitive as object_rprimitive
from mypyc.irbuild.builder import IRBuilder as IRBuilder
from mypyc.irbuild.function import gen_property_getter_ir as gen_property_getter_ir, gen_property_setter_ir as gen_property_setter_ir, handle_ext_method as handle_ext_method, handle_non_ext_method as handle_non_ext_method, load_type as load_type
from mypyc.irbuild.util import dataclass_type as dataclass_type, get_func_def as get_func_def, is_constant as is_constant, is_dataclass_decorator as is_dataclass_decorator
from mypyc.primitives.dict_ops import dict_new_op as dict_new_op, dict_set_item_op as dict_set_item_op
from mypyc.primitives.generic_ops import py_hasattr_op as py_hasattr_op, py_setattr_op as py_setattr_op
from mypyc.primitives.misc_ops import dataclass_sleight_of_hand as dataclass_sleight_of_hand, not_implemented_op as not_implemented_op, py_calc_meta_op as py_calc_meta_op, pytype_from_template_op as pytype_from_template_op, type_object_op as type_object_op
from typing import Callable, Final

def transform_class_def(builder: IRBuilder, cdef: ClassDef) -> None:
    '''Create IR for a class definition.

    This can generate both extension (native) and non-extension
    classes.  These are generated in very different ways. In the
    latter case we construct a Python type object at runtime by doing
    the equivalent of "type(name, bases, dict)" in IR. Extension
    classes are defined via C structs that are generated later in
    mypyc.codegen.emitclass.

    This is the main entry point to this module.
    '''

class ClassBuilder(metaclass=abc.ABCMeta):
    """Create IR for a class definition.

    This is an abstract base class.
    """
    builder: Incomplete
    cdef: Incomplete
    attrs_to_cache: Incomplete
    def __init__(self, builder: IRBuilder, cdef: ClassDef) -> None: ...
    @abstractmethod
    def add_method(self, fdef: FuncDef) -> None:
        """Add a method to the class IR"""
    @abstractmethod
    def add_attr(self, lvalue: NameExpr, stmt: AssignmentStmt) -> None:
        """Add an attribute to the class IR"""
    @abstractmethod
    def finalize(self, ir: ClassIR) -> None:
        """Perform any final operations to complete the class IR"""

class NonExtClassBuilder(ClassBuilder):
    non_ext: Incomplete
    def __init__(self, builder: IRBuilder, cdef: ClassDef) -> None: ...
    def create_non_ext_info(self) -> NonExtClassInfo: ...
    def add_method(self, fdef: FuncDef) -> None: ...
    def add_attr(self, lvalue: NameExpr, stmt: AssignmentStmt) -> None: ...
    def finalize(self, ir: ClassIR) -> None: ...

class ExtClassBuilder(ClassBuilder):
    type_obj: Incomplete
    def __init__(self, builder: IRBuilder, cdef: ClassDef) -> None: ...
    def skip_attr_default(self, name: str, stmt: AssignmentStmt) -> bool:
        """Controls whether to skip generating a default for an attribute."""
    def add_method(self, fdef: FuncDef) -> None: ...
    def add_attr(self, lvalue: NameExpr, stmt: AssignmentStmt) -> None: ...
    def finalize(self, ir: ClassIR) -> None: ...

class DataClassBuilder(ExtClassBuilder):
    add_annotations_to_dict: bool
    non_ext: Incomplete
    def __init__(self, builder: IRBuilder, cdef: ClassDef) -> None: ...
    def create_non_ext_info(self) -> NonExtClassInfo:
        """Set up a NonExtClassInfo to track dataclass attributes.

        In addition to setting up a normal extension class for dataclasses,
        we also collect its class attributes like a non-extension class so
        that we can hand them to the dataclass decorator.
        """
    def skip_attr_default(self, name: str, stmt: AssignmentStmt) -> bool: ...
    def get_type_annotation(self, stmt: AssignmentStmt) -> TypeInfo | None: ...
    def add_attr(self, lvalue: NameExpr, stmt: AssignmentStmt) -> None: ...
    def finalize(self, ir: ClassIR) -> None:
        """Generate code to finish instantiating a dataclass.

        This works by replacing all of the attributes on the class
        (which will be descriptors) with whatever they would be in a
        non-extension class, calling dataclass, then switching them back.

        The resulting class is an extension class and instances of it do not
        have a __dict__ (unless something else requires it).
        All methods written explicitly in the source are compiled and
        may be called through the vtable while the methods generated
        by dataclasses are interpreted and may not be.

        (If we just called dataclass without doing this, it would think that all
        of the descriptors for our attributes are default values and generate an
        incorrect constructor. We need to do the switch so that dataclass gets the
        appropriate defaults.)
        """

class AttrsClassBuilder(DataClassBuilder):
    """Create IR for an attrs class where auto_attribs=False (the default).

    When auto_attribs is enabled, attrs classes behave similarly to dataclasses
    (i.e. types are stored as annotations on the class) and are thus handled
    by DataClassBuilder, but when auto_attribs is disabled the types are
    provided via attr.ib(type=...)
    """
    add_annotations_to_dict: bool
    def skip_attr_default(self, name: str, stmt: AssignmentStmt) -> bool: ...
    def get_type_annotation(self, stmt: AssignmentStmt) -> TypeInfo | None: ...

def allocate_class(builder: IRBuilder, cdef: ClassDef) -> Value: ...

MAGIC_TYPED_DICT_CLASSES: Final[tuple[str, ...]]

def populate_non_ext_bases(builder: IRBuilder, cdef: ClassDef) -> Value:
    """Create base class tuple of a non-extension class.

    The tuple is passed to the metaclass constructor.
    """
def find_non_ext_metaclass(builder: IRBuilder, cdef: ClassDef, bases: Value) -> Value:
    """Find the metaclass of a class from its defs and bases."""
def setup_non_ext_dict(builder: IRBuilder, cdef: ClassDef, metaclass: Value, bases: Value) -> Value:
    """Initialize the class dictionary for a non-extension class.

    This class dictionary is passed to the metaclass constructor.
    """
def add_non_ext_class_attr_ann(builder: IRBuilder, non_ext: NonExtClassInfo, lvalue: NameExpr, stmt: AssignmentStmt, get_type_info: Callable[[AssignmentStmt], TypeInfo | None] | None = None) -> None:
    """Add a class attribute to __annotations__ of a non-extension class."""
def add_non_ext_class_attr(builder: IRBuilder, non_ext: NonExtClassInfo, lvalue: NameExpr, stmt: AssignmentStmt, cdef: ClassDef, attr_to_cache: list[tuple[Lvalue, RType]]) -> None:
    """Add a class attribute to __dict__ of a non-extension class."""
def find_attr_initializers(builder: IRBuilder, cdef: ClassDef, skip: Callable[[str, AssignmentStmt], bool] | None = None) -> tuple[set[str], list[AssignmentStmt]]:
    """Find initializers of attributes in a class body.

    If provided, the skip arg should be a callable which will return whether
    to skip generating a default for an attribute.  It will be passed the name of
    the attribute and the corresponding AssignmentStmt.
    """
def generate_attr_defaults_init(builder: IRBuilder, cdef: ClassDef, default_assignments: list[AssignmentStmt]) -> None:
    """Generate an initialization method for default attr values (from class vars)."""
def check_deletable_declaration(builder: IRBuilder, cl: ClassIR, line: int) -> None: ...
def create_ne_from_eq(builder: IRBuilder, cdef: ClassDef) -> None:
    '''Create a "__ne__" method from a "__eq__" method (if only latter exists).'''
def gen_glue_ne_method(builder: IRBuilder, cls: ClassIR, line: int) -> None:
    '''Generate a "__ne__" method from a "__eq__" method.'''
def load_non_ext_class(builder: IRBuilder, ir: ClassIR, non_ext: NonExtClassInfo, line: int) -> Value: ...
def load_decorated_class(builder: IRBuilder, cdef: ClassDef, type_obj: Value) -> Value:
    """Apply class decorators to create a decorated (non-extension) class object.

    Given a decorated ClassDef and a register containing a
    non-extension representation of the ClassDef created via the type
    constructor, applies the corresponding decorator functions on that
    decorated ClassDef and returns a register containing the decorated
    ClassDef.
    """
def cache_class_attrs(builder: IRBuilder, attrs_to_cache: list[tuple[Lvalue, RType]], cdef: ClassDef) -> None:
    """Add class attributes to be cached to the global cache."""
def create_mypyc_attrs_tuple(builder: IRBuilder, ir: ClassIR, line: int) -> Value: ...
def add_dunders_to_non_ext_dict(builder: IRBuilder, non_ext: NonExtClassInfo, line: int, add_annotations: bool = True) -> None: ...
