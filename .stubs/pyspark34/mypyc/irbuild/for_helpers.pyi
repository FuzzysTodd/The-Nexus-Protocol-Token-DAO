from _typeshed import Incomplete
from mypy.nodes import Expression as Expression, GeneratorExpr as GeneratorExpr, Lvalue as Lvalue, RefExpr
from mypyc.ir.ops import BasicBlock as BasicBlock, Branch as Branch, IntOp as IntOp, Integer as Integer, LoadAddress as LoadAddress, LoadMem as LoadMem, Register as Register, TupleGet as TupleGet, TupleSet as TupleSet, Value as Value
from mypyc.ir.rtypes import RTuple as RTuple, RType as RType, bool_rprimitive as bool_rprimitive, int_rprimitive as int_rprimitive, is_dict_rprimitive as is_dict_rprimitive, is_fixed_width_rtype as is_fixed_width_rtype, is_list_rprimitive as is_list_rprimitive, is_sequence_rprimitive as is_sequence_rprimitive, is_short_int_rprimitive as is_short_int_rprimitive, is_str_rprimitive as is_str_rprimitive, is_tuple_rprimitive as is_tuple_rprimitive, pointer_rprimitive as pointer_rprimitive, short_int_rprimitive as short_int_rprimitive
from mypyc.irbuild.builder import IRBuilder as IRBuilder
from mypyc.irbuild.targets import AssignmentTarget as AssignmentTarget, AssignmentTargetTuple as AssignmentTargetTuple
from mypyc.primitives.dict_ops import dict_check_size_op as dict_check_size_op, dict_item_iter_op as dict_item_iter_op, dict_key_iter_op as dict_key_iter_op, dict_next_item_op as dict_next_item_op, dict_next_key_op as dict_next_key_op, dict_next_value_op as dict_next_value_op, dict_value_iter_op as dict_value_iter_op
from mypyc.primitives.exc_ops import no_err_occurred_op as no_err_occurred_op
from mypyc.primitives.generic_ops import aiter_op as aiter_op, anext_op as anext_op, iter_op as iter_op, next_op as next_op
from mypyc.primitives.list_ops import list_append_op as list_append_op, list_get_item_unsafe_op as list_get_item_unsafe_op, new_list_set_item_op as new_list_set_item_op
from mypyc.primitives.misc_ops import stop_async_iteration_op as stop_async_iteration_op
from mypyc.primitives.registry import CFunctionDescription as CFunctionDescription
from mypyc.primitives.set_ops import set_add_op as set_add_op
from typing import Callable, ClassVar

GenFunc = Callable[[], None]

def for_loop_helper(builder: IRBuilder, index: Lvalue, expr: Expression, body_insts: GenFunc, else_insts: GenFunc | None, is_async: bool, line: int) -> None:
    """Generate IR for a loop.

    Args:
        index: the loop index Lvalue
        expr: the expression to iterate over
        body_insts: a function that generates the body of the loop
        else_insts: a function that generates the else block instructions
    """
def for_loop_helper_with_index(builder: IRBuilder, index: Lvalue, expr: Expression, expr_reg: Value, body_insts: Callable[[Value], None], line: int) -> None:
    """Generate IR for a sequence iteration.

    This function only works for sequence type. Compared to for_loop_helper,
    it would feed iteration index to body_insts.

    Args:
        index: the loop index Lvalue
        expr: the expression to iterate over
        body_insts: a function that generates the body of the loop.
                    It needs a index as parameter.
    """
def sequence_from_generator_preallocate_helper(builder: IRBuilder, gen: GeneratorExpr, empty_op_llbuilder: Callable[[Value, int], Value], set_item_op: CFunctionDescription) -> Value | None:
    """Generate a new tuple or list from a simple generator expression.

    Currently we only optimize for simplest generator expression, which means that
    there is no condition list in the generator and only one original sequence with
    one index is allowed.

    e.g.  (1) tuple(f(x) for x in a_list/a_tuple)
          (2) list(f(x) for x in a_list/a_tuple)
          (3) [f(x) for x in a_list/a_tuple]
    RTuple as an original sequence is not supported yet.

    Args:
        empty_op_llbuilder: A function that can generate an empty sequence op when
            passed in length. See `new_list_op_with_length` and `new_tuple_op_with_length`
            for detailed implementation.
        set_item_op: A primitive that can modify an arbitrary position of a sequence.
            The op should have three arguments:
                - Self
                - Target position
                - New Value
            See `new_list_set_item_op` and `new_tuple_set_item_op` for detailed
            implementation.
    """
