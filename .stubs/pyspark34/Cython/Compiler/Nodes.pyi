from . import Builtin as Builtin, DebugFlags as DebugFlags, Future as Future, Naming as Naming, Options as Options, PyrexTypes as PyrexTypes, TypeSlots as TypeSlots
from ..Utils import add_metaclass as add_metaclass, str_to_number as str_to_number
from .Code import UtilityCode as UtilityCode
from .Errors import CannotSpecialize as CannotSpecialize, CompileError as CompileError, InternalError as InternalError, error as error, warning as warning
from .PyrexTypes import error_type as error_type, py_object_type as py_object_type
from .Pythran import has_np_pythran as has_np_pythran, is_pythran_buffer as is_pythran_buffer, pythran_type as pythran_type
from .StringEncoding import EncodedString as EncodedString
from .Symtab import ClosureScope as ClosureScope, CppClassScope as CppClassScope, CppScopedEnumScope as CppScopedEnumScope, GeneratorExpressionScope as GeneratorExpressionScope, LocalScope as LocalScope, ModuleScope as ModuleScope, PropertyScope as PropertyScope, PyClassScope as PyClassScope, StructOrUnionScope as StructOrUnionScope, TemplateScope as TemplateScope, punycodify_name as punycodify_name
from _typeshed import Incomplete

IMPLICIT_CLASSMETHODS: Incomplete

def relative_position(pos): ...
def embed_position(pos, docstring): ...
def write_func_call(func, codewriter_class): ...

class VerboseCodeWriter(type):
    def __new__(cls, name, bases, attrs): ...

class CheckAnalysers(type):
    """Metaclass to check that type analysis functions return a node.
    """
    methods: Incomplete
    def __new__(cls, name, bases, attrs): ...

class Node:
    is_name: int
    is_none: int
    is_nonecheck: int
    is_literal: int
    is_terminator: int
    is_wrapper: bool
    is_cproperty: bool
    is_templated_type_node: bool
    temps: Incomplete
    child_attrs: Incomplete
    outer_attrs: Incomplete
    cf_state: Incomplete
    coercion_type: Incomplete
    pos: Incomplete
    def __init__(self, pos, **kw) -> None: ...
    gil_message: str
    nogil_check: Incomplete
    in_nogil_context: bool
    def gil_error(self, env: Incomplete | None = None) -> None: ...
    cpp_message: str
    def cpp_check(self, env) -> None: ...
    def cpp_error(self) -> None: ...
    def clone_node(self):
        """Clone the node. This is defined as a shallow copy, except for member lists
           amongst the child attributes (from get_child_accessors) which are also
           copied. Lists containing child nodes are thus seen as a way for the node
           to hold multiple children directly; the list is not treated as a separate
           level in the tree."""
    def analyse_declarations(self, env) -> None: ...
    def analyse_expressions(self, env) -> None: ...
    def generate_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...
    def end_pos(self): ...
    def dump(self, level: int = 0, filter_out=('pos',), cutoff: int = 100, encountered: Incomplete | None = None):
        """Debug helper method that returns a recursive string representation of this node.
        """
    def dump_pos(self, mark_column: bool = False, marker: str = '(#)'):
        """Debug helper method that returns the source code context of this node as a string.
        """

class CompilerDirectivesNode(Node):
    """
    Sets compiler directives for the children nodes
    """
    child_attrs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    body: Incomplete
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...

class BlockNode:
    def generate_cached_builtins_decls(self, env, code) -> None: ...
    def generate_lambda_definitions(self, env, code) -> None: ...

class StatListNode(Node):
    child_attrs: Incomplete
    @staticmethod
    def create_analysed(pos, env, **kw): ...
    def analyse_declarations(self, env) -> None: ...
    stats: Incomplete
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...

class StatNode(Node):
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...

class CDefExternNode(StatNode):
    child_attrs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    body: Incomplete
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...

class CDeclaratorNode(Node):
    child_attrs: Incomplete
    calling_convention: str
    def declared_name(self) -> None: ...
    def analyse_templates(self) -> None: ...

class CNameDeclaratorNode(CDeclaratorNode):
    child_attrs: Incomplete
    default: Incomplete
    def declared_name(self): ...
    name: Incomplete
    type: Incomplete
    def analyse(self, base_type, env, nonempty: int = 0, visibility: Incomplete | None = None, in_pxd: bool = False): ...

class CPtrDeclaratorNode(CDeclaratorNode):
    child_attrs: Incomplete
    def declared_name(self): ...
    def analyse_templates(self): ...
    def analyse(self, base_type, env, nonempty: int = 0, visibility: Incomplete | None = None, in_pxd: bool = False): ...

class _CReferenceDeclaratorBaseNode(CDeclaratorNode):
    child_attrs: Incomplete
    def declared_name(self): ...
    def analyse_templates(self): ...

class CReferenceDeclaratorNode(_CReferenceDeclaratorBaseNode):
    def analyse(self, base_type, env, nonempty: int = 0, visibility: Incomplete | None = None, in_pxd: bool = False): ...

class CppRvalueReferenceDeclaratorNode(_CReferenceDeclaratorBaseNode):
    def analyse(self, base_type, env, nonempty: int = 0, visibility: Incomplete | None = None, in_pxd: bool = False): ...

class CArrayDeclaratorNode(CDeclaratorNode):
    child_attrs: Incomplete
    dimension: Incomplete
    def analyse(self, base_type, env, nonempty: int = 0, visibility: Incomplete | None = None, in_pxd: bool = False): ...

