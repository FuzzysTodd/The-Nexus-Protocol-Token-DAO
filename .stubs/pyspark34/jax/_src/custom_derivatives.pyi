import dataclasses
from _typeshed import Incomplete
from jax._src import core as core, custom_api_util as custom_api_util, dtypes as dtypes, effects as effects, linear_util as lu, traceback_util as traceback_util
from jax._src.ad_util import SymbolicZero as SymbolicZero, Zero as Zero, stop_gradient_p as stop_gradient_p, zeros_like_aval as zeros_like_aval
from jax._src.api_util import argnums_partial as argnums_partial, flatten_fun_nokwargs as flatten_fun_nokwargs
from jax._src.config import config as config
from jax._src.core import raise_to_shaped as raise_to_shaped
from jax._src.custom_transpose import custom_transpose as custom_transpose
from jax._src.errors import UnexpectedTracerError as UnexpectedTracerError
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, xla as xla
from jax._src.interpreters.batching import not_mapped as not_mapped
from jax._src.lax import lax as lax
from jax._src.tree_util import register_pytree_node_class as register_pytree_node_class, tree_flatten as tree_flatten, tree_leaves as tree_leaves, tree_map as tree_map, tree_unflatten as tree_unflatten, treedef_is_leaf as treedef_is_leaf, treedef_tuple as treedef_tuple
from jax._src.util import Unhashable as Unhashable, cache as cache, safe_map as safe_map, safe_zip as safe_zip, split_list as split_list
from typing import Any, Callable, Generic, TypeVar

map = safe_map
zip = safe_zip
ReturnValue = TypeVar('ReturnValue')

class custom_jvp(Generic[ReturnValue]):
    """Set up a JAX-transformable function for a custom JVP rule definition.

  This class is meant to be used as a function decorator. Instances are
  callables that behave similarly to the underlying function to which the
  decorator was applied, except when a differentiation transformation (like
  :py:func:`jax.jvp` or :py:func:`jax.grad`) is applied, in which case a custom
  user-supplied JVP rule function is used instead of tracing into and
  performing automatic differentiation of the underlying function's
  implementation.

  There are two instance methods available for defining the custom JVP rule:
  :py:func:`~jax.custom_jvp.defjvp` for defining a *single* custom JVP rule for
  all the function's inputs, and for convenience
  :py:func:`~jax.custom_jvp.defjvps`, which wraps
  :py:func:`~jax.custom_jvp.defjvp`, and allows you to provide separate
  definitions for the partial derivatives of the function w.r.t. each of its
  arguments.

  For example::

    @jax.custom_jvp
    def f(x, y):
      return jnp.sin(x) * y

    @f.defjvp
    def f_jvp(primals, tangents):
      x, y = primals
      x_dot, y_dot = tangents
      primal_out = f(x, y)
      tangent_out = jnp.cos(x) * x_dot * y + jnp.sin(x) * y_dot
      return primal_out, tangent_out

  For a more detailed introduction, see the tutorial_.

  .. _tutorial: https://jax.readthedocs.io/en/latest/notebooks/Custom_derivative_rules_for_Python_code.html
  """
    fun: Callable[..., ReturnValue]
    nondiff_argnums: tuple[int, ...]
    jvp: Callable[..., tuple[ReturnValue, ReturnValue]] | None
    symbolic_zeros: bool
    def __init__(self, fun: Callable[..., ReturnValue], nondiff_argnums: tuple[int, ...] = ()) -> None: ...
    __getattr__: Incomplete
    def defjvp(self, jvp: Callable[..., tuple[ReturnValue, ReturnValue]], symbolic_zeros: bool = False) -> Callable[..., tuple[ReturnValue, ReturnValue]]:
        """Define a custom JVP rule for the function represented by this instance.

    Args:
      jvp: a Python callable representing the custom JVP rule. When there are no
        ``nondiff_argnums``, the ``jvp`` function should accept two arguments,
        where the first is a tuple of primal inputs and the second is a tuple of
        tangent inputs. The lengths of both tuples are equal to the number of
        parameters of the ``custom_jvp`` function. The ``jvp`` function should
        produce as output a pair where the first element is the primal output
        and the second element is the tangent output. Elements of the input and
        output tuples may be arrays or any nested tuples/lists/dicts thereof.
      symbolic_zeros: boolean, indicating whether the rule should be passed
        objects representing static symbolic zeros in its tangent argument in
        correspondence with unperturbed values; otherwise, only standard JAX
        types (e.g. array-likes) are passed. Setting this option to ``True``
        allows a JVP rule to detect whether certain inputs are not involved in
        differentiation, but at the cost of needing special handling for these
        objects (which e.g. can't be passed into jax.numpy functions). Default
        ``False``.

    Returns:
      None.

    Example::

      @jax.custom_jvp
      def f(x, y):
        return jnp.sin(x) * y

      @f.defjvp
      def f_jvp(primals, tangents):
        x, y = primals
        x_dot, y_dot = tangents
        primal_out = f(x, y)
        tangent_out = jnp.cos(x) * x_dot * y + jnp.sin(x) * y_dot
        return primal_out, tangent_out
    """
    def defjvps(self, *jvps: Callable[..., ReturnValue] | None):
        """Convenience wrapper for defining JVPs for each argument separately.

    This convenience wrapper cannot be used together with ``nondiff_argnums``.

    Args:
      *jvps: a sequence of functions, one for each positional argument of the
        ``custom_jvp`` function. Each function takes as arguments the tangent
        value for the corresponding primal input, the primal output, and the
        primal inputs. See the example below.

    Returns:
      None.

    Example::

      @jax.custom_jvp
      def f(x, y):
        return jnp.sin(x) * y

      f.defjvps(lambda x_dot, primal_out, x, y: jnp.cos(x) * x_dot * y,
                lambda y_dot, primal_out, x, y: jnp.sin(x) * y_dot)
    """
    def __call__(self, *args: Any, **kwargs: Any) -> ReturnValue: ...