def translate_list_comprehension(builder: IRBuilder, gen: GeneratorExpr) -> Value: ...
def translate_set_comprehension(builder: IRBuilder, gen: GeneratorExpr) -> Value: ...
def comprehension_helper(builder: IRBuilder, loop_params: list[tuple[Lvalue, Expression, list[Expression], bool]], gen_inner_stmts: Callable[[], None], line: int) -> None:
    '''Helper function for list comprehensions.

    Args:
        loop_params: a list of (index, expr, [conditions]) tuples defining nested loops:
            - "index" is the Lvalue indexing that loop;
            - "expr" is the expression for the object to be iterated over;
            - "conditions" is a list of conditions, evaluated in order with short-circuiting,
                that must all be true for the loop body to be executed
        gen_inner_stmts: function to generate the IR for the body of the innermost loop
    '''
def is_range_ref(expr: RefExpr) -> bool: ...
def make_for_loop_generator(builder: IRBuilder, index: Lvalue, expr: Expression, body_block: BasicBlock, loop_exit: BasicBlock, line: int, is_async: bool = False, nested: bool = False) -> ForGenerator:
    '''Return helper object for generating a for loop over an iterable.

    If "nested" is True, this is a nested iterator such as "e" in "enumerate(e)".
    '''

class ForGenerator:
    """Abstract base class for generating for loops."""
    builder: Incomplete
    index: Incomplete
    body_block: Incomplete
    line: Incomplete
    loop_exit: Incomplete
    def __init__(self, builder: IRBuilder, index: Lvalue, body_block: BasicBlock, loop_exit: BasicBlock, line: int, nested: bool) -> None: ...
    def need_cleanup(self) -> bool:
        """If this returns true, we need post-loop cleanup."""
    def add_cleanup(self, exit_block: BasicBlock) -> None:
        """Add post-loop cleanup, if needed."""
    def gen_condition(self) -> None:
        """Generate check for loop exit (e.g. exhaustion of iteration)."""
    def begin_body(self) -> None:
        """Generate ops at the beginning of the body (if needed)."""
    def gen_step(self) -> None:
        """Generate stepping to the next item (if needed)."""
    def gen_cleanup(self) -> None:
        """Generate post-loop cleanup (if needed)."""
    def load_len(self, expr: Value | AssignmentTarget) -> Value:
        """A helper to get collection length, used by several subclasses."""

class ForIterable(ForGenerator):
    """Generate IR for a for loop over an arbitrary iterable (the general case)."""
    def need_cleanup(self) -> bool: ...
    iter_target: Incomplete
    target_type: Incomplete
    def init(self, expr_reg: Value, target_type: RType) -> None: ...
    next_reg: Incomplete
    def gen_condition(self) -> None: ...
    def begin_body(self) -> None: ...
    def gen_step(self) -> None: ...
    def gen_cleanup(self) -> None: ...

class ForAsyncIterable(ForGenerator):
    """Generate IR for an async for loop."""
    iter_target: Incomplete
    target_type: Incomplete
    stop_reg: Incomplete
    def init(self, expr_reg: Value, target_type: RType) -> None: ...
    next_reg: Incomplete
    def gen_condition(self) -> None: ...
    def begin_body(self) -> None: ...
    def gen_step(self) -> None: ...

def unsafe_index(builder: IRBuilder, target: Value, index: Value, line: int) -> Value:
    """Emit a potentially unsafe index into a target."""