class CFuncDeclaratorNode(CDeclaratorNode):
    child_attrs: Incomplete
    overridable: int
    optional_arg_count: int
    is_const_method: int
    templates: Incomplete
    def declared_name(self): ...
    base: Incomplete
    def analyse_templates(self): ...
    exception_check: bool
    exception_value: Incomplete
    def analyse(self, return_type, env, nonempty: int = 0, directive_locals: Incomplete | None = None, visibility: Incomplete | None = None, in_pxd: bool = False): ...
    def declare_optional_arg_struct(self, func_type, env, fused_cname: Incomplete | None = None) -> None:
        """
        Declares the optional argument struct (the struct used to hold the
        values for optional arguments). For fused cdef functions, this is
        deferred as analyse_declarations is called only once (on the fused
        cdef function).
        """

class CConstDeclaratorNode(CDeclaratorNode):
    child_attrs: Incomplete
    def analyse(self, base_type, env, nonempty: int = 0, visibility: Incomplete | None = None, in_pxd: bool = False): ...

class CArgDeclNode(Node):
    child_attrs: Incomplete
    outer_attrs: Incomplete
    is_self_arg: int
    is_type_arg: int
    is_generic: int
    is_special_method_optional: bool
    kw_only: int
    pos_only: int
    not_none: int
    or_none: int
    type: Incomplete
    name_declarator: Incomplete
    default_value: Incomplete
    annotation: Incomplete
    is_dynamic: int
    def declared_name(self): ...
    @property
    def name_cstring(self): ...
    @property
    def hdr_cname(self): ...
    def analyse(self, env, nonempty: int = 0, is_self_arg: bool = False): ...
    base_type: Incomplete
    def inject_type_from_annotations(self, env): ...
    def calculate_default_value_code(self, code): ...
    def annotate(self, code) -> None: ...
    def generate_assignment_code(self, code, target: Incomplete | None = None, overloaded_assignment: bool = False) -> None: ...

class CBaseTypeNode(Node):
    def analyse_as_type(self, env): ...

class CAnalysedBaseTypeNode(Node):
    child_attrs: Incomplete
    def analyse(self, env, could_be_name: bool = False): ...

class CSimpleBaseTypeNode(CBaseTypeNode):
    child_attrs: Incomplete
    arg_name: Incomplete
    module_path: Incomplete
    is_basic_c_type: bool
    complex: bool
    is_self_arg: bool
    def analyse(self, env, could_be_name: bool = False): ...

class MemoryViewSliceTypeNode(CBaseTypeNode):
    name: str
    child_attrs: Incomplete
    type: Incomplete
    def analyse(self, env, could_be_name: bool = False): ...
    def use_memview_utilities(self, env) -> None: ...

class CNestedBaseTypeNode(CBaseTypeNode):
    child_attrs: Incomplete
    def analyse(self, env, could_be_name: Incomplete | None = None): ...

class TemplatedTypeNode(CBaseTypeNode):
    child_attrs: Incomplete
    is_templated_type_node: bool
    dtype_node: Incomplete
    name: Incomplete
    type: Incomplete
    array_declarator: Incomplete
    def analyse(self, env, could_be_name: bool = False, base_type: Incomplete | None = None): ...
    def analyse_pytyping_modifiers(self, env): ...

class CComplexBaseTypeNode(CBaseTypeNode):
    child_attrs: Incomplete
    def analyse(self, env, could_be_name: bool = False): ...

class CTupleBaseTypeNode(CBaseTypeNode):
    child_attrs: Incomplete
    def analyse(self, env, could_be_name: bool = False): ...

class FusedTypeNode(CBaseTypeNode):
    """
    Represents a fused type in a ctypedef statement:

        ctypedef cython.fused_type(int, long, long long) integral

    name            str                     name of this fused type
    types           [CSimpleBaseTypeNode]   is the list of types to be fused
    """
    child_attrs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    def analyse(self, env, could_be_name: bool = False): ...

class CConstOrVolatileTypeNode(CBaseTypeNode):
    child_attrs: Incomplete
    def analyse(self, env, could_be_name: bool = False): ...

class CVarDefNode(StatNode):
    child_attrs: Incomplete
    decorators: Incomplete
    directive_locals: Incomplete
    dest_scope: Incomplete
    entry: Incomplete
    def analyse_declarations(self, env, dest_scope: Incomplete | None = None): ...

class CStructOrUnionDefNode(StatNode):
    child_attrs: Incomplete
    entry: Incomplete
    def declare(self, env, scope: Incomplete | None = None) -> None: ...
    def analyse_declarations(self, env) -> None: ...
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class CppClassNode(CStructOrUnionDefNode, BlockNode):
    decorators: Incomplete
    entry: Incomplete
    def declare(self, env) -> None: ...
    body: Incomplete
    scope: Incomplete
    def analyse_declarations(self, env): ...
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...

class CEnumDefNode(StatNode):
    child_attrs: Incomplete
    doc: Incomplete
    entry: Incomplete
    def declare(self, env) -> None: ...
    def analyse_declarations(self, env) -> None: ...
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class CEnumDefItemNode(StatNode):
    child_attrs: Incomplete
    value: Incomplete
    entry: Incomplete
    def analyse_enum_declarations(self, env, enum_entry, incremental_int_value) -> None: ...

