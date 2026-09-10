import dataclasses
import jax
import threading
import tokenize
from _typeshed import Incomplete
from collections.abc import Iterable, Sequence
from enum import Enum
from jax import config as config
from jax._src import core as core, dtypes as dtypes, effects as effects, tree_util as tree_util, util as util
from jax._src.interpreters import mlir as mlir
from jax._src.lax import lax as lax
from jax._src.numpy import lax_numpy as lax_numpy
from jax._src.typing import DimSize as DimSize, Shape as Shape
from jax.interpreters import xla as xla
from typing import Any

TfVal = Any
DimVarEnv: Incomplete
DType = Any

class InconclusiveDimensionOperation(core.InconclusiveDimensionOperation):
    """Raised when we cannot conclusively compute with symbolic dimensions."""
    def __init__(self, message: str) -> None: ...

class _ShapePolyThreadLocalState(threading.local):
    enable_shape_assertions: bool
    def __init__(self) -> None: ...

thread_local_state: Incomplete

class _DimAtom:
    """Represents an atom in a symbolic dimension expression.

  Atoms are either variables, or expressions of the form floordiv(E1, E2) or
  mod(E1, E2). Atoms are multiplied to form monomials (see _DimMon), and
  monomials are added to form symbolic expressions (see _DimExpr).

  Args:
    * var: if specified then the atom is a dimension variable. `operation`
      must be `None`.
    * operation: if specified then the atom is an operation applied to
      `operands`. One of `FLOORDIR` or `MOD` or `NON_NEGATIVE`. `var` must be `None`
    * operands: the operands to which the operation is applied.
  """
    FLOORDIV: str
    MOD: str
    NON_NEGATIVE: str
    var: Incomplete
    operation: Incomplete
    operands: Incomplete
    def __init__(self, *operands: _DimExpr, var: str | None = None, operation: str | None = None) -> None: ...
    @classmethod
    def from_var(cls, v: str) -> _DimAtom: ...
    def to_var(self) -> str | None: ...
    def get_vars(self) -> set[str]: ...
    @classmethod
    def from_operation(cls, operation: str, *operands: _DimExpr) -> _DimAtom: ...
    def __hash__(self): ...
    def __eq__(self, other: Any): ...
    def __lt__(self, other: _DimAtom):
        """
    Comparison to another atom in graded reverse lexicographic order.
    Used only for determining a sorting order, does not relate to the
    comparison of the values of the atom.
    """
    def bounds(self) -> tuple[float, float]:
        """Returns the lower and upper bounds, or -+ inf."""
    def evaluate(self, env: DimVarEnv): ...

class _DimMon(dict):
    """Represents a multiplication of atoms.

  The representation is a dictionary mapping _DimAtom to exponent.
  The exponents are integers >= 1.
  """
    def __hash__(self): ...
    @classmethod
    def from_var(cls, v: str) -> _DimMon: ...
    @classmethod
    def from_atom(clscls, a: _DimAtom, aexp: int): ...
    def to_var(self) -> str | None:
        '''Extract the variable name "x", from a monomial "x".
     Return None, if the monomial is not a single variable.'''
    def get_vars(self) -> set[str]: ...
    @classmethod
    def from_operation(cls, operation: str, *operands: _DimExpr) -> _DimMon: ...
    @property
    def degree(self): ...
    def __lt__(self, other: _DimMon):
        """
    Comparison to another monomial in graded reverse lexicographic order.
    Used only for determining a sorting order, does not relate to the
    comparison of the values of the monomial.
    """
    def mul(self, other: _DimMon) -> _DimMon:
        """
    Returns the product with another monomial. Example: (n^2*m) * n == n^3 * m.
    """
    def divide(self, divisor: _DimMon) -> _DimMon:
        """
    Divides by another monomial. Raises a InconclusiveDimensionOperation
    if the result is not a monomial.
    For example, (n^3 * m) // n == n^2*m, but n // m fails.
    """
    def bounds(self) -> tuple[float, float]:
        """Returns the lower and upper bounds, or -+inf."""
    def evaluate(self, env: DimVarEnv): ...

