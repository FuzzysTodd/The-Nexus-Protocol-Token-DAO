from _typeshed import Incomplete
from jax._src import ad_util as ad_util, core as core
from jax._src.core import raise_to_shaped as raise_to_shaped
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, xla as xla
from jax._src.lax import lax as lax
from jax._src.traceback_util import api_boundary as api_boundary
from jax._src.util import safe_map as safe_map, split_list as split_list
from jax.tree_util import tree_flatten as tree_flatten, tree_leaves as tree_leaves, tree_unflatten as tree_unflatten, treedef_children as treedef_children, treedef_tuple as treedef_tuple
from typing import NamedTuple

class _RootTuple(NamedTuple):
    f: Incomplete
    solve: Incomplete
    l_and_s: Incomplete

def custom_root(f, initial_guess, solve, tangent_solve, has_aux: bool = False):
    """Differentiably solve for a roots of a function.

  This is a low-level routine, mostly intended for internal use in JAX.
  Gradients of custom_root() are defined with respect to closed-over variables
  from the provided function ``f`` via the implicit function theorem:
  https://en.wikipedia.org/wiki/Implicit_function_theorem

  Args:
    f: function for which to find a root. Should accept a single argument,
      return a tree of arrays with the same structure as its input.
    initial_guess: initial guess for a zero of f.
    solve: function to solve for the roots of f. Should take two positional
      arguments, f and initial_guess, and return a solution with the same
      structure as initial_guess such that func(solution) = 0. In other words,
      the following is assumed to be true (but not checked)::

        solution = solve(f, initial_guess)
        error = f(solution)
        assert all(error == 0)

    tangent_solve: function to solve the tangent system. Should take two
      positional arguments, a linear function ``g`` (the function ``f``
      linearized at its root) and a tree of array(s) ``y`` with the same
      structure as initial_guess, and return a solution ``x`` such that
      ``g(x)=y``:

      - For scalar ``y``, use ``lambda g, y: y / g(1.0)``.
      - For vector ``y``, you could use a linear solve with the Jacobian, if
        dimensionality of ``y`` is not too large:
        ``lambda g, y: np.linalg.solve(jacobian(g)(y), y)``.
    has_aux: bool indicating whether the ``solve`` function returns
      auxiliary data like solver diagnostics as a second argument.

  Returns:
    The result of calling solve(f, initial_guess) with gradients defined via
    implicit differentiation assuming ``f(solve(f, initial_guess)) == 0``.
  """

class _LinearSolveTuple(NamedTuple('_LinearSolveTuple', [('matvec', Incomplete), ('vecmat', Incomplete), ('solve', Incomplete), ('transpose_solve', Incomplete)])):
    def transpose(self): ...

def custom_linear_solve(matvec, b, solve, transpose_solve: Incomplete | None = None, symmetric: bool = False, has_aux: bool = False):
    """Perform a matrix-free linear solve with implicitly defined gradients.

  This function allows for overriding or defining gradients for a linear
  solve directly via implicit differentiation at the solution, rather than by
  differentiating *through* the solve operation. This can sometimes be much faster
  or more numerically stable, or differentiating through the solve operation
  may not even be implemented (e.g., if ``solve`` uses ``lax.while_loop``).

  Required invariant::

      x = solve(matvec, b)  # solve the linear equation
      assert matvec(x) == b  # not checked

  Args:
    matvec: linear function to invert. Must be differentiable.
    b: constant right handle side of the equation. May be any nested structure
      of arrays.
    solve: higher level function that solves for solution to the linear
      equation, i.e., ``solve(matvec, x) == x`` for all ``x`` of the same form
      as ``b``. This function need not be differentiable.
    transpose_solve: higher level function for solving the transpose linear
      equation, i.e., ``transpose_solve(vecmat, x) == x``, where ``vecmat`` is
      the transpose of the linear map ``matvec`` (computed automatically with
      autodiff). Required for backwards mode automatic differentiation, unless
      ``symmetric=True``, in which case ``solve`` provides the default value.
    symmetric: bool indicating if it is safe to assume the linear map
      corresponds to a symmetric matrix, i.e., ``matvec == vecmat``.
    has_aux: bool indicating whether the ``solve`` and ``transpose_solve`` functions
      return auxiliary data like solver diagnostics as a second argument.

  Returns:
    Result of ``solve(matvec, b)``, with gradients defined assuming that the
      solution ``x`` satisfies the linear equation ``matvec(x) == b``.
  """

linear_solve_p: Incomplete
