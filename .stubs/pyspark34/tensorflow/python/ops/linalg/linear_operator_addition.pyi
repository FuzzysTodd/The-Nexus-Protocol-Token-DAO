import abc
from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops
from tensorflow.python.ops.linalg import linear_operator as linear_operator, linear_operator_diag as linear_operator_diag, linear_operator_full_matrix as linear_operator_full_matrix, linear_operator_identity as linear_operator_identity, linear_operator_lower_triangular as linear_operator_lower_triangular

def add_operators(operators, operator_name: Incomplete | None = None, addition_tiers: Incomplete | None = None, name: Incomplete | None = None):
    '''Efficiently add one or more linear operators.

  Given operators `[A1, A2,...]`, this `Op` returns a possibly shorter list of
  operators `[B1, B2,...]` such that

  ```sum_k Ak.matmul(x) = sum_k Bk.matmul(x).```

  The operators `Bk` result by adding some of the `Ak`, as allowed by
  `addition_tiers`.

  Example of efficient adding of diagonal operators.

  ```python
  A1 = LinearOperatorDiag(diag=[1., 1.], name="A1")
  A2 = LinearOperatorDiag(diag=[2., 2.], name="A2")

  # Use two tiers, the first contains an Adder that returns Diag.  Since both
  # A1 and A2 are Diag, they can use this Adder.  The second tier will not be
  # used.
  addition_tiers = [
      [_AddAndReturnDiag()],
      [_AddAndReturnMatrix()]]
  B_list = add_operators([A1, A2], addition_tiers=addition_tiers)

  len(B_list)
  ==> 1

  B_list[0].__class__.__name__
  ==> \'LinearOperatorDiag\'

  B_list[0].to_dense()
  ==> [[3., 0.],
       [0., 3.]]

  B_list[0].name
  ==> \'Add/A1__A2/\'
  ```

  Args:
    operators:  Iterable of `LinearOperator` objects with same `dtype`, domain
      and range dimensions, and broadcastable batch shapes.
    operator_name:  String name for returned `LinearOperator`.  Defaults to
      concatenation of "Add/A__B/" that indicates the order of addition steps.
    addition_tiers:  List tiers, like `[tier_0, tier_1, ...]`, where `tier_i`
      is a list of `Adder` objects.  This function attempts to do all additions
      in tier `i` before trying tier `i + 1`.
    name:  A name for this `Op`.  Defaults to `add_operators`.

  Returns:
    Subclass of `LinearOperator`.  Class and order of addition may change as new
      (and better) addition strategies emerge.

  Raises:
    ValueError:  If `operators` argument is empty.
    ValueError:  If shapes are incompatible.
  '''

class _Hints:
    """Holds 'is_X' flags that every LinearOperator is initialized with."""
    is_non_singular: Incomplete
    is_positive_definite: Incomplete
    is_self_adjoint: Incomplete
    def __init__(self, is_non_singular: Incomplete | None = None, is_positive_definite: Incomplete | None = None, is_self_adjoint: Incomplete | None = None) -> None: ...

class _Adder(metaclass=abc.ABCMeta):
    """Abstract base class to add two operators.

  Each `Adder` acts independently, adding everything it can, paying no attention
  as to whether another `Adder` could have done the addition more efficiently.
  """
    @property
    def name(self): ...
    @abc.abstractmethod
    def can_add(self, op1, op2):
        """Returns `True` if this `Adder` can add `op1` and `op2`.  Else `False`."""
    def add(self, op1, op2, operator_name, hints: Incomplete | None = None):
        """Return new `LinearOperator` acting like `op1 + op2`.

    Args:
      op1:  `LinearOperator`
      op2:  `LinearOperator`, with `shape` and `dtype` such that adding to
        `op1` is allowed.
      operator_name:  `String` name to give to returned `LinearOperator`
      hints:  `_Hints` object.  Returned `LinearOperator` will be created with
        these hints.

    Returns:
      `LinearOperator`
    """

class _AddAndReturnScaledIdentity(_Adder):
    """Handles additions resulting in an Identity family member.

  The Identity (`LinearOperatorScaledIdentity`, `LinearOperatorIdentity`) family
  is closed under addition.  This `Adder` respects that, and returns an Identity
  """
    def can_add(self, op1, op2): ...

class _AddAndReturnDiag(_Adder):
    """Handles additions resulting in a Diag operator."""
    def can_add(self, op1, op2): ...

class _AddAndReturnTriL(_Adder):
    """Handles additions resulting in a TriL operator."""
    def can_add(self, op1, op2): ...

class _AddAndReturnMatrix(_Adder):
    '''"Handles additions resulting in a `LinearOperatorFullMatrix`.'''
    def can_add(self, op1, op2): ...

SUPPORTED_OPERATORS: Incomplete