class _DimExpr:
    """Symbolic expression in terms of dimension variables.

  A dimension expression is an addition of products (_DimMon)
  of atoms (_DimAtom).

  We overload integer operations, but we do that soundly, raising
  :class:`InconclusiveDimensionOperation` when the result is not
  representable as a _DimExpr.

  The representation of a _DimExpr is as a dictionary mapping _DimMon to
  integer coefficients. The special monomial `_DimMon()` is mapped to the
  free integer coefficient of the expression.
  """
    __array_priority__: int
    def __init__(self, coeffs: dict[_DimMon, int]) -> None: ...
    def monomials(self) -> Iterable[tuple[_DimMon, int]]: ...
    @classmethod
    def normalize(cls, coeffs: dict[_DimMon, int]) -> DimSize:
        """The main constructor for _DimExpr.

    Ensures that the symbolic dimension is normalized, e.g.,
    it is represented as a Python int if it is known to be a constant.
    """
    @classmethod
    def normalize_floordiv_times_divisor(cls, coeffs: dict[_DimMon, int]) -> DimSize: ...
    @classmethod
    def from_monomial(cls, mon: _DimMon, exp: int): ...
    @classmethod
    def from_var(cls, v: str) -> _DimExpr: ...
    @classmethod
    def from_operation(cls, operation: str, *operands: _DimExpr) -> _DimExpr: ...
    def to_var(self) -> str | None:
        '''Extract the variable name "x", from a symbolic expression.'''
    def get_vars(self) -> set[str]:
        """The variables that appear in a symbolic dimension."""
    def eq(self, other: DimSize) -> bool: ...
    def inconclusive_comparison(self, operation: str, op: Any) -> Exception: ...
    def ge(self, other: DimSize) -> bool: ...
    def __hash__(self): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __neg__(self) -> _DimExpr: ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __pow__(self, power, modulo: Incomplete | None = None): ...
    def __floordiv__(self, divisor): ...
    def __rfloordiv__(self, other): ...
    def __truediv__(self, divisor): ...
    def __rtruediv__(self, dividend): ...
    def __mod__(self, divisor): ...
    def __rmod__(self, dividend): ...
    def __divmod__(self, divisor): ...
    def __rdivmod__(self, dividend): ...
    def __int__(self) -> int: ...
    __eq__ = eq
    def __ne__(self, other: DimSize) -> bool: ...
    __ge__ = ge
    def __le__(self, other: DimSize): ...
    def __gt__(self, other: DimSize): ...
    def __lt__(self, other: DimSize): ...
    def divmod(self, divisor: _DimExpr) -> tuple[DimSize, int]:
        """
    Floor division with remainder (divmod) generalized to polynomials.
    If the `divisor` is not a constant, the remainder must be 0.
    If the `divisor` is a constant, the remainder may be non 0, for consistency
    with integer divmod.

    :return: Quotient resulting from polynomial division and integer remainder.
    """
    def bounds(self) -> tuple[float, float]:
        """Returns the lower and upper bounds, or -+inf."""
    @property
    def is_constant(self): ...
    @property
    def leading_term(self) -> tuple[_DimMon, int]:
        """Returns the highest degree term that comes first lexicographically."""
    def evaluate(self, env: DimVarEnv): ...
    def non_negative(self) -> _DimExpr: ...
    @staticmethod
    def get_aval(dim: _DimExpr): ...
    def dimension_as_value(self):
        """Turns a dimension size into a Jax value that we can compute with."""
    def __jax_array__(self): ...

@dataclasses.dataclass
class _Decomposition:
    """Decomposition of an expression around an operation atom.

  E = factor * mod(*operands)^exp * rest_monomial + rest_expr
  """
    factor: int
    operands: Sequence[_DimExpr]
    exp: int
    rest_monomial: _DimExpr
    rest_expr: _DimExpr
    def __init__(self, factor, operands, exp, rest_monomial, rest_expr) -> None: ...

def is_poly_dim(p: DimSize) -> bool: ...

shape_assertion_p: Incomplete

class ShapeAssertionEffect(effects.Effect): ...

