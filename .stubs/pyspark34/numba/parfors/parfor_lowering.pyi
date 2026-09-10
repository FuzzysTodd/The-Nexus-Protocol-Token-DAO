from numba.core import cgutils as cgutils, compiler as compiler, config as config, ir as ir, lowering as lowering, sigutils as sigutils, types as types
from numba.core.errors import CompilerError as CompilerError, InternalError as InternalError, NotDefinedError as NotDefinedError, NumbaParallelSafetyWarning as NumbaParallelSafetyWarning
from numba.core.ir_utils import add_offset_to_labels as add_offset_to_labels, find_max_label as find_max_label, fixup_var_define_in_scope as fixup_var_define_in_scope, get_call_table as get_call_table, get_definition as get_definition, get_global_func_typ as get_global_func_typ, get_name_var_table as get_name_var_table, get_np_ufunc_typ as get_np_ufunc_typ, get_unused_var_name as get_unused_var_name, guard as guard, is_const_call as is_const_call, is_pure as is_pure, legalize_names as legalize_names, remove_dels as remove_dels, rename_labels as rename_labels, replace_var_names as replace_var_names, transfer_scope as transfer_scope, visit_vars_inner as visit_vars_inner
from numba.core.typing import signature as signature
from numba.parfors import parfor as parfor
from numba.parfors.parfor import ensure_parallel_support as ensure_parallel_support
from numba.parfors.parfor_lowering_utils import ParforLoweringBuilder as ParforLoweringBuilder

class ParforLower(lowering.Lower):
    """This is a custom lowering class that extends standard lowering so as
    to accommodate parfor.Parfor nodes."""
    def lower_inst(self, inst) -> None: ...

class ParforsUnexpectedReduceNodeError(InternalError):
    def __init__(self, inst) -> None: ...

def wrap_loop_body(loop_body): ...
def unwrap_loop_body(loop_body) -> None: ...
def add_to_def_once_sets(a_def, def_once, def_more) -> None:
    """If the variable is already defined more than once, do nothing.
       Else if defined exactly once previously then transition this
       variable to the defined more than once set (remove it from
       def_once set and add to def_more set).
       Else this must be the first time we've seen this variable defined
       so add to def_once set.
    """
def compute_def_once_block(block, def_once, def_more, getattr_taken, typemap, module_assigns) -> None:
    """Effect changes to the set of variables defined once or more than once
       for a single block.
       block - the block to process
       def_once - set of variable names known to be defined exactly once
       def_more - set of variable names known to be defined more than once
       getattr_taken - dict mapping variable name to tuple of object and attribute taken
       module_assigns - dict mapping variable name to the Global that they came from
    """
def compute_def_once_internal(loop_body, def_once, def_more, getattr_taken, typemap, module_assigns) -> None:
    """Compute the set of variables defined exactly once in the given set of blocks
       and use the given sets for storing which variables are defined once, more than
       once and which have had a getattr call on them.
    """
def compute_def_once(loop_body, typemap):
    """Compute the set of variables defined exactly once in the given set of blocks.
    """
def find_vars(var, varset): ...
def find_setitems_block(setitems, itemsset, block, typemap) -> None: ...
def find_setitems_body(setitems, itemsset, loop_body, typemap) -> None:
    """
      Find the arrays that are written into (goes into setitems) and the
      mutable objects (mostly arrays) that are written into other arrays
      (goes into itemsset).
    """
def empty_container_allocator_hoist(inst, dep_on_param, call_table, hoisted, not_hoisted, typemap, stored_arrays): ...
def hoist(parfor_params, loop_body, typemap, wrapped_blocks): ...
def redtyp_is_scalar(redtype): ...
def redtyp_to_redarraytype(redtyp):
    """Go from a reducation variable type to a reduction array type used to hold
       per-worker results.
    """
def redarraytype_to_sig(redarraytyp):
    """Given a reduction array type, find the type of the reduction argument to the gufunc.
    """
def legalize_names_with_typemap(names, typemap):
    """ We use ir_utils.legalize_names to replace internal IR variable names
        containing illegal characters (e.g. period) with a legal character
        (underscore) so as to create legal variable names.
        The original variable names are in the typemap so we also
        need to add the legalized name to the typemap as well.
    """
def to_scalar_from_0d(x): ...
def replace_var_with_array_in_block(vars, block, typemap, calltypes): ...
def replace_var_with_array_internal(vars, loop_body, typemap, calltypes) -> None: ...
def replace_var_with_array(vars, loop_body, typemap, calltypes) -> None: ...
def call_parallel_gufunc(lowerer, cres, gu_signature, outer_sig, expr_args, expr_arg_types, loop_ranges, redvars, reddict, redarrdict, init_block, index_var_typ, races, exp_name_to_tuple_var):
    """
    Adds the call to the gufunc function from the main function.
    """
