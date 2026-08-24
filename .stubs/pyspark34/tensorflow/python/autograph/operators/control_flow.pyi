from _typeshed import Incomplete
from tensorflow.python.autograph.operators import py_builtins as py_builtins, variables as variables
from tensorflow.python.autograph.utils import ag_logging as ag_logging, misc as misc, tensors as tensors, type_registry as type_registry
from tensorflow.python.framework import dtypes as dtypes, errors_impl as errors_impl, func_graph as func_graph, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util as control_flow_util, math_ops as math_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.types import distribute as distribute
from tensorflow.python.util import nest as nest, variable_utils as variable_utils

PYTHON_MAX_ITERATIONS: int
WARN_INEFFICIENT_UNROLL: bool
INEFFICIENT_UNROLL_MIN_ITERATIONS: int
INEFFICIENT_UNROLL_MIN_OPS: int
for_loop_registry: Incomplete

def verify_loop_init_vars(init_vars, symbol_names, first_iter_vars: Incomplete | None = None, extra_message: Incomplete | None = None) -> None:
    '''Ensures that all values in the state are valid to use in a TF loop.

  The init_vars may contain placeholder values derived from first_iter_vars.

  Args:
    init_vars: initial loop variables (as taken before entering the loop)
    symbol_names: corresponding names of the initial loop variables
    first_iter_vars: loop variables after one iteration of the loop
    extra_message: an extra string to append to the error message, in case of
      "undefined variable" errors (see variables.Undefined)
  '''
def verify_tf_loop_vars(init_vars, iter_entry_vars, iter_exit_vars, symbol_names, opts, check_shapes: bool = True) -> None:
    """Verifies loop variables for consistency."""
def verify_single_cond_var(name, body_var, orelse_var) -> None:
    """Verifies whether body_var and orelse_var are consistent."""
def for_stmt(iter_, extra_test, body, get_state, set_state, symbol_names, opts) -> None:
    """Functional form of a for statement.

  The loop operates on a state, which includes all symbols that are
  variant across loop iterations, excluding the variables local to the loop.

  For example, given the loop below that calculates the geometric and
  arithmetic means or some numbers:

  ```
    geo_mean = 1
    arith_mean = 0
    for i in range(n):
      a = numbers[i]
      geo_mean *= a
      arith_mean += a
  ```

  The state is represented by the variables named geo_mean and arith_mean. The
  `extra_test`, `body`, `get_state` and `set_state` functions must bind to the
  original `geo_mean` and `arith_mean` symbols, using `nonlocal`.

  The inputs and outputs of the callables representing the loop blocks are not
  explicit - instead, these functions must use nonlocal/global for side effects.
  The inputs and outputs are instead controlled by the set_state/get_state
  functions.

  Args:
    iter_: The entity being iterated over.
    extra_test: Callable with boolean return type. An additional loop condition.
    body: Callable representing the actual loop body.
    get_state: Additional callable which can capture additional state (such as
      the values of composite symbols). This is only useful when staging the
      loop.
    set_state: Additional callable which save values captured by get_state back
      into the Python environment. This is only useful when staging the loop.
    symbol_names: Tuple containing names of the loop variables returned by
      get_state.
    opts: Optional dict of extra loop parameters.
  """
def while_stmt(test, body, get_state, set_state, symbol_names, opts) -> None:
    """Functional form of a while statement.

  The loop operates on a so-called state, which includes all symbols that are
  variant across loop iterations. In what follows we refer to state as either
  a tuple of entities that represent an actual state, or a list of arguments
  of the corresponding types.

  The inputs and outputs of the callables representing the loop blocks are not
  explicit - instead, these functions must use nonlocal/global for side effects.
  The inputs and outputs are instead controlled by the set_state/get_state
  functions.

  Args:
    test: Callable with boolean return type. The loop condition.
    body: Callable representing the actual loop body.
    get_state: Additional callable which can capture additional state (such as
      the values of composite symbols). This is only useful when staging the
      loop.
    set_state: Additional callable which save values captured by get_state back
      into the Python environment. This is only useful when staging the loop.
    symbol_names: Tuple containing the names of all loop variables.
    opts: Optional dict of extra loop parameters.

  Returns:
    Tuple containing the final state.
  """

class _PythonLoopChecker:
    """Verifies Python loops for TF-specific limits."""
    iterations: int
    check_inefficient_unroll: Incomplete
    check_op_count_after_iteration: bool
    def __init__(self) -> None: ...
    ops_before_iteration: Incomplete
    def before_iteration(self) -> None:
        """Called before each iteration in a Python loop."""
    def after_iteration(self) -> None:
        """Called after each iteration in a Python loop."""

LEGAL_LOOP_TYPES: str

def if_stmt(cond, body, orelse, get_state, set_state, symbol_names, nouts) -> None:
    """Functional form of an if statement.

  The conditional operates on a state, which includes all symbols whose values
  are a function of the branch taken.

  For example, given the code below that calculates the abs function:

  ```
    x = 1
    if x > 0:
      x = -x
  ```

  The state is represented by the variable `x`. The `body, `orelse` and
  `set_state` functions must bind to the original `x` symbol, using `nonlocal`.

  The inputs and outputs of the callables representing the loop blocks are not
  explicit - instead, these functions must use nonlocal/global for side effects.
  The inputs and outputs are instead controlled by the set_state/get_state
  functions.

  Args:
    cond: Boolean.
    body: Callable representing the main block of the conditional.
    orelse: Callable representing the else block of the conditional.
    get_state: Function that returns a tuple containing the values of all
      composite symbols modified within the conditional. This allows access to
      state that branches may mutate through side effects. This function is not
      needed and should not be called when dispatching to code matching Python's
      default semantics. This is useful for checkpointing to avoid unintended
      side-effects when staging requires evaluating all code-paths.
    set_state: Function to set the values of all composite symbols modified
      within the conditional. This is the complement to get_state, used to
      restore checkpointed values. The single argument a tuple containing values
      for each composite symbol that may be modified in a branch of the
      conditional. The is usually the result of a call to get_state.
    symbol_names: Tuple containing basic loop var names.
    nouts: Number of variables output by the statement. Vars which are not
      outputs will not be passed through staged control flow such as tf.cond.
      This includes variables that are defined before the conditional, but are
      not used after it.
  """