shape_assertion_effect: Incomplete

def shape_assertion(assert_what: jax.Array, *error_message_inputs: jax.Array, error_message: str) -> None:
    """Adds a shape assertion in the code.

  Args:
    assert_what: a boolean asserted to be true. Must be computed based only
      on dimension expressions, so that it can be evaluated after shape
      refinement.
    error_message_inputs: integers expressions whose values can be referenced
      in the `error_message`. Must be computed based only
      on dimension expressions, so that they can be evaluated after shape
      refinement.
    error_message: an error message, possibly containing format specifiers
      {0}, {1}, ..., referencing the values of the `error_message_inputs`.
      The format specifiers are sometimes processed with Python's
      `string::format` method, and sometimes with `llvm::formatv`.
  """

dim_as_value_p: Incomplete

def dim_as_value_impl(dim: DimSize): ...

class PolyShape(tuple):
    """Tuple of polymorphic dimension specifications.

  See docstring of :func:`jax2tf.convert`.
  """
    def __init__(self, *dim_specs) -> None: ...
    def __new__(cls, *dim_specs): ...

class _Parser:
    shape_spec: Incomplete
    shape_spec_repr: Incomplete
    arg_shape: Incomplete
    dimensions: Incomplete
    def __init__(self, shape_spec: str, arg_shape: Sequence[int | None], shape_spec_repr: str) -> None: ...
    tokstream: Incomplete
    def parse(self) -> Sequence[DimSize]: ...
    def add_dim(self, expr: DimSize | None, tok: tokenize.TokenInfo): ...
    def parse_err(self, tok: tokenize.TokenInfo | None, detail: str) -> Exception: ...
    def next_tok(self) -> tokenize.TokenInfo: ...
    def expect_token(self, tok: tokenize.TokenInfo, expected: Sequence[int]) -> None: ...
    def consume_token(self, tok: tokenize.TokenInfo, expected: int) -> tokenize.TokenInfo: ...
    def integer(self, tok: tokenize.TokenInfo) -> tuple[int, tokenize.TokenInfo]: ...
    FOLLOW_SHAPE: Incomplete
    def shape(self, tok: tokenize.TokenInfo) -> tuple[Sequence[DimSize], tokenize.TokenInfo]: ...
    FOLLOW_EXPR: Incomplete
    def expr(self, tok: tokenize.TokenInfo) -> tuple[DimSize, tokenize.TokenInfo]: ...
    FOLLOW_MON: Incomplete
    def mon(self, tok: tokenize.TokenInfo) -> tuple[DimSize, tokenize.TokenInfo]: ...
    def atom(self, tok: tokenize.TokenInfo) -> tuple[DimSize, tokenize.TokenInfo]: ...
    def unary_op(self, op: str, tok) -> tuple[DimSize, tokenize.TokenInfo]: ...
    def binary_op(self, op: str, tok) -> tuple[DimSize, tokenize.TokenInfo]: ...

dimension_size_p: Incomplete

def arg_aval(arg_shape: Sequence[int | None], arg_jax_dtype: DType, polymorphic_shape: str | PolyShape | None) -> core.ShapedArray:
    """Computes abstract values.

  Args:
    arg_shape: the shape for the argument, possibly having None dimensions.
    arg_dtype: the inferred JAX dtype for the arg.
    polymorphic_shape: the polymorphic specification for the argument.
  Returns: the JAX abstract value for the argument.
  """
def all_dim_vars(args_avals: Sequence[core.AbstractValue]) -> Sequence[str]: ...

class CachingShapeEvaluator:
    env: Incomplete
    def __init__(self, **env) -> None: ...
    def evaluate(self, e: DimSize): ...