class ForSequence(ForGenerator):
    """Generate optimized IR for a for loop over a sequence.

    Supports iterating in both forward and reverse.
    """
    reverse: Incomplete
    expr_target: Incomplete
    index_target: Incomplete
    target_type: Incomplete
    def init(self, expr_reg: Value, target_type: RType, reverse: bool) -> None: ...
    def gen_condition(self) -> None: ...
    def begin_body(self) -> None: ...
    def gen_step(self) -> None: ...

class ForDictionaryCommon(ForGenerator):
    """Generate optimized IR for a for loop over dictionary keys/values.

    The logic is pretty straightforward, we use PyDict_Next() API wrapped in
    a tuple, so that we can modify only a single register. The layout of the tuple:
      * f0: are there more items (bool)
      * f1: current offset (int)
      * f2: next key (object)
      * f3: next value (object)
    For more info see https://docs.python.org/3/c-api/dict.html#c.PyDict_Next.

    Note that for subclasses we fall back to generic PyObject_GetIter() logic,
    since they may override some iteration methods in subtly incompatible manner.
    The fallback logic is implemented in CPy.h via dynamic type check.
    """
    dict_next_op: ClassVar[CFunctionDescription]
    dict_iter_op: ClassVar[CFunctionDescription]
    def need_cleanup(self) -> bool: ...
    target_type: Incomplete
    expr_target: Incomplete
    offset_target: Incomplete
    size: Incomplete
    iter_target: Incomplete
    def init(self, expr_reg: Value, target_type: RType) -> None: ...
    next_tuple: Incomplete
    def gen_condition(self) -> None:
        """Get next key/value pair, set new offset, and check if we should continue."""
    def gen_step(self) -> None:
        """Check that dictionary didn't change size during iteration.

        Raise RuntimeError if it is not the case to match CPython behavior.
        """
    def gen_cleanup(self) -> None: ...

class ForDictionaryKeys(ForDictionaryCommon):
    """Generate optimized IR for a for loop over dictionary keys."""
    dict_next_op = dict_next_key_op
    dict_iter_op = dict_key_iter_op
    def begin_body(self) -> None: ...

class ForDictionaryValues(ForDictionaryCommon):
    """Generate optimized IR for a for loop over dictionary values."""
    dict_next_op = dict_next_value_op
    dict_iter_op = dict_value_iter_op
    def begin_body(self) -> None: ...

class ForDictionaryItems(ForDictionaryCommon):
    """Generate optimized IR for a for loop over dictionary items."""
    dict_next_op = dict_next_item_op
    dict_iter_op = dict_item_iter_op
    def begin_body(self) -> None: ...

class ForRange(ForGenerator):
    """Generate optimized IR for a for loop over an integer range."""
    start_reg: Incomplete
    end_reg: Incomplete
    step: Incomplete
    end_target: Incomplete
    index_reg: Incomplete
    index_target: Incomplete
    def init(self, start_reg: Value, end_reg: Value, step: int) -> None: ...
    def gen_condition(self) -> None: ...
    def gen_step(self) -> None: ...

class ForInfiniteCounter(ForGenerator):
    """Generate optimized IR for a for loop counting from 0 to infinity."""
    index_reg: Incomplete
    index_target: Incomplete
    def init(self) -> None: ...
    def gen_step(self) -> None: ...

class ForEnumerate(ForGenerator):
    '''Generate optimized IR for a for loop of form "for i, x in enumerate(it)".'''
    def need_cleanup(self) -> bool: ...
    index_gen: Incomplete
    main_gen: Incomplete
    def init(self, index1: Lvalue, index2: Lvalue, expr: Expression) -> None: ...
    def gen_condition(self) -> None: ...
    def begin_body(self) -> None: ...
    def gen_step(self) -> None: ...
    def gen_cleanup(self) -> None: ...

class ForZip(ForGenerator):
    """Generate IR for a for loop of form `for x, ... in zip(a, ...)`."""
    def need_cleanup(self) -> bool: ...
    cond_blocks: Incomplete
    gens: Incomplete
    def init(self, indexes: list[Lvalue], exprs: list[Expression]) -> None: ...
    def gen_condition(self) -> None: ...
    def begin_body(self) -> None: ...
    def gen_step(self) -> None: ...
    def gen_cleanup(self) -> None: ...
