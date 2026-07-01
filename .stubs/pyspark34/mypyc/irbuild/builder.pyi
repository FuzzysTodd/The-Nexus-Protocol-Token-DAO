from _typeshed import Incomplete
from mypy.build import Graph as Graph
from mypy.nodes import ArgKind as ArgKind, CallExpr as CallExpr, Expression, FuncDef as FuncDef, Lvalue as Lvalue, MemberExpr, NameExpr, OpExpr as OpExpr, RefExpr, Statement as Statement, SymbolNode, TupleExpr, TypeInfo, Var
from mypy.types import Instance, ProperType as ProperType, Type as Type
from mypy.visitor import ExpressionVisitor, StatementVisitor
from mypyc.common import BITMAP_BITS as BITMAP_BITS, SELF_NAME as SELF_NAME, TEMP_ATTR_NAME as TEMP_ATTR_NAME
from mypyc.crash import catch_errors as catch_errors
from mypyc.errors import Errors as Errors
from mypyc.ir.class_ir import ClassIR as ClassIR, NonExtClassInfo as NonExtClassInfo
from mypyc.ir.func_ir import FuncDecl as FuncDecl, FuncIR as FuncIR, FuncSignature as FuncSignature, INVALID_FUNC_DEF as INVALID_FUNC_DEF, RuntimeArg as RuntimeArg
from mypyc.ir.ops import Assign as Assign, BasicBlock as BasicBlock, Branch as Branch, ComparisonOp as ComparisonOp, GetAttr as GetAttr, InitStatic as InitStatic, IntOp as IntOp, Integer as Integer, LoadStatic as LoadStatic, NAMESPACE_MODULE as NAMESPACE_MODULE, Op as Op, RaiseStandardError as RaiseStandardError, Register as Register, SetAttr as SetAttr, TupleGet as TupleGet, Unreachable as Unreachable, Value as Value
from mypyc.ir.rtypes import RInstance as RInstance, RTuple as RTuple, RType as RType, RUnion as RUnion, bitmap_rprimitive as bitmap_rprimitive, c_pyssize_t_rprimitive as c_pyssize_t_rprimitive, dict_rprimitive as dict_rprimitive, int_rprimitive as int_rprimitive, is_float_rprimitive as is_float_rprimitive, is_list_rprimitive as is_list_rprimitive, is_none_rprimitive as is_none_rprimitive, is_object_rprimitive as is_object_rprimitive, is_tagged as is_tagged, is_tuple_rprimitive as is_tuple_rprimitive, none_rprimitive as none_rprimitive, object_rprimitive as object_rprimitive, str_rprimitive as str_rprimitive
from mypyc.irbuild.context import FuncInfo as FuncInfo, ImplicitClass as ImplicitClass
from mypyc.irbuild.ll_builder import LowLevelIRBuilder as LowLevelIRBuilder
from mypyc.irbuild.mapper import Mapper as Mapper
from mypyc.irbuild.nonlocalcontrol import BaseNonlocalControl as BaseNonlocalControl, GeneratorNonlocalControl as GeneratorNonlocalControl, LoopNonlocalControl as LoopNonlocalControl, NonlocalControl as NonlocalControl
from mypyc.irbuild.prebuildvisitor import PreBuildVisitor as PreBuildVisitor
from mypyc.irbuild.prepare import RegisterImplInfo as RegisterImplInfo
from mypyc.irbuild.targets import AssignmentTarget as AssignmentTarget, AssignmentTargetAttr as AssignmentTargetAttr, AssignmentTargetIndex as AssignmentTargetIndex, AssignmentTargetRegister as AssignmentTargetRegister, AssignmentTargetTuple as AssignmentTargetTuple
from mypyc.irbuild.util import bytes_from_str as bytes_from_str, is_constant as is_constant
from mypyc.options import CompilerOptions as CompilerOptions
from mypyc.primitives.dict_ops import dict_get_item_op as dict_get_item_op, dict_set_item_op as dict_set_item_op
from mypyc.primitives.generic_ops import iter_op as iter_op, next_op as next_op, py_setattr_op as py_setattr_op
from mypyc.primitives.list_ops import list_get_item_unsafe_op as list_get_item_unsafe_op, list_pop_last as list_pop_last, to_list as to_list
from mypyc.primitives.misc_ops import check_unpack_count_op as check_unpack_count_op, get_module_dict_op as get_module_dict_op, import_op as import_op
from mypyc.primitives.registry import CFunctionDescription as CFunctionDescription, function_ops as function_ops
from typing import Any, Callable, Final, Iterator, Sequence
from typing_extensions import overload