@dataclasses.dataclass(frozen=True)
class ShapeConstraint:
    class Comparator(Enum):
        EQ = ...
        GEQ = ...
    comp: Comparator
    left: DimSize
    right: DimSize
    error_message_pieces: Sequence[str | DimSize]
    def check_statically(self, eval: CachingShapeEvaluator) -> None:
        """Evaluates a constraint statically."""
    def compute(self, eval: CachingShapeEvaluator) -> jax.Array | None:
        """Computes if the constraint is satisfied.

    If the constraint can be resolved statically returns None
    or raises ValueError otherwise. If the constraint cannot be
    resolved statically, returns a value representing if the
    constraint is satisfied.
    """
    def error_message_and_inputs(self, eval: CachingShapeEvaluator) -> tuple[str, Sequence[Any]]:
        """Forms the error_message and error message_inputs.
    See shape_assertion.
    """
    def make_error(self, eval: CachingShapeEvaluator) -> Exception: ...
    def __init__(self, comp, left, right, error_message_pieces) -> None: ...

class ShapeConstraints:
    constraints: Incomplete
    def __init__(self) -> None: ...
    def add_constraint(self, comp: ShapeConstraint.Comparator, left: DimSize, right: DimSize, error_message_pieces: Sequence[str | DimSize]): ...
    def check_statically(self, eval: CachingShapeEvaluator) -> None:
        """Evaluates all the constraints statically.

    If the static checking of any constraint fails, raises ValueError.
    """
    def shape_assertions(self, eval: CachingShapeEvaluator) -> None:
        """Computes the shape assertions for the set of constraints.

    See jax_export._wrap_main_func docstring.
    """

@dataclasses.dataclass
class _DimEquation:
    aval_dim_expr: _DimExpr
    dim_name: str
    def __init__(self, aval_dim_expr, dim_name) -> None: ...

def args_kwargs_path_to_str(path: tree_util.KeyPath) -> str: ...
def pretty_print_dimension_descriptor(args_kwargs_tree: tree_util.PyTreeDef, flat_arg_idx: int, dim_idx: int | None) -> str: ...
def solve_dim_vars(args_avals: Sequence[core.AbstractValue], args_kwargs_tree: tree_util.PyTreeDef) -> tuple[DimVarEnv, ShapeConstraints, Sequence[tuple[str, int, int]]]:
    '''Solves dimension variables in a called function\'s avals in terms of actual argument shapes.

  For example, given:

     args_avals = [ShapedArray((3, a, a + b), f32)]

  we introduce fresh "synthetic" dimension variables to represent the actual
  dimension size of actual arguments for each non-constant dimension.
  Each synthetic variable has a name, an arg_idx, and a dim_idx, e.g.:

    synthetic_vars = [("args[0].shape[1]", 0, 1), ("args[0].shape[2]", 0, 2)]

  and then we express the solution for the unknown dimension variables {a, b}
  as symbolic expressions in terms of the synthetic variables:

    dict(a=args[0].shape[1], b=args[0].shape[2] - args[0].shape[1])

  Not all equations are solvable. For now, we solve first the linear
  uni-variate equations, then the solved variables are used to simplify the
  remaining equations to linear uni-variate equations, and the process
  continues until all dimension variables are solved.

  Args:
    args_avals: the abstract values of the `args`, with shapes that may
      include unknown dimension variables.
    args_kwargs_tree: a PyTreeDef that describes the tuple `(args, kwargs)`
      from which the flat sequence `args_avals` is extracted. Used for
      describing args and kwargs in synthetic variable names and in
      error messages.

  Returns: a 3-tuple with: (a) the solution for the unknown dimension variables
   (b) a list of constraints that must be satisfied for the solution to be a
   valid one, and (c) and the list of synthetic variables that may appear in
   the solution and the constraints.

  Raises ValueError if it cannot solve some dimension variable.
  '''
def compute_dim_vars_from_arg_shapes(args_avals: Sequence[core.AbstractValue], *actual_args: jax.Array, args_kwargs_tree: tree_util.PyTreeDef) -> Sequence[jax.Array]:
    """Computes values of dimension variables to unify args_avals with actual arguments.

  Like `solve_dim_vars` except that here we express the solution as
  JAX arrays that reference the `actual_args`. This function can be used to
  generate the code for computing the dimension variables. It also generates
  the shape assertions.

  Returns: the values of the dimension variables, in the order determined by
    `all_dim_vars(args_avals)`.
  """