class CustomJVPCallPrimitive(core.Primitive):
    multiple_results: bool
    def bind(self, fun, jvp, *args, symbolic_zeros): ...
    def impl(self, fun, _, *args): ...
    def post_process(self, trace, out_tracers, jvp_was_run: bool): ...
    def get_bind_params(self, params): ...

def lift_jvp(num_consts: int, jvp_jaxpr_thunk: Callable) -> lu.WrappedFun: ...
def process_env_traces(primitive, level: int, jvp_was_run: bool, *args): ...

custom_jvp_call_p: Incomplete

class custom_vjp(Generic[ReturnValue]):
    """Set up a JAX-transformable function for a custom VJP rule definition.

  This class is meant to be used as a function decorator. Instances are
  callables that behave similarly to the underlying function to which the
  decorator was applied, except when a reverse-mode differentiation
  transformation (like :py:func:`jax.grad`) is applied, in which case a custom
  user-supplied VJP rule function is used instead of tracing into and performing
  automatic differentiation of the underlying function's implementation. There
  is a single instance method, :py:func:`~jax.custom_vjp.defvjp`, which may be
  used to define the custom VJP rule.

  This decorator precludes the use of forward-mode automatic differentiation.

  For example::

    @jax.custom_vjp
    def f(x, y):
      return jnp.sin(x) * y

    def f_fwd(x, y):
      return f(x, y), (jnp.cos(x), jnp.sin(x), y)

    def f_bwd(res, g):
      cos_x, sin_x, y = res
      return (cos_x * g * y, sin_x * g)

    f.defvjp(f_fwd, f_bwd)

  For a more detailed introduction, see the tutorial_.

  .. _tutorial: https://jax.readthedocs.io/en/latest/notebooks/Custom_derivative_rules_for_Python_code.html
  """
    fun: Incomplete
    nondiff_argnums: Incomplete
    fwd: Incomplete
    bwd: Incomplete
    symbolic_zeros: bool
    def __init__(self, fun: Callable[..., ReturnValue], nondiff_argnums: tuple[int, ...] = ()) -> None: ...
    __getattr__: Incomplete
    def defvjp(self, fwd: Callable[..., tuple[ReturnValue, Any]], bwd: Callable[..., tuple[Any, ...]], symbolic_zeros: bool = False) -> None:
        '''Define a custom VJP rule for the function represented by this instance.

    Args:
      fwd: a Python callable representing the forward pass of the custom VJP
        rule. When there are no ``nondiff_argnums``, the ``fwd`` function has
        the same input signature as the underlying primal function. It should
        return as output a pair, where the first element represents the primal
        output and the second element represents any "residual" values to store
        from the forward pass for use on the backward pass by the function
        ``bwd``. Input arguments and elements of the output pair may be arrays
        or nested tuples/lists/dicts thereof.
      bwd: a Python callable representing the backward pass of the custom VJP
        rule. When there are no ``nondiff_argnums``, the ``bwd`` function takes
        two arguments, where the first is the "residual" values produced on the
        forward pass by ``fwd``, and the second is the output cotangent with the
        same structure as the primal function output. The output of ``bwd`` must
        be a tuple of length equal to the number of arguments of the primal
        function, and the tuple elements may be arrays or nested
        tuples/lists/dicts thereof so as to match the structure of the primal
        input arguments.
      symbolic_zeros: boolean, determining whether to indicate symbolic zeros
        to the ``fwd`` and ``bwd`` rules. Enabling this option allows custom
        derivative rules to detect when certain inputs, and when certain
        output cotangents, are not involved in differentiation. If ``True``:

        * ``fwd`` must accept, in place of each leaf value ``x`` in
          the pytree comprising an argument to the original function,
          an object (of type
          ``jax.custom_derivatives.CustomVJPPrimal``) with two
          attributes instead: ``value`` and ``perturbed``. The
          ``value`` field is the original primal argument, and
          ``perturbed`` is a boolean.  The ``perturbed`` bit indicates
          whether the argument is involved in differentiation (i.e.,
          if it is ``False``, then the corresponding Jacobian "column"
          is zero).

        * ``bwd`` will be passed objects representing static symbolic zeros in
          its cotangent argument in correspondence with unperturbed values;
          otherwise, only standard JAX types (e.g. array-likes) are passed.

        Setting this option to ``True`` allows these rules to detect whether
        certain inputs and outputs are not involved in differentiation, but at
        the cost of special handling. For instance:

        * The signature of ``fwd`` changes, and the objects it is passed cannot
          be output from the rule directly.

        * The ``bwd`` rule is passed objects that are not entirely array-like,
          and that cannot be passed to most ``jax.numpy`` functions.

        * Any custom pytree nodes involved in the primal function\'s arguments
          must accept, in their unflattening functions, the two-field record
          objects that are given as input leaves to the ``fwd`` rule.

        Default ``False``.

    Returns:
      None.

    Example::

      @jax.custom_vjp
      def f(x, y):
        return jnp.sin(x) * y

      def f_fwd(x, y):
        return f(x, y), (jnp.cos(x), jnp.sin(x), y)

      def f_bwd(res, g):
        cos_x, sin_x, y = res
        return (cos_x * g * y, sin_x * g)

      f.defvjp(f_fwd, f_bwd)
    '''
    def __call__(self, *args: Any, **kwargs: Any) -> ReturnValue: ...