class CTypeDefNode(StatNode):
    child_attrs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class FuncDefNode(StatNode, BlockNode):
    py_func: Incomplete
    needs_closure: bool
    needs_outer_scope: bool
    pymethdef_required: bool
    is_generator: bool
    is_generator_expression: bool
    is_coroutine: bool
    is_asyncgen: bool
    is_generator_body: bool
    is_async_def: bool
    modifiers: Incomplete
    has_fused_arguments: bool
    star_arg: Incomplete
    starstar_arg: Incomplete
    is_cyfunction: bool
    code_object: Incomplete
    return_type_annotation: Incomplete
    outer_attrs: Incomplete
    def analyse_default_values(self, env) -> None: ...
    def analyse_annotations(self, env) -> None: ...
    def align_argument_type(self, env, arg): ...
    def need_gil_acquisition(self, lenv): ...
    local_scope: Incomplete
    def create_local_scope(self, env): ...
    def generate_function_body(self, env, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def declare_argument(self, env, arg): ...
    def generate_arg_type_test(self, arg, code) -> None: ...
    def generate_arg_none_check(self, arg, code) -> None: ...
    def generate_wrapper_functions(self, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    def getbuffer_check(self, code) -> None: ...
    def getbuffer_init(self, code) -> None: ...
    def getbuffer_error_cleanup(self, code) -> None: ...
    def getbuffer_normal_cleanup(self, code) -> None: ...
    def get_preprocessor_guard(self): ...

class CFuncDefNode(FuncDefNode):
    child_attrs: Incomplete
    outer_attrs: Incomplete
    inline_in_pxd: bool
    decorators: Incomplete
    directive_locals: Incomplete
    directive_returns: Incomplete
    override: Incomplete
    template_declaration: Incomplete
    is_const_method: bool
    py_func_stat: Incomplete
    def unqualified_name(self): ...
    def declared_name(self): ...
    @property
    def code_object(self): ...
    is_c_class_method: Incomplete
    is_static_method: Incomplete
    type: Incomplete
    cfunc_declarator: Incomplete
    args: Incomplete
    has_fused_arguments: bool
    entry: Incomplete
    return_type: Incomplete
    overridable: bool
    def analyse_declarations(self, env) -> None: ...
    py_func: Incomplete
    body: Incomplete
    def declare_cpdef_wrapper(self, env) -> None: ...
    def call_self_node(self, omit_optional_args: int = 0, is_module_scope: int = 0): ...
    def declare_arguments(self, env) -> None: ...
    def need_gil_acquisition(self, lenv): ...
    def nogil_check(self, env) -> None: ...
    acquire_gil: Incomplete
    def analyse_expressions(self, env): ...
    def needs_assignment_synthesis(self, env, code: Incomplete | None = None): ...
    def generate_function_header(self, code, with_pymethdef, with_opt_args: int = 1, with_dispatch: int = 1, cname: Incomplete | None = None) -> None: ...
    def generate_argument_declarations(self, env, code) -> None: ...
    def generate_keyword_list(self, code) -> None: ...
    def generate_argument_parsing_code(self, env, code) -> None: ...
    def generate_argument_conversion_code(self, code) -> None: ...
    def generate_argument_type_tests(self, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    def error_value(self): ...
    def caller_will_check_exceptions(self): ...
    def generate_wrapper_functions(self, code) -> None: ...

class PyArgDeclNode(Node):
    child_attrs: Incomplete
    is_self_arg: bool
    is_type_arg: bool
    def generate_function_definitions(self, env, code) -> None: ...

class DecoratorNode(Node):
    child_attrs: Incomplete

class DefNode(FuncDefNode):
    child_attrs: Incomplete
    outer_attrs: Incomplete
    is_staticmethod: bool
    is_classmethod: bool
    lambda_name: Incomplete
    reqd_kw_flags_cname: str
    is_wrapper: int
    no_assignment_synthesis: int
    decorators: Incomplete
    return_type_annotation: Incomplete
    entry: Incomplete
    acquire_gil: int
    self_in_stararg: int
    py_cfunc_node: Incomplete
    requires_classobj: bool
    defaults_struct: Incomplete
    doc: Incomplete
    fused_py_func: bool
    specialized_cpdefs: Incomplete
    py_wrapper: Incomplete
    py_wrapper_required: bool
    func_cname: Incomplete
    defaults_getter: Incomplete
    num_posonly_args: Incomplete
    num_kwonly_args: Incomplete
    num_required_kw_args: Incomplete
    num_required_args: Incomplete
    def __init__(self, pos, **kwds) -> None: ...
    def as_cfunction(self, cfunc: Incomplete | None = None, scope: Incomplete | None = None, overridable: bool = True, returns: Incomplete | None = None, except_val: Incomplete | None = None, modifiers: Incomplete | None = None, nogil: bool = False, with_gil: bool = False): ...
    def is_cdef_func_compatible(self):
        """Determines if the function's signature is compatible with a
        cdef function.  This can be used before calling
        .as_cfunction() to see if that will be successful.
        """
    return_type: Incomplete
    def analyse_declarations(self, env) -> None: ...
    directive_locals: Incomplete
    has_fused_arguments: bool
    np_args_idx: Incomplete
    def analyse_argument_types(self, env) -> None: ...
    def analyse_signature(self, env) -> None: ...
    def bad_signature(self) -> None: ...
    def declare_pyfunction(self, env) -> None: ...
    def declare_lambda_function(self, env) -> None: ...
    def declare_arguments(self, env) -> None: ...
    def declare_python_arg(self, env, arg) -> None: ...
    def analyse_expressions(self, env): ...
    def needs_assignment_synthesis(self, env, code: Incomplete | None = None): ...
    def error_value(self): ...
    def caller_will_check_exceptions(self): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_function_header(self, code, with_pymethdef, proto_only: int = 0): ...
    def generate_argument_declarations(self, env, code) -> None: ...
    def generate_keyword_list(self, code) -> None: ...
    def generate_argument_parsing_code(self, env, code) -> None: ...
    def generate_argument_type_tests(self, code) -> None: ...

class DefNodeWrapper(FuncDefNode):
    defnode: Incomplete
    target: Incomplete
    needs_values_cleanup: bool
    num_posonly_args: Incomplete
    num_kwonly_args: Incomplete
    num_required_kw_args: Incomplete
    num_required_args: Incomplete
    self_in_stararg: Incomplete
    signature: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    np_args_idx: Incomplete
    def analyse_declarations(self, env) -> None: ...
    def prepare_argument_coercion(self, env) -> None: ...
    def signature_has_nongeneric_args(self): ...
    def signature_has_generic_args(self): ...
    def generate_function_body(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_function_header(self, code, with_pymethdef, proto_only: int = 0) -> None: ...
    def generate_argument_declarations(self, env, code) -> None: ...
    def generate_argument_parsing_code(self, env, code, decl_code) -> None: ...
    def generate_arg_xdecref(self, arg, code) -> None: ...
    def generate_arg_decref(self, arg, code) -> None: ...
    def generate_stararg_copy_code(self, code) -> None: ...
    def generate_tuple_and_keyword_parsing_code(self, args, code, decl_code) -> None: ...
    def generate_arg_assignment(self, arg, item, code) -> None: ...
    def generate_stararg_init_code(self, max_positional_args, code) -> None: ...
    def generate_argument_values_setup_code(self, args, code, decl_code) -> None: ...
    def generate_argument_values_cleanup_code(self, code) -> None: ...
    def generate_keyword_unpacking_code(self, min_positional_args, max_positional_args, has_fixed_positional_count, has_kw_only_args, all_args, argtuple_error_label, code) -> None: ...
    def generate_optional_kwonly_args_unpacking_code(self, all_args, code) -> None: ...
    def generate_argument_conversion_code(self, code) -> None: ...
    def generate_arg_conversion(self, arg, code) -> None: ...
    def generate_arg_conversion_from_pyobject(self, arg, code) -> None: ...
    def generate_arg_conversion_to_pyobject(self, arg, code) -> None: ...
    def generate_argument_type_tests(self, code) -> None: ...
    def error_value(self): ...

class GeneratorDefNode(DefNode):
    is_generator: bool
    is_iterable_coroutine: bool
    gen_type_name: str
    needs_closure: bool
    child_attrs: Incomplete
    def __init__(self, pos, **kwargs) -> None: ...
    def analyse_declarations(self, env) -> None: ...
    def generate_function_body(self, env, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...

class AsyncDefNode(GeneratorDefNode):
    gen_type_name: str
    is_coroutine: bool

class IterableAsyncDefNode(AsyncDefNode):
    gen_type_name: str
    is_iterable_coroutine: bool

class AsyncGenNode(AsyncDefNode):
    gen_type_name: str
    is_asyncgen: bool

class GeneratorBodyDefNode(DefNode):
    is_generator_body: bool
    is_inlined: bool
    is_async_gen_body: bool
    inlined_comprehension_type: Incomplete
    def __init__(self, pos: Incomplete | None = None, name: Incomplete | None = None, body: Incomplete | None = None, is_async_gen_body: bool = False) -> None: ...
    entry: Incomplete
    def declare_generator_body(self, env) -> None: ...
    def analyse_declarations(self, env) -> None: ...
    def generate_function_header(self, code, proto: bool = False) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...

class OverrideCheckNode(StatNode):
    child_attrs: Incomplete
    body: Incomplete
    args: Incomplete
    func_node: Incomplete
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class ClassDefNode(StatNode, BlockNode): ...

class PyClassDefNode(ClassDefNode):
    child_attrs: Incomplete
    decorators: Incomplete
    class_result: Incomplete
    is_py3_style_class: bool
    metaclass: Incomplete
    mkw: Incomplete
    doc_node: Incomplete
    orig_bases: Incomplete
    name: Incomplete
    doc: Incomplete
    body: Incomplete
    bases: Incomplete
    dict: Incomplete
    classobj: Incomplete
    target: Incomplete
    class_cell: Incomplete
    def __init__(self, pos, name, bases, doc, body, decorators: Incomplete | None = None, keyword_args: Incomplete | None = None, force_py3_semantics: bool = False) -> None: ...
    def as_cclass(self):
        """
        Return this node as if it were declared as an extension class
        """
    def create_scope(self, env): ...
    def analyse_declarations(self, env) -> None: ...
    update_bases_functype: Incomplete
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...

class CClassDefNode(ClassDefNode):
    child_attrs: Incomplete
    buffer_defaults_node: Incomplete
    buffer_defaults_pos: Incomplete
    typedef_flag: bool
    api: bool
    objstruct_name: Incomplete
    typeobj_name: Incomplete
    check_size: Incomplete
    decorators: Incomplete
    shadow: bool
    @property
    def punycode_class_name(self): ...
    def buffer_defaults(self, env): ...
    entry: Incomplete
    def declare(self, env) -> None: ...
    base_type: Incomplete
    module: Incomplete
    scope: Incomplete
    type_init_args: Incomplete
    def analyse_declarations(self, env): ...
    body: Incomplete
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    @staticmethod
    def generate_type_ready_code(entry, code, bases_tuple_cname: Incomplete | None = None, check_heap_type_bases: bool = False) -> None: ...
    def annotate(self, code) -> None: ...

class PropertyNode(StatNode):
    child_attrs: Incomplete
    entry: Incomplete
    def analyse_declarations(self, env) -> None: ...
    body: Incomplete
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...

class CPropertyNode(StatNode):
    """Definition of a C property, backed by a CFuncDefNode getter.
    """
    child_attrs: Incomplete
    is_cproperty: bool
    @property
    def cfunc(self): ...
    def analyse_declarations(self, env) -> None: ...
    body: Incomplete
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...

class GlobalNode(StatNode):
    child_attrs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class NonlocalNode(StatNode):
    child_attrs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class ExprStatNode(StatNode):
    child_attrs: Incomplete
    __class__: Incomplete
    def analyse_declarations(self, env) -> None: ...
    expr: Incomplete
    def analyse_expressions(self, env): ...
    def nogil_check(self, env) -> None: ...
    gil_message: str
    def generate_execution_code(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class AssignmentNode(StatNode):
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class SingleAssignmentNode(AssignmentNode):
    child_attrs: Incomplete
    first: bool
    is_overloaded_assignment: bool
    is_assignment_expression: bool
    declaration_only: bool
    rhs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    lhs: Incomplete
    exception_check: Incomplete
    exception_value: Incomplete
    def analyse_types(self, env, use_temp: int = 0): ...
    def unroll(self, node, target_size, env): ...
    def unroll_assignments(self, refs, check_node, lhs_list, rhs_list, env): ...
    def unroll_rhs(self, env): ...
    def unroll_lhs(self, env): ...
    def generate_rhs_evaluation_code(self, code) -> None: ...
    def generate_assignment_code(self, code, overloaded_assignment: bool = False) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class CascadedAssignmentNode(AssignmentNode):
    child_attrs: Incomplete
    cloned_values: Incomplete
    coerced_values: Incomplete
    assignment_overloads: Incomplete
    def analyse_declarations(self, env) -> None: ...
    rhs: Incomplete
    def analyse_types(self, env, use_temp: int = 0): ...
    def generate_rhs_evaluation_code(self, code) -> None: ...
    def generate_assignment_code(self, code, overloaded_assignment: bool = False) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class ParallelAssignmentNode(AssignmentNode):
    child_attrs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    stats: Incomplete
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class InPlaceAssignmentNode(AssignmentNode):
    child_attrs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    rhs: Incomplete
    lhs: Incomplete
    def analyse_types(self, env): ...
    def generate_execution_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...
    def create_binop_node(self): ...

class PrintStatNode(StatNode):
    child_attrs: Incomplete
    stream: Incomplete
    arg_tuple: Incomplete
    def analyse_expressions(self, env): ...
    nogil_check: Incomplete
    gil_message: str
    def generate_execution_code(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class ExecStatNode(StatNode):
    child_attrs: Incomplete
    def analyse_expressions(self, env): ...
    nogil_check: Incomplete
    gil_message: str
    def generate_execution_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...

class DelStatNode(StatNode):
    child_attrs: Incomplete
    ignore_nonexisting: bool
    def analyse_declarations(self, env) -> None: ...
    def analyse_expressions(self, env): ...
    def nogil_check(self, env) -> None: ...
    gil_message: str
    def generate_execution_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...

class PassStatNode(StatNode):
    child_attrs: Incomplete
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class IndirectionNode(StatListNode):
    """
    This adds an indirection so that the node can be shared and a subtree can
    be removed at any time by clearing self.stats.
    """
    def __init__(self, stats) -> None: ...

class BreakStatNode(StatNode):
    child_attrs: Incomplete
    is_terminator: bool
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class ContinueStatNode(StatNode):
    child_attrs: Incomplete
    is_terminator: bool
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class ReturnStatNode(StatNode):
    child_attrs: Incomplete
    is_terminator: bool
    in_generator: bool
    in_async_gen: bool
    in_parallel: bool
    return_type: Incomplete
    value: Incomplete
    def analyse_expressions(self, env): ...
    def nogil_check(self, env) -> None: ...
    gil_message: str
    def generate_execution_code(self, code) -> None: ...
    def put_return(self, code, value) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class RaiseStatNode(StatNode):
    child_attrs: Incomplete
    is_terminator: bool
    builtin_exc_name: Incomplete
    wrap_tuple_value: bool
    in_try_block: bool
    exc_type: Incomplete
    exc_value: Incomplete
    exc_tb: Incomplete
    cause: Incomplete
    def analyse_expressions(self, env): ...
    nogil_check: Incomplete
    gil_message: str
    def generate_execution_code(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class ReraiseStatNode(StatNode):
    child_attrs: Incomplete
    is_terminator: bool
    def analyse_expressions(self, env): ...
    nogil_check: Incomplete
    gil_message: str
    def generate_execution_code(self, code) -> None: ...

class AssertStatNode(StatNode):
    child_attrs: Incomplete
    exception: Incomplete
    def analyse_declarations(self, env) -> None: ...
    condition: Incomplete
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class IfStatNode(StatNode):
    child_attrs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    if_clauses: Incomplete
    else_clause: Incomplete
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class IfClauseNode(Node):
    child_attrs: Incomplete
    branch_hint: Incomplete
    def analyse_declarations(self, env) -> None: ...
    condition: Incomplete
    body: Incomplete
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code, end_label, is_last) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class SwitchCaseNode(StatNode):
    child_attrs: Incomplete
    def generate_condition_evaluation_code(self, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class SwitchStatNode(StatNode):
    child_attrs: Incomplete
    def generate_execution_code(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class LoopNode: ...

class WhileStatNode(LoopNode, StatNode):
    child_attrs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    condition: Incomplete
    body: Incomplete
    else_clause: Incomplete
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class DictIterationNextNode(Node):
    child_attrs: Incomplete
    coerced_key_var: Incomplete
    key_ref: Incomplete
    coerced_value_var: Incomplete
    value_ref: Incomplete
    coerced_tuple_var: Incomplete
    tuple_ref: Incomplete
    def __init__(self, dict_obj, expected_size, pos_index_var, key_target, value_target, tuple_target, is_dict_flag) -> None: ...
    dict_obj: Incomplete
    expected_size: Incomplete
    pos_index_var: Incomplete
    key_target: Incomplete
    value_target: Incomplete
    tuple_target: Incomplete
    is_dict_flag: Incomplete
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...

class SetIterationNextNode(Node):
    child_attrs: Incomplete
    coerced_value_var: Incomplete
    value_ref: Incomplete
    def __init__(self, set_obj, expected_size, pos_index_var, value_target, is_set_flag) -> None: ...
    set_obj: Incomplete
    expected_size: Incomplete
    pos_index_var: Incomplete
    value_target: Incomplete
    is_set_flag: Incomplete
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def generate_execution_code(self, code) -> None: ...

def ForStatNode(pos, **kw): ...

class _ForInStatNode(LoopNode, StatNode):
    child_attrs: Incomplete
    item: Incomplete
    is_async: bool
    def analyse_declarations(self, env) -> None: ...
    target: Incomplete
    iterator: Incomplete
    body: Incomplete
    else_clause: Incomplete
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class ForInStatNode(_ForInStatNode):
    is_async: bool

class AsyncForStatNode(_ForInStatNode):
    is_async: bool
    def __init__(self, pos, **kw) -> None: ...

class ForFromStatNode(LoopNode, StatNode):
    child_attrs: Incomplete
    is_py_target: bool
    loopvar_node: Incomplete
    py_loopvar_node: Incomplete
    from_range: bool
    gil_message: str
    def nogil_check(self, env) -> None: ...
    def analyse_declarations(self, env) -> None: ...
    target: Incomplete
    bound1: Incomplete
    bound2: Incomplete
    step: Incomplete
    body: Incomplete
    else_clause: Incomplete
    def analyse_expressions(self, env): ...
    def set_up_loop(self, env) -> None: ...
    def generate_execution_code(self, code) -> None: ...
    relation_table: Incomplete
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class WithStatNode(StatNode):
    """
    Represents a Python with statement.

    Implemented by the WithTransform as follows:

        MGR = EXPR
        EXIT = MGR.__exit__
        VALUE = MGR.__enter__()
        EXC = True
        try:
            try:
                TARGET = VALUE  # optional
                BODY
            except:
                EXC = False
                if not EXIT(*EXCINFO):
                    raise
        finally:
            if EXC:
                EXIT(None, None, None)
            MGR = EXIT = VALUE = None
    """
    child_attrs: Incomplete
    enter_call: Incomplete
    target_temp: Incomplete
    def analyse_declarations(self, env) -> None: ...
    manager: Incomplete
    body: Incomplete
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None: ...
    exit_var: Incomplete
    def generate_execution_code(self, code) -> None: ...

class WithTargetAssignmentStatNode(AssignmentNode):
    child_attrs: Incomplete
    with_node: Incomplete
    rhs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    lhs: Incomplete
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...
    def annotate(self, code) -> None: ...

class TryExceptStatNode(StatNode):
    child_attrs: Incomplete
    in_generator: bool
    def analyse_declarations(self, env) -> None: ...
    body: Incomplete
    has_default_clause: Incomplete
    else_clause: Incomplete
    def analyse_expressions(self, env): ...
    nogil_check: Incomplete
    gil_message: str
    def generate_execution_code(self, code) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class ExceptClauseNode(Node):
    child_attrs: Incomplete
    exc_value: Incomplete
    excinfo_target: Incomplete
    is_except_as: bool
    def analyse_declarations(self, env) -> None: ...
    function_name: Incomplete
    target: Incomplete
    body: Incomplete
    def analyse_expressions(self, env): ...
    def generate_handling_code(self, code, end_label) -> None: ...
    def generate_function_definitions(self, env, code) -> None: ...
    def annotate(self, code) -> None: ...

class TryFinallyStatNode(StatNode):
    child_attrs: Incomplete
    preserve_exception: int
    handle_error_case: bool
    func_return_type: Incomplete
    finally_except_clause: Incomplete
    is_try_finally_in_nogil: bool
    in_generator: bool
    @staticmethod
    def create_analysed(pos, env, body, finally_clause): ...
    def analyse_declarations(self, env) -> None: ...
    body: Incomplete
    finally_clause: Incomplete
    def analyse_expressions(self, env): ...
    nogil_check: Incomplete
    gil_message: str
    def generate_execution_code(self, code): ...
    def generate_function_definitions(self, env, code) -> None: ...
    def put_error_catcher(self, code, temps_to_clean_up, exc_vars, exc_lineno_cnames: Incomplete | None = None, exc_filename_cname: Incomplete | None = None) -> None: ...
    def put_error_uncatcher(self, code, exc_vars, exc_lineno_cnames: Incomplete | None = None, exc_filename_cname: Incomplete | None = None) -> None: ...
    def put_error_cleaner(self, code, exc_vars) -> None: ...
    def annotate(self, code) -> None: ...

class NogilTryFinallyStatNode(TryFinallyStatNode):
    """
    A try/finally statement that may be used in nogil code sections.
    """
    preserve_exception: bool
    nogil_check: Incomplete

class GILStatNode(NogilTryFinallyStatNode):
    child_attrs: Incomplete
    state_temp: Incomplete
    scope_gil_state_known: bool
    state: Incomplete
    condition: Incomplete
    def __init__(self, pos, state, body, condition: Incomplete | None = None) -> None: ...
    def create_state_temp_if_needed(self, pos, state, body) -> None: ...
    def analyse_declarations(self, env): ...
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class GILExitNode(StatNode):
    """
    Used as the 'finally' block in a GILStatNode

    state   string   'gil' or 'nogil'
    #   scope_gil_state_known  bool  For nogil functions this can be False, since they can also be run with gil
    #                           set to False by GilCheck transform
    """
    child_attrs: Incomplete
    state_temp: Incomplete
    scope_gil_state_known: bool
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class EnsureGILNode(GILExitNode):
    """
    Ensure the GIL in nogil functions for cleanup before returning.
    """
    def generate_execution_code(self, code) -> None: ...

def cython_view_utility_code(): ...

utility_code_for_cimports: Incomplete
utility_code_for_imports: Incomplete

def cimport_numpy_check(node, code) -> None: ...

class CImportStatNode(StatNode):
    child_attrs: Incomplete
    is_absolute: bool
    def analyse_declarations(self, env) -> None: ...
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class FromCImportStatNode(StatNode):
    child_attrs: Incomplete
    module_name: Incomplete
    relative_level: Incomplete
    imported_names: Incomplete
    def analyse_declarations(self, env) -> None: ...
    def declaration_matches(self, entry, kind): ...
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class FromImportStatNode(StatNode):
    child_attrs: Incomplete
    import_star: int
    def analyse_declarations(self, env) -> None: ...
    module: Incomplete
    item: Incomplete
    interned_items: Incomplete
    def analyse_expressions(self, env): ...
    def generate_execution_code(self, code) -> None: ...

class ParallelNode(Node):
    """
    Base class for cython.parallel constructs.
    """
    nogil_check: Incomplete

class ParallelStatNode(StatNode, ParallelNode):
    '''
    Base class for \'with cython.parallel.parallel():\' and \'for i in prange():\'.

    assignments     { Entry(var) : (var.pos, inplace_operator_or_None) }
                    assignments to variables in this parallel section

    parent          parent ParallelStatNode or None
    is_parallel     indicates whether this node is OpenMP parallel
                    (true for #pragma omp parallel for and
                              #pragma omp parallel)

    is_parallel is true for:

        #pragma omp parallel
        #pragma omp parallel for

    sections, but NOT for

        #pragma omp for

    We need this to determine the sharing attributes.

    privatization_insertion_point   a code insertion point used to make temps
                                    private (esp. the "nsteps" temp)

    args         tuple          the arguments passed to the parallel construct
    kwargs       DictNode       the keyword arguments passed to the parallel
                                construct (replaced by its compile time value)
    '''
    child_attrs: Incomplete
    body: Incomplete
    is_prange: bool
    is_nested_prange: bool
    error_label_used: bool
    num_threads: Incomplete
    chunksize: Incomplete
    parallel_exc: Incomplete
    parallel_pos_info: Incomplete
    pos_info: Incomplete
    critical_section_counter: int
    assignments: Incomplete
    seen_closure_vars: Incomplete
    privates: Incomplete
    assigned_nodes: Incomplete
    def __init__(self, pos, **kwargs) -> None: ...
    kwargs: Incomplete
    def analyse_declarations(self, env) -> None: ...
    def analyse_expressions(self, env): ...
    def analyse_sharing_attributes(self, env) -> None:
        """
        Analyse the privates for this block and set them in self.privates.
        This should be called in a post-order fashion during the
        analyse_expressions phase
        """
    def propagate_var_privatization(self, entry, pos, op, lastprivate) -> None:
        """
        Propagate the sharing attributes of a variable. If the privatization is
        determined by a parent scope, done propagate further.

        If we are a prange, we propagate our sharing attributes outwards to
        other pranges. If we are a prange in parallel block and the parallel
        block does not determine the variable private, we propagate to the
        parent of the parent. Recursion stops at parallel blocks, as they have
        no concept of lastprivate or reduction.

        So the following cases propagate:

            sum is a reduction for all loops:

                for i in prange(n):
                    for j in prange(n):
                        for k in prange(n):
                            sum += i * j * k

            sum is a reduction for both loops, local_var is private to the
            parallel with block:

                for i in prange(n):
                    with parallel:
                        local_var = ... # private to the parallel
                        for j in prange(n):
                            sum += i * j

        Nested with parallel blocks are disallowed, because they wouldn't
        allow you to propagate lastprivates or reductions:

            #pragma omp parallel for lastprivate(i)
            for i in prange(n):

                sum = 0

                #pragma omp parallel private(j, sum)
                with parallel:

                    #pragma omp parallel
                    with parallel:

                        #pragma omp for lastprivate(j) reduction(+:sum)
                        for j in prange(n):
                            sum += i

                    # sum and j are well-defined here

                # sum and j are undefined here

            # sum and j are undefined here
        """
    def initialize_privates_to_nan(self, code, exclude: Incomplete | None = None) -> None: ...
    def evaluate_before_block(self, code, expr): ...
    def put_num_threads(self, code) -> None:
        """
        Write self.num_threads if set as the num_threads OpenMP directive
        """
    modified_entries: Incomplete
    def declare_closure_privates(self, code) -> None:
        """
        If a variable is in a scope object, we need to allocate a temp and
        assign the value from the temp to the variable in the scope object
        after the parallel section. This kind of copying should be done only
        in the outermost parallel section.
        """
    def release_closure_privates(self, code) -> None:
        """
        Release any temps used for variables in scope objects. As this is the
        outermost parallel block, we don't need to delete the cnames from
        self.seen_closure_vars.
        """
    privatization_insertion_point: Incomplete
    temps: Incomplete
    def privatize_temps(self, code, exclude_temps=()) -> None:
        """
        Make any used temporaries private. Before the relevant code block
        code.start_collecting_temps() should have been called.
        """
    def cleanup_temps(self, code) -> None: ...
    old_loop_labels: Incomplete
    old_error_label: Incomplete
    old_return_label: Incomplete
    begin_of_parallel_control_block_point: Incomplete
    begin_of_parallel_control_block_point_after_decls: Incomplete
    def setup_parallel_control_flow_block(self, code) -> None:
        """
        Sets up a block that surrounds the parallel block to determine
        how the parallel section was exited. Any kind of return is
        trapped (break, continue, return, exceptions). This is the idea:

        {
            int why = 0;

            #pragma omp parallel
            {
                return # -> goto new_return_label;
                goto end_parallel;

            new_return_label:
                why = 3;
                goto end_parallel;

            end_parallel:;
                #pragma omp flush(why) # we need to flush for every iteration
            }

            if (why == 3)
                goto old_return_label;
        }
        """
    begin_of_parallel_block: Incomplete
    def begin_parallel_block(self, code) -> None:
        """
        Each OpenMP thread in a parallel section that contains a with gil block
        must have the thread-state initialized. The call to
        PyGILState_Release() then deallocates our threadstate. If we wouldn't
        do this, each with gil block would allocate and deallocate one, thereby
        losing exception information before it can be saved before leaving the
        parallel section.
        """
    def end_parallel_block(self, code) -> None:
        """
        To ensure all OpenMP threads have thread states, we ensure the GIL
        in each thread (which creates a thread state if it doesn't exist),
        after which we release the GIL.
        On exit, reacquire the GIL and release the thread state.

        If compiled without OpenMP support (at the C level), then we still have
        to acquire the GIL to decref any object temporaries.
        """
    any_label_used: bool
    breaking_label_used: bool
    parallel_private_temps: Incomplete
    def trap_parallel_exit(self, code, should_flush: bool = False) -> None:
        """
        Trap any kind of return inside a parallel construct. 'should_flush'
        indicates whether the variable should be flushed, which is needed by
        prange to skip the loop. It also indicates whether we need to register
        a continue (we need this for parallel blocks, but not for prange
        loops, as it is a direct jump there).

        It uses the same mechanism as try/finally:
            1 continue
            2 break
            3 return
            4 error
        """
    def save_parallel_vars(self, code) -> None:
        """
        The following shenanigans are instated when we break, return or
        propagate errors from a prange. In this case we cannot rely on
        lastprivate() to do its job, as no iterations may have executed yet
        in the last thread, leaving the values undefined. It is most likely
        that the breaking thread has well-defined values of the lastprivate
        variables, so we keep those values.
        """
    def fetch_parallel_exception(self, code) -> None:
        """
        As each OpenMP thread may raise an exception, we need to fetch that
        exception from the threadstate and save it for after the parallel
        section where it can be re-raised in the master thread.

        Although it would seem that __pyx_filename, __pyx_lineno and
        __pyx_clineno are only assigned to under exception conditions (i.e.,
        when we have the GIL), and thus should be allowed to be shared without
        any race condition, they are in fact subject to the same race
        conditions that they were previously when they were global variables
        and functions were allowed to release the GIL:

            thread A                thread B
                acquire
                set lineno
                release
                                        acquire
                                        set lineno
                                        release
                acquire
                fetch exception
                release
                                        skip the fetch

                deallocate threadstate  deallocate threadstate
        """
    def restore_parallel_exception(self, code) -> None:
        """Re-raise a parallel exception"""
    def restore_labels(self, code) -> None:
        """
        Restore all old labels. Call this before the 'else' clause to for
        loops and always before ending the parallel control flow block.
        """
    def end_parallel_control_flow_block(self, code, break_: bool = False, continue_: bool = False, return_: bool = False) -> None:
        """
        This ends the parallel control flow block and based on how the parallel
        section was exited, takes the corresponding action. The break_ and
        continue_ parameters indicate whether these should be propagated
        outwards:

            for i in prange(...):
                with cython.parallel.parallel():
                    continue

        Here break should be trapped in the parallel block, and propagated to
        the for loop.
        """
    buggy_platform_macro_condition: str
    have_expect_condition: str
    redef_condition: Incomplete
    def undef_builtin_expect_apple_gcc_bug(self, code) -> None:
        """
        A bug on OS X Lion disallows __builtin_expect macros. This code avoids them
        """
    def redef_builtin_expect_apple_gcc_bug(self, code) -> None: ...

class ParallelWithBlockNode(ParallelStatNode):
    """
    This node represents a 'with cython.parallel.parallel():' block
    """
    valid_keyword_arguments: Incomplete
    num_threads: Incomplete
    def analyse_declarations(self, env) -> None: ...
    privatization_insertion_point: Incomplete
    def generate_execution_code(self, code) -> None: ...

class ParallelRangeNode(ParallelStatNode):
    """
    This node represents a 'for i in cython.parallel.prange():' construct.

    target       NameNode       the target iteration variable
    else_clause  Node or None   the else clause of this loop
    """
    child_attrs: Incomplete
    body: Incomplete
    target: Incomplete
    else_clause: Incomplete
    args: Incomplete
    start: Incomplete
    stop: Incomplete
    step: Incomplete
    is_prange: bool
    nogil: Incomplete
    schedule: Incomplete
    valid_keyword_arguments: Incomplete
    iterator: Incomplete
    def __init__(self, pos, **kwds) -> None: ...
    def analyse_declarations(self, env) -> None: ...
    index_type: Incomplete
    names: Incomplete
    def analyse_expressions(self, env): ...
    def nogil_check(self, env) -> None: ...
    def generate_execution_code(self, code) -> None:
        """
        Generate code in the following steps

            1)  copy any closure variables determined thread-private
                into temporaries

            2)  allocate temps for start, stop and step

            3)  generate a loop that calculates the total number of steps,
                which then computes the target iteration variable for every step:

                    for i in prange(start, stop, step):
                        ...

                becomes

                    nsteps = (stop - start) / step;
                    i = start;

                    #pragma omp parallel for lastprivate(i)
                    for (temp = 0; temp < nsteps; temp++) {
                        i = start + step * temp;
                        ...
                    }

                Note that accumulation of 'i' would have a data dependency
                between iterations.

                Also, you can't do this

                    for (i = start; i < stop; i += step)
                        ...

                as the '<' operator should become '>' for descending loops.
                'for i from x < i < y:' does not suffer from this problem
                as the relational operator is known at compile time!

            4) release our temps and write back any private closure variables
        """
    privatization_insertion_point: Incomplete
    def generate_loop(self, code, fmt_dict) -> None: ...

class CnameDecoratorNode(StatNode):
    """
    This node is for the cname decorator in CythonUtilityCode:

        @cname('the_cname')
        cdef func(...):
            ...

    In case of a cdef class the cname specifies the objstruct_cname.

    node        the node to which the cname decorator is applied
    cname       the cname the node should get
    """
    child_attrs: Incomplete
    is_function: Incomplete
    def analyse_declarations(self, env) -> None: ...
    def mangle(self, cname): ...
    node: Incomplete
    def analyse_expressions(self, env): ...
    def generate_function_definitions(self, env, code) -> None:
        """Ensure a prototype for every @cname method in the right place"""
    def generate_execution_code(self, code) -> None: ...

branch_prediction_macros: str
printing_utility_code: Incomplete
printing_one_utility_code: Incomplete
restore_exception_utility_code: Incomplete
raise_utility_code: Incomplete
get_exception_utility_code: Incomplete
swap_exception_utility_code: Incomplete
reset_exception_utility_code: Incomplete
traceback_utility_code: Incomplete
get_exception_tuple_utility_code: Incomplete