int_borrow_friendly_op: Final[Incomplete]

class IRVisitor(ExpressionVisitor[Value], StatementVisitor[None]): ...
class UnsupportedException(Exception): ...
SymbolTarget = AssignmentTargetRegister | AssignmentTargetAttr

class IRBuilder:
    builder: Incomplete
    builders: Incomplete
    symtables: Incomplete
    runtime_args: Incomplete
    function_name_stack: Incomplete
    class_ir_stack: Incomplete
    block_reachable_stack: Incomplete
    current_module: Incomplete
    mapper: Incomplete
    types: Incomplete
    graph: Incomplete
    ret_types: Incomplete
    functions: Incomplete
    function_names: Incomplete
    classes: Incomplete
    final_names: Incomplete
    callable_class_names: Incomplete
    options: Incomplete
    lambda_counter: int
    temp_counter: int
    free_variables: Incomplete
    prop_setters: Incomplete
    encapsulating_funcs: Incomplete
    nested_fitems: Incomplete
    fdefs_to_decorators: Incomplete
    module_import_groups: Incomplete
    singledispatch_impls: Incomplete
    visitor: Incomplete
    fn_info: Incomplete
    fn_infos: Incomplete
    nonlocal_control: Incomplete
    errors: Incomplete
    imports: Incomplete
    can_borrow: bool
    def __init__(self, current_module: str, types: dict[Expression, Type], graph: Graph, errors: Errors, mapper: Mapper, pbv: PreBuildVisitor, visitor: IRVisitor, options: CompilerOptions, singledispatch_impls: dict[FuncDef, list[RegisterImplInfo]]) -> None: ...
    module_name: Incomplete
    module_path: Incomplete
    def set_module(self, module_name: str, module_path: str) -> None:
        """Set the name and path of the current module.

        This must be called before transforming any AST nodes.
        """
    @overload
    def accept(self, node: Expression, *, can_borrow: bool = False) -> Value: ...
    @overload
    def accept(self, node: Statement) -> None: ...
    def flush_keep_alives(self) -> None: ...
    def add(self, op: Op) -> Value: ...
    def goto(self, target: BasicBlock) -> None: ...
    def activate_block(self, block: BasicBlock) -> None: ...
    def goto_and_activate(self, block: BasicBlock) -> None: ...
    def self(self) -> Register: ...
    def py_get_attr(self, obj: Value, attr: str, line: int) -> Value: ...
    def load_str(self, value: str) -> Value: ...
    def load_bytes_from_str_literal(self, value: str) -> Value:
        """Load bytes object from a string literal.

        The literal characters of BytesExpr (the characters inside b'')
        are stored in BytesExpr.value, whose type is 'str' not 'bytes'.
        Thus we perform a special conversion here.
        """
    def load_int(self, value: int) -> Value: ...
    def load_float(self, value: float) -> Value: ...
    def unary_op(self, lreg: Value, expr_op: str, line: int) -> Value: ...
    def binary_op(self, lreg: Value, rreg: Value, expr_op: str, line: int) -> Value: ...
    def coerce(self, src: Value, target_type: RType, line: int, force: bool = False) -> Value: ...
    def none_object(self) -> Value: ...
    def none(self) -> Value: ...
    def true(self) -> Value: ...
    def false(self) -> Value: ...
    def new_list_op(self, values: list[Value], line: int) -> Value: ...
    def new_set_op(self, values: list[Value], line: int) -> Value: ...
    def translate_is_op(self, lreg: Value, rreg: Value, expr_op: str, line: int) -> Value: ...
    def py_call(self, function: Value, arg_values: list[Value], line: int, arg_kinds: list[ArgKind] | None = None, arg_names: Sequence[str | None] | None = None) -> Value: ...
    def add_bool_branch(self, value: Value, true: BasicBlock, false: BasicBlock) -> None: ...
    def load_native_type_object(self, fullname: str) -> Value: ...
    def gen_method_call(self, base: Value, name: str, arg_values: list[Value], result_type: RType | None, line: int, arg_kinds: list[ArgKind] | None = None, arg_names: list[str | None] | None = None) -> Value: ...
    def load_module(self, name: str) -> Value: ...
    def call_c(self, desc: CFunctionDescription, args: list[Value], line: int) -> Value: ...
    def int_op(self, type: RType, lhs: Value, rhs: Value, op: int, line: int) -> Value: ...
    def compare_tagged(self, lhs: Value, rhs: Value, op: str, line: int) -> Value: ...
    def compare_tuples(self, lhs: Value, rhs: Value, op: str, line: int) -> Value: ...
    def builtin_len(self, val: Value, line: int) -> Value: ...
    def new_tuple(self, items: list[Value], line: int) -> Value: ...
    def add_to_non_ext_dict(self, non_ext: NonExtClassInfo, key: str, val: Value, line: int) -> None: ...
    def gen_import(self, id: str, line: int) -> None: ...
    def check_if_module_loaded(self, id: str, line: int, needs_import: BasicBlock, out: BasicBlock) -> None:
        """Generate code that checks if the module `id` has been loaded yet.

        Arguments:
            id: name of module to check if imported
            line: line number that the import occurs on
            needs_import: the BasicBlock that is run if the module has not been loaded yet
            out: the BasicBlock that is run if the module has already been loaded"""
    def get_module(self, module: str, line: int) -> Value: ...
    def get_module_attr(self, module: str, attr: str, line: int) -> Value:
        """Look up an attribute of a module without storing it in the local namespace.

        For example, get_module_attr('typing', 'TypedDict', line) results in
        the value of 'typing.TypedDict'.

        Import the module if needed.
        """
    def assign_if_null(self, target: Register, get_val: Callable[[], Value], line: int) -> None:
        """If target is NULL, assign value produced by get_val to it."""
    def assign_if_bitmap_unset(self, target: Register, get_val: Callable[[], Value], index: int, line: int) -> None: ...
    def maybe_add_implicit_return(self) -> None: ...
    def add_implicit_return(self) -> None: ...
    def add_implicit_unreachable(self) -> None: ...
    def disallow_class_assignments(self, lvalues: list[Lvalue], line: int) -> None: ...
    def non_function_scope(self) -> bool: ...
    def top_level_fn_info(self) -> FuncInfo | None: ...
    def init_final_static(self, lvalue: Lvalue, rvalue_reg: Value, class_name: str | None = None, *, type_override: RType | None = None) -> None: ...
    def load_final_static(self, fullname: str, typ: RType, line: int, error_name: str | None = None) -> Value: ...
    def load_literal_value(self, val: int | str | bytes | float | complex | bool) -> Value:
        """Load value of a final name, class-level attribute, or constant folded expression."""
    def get_assignment_target(self, lvalue: Lvalue, line: int = -1, *, for_read: bool = False) -> AssignmentTarget: ...
    def read(self, target: Value | AssignmentTarget, line: int = -1, can_borrow: bool = False) -> Value: ...
    def assign(self, target: Register | AssignmentTarget, rvalue_reg: Value, line: int) -> None: ...
    def coerce_rvalue(self, rvalue: Value, rtype: RType, line: int) -> Value: ...
    def process_sequence_assignment(self, target: AssignmentTargetTuple, rvalue: Value, line: int) -> None:
        """Process assignment like 'x, y = s', where s is a variable-length list or tuple."""
    def process_iterator_tuple_assignment_helper(self, litem: AssignmentTarget, ritem: Value, line: int) -> None: ...
    def process_iterator_tuple_assignment(self, target: AssignmentTargetTuple, rvalue_reg: Value, line: int) -> None: ...
    def push_loop_stack(self, continue_block: BasicBlock, break_block: BasicBlock) -> None: ...
    def pop_loop_stack(self) -> None: ...
    def make_spill_target(self, type: RType) -> AssignmentTarget:
        """Moves a given Value instance into the generator class' environment class."""
    def spill(self, value: Value) -> AssignmentTarget:
        """Moves a given Value instance into the generator class' environment class."""
    def maybe_spill(self, value: Value) -> Value | AssignmentTarget:
        """
        Moves a given Value instance into the environment class for generator functions. For
        non-generator functions, leaves the Value instance as it is.

        Returns an AssignmentTarget associated with the Value for generator functions and the
        original Value itself for non-generator functions.
        """
    def maybe_spill_assignable(self, value: Value) -> Register | AssignmentTarget:
        """
        Moves a given Value instance into the environment class for generator functions. For
        non-generator functions, allocate a temporary Register.

        Returns an AssignmentTarget associated with the Value for generator functions and an
        assignable Register for non-generator functions.
        """
    def extract_int(self, e: Expression) -> int | None: ...
    def get_sequence_type(self, expr: Expression) -> RType: ...
    def get_sequence_type_from_type(self, target_type: Type) -> RType: ...
    def get_dict_base_type(self, expr: Expression) -> list[Instance]:
        """Find dict type of a dict-like expression.

        This is useful for dict subclasses like SymbolTable.
        """
    def get_dict_key_type(self, expr: Expression) -> RType: ...
    def get_dict_value_type(self, expr: Expression) -> RType: ...
    def get_dict_item_type(self, expr: Expression) -> RType: ...
    def is_native_module(self, module: str) -> bool:
        """Is the given module one compiled by mypyc?"""
    def is_native_ref_expr(self, expr: RefExpr) -> bool: ...
    def is_native_module_ref_expr(self, expr: RefExpr) -> bool: ...
    def is_synthetic_type(self, typ: TypeInfo) -> bool:
        """Is a type something other than just a class we've created?"""
    def get_final_ref(self, expr: MemberExpr) -> tuple[str, Var, bool] | None:
        """Check if `expr` is a final attribute.

        This needs to be done differently for class and module attributes to
        correctly determine fully qualified name. Return a tuple that consists of
        the qualified name, the corresponding Var node, and a flag indicating whether
        the final name was defined in a compiled module. Return None if `expr` does not
        refer to a final attribute.
        """
    def emit_load_final(self, final_var: Var, fullname: str, name: str, native: bool, typ: Type, line: int) -> Value | None:
        """Emit code for loading value of a final name (if possible).

        Args:
            final_var: Var corresponding to the final name
            fullname: its qualified name
            name: shorter name to show in errors
            native: whether the name was defined in a compiled module
            typ: its type
            line: line number where loading occurs
        """
    def is_module_member_expr(self, expr: MemberExpr) -> bool: ...
    def call_refexpr_with_args(self, expr: CallExpr, callee: RefExpr, arg_values: list[Value]) -> Value: ...
    def shortcircuit_expr(self, expr: OpExpr) -> Value: ...
    def flatten_classes(self, arg: RefExpr | TupleExpr) -> list[ClassIR] | None:
        """Flatten classes in isinstance(obj, (A, (B, C))).

        If at least one item is not a reference to a native class, return None.
        """
    def enter(self, fn_info: FuncInfo | str = '') -> None: ...
    def leave(self) -> tuple[list[Register], list[RuntimeArg], list[BasicBlock], RType, FuncInfo]: ...
    def enter_method(self, class_ir: ClassIR, name: str, ret_type: RType, fn_info: FuncInfo | str = '', self_type: RType | None = None) -> Iterator[None]:
        """Generate IR for a method.

        If the method takes arguments, you should immediately afterwards call
        add_argument() for each non-self argument (self is created implicitly).

        Args:
            class_ir: Add method to this class
            name: Short name of the method
            ret_type: Return type of the method
            fn_info: Optionally, additional information about the method
            self_type: If not None, override default type of the implicit 'self'
                argument (by default, derive type from class_ir)
        """
    def add_argument(self, var: str | Var, typ: RType, kind: ArgKind = ...) -> Register:
        """Declare an argument in the current function.

        You should use this instead of directly calling add_local() in new code.
        """
    def lookup(self, symbol: SymbolNode) -> SymbolTarget: ...
    def add_local(self, symbol: SymbolNode, typ: RType, is_arg: bool = False) -> Register:
        """Add register that represents a symbol to the symbol table.

        Args:
            is_arg: is this a function argument
        """
    def add_local_reg(self, symbol: SymbolNode, typ: RType, is_arg: bool = False) -> AssignmentTargetRegister:
        """Like add_local, but return an assignment target instead of value."""
    def add_self_to_env(self, cls: ClassIR) -> AssignmentTargetRegister:
        """Low-level function that adds a 'self' argument.

        This is only useful if using enter() instead of enter_method().
        """
    def add_target(self, symbol: SymbolNode, target: SymbolTarget) -> SymbolTarget: ...
    def type_to_rtype(self, typ: Type | None) -> RType: ...
    def node_type(self, node: Expression) -> RType: ...
    def add_var_to_env_class(self, var: SymbolNode, rtype: RType, base: FuncInfo | ImplicitClass, reassign: bool = False) -> AssignmentTarget: ...
    def is_builtin_ref_expr(self, expr: RefExpr) -> bool: ...
    def load_global(self, expr: NameExpr) -> Value:
        """Loads a Python-level global.

        This takes a NameExpr and uses its name as a key to retrieve the corresponding PyObject *
        from the _globals dictionary in the C-generated code.
        """
    def load_global_str(self, name: str, line: int) -> Value: ...
    def load_globals_dict(self) -> Value: ...
    def load_module_attr_by_fullname(self, fullname: str, line: int) -> Value: ...
    def is_native_attr_ref(self, expr: MemberExpr) -> bool:
        """Is expr a direct reference to a native (struct) attribute of an instance?"""
    def mark_block_unreachable(self) -> None:
        """Mark statements in the innermost block being processed as unreachable.

        This should be called after a statement that unconditionally leaves the
        block, such as 'break' or 'return'.
        """
    def catch_errors(self, line: int) -> Any: ...
    def warning(self, msg: str, line: int) -> None: ...
    def error(self, msg: str, line: int) -> None: ...
    def note(self, msg: str, line: int) -> None: ...
    def add_function(self, func_ir: FuncIR, line: int) -> None: ...

def gen_arg_defaults(builder: IRBuilder) -> None:
    """Generate blocks for arguments that have default values.

    If the passed value is an error value, then assign the default
    value to the argument.
    """
def remangle_redefinition_name(name: str) -> str:
    """Remangle names produced by mypy when allow-redefinition is used and a name
    is used with multiple types within a single block.

    We only need to do this for locals, because the name is used as the name of the register;
    for globals, the name itself is stored in a register for the purpose of doing dict
    lookups.
    """
def get_call_target_fullname(ref: RefExpr) -> str: ...