@dataclasses.dataclass
class CustomVJPPrimal:
    """Primal to a ``custom_vjp``'s forward rule when ``symbolic_zeros`` is set"""
    value: Any
    perturbed: bool
    def __init__(self, value, perturbed) -> None: ...

def custom_vjp_primal_tree_values(tree):
    """Strips away perturbation information from forward rule arguments.

  This is a helper function for user with the ``symbolic_zeros`` option to
  the ``defvjp`` method of a ``custom_vjp``-decorated function.

  In ``symbolic_zeros`` mode, the custom forward rule receives arguments
  whose pytree leaves are records with a ``value`` attribute that carries
  the primal argument. This is a way to convert such argument trees back to
  their original form, replacing each such record with its carried value at
  each leaf.
  """

class CustomVJPCallPrimitive(core.CallPrimitive):
    initial_style: core.Primitive
    def bind(self, fun, fwd, bwd, *args, out_trees, symbolic_zeros): ...
    def impl(self, fun, fwd, bwd, *args, out_trees): ...
    def post_process(self, trace, out_tracers, params): ...

custom_vjp_call_p: Incomplete

def process_env_traces_fwd(level: int, out_trees, *args): ...

custom_vjp_call_jaxpr_p: Incomplete

def custom_gradient(fun):
    '''Convenience function for defining custom VJP rules (aka custom gradients).

  While the canonical way to define custom VJP rules is via ``jax.custom_vjp``,
  the ``custom_gradient`` convenience wrapper follows TensorFlow\'s
  ``tf.custom_gradient`` API. The difference here is that ``custom_gradient``
  can be used as a decorator on one function that returns both the primal value
  (representing the output of the mathematical function to be differentiated)
  and the VJP (gradient) function. See
  https://www.tensorflow.org/api_docs/python/tf/custom_gradient.

  If the mathematical function to be differentiated has Haskell-like signature
  ``a -> b``, then the Python callable ``fun`` should have the signature
  ``a -> (b, CT b --o CT a)`` where we use ``CT x`` to denote a cotangent type
  for ``x`` and the ``--o`` arrow to denote a linear function. See the example
  below. That is, ``fun`` should return a pair where the first element
  represents the value of the mathematical function to be differentiated and the
  second element is a function to be called on the backward pass of reverse-mode
  automatic differentiation (i.e. the "custom gradient" function).

  The function returned as the second element of the output of ``fun`` can close
  over intermediate values computed when evaluating the function to be
  differentiated. That is, use lexical closure to share work between the forward
  pass and the backward pass of reverse-mode automatic differentiation. However,
  it cannot perform Python control flow which depends on the values of the
  closed-over intermediate values or its cotangent arguments; if the function
  includes such control flow, an error is raised.

  Args:
    fun: a Python callable specifying both the mathematical function to be
      differentiated and its reverse-mode differentiation rule. It should return
      a pair consisting of an output value and a Python callable that represents
      the custom gradient function.

  Returns:
    A Python callable that accepts the same arguments as ``fun`` and returns the
    output value specified by the first element of ``fun``\'s output pair.

  For example:

  >>> @jax.custom_gradient
  ... def f(x):
  ...   return x ** 2, lambda g: (g * x,)
  ...
  >>> print(f(3.))
  9.0
  >>> print(jax.grad(f)(3.))
  3.0

  An example with a function on two arguments, so that the VJP function must
  return a tuple of length two:

  >>> @jax.custom_gradient
  ... def f(x, y):
  ...   return x * y, lambda g: (g * y, g * x)
  ...
  >>> print(f(3., 4.))
  12.0
  >>> print(jax.grad(f, argnums=(0, 1))(3., 4.))
  (Array(4., dtype=float32, weak_type=True), Array(3., dtype=float32, weak_type=True))
  '''

