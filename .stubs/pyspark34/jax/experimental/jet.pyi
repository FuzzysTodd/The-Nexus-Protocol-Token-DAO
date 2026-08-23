from _typeshed import Incomplete
from collections.abc import Generator
from jax import lax as lax
from jax._src import ad_util as ad_util, core as core, dispatch as dispatch, sharding_impls as sharding_impls
from jax._src.api_util import shaped_abstractify as shaped_abstractify
from jax._src.util import unzip2 as unzip2, weakref_lru_cache as weakref_lru_cache
from jax.experimental import pjit as pjit
from jax.tree_util import register_pytree_node as register_pytree_node, tree_flatten as tree_flatten, tree_structure as tree_structure, tree_unflatten as tree_unflatten, treedef_is_leaf as treedef_is_leaf
from typing import Any, Callable

def jet(fun, primals, series):
    """Taylor-mode higher-order automatic differentiation.

  Args:
    fun: Function to be differentiated. Its arguments should be arrays, scalars,
      or standard Python containers of arrays or scalars. It should return an
      array, scalar, or standard Python container of arrays or scalars.
    primals: The primal values at which the Taylor approximation of ``fun`` should be
      evaluated. Should be either a tuple or a list of arguments,
      and its length should be equal to the number of positional parameters of
      ``fun``.
    series: Higher order Taylor-series-coefficients.
      Together, `primals` and `series` make up a truncated Taylor polynomial.
      Should be either a tuple or a list of tuples or lists,
      and its length dictates the degree of the truncated Taylor polynomial.

  Returns:
    A ``(primals_out, series_out)`` pair, where ``primals_out`` is ``fun(*primals)``,
    and together, ``primals_out`` and ``series_out`` are a
    truncated Taylor polynomial of :math:`f(h(\\cdot))`.
    The ``primals_out`` value has the same Python tree structure as ``primals``,
    and the ``series_out`` value the same Python tree structure as ``series``.

  For example:

  >>> import jax
  >>> import jax.numpy as np

  Consider the function :math:`h(z) = z^3`, :math:`x = 0.5`,
  and the first few Taylor coefficients
  :math:`h_0=x^3`, :math:`h_1=3x^2`, and :math:`h_2=6x`.
  Let :math:`f(y) = \\sin(y)`.

  >>> h0, h1, h2 = 0.5**3., 3.*0.5**2., 6.*0.5
  >>> f, df, ddf = np.sin, np.cos, lambda *args: -np.sin(*args)

  :func:`jet` returns the Taylor coefficients of :math:`f(h(z)) = \\sin(z^3)`
  according to Faà di Bruno's formula:

  >>> f0, (f1, f2) =  jet(f, (h0,), ((h1, h2),))
  >>> print(f0,  f(h0))
  0.12467473 0.12467473

  >>> print(f1, df(h0) * h1)
  0.7441479 0.74414825

  >>> print(f2, ddf(h0) * h1 ** 2 + df(h0) * h2)
  2.9064622 2.9064634
  """
def jet_fun(order, primals, series) -> Generator[Incomplete, Incomplete, None]: ...
def jet_subtrace(main, primals, series) -> Generator[Incomplete, Incomplete, None]: ...
def traceable(in_tree_def, *primals_and_series) -> Generator[Incomplete, Incomplete, None]: ...

class JetTracer(core.Tracer):
    primal: Incomplete
    terms: Incomplete
    def __init__(self, trace, primal, terms) -> None: ...
    @property
    def aval(self): ...
    def full_lower(self): ...

class JetTrace(core.Trace):
    def pure(self, val): ...
    def lift(self, val): ...
    def sublift(self, val): ...
    def process_primitive(self, primitive, tracers, params): ...
    def process_call(self, call_primitive, f, tracers, params): ...
    def post_process_call(self, call_primitive, out_tracers, params): ...
    def process_custom_jvp_call(self, primitive, fun, jvp, tracers, *, symbolic_zeros): ...
    def process_custom_vjp_call(self, primitive, fun, fwd, bwd, tracers, out_trees): ...

class ZeroTerm: ...

zero_term: Incomplete

class ZeroSeries: ...

zero_series: Incomplete
call_param_updaters: dict[core.Primitive, Callable[..., Any]]
jet_rules: Incomplete

def defzero(prim) -> None: ...
def zero_prop(prim, primals_in, series_in, **params): ...
def deflinear(prim) -> None: ...
def linear_prop(prim, primals_in, series_in, **params): ...
def def_deriv(prim, deriv) -> None:
    """
  Define the jet rule for a primitive in terms of its first derivative.
  """
def deriv_prop(prim, deriv, primals_in, series_in): ...
def def_comp(prim, comp) -> None:
    """
  Define the jet rule for a primitive in terms of a composition of simpler primitives.
  """
def fact(n): ...