class Residuals:
    jaxpr: Incomplete
    in_tree: Incomplete
    out_tree: Incomplete
    consts: Incomplete
    def __init__(self, jaxpr, in_tree, out_tree, consts) -> None: ...
    def __iter__(self): ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, aux, consts): ...

def closure_convert(fun: Callable, *example_args) -> tuple[Callable, list[Any]]:
    '''Closure conversion utility, for use with higher-order custom derivatives.

  To define custom derivatives such as with ``jax.custom_vjp(f)``, the target
  function ``f`` must take, as formal arguments, all values involved in
  differentiation. If ``f`` is a higher-order function, in that it accepts as an
  argument a Python function ``g``, then values stored away in ``g``\'s closure
  will not be visible to the custom derivative rules, and attempts at AD
  involving these values will fail. One way around this is to convert the
  closure by extracting these values, and to pass them as explicit formal
  arguments across the custom derivative boundary. This utility carries out that
  conversion. More precisely, it closure-converts the function ``fun``
  specialized to the types of the arguments given in ``example_args``.

  When we refer here to "values in the closure" of ``fun``, we do not mean the
  values that are captured by Python directly when ``fun`` is defined (e.g. the
  Python objects in ``fun.__closure__``, if the attribute exists). Rather, we
  mean values encountered during the execution of ``fun`` on ``example_args``
  that determine its output. This may include, for instance, arrays captured
  transitively in Python closures, i.e. in the Python closure of functions
  called by ``fun``, the closures of the functions that they call, and so forth.

  The function ``fun`` must be a pure function.

  Example usage::

    def minimize(objective_fn, x0):
      converted_fn, aux_args = closure_convert(objective_fn, x0)
      return _minimize(converted_fn, x0, *aux_args)

    @partial(custom_vjp, nondiff_argnums=(0,))
    def _minimize(objective_fn, x0, *args):
      z = objective_fn(x0, *args)
      # ... find minimizer x_opt ...
      return x_opt

    def fwd(objective_fn, x0, *args):
      y = _minimize(objective_fn, x0, *args)
      return y, (y, args)

    def rev(objective_fn, res, g):
      y, args = res
      y_bar = g
      # ... custom reverse-mode AD ...
      return x0_bar, *args_bars

    _minimize.defvjp(fwd, rev)

  Args:
    fun: Python callable to be converted. Must be a pure function.
    example_args: Arrays, scalars, or (nested) standard Python
      containers (tuples, lists, dicts, namedtuples, i.e., pytrees)
      thereof, used to determine the types of the formal arguments to
      ``fun``. This type-specialized form of ``fun`` is the function
      that will be closure converted.

  Returns:
    A pair comprising (i) a Python callable, accepting the same
    arguments as ``fun`` followed by arguments corresponding to the
    values hoisted from its closure, and (ii) a list of values hoisted
    from the closure.
  '''
def partition_list(choice, lst): ...
def abstractify(x): ...
def linear_call(fun: Callable, fun_transpose: Callable, residual_args, linear_args):
    '''Call a linear function, with a custom implementation for its transpose.

  The `Haskell-like type signatures`_ of ``fun`` and ``fun_transpose`` are:

  .. code-block:: haskell

    fun           :: r -> a -o b
    fun_transpose :: r -> b -o a

  where the ``-o`` arrow indicates a linear function, ``r`` is the
  residual input type and ``a`` is the linear input type.

  The functions ``fun`` and ``fun_transpose`` are coupled as
  transposes of one another. Specifically, the transpose of a
  ``linear_call`` primitive is another ``linear_call`` to
  ``fun_transpose``, with ``fun`` as its custom transposition.

  For example:

  >>> def f(r, x):
  ...   return x / r

  >>> def t(r, t):
  ...   return t / r

  >>> def div_add(x, denom):
  ...   return x + linear_call(f, t, denom, x)

  >>> def transpose(f, x_example):
  ...   def transposed(y):
  ...     x, = jax.linear_transpose(f, x_example)(y)
  ...     return x
  ...   return transposed

  >>> div_add(9., 3.)
  Array(12., dtype=float32, weak_type=True)

  >>> transpose(partial(div_add, denom=3.), 1.)(18.)  # custom
  Array(24., dtype=float32, weak_type=True)

  >>> transpose(lambda x: x + x / 3., 1.)(18.)  # reference
  Array(24., dtype=float32, weak_type=True)

  The above definition of ``f`` illustrates the purpose of a residual
  argument: division is linear in one of its inputs (the dividend
  ``x``) but not the other (the divisor ``r``).

  As another example:

  >>> def custom_id(x):
  ...   def f(_, x): return x
  ...   def t(_, t): return 7.
  ...   return linear_call(f, t, (), x)
  >>> custom_id(1.)
  1.0
  >>> transpose(custom_id, 1.)(1.)
  7.0
  >>> transpose(transpose(custom_id, 1.), 1.)(1.)
  1.0
  >>> transpose(transpose(transpose(custom_id, 1.), 1.), 1.)(1.)
  7.0

  Args:
    fun: a Python callable specifying a linear function. It should
      take two arguments: one of "residual" inputs (type ``r``),
      i.e. inputs in which the function is not necessarily linear, and
      one of "linear" inputs (type ``a``).  It should return output
      whose components are linear in the linear input (type ``b``).
    fun_transpose: a Python callable specifying a structurally linear
      function that is the transpose of ``fun`` with respect to its
      linear inputs. Its first argument is the same residual inputs
      (``r``) as ``fun``. Its second argument is of type
      ``b``. Finally, its output is of type ``a`` and each of its
      component are linear in its second argument (the ``b`` inputs).
    residual_args: Argument in which ``fun`` and ``fun_transpose`` are
      not necessarily linear. Not involved in transposition.
    linear_args: Argument in which ``fun`` and ``fun_transpose`` are
      linear and with respect to which the two are transposes.

  Returns:
    The call result, i.e. ``fun(residual_args, linear_args)``.

  .. _Haskell-like type signatures: https://wiki.haskell.org/Type_signature
  '''

linear_call_p: Incomplete
unreachable_p: core.Primitive

def unreachable_impl(*_, out_avals, exc_type, message) -> None: ...
def unreachable(*args, out_avals: Incomplete | None = None, exc_type=..., message: str = 'unreachable'):
    '''Fail when evaluated concretely (but allow for staging).

  This function allows one to assert an impossibility of
  evaluation. It can be used to guarantee that evaluation does not
  "reach" a certain point in the sense that it does not execute, but
  it can nonetheless be staged out by JAX without error.

  Args:
    *args: The arbitrary pytree of arguments to the function.
    out_avals: Optional specification of the output types of this
     function invocation from the point of view of staging. If
     ``None``, these are chosen as equal to types of input arguments.
    exc_type: Optional constructor for the Python exception raised if
      evaluated.
    message: Optional string message for the Python exception raised
      if evaluated.

  '''

disallow_jvp: Incomplete

def custom_vjp_by_custom_transpose(fun, fwd, bwd): ...

custom_jvp_call_jaxpr_p: Incomplete
