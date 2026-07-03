from _typeshed import Incomplete
from collections import abc
from collections.abc import Generator, Mapping, Sequence
from jax import lax as lax
from jax._src import core as core, dispatch as dispatch, effects as effects, linear_util as lu, op_shardings as op_shardings, sharding_impls as sharding_impls, source_info_util as source_info_util, stages as stages, traceback_util as traceback_util
from jax._src.api_util import check_callable as check_callable, donation_vector as donation_vector, flatten_axes as flatten_axes, flatten_fun_nokwargs as flatten_fun_nokwargs, shaped_abstractify as shaped_abstractify
from jax._src.array import ArrayImpl as ArrayImpl
from jax._src.config import config as config
from jax._src.errors import JAXTypeError as JAXTypeError
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, pxla as pxla, xla as xla
from jax._src.interpreters.partial_eval import DynamicJaxprTracer as DynamicJaxprTracer, convert_constvars_jaxpr as convert_constvars_jaxpr, new_jaxpr_eqn as new_jaxpr_eqn, trace_to_subjaxpr_dynamic as trace_to_subjaxpr_dynamic
from jax._src.pjit import GSPMDSharding as GSPMDSharding, get_unconstrained_dims as get_unconstrained_dims, sharding_constraint_p as sharding_constraint_p
from jax._src.sharding_impls import ArrayMapping as ArrayMapping, NamedSharding as NamedSharding, ParsedPartitionSpec as ParsedPartitionSpec, array_mapping_to_axis_resources as array_mapping_to_axis_resources
from jax._src.tree_util import all_leaves as all_leaves, tree_flatten as tree_flatten, tree_map as tree_map, tree_unflatten as tree_unflatten, treedef_tuple as treedef_tuple
from jax._src.util import HashableFunction as HashableFunction, as_hashable_function as as_hashable_function, distributed_debug_log as distributed_debug_log, merge_lists as merge_lists, moveaxis as moveaxis, partition_list as partition_list, safe_map as safe_map, safe_zip as safe_zip, split_list as split_list, tuple_insert as tuple_insert, unzip2 as unzip2, unzip3 as unzip3, wrap_name as wrap_name
from typing import Callable, NamedTuple

map: Incomplete
unsafe_map: Incomplete
zip = safe_zip

class FrozenDict(abc.Mapping):
    contents: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, name): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

AxisName: Incomplete
ResourceAxisName: Incomplete
Mesh: Incomplete
MeshAxisName: Incomplete
ResourceEnv: Incomplete
EMPTY_ENV: Incomplete
thread_resources: Incomplete

class SerialLoop:
    """Create an anonymous serial loop resource for use in a single xmap axis.

  A use of :py:class:`SerialLoop` in :py:func:`xmap`'s ``axis_resources``
  extends the resource environment with a new serial loop with a unique
  unspecified name, that will only be used to partition the axis that
  used a given instance.

  This is unlike :py:func:`serial_loop`, which makes it possible to iterate
  jointly over chunks of multiple axes (with the usual requirement that they
  do not coincide in a named shape of any value in the program).

  Example::

      # Processes `x` in a vectorized way, but in 20 micro-batches.
      xmap(f, in_axes=['i'], out_axes=[i], axis_resources={'i': SerialLoop(20)})(x)

      # Computes the result in a vectorized way, but in 400 micro-batches,
      # once for each coordinate (0, 0) <= (i, j) < (20, 20). Each `SerialLoop`
      # creates a fresh anonymous loop.
      xmap(h, in_axes=(['i'], ['j']), out_axes=['i', 'j'],
           axis_resources={'i': SerialLoop(20), 'j': SerialLoop(20)})(x, y)
  """
    length: int
    def __init__(self, length) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...

def serial_loop(name: ResourceAxisName, length: int):
    """Define a serial loop resource to be available in scope of this context manager.

  This is similar to :py:class:`Mesh` in that it extends the resource
  environment with a resource called ``name``. But, any use of this resource
  axis in ``axis_resources`` argument of :py:func:`xmap` will cause the
  body of :py:func:`xmap` to get executed ``length`` times with each execution
  only processing only a slice of inputs mapped along logical axes assigned
  to this resource.

  This is especially useful in that it makes it possible to lower the memory
  usage compared to :py:func:`vmap`, because it will avoid simultaneous
  materialization of intermediate values for every point in the batch.

  Note that collectives over loop axes are not supported, so they are less
  versatile than physical mesh axes.

  Args:
    name: Name of the loop in the resource environment.
    length: Number of iterations.

  Example::

    >>> x = jnp.linspace(0, jnp.pi, 4)
    ...
    >>> with serial_loop('l', len(x)):
    ...   out = xmap(
    ...     lambda x: jnp.sin(x) * 5,  # This will be called 4 times with different
    ...                                # slices of x.
    ...     in_axes=['i'], out_axes=['i'],
    ...     axis_resources={'i': 'l'})(x)
    >>> out.shape
    (4,)
  """

class _UniqueResourceName:
    uid: Incomplete
    tag: Incomplete
    def __init__(self, uid, tag: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...

def fresh_resource_name(tag: Incomplete | None = None): ...

class AxisNamePos(FrozenDict):
    user_repr: str
    expected_rank: int | None
    def __init__(self, *args, user_repr, **kwargs) -> None: ...

class AxisNamePosWithRank(AxisNamePos):
    expected_rank: Incomplete
    def __init__(self, *args, expected_rank, **kwargs) -> None: ...

class DotDotDotRepr: ...
Resource = ResourceAxisName | SerialLoop
ResourceSet = Resource | tuple[Resource, ...]

def xmap(fun: Callable, in_axes, out_axes, *, axis_sizes: Mapping[AxisName, int] | None = None, axis_resources: Mapping[AxisName, ResourceSet] | None = None, donate_argnums: int | Sequence[int] = (), backend: str | None = None) -> stages.Wrapped:
    '''Assign a positional signature to a program that uses named array axes.

  .. warning::
    This is an experimental feature and the details can change at
    any time. Use at your own risk!

  .. warning::
    This docstring is aspirational. Not all features of the named axis
    programming model have been implemented just yet.

  The usual programming model of JAX (or really NumPy) associates each array
  with two pieces of metadata describing its type: the element type (``dtype``)
  and the ``shape``. :py:func:`xmap` extends this model by adding support for
  *named axes*.  In particular, each array used in a function wrapped by
  :py:func:`xmap` can additionally have a non-empty ``named_shape`` attribute,
  which can be used to query the set of named axes (introduced by
  :py:func:`xmap`) appearing in that value along with their shapes.
  Furthermore, in most places where positional axis indices are allowed (for
  example the `axes` arguments in :py:func:`sum`), bound axis names are also
  accepted. The :py:func:`einsum` language is extended inside :py:func:`xmap`
  to additionally allow contractions that involve named axes.  Broadcasting of
  named axes happens *by name*, i.e. all axes with equal names are expected to
  have equal shapes in all arguments of a broadcasting operation, while the
  result has a (set) union of all named axes.  The positional semantics of the
  program remain unchanged, and broadcasting still implicitly right-aligns
  positional axes for unification. For an extended description of the
  :py:func:`xmap` programming model, please refer to the :py:func:`xmap`
  tutorial notebook in main JAX documentation.

  Note that since all top-level JAX expressions are interpreted in the NumPy
  programming model, :py:func:`xmap` can also be seen as an adapter that
  converts a function that uses named axes (including in arguments and returned
  values) into one that takes and returns values that only have positional
  axes.

  The default lowering strategy of :py:func:`xmap` converts all named axes into
  positional axes, working similarly to multiple applications of
  :py:func:`vmap`. However, this behavior can be further customized by the
  ``axis_resources`` argument.  When specified, each axis introduced by
  :py:func:`xmap` can be assigned to one or more *resource axes*. Those include
  the axes of the hardware mesh, as defined by the :py:class:`Mesh` context
  manager. Each value that has a named axis in its ``named_shape`` will be
  partitioned over all mesh axes that axis is assigned to. Hence,
  :py:func:`xmap` can be seen as an alternative to :py:func:`pmap` that also
  exposes a way to automatically partition the computation over multiple
  devices.

  .. warning::
    While it is possible to assign multiple axis names to a single resource axis,
    care has to be taken to ensure that none of those named axes co-occur in a
    ``named_shape`` of any value in the named program. At the moment this is
    **completely unchecked** and will result in **undefined behavior**. The
    final release of :py:func:`xmap` will enforce this invariant, but it is a
    work in progress.

    Note that you do not have to worry about any of this for as long as no
    resource axis is repeated in ``axis_resources.values()``.

  Note that any assignment of ``axis_resources`` doesn\'t ever change the
  results of the computation, but only how it is carried out (e.g. how many
  devices are used).  This makes it easy to try out various ways of
  partitioning a single program in many distributed scenarios (both small- and
  large-scale), to maximize the performance.  As such, :py:func:`xmap` can be
  seen as a way to seamlessly interpolate between :py:func:`vmap` and
  :py:func:`pmap`-style execution.

  Args:
    fun: Function that uses named axes. Its arguments and return
      value should be arrays, scalars, or (nested) standard Python containers
      (tuple/list/dict) thereof (in general: valid pytrees).
    in_axes: A Python object with the same container (pytree) structure as the
      signature of arguments to ``fun``, but with a positional-to-named axis
      mapping in place of every array argument. The valid positional-to-named
      mappings are: (1) a ``Dict[int, AxisName]`` specifying that a positional
      dimensions given by dictionary keys are to be converted to named axes
      of given names (2) a list of axis names that ends with the Ellipsis object
      (``...``) in which case a number of leading positional axes of the argument
      will be converted into named axes inside the function. Note that ``in_axes``
      can also be a prefix of the argument container structure, in which case the
      mapping is repeated for all arrays in the collapsed subtree.
    out_axes: A Python object with the same container (pytree) structure as the
      returns of ``fun``, but with a positional-to-named axis mapping in place
      of every returned array. The valid positional-to-named mappings are the same
      as in ``in_axes``. Note that ``out_axes`` can also be a prefix of the return
      container structure, in which case the mapping is repeated for all arrays
      in the collapsed subtree.
    axis_sizes: A dict mapping axis names to their sizes. All axes defined by xmap
      have to appear either in ``in_axes`` or ``axis_sizes``. Sizes of axes
      that appear in ``in_axes`` are inferred from arguments whenever possible.
      In multi-host scenarios, the user-specified sizes are expected to be the
      global axis sizes (and might not match the expected size of local inputs).
    axis_resources: A dictionary mapping the axes introduced in this
      :py:func:`xmap` to one or more resource axes. Any array that has in its
      shape an axis with some resources assigned will be partitioned over the
      resources associated with the respective resource axes.
    donate_argnums: Specify which argument buffers are "donated" to the computation.
      It is safe to donate argument buffers if you no longer need them once the
      computation has finished. In some cases XLA can make use of donated
      buffers to reduce the amount of memory needed to perform a computation,
      for example recycling one of your input buffers to store a result. You
      should not reuse buffers that you donate to a computation, JAX will raise
      an error if you try to.

      For more details on buffer donation see the `FAQ <https://jax.readthedocs.io/en/latest/faq.html#buffer-donation>`_.

    backend: This is an experimental feature and the API is likely to change.
      Optional, a string representing the XLA backend. \'cpu\', \'gpu\', or \'tpu\'.

  Returns:
    A version of ``fun`` that takes in arrays with positional axes in place of
    named axes bound in this :py:func:`xmap` call, and results with all named
    axes converted to positional axes. If ``axis_resources`` is specified,
    ``fun`` can additionally execute in parallel on multiple devices.

  For example, :py:func:`xmap` makes it very easy to convert a function that
  computes the vector inner product (such as :py:func:`jax.numpy.vdot`) into
  one that computes a matrix multiplication:

  >>> import jax.numpy as jnp
  >>> x = jnp.arange(10).reshape((2, 5))
  >>> xmap(jnp.vdot,
  ...      in_axes=({0: \'left\'}, {1: \'right\'}),
  ...      out_axes=[\'left\', \'right\', ...])(x, x.T)
  Array([[ 30,  80],
         [ 80, 255]], dtype=int32)

  Note that the contraction in the program is performed over the positional axes,
  while named axes are just a convenient way to achieve batching. While this
  might seem like a silly example at first, it might turn out to be useful in
  practice, since with conjunction with ``axis_resources`` this makes it possible
  to implement a distributed matrix-multiplication in just a few lines of code::

    devices = np.array(jax.devices())[:4].reshape((2, 2))
    with Mesh(devices, (\'x\', \'y\')):  # declare a 2D mesh with axes \'x\' and \'y\'
      distributed_out = xmap(
        jnp.vdot,
        in_axes=({0: \'left\'}, {1: \'right\'}),
        out_axes=[\'left\', \'right\', ...],
        axis_resources={\'left\': \'x\', \'right\': \'y\'})(x, x.T)

  Still, the above examples are quite simple. After all, the xmapped
  computation was a simple NumPy function that didn\'t use the axis names at all!
  So, let\'s explore a slightly larger example which is linear regression::

    def regression_loss(x, y, w, b):
      # Contract over in_features. Batch and out_features are present in
      # both inputs and output, so they don\'t need to be mentioned
      y_pred = jnp.einsum(\'{in_features},{in_features}->{}\', x, w) + b
      error = jnp.sum((y - y_pred) ** 2, axis=\'out_features\')
      return jnp.mean(error, axis=\'batch\')

    xmap(regression_loss,
         in_axes=([\'batch\', \'in_features\', ...],
                  [\'batch\', \'out_features\', ...],
                  [\'in_features\', \'out_features\', ...],
                  [\'out_features\', ...]),
         out_axes={})  # Loss is reduced over all axes, including batch!

  .. note::
    When using ``axis_resources`` along with a mesh that is controlled by
    multiple JAX hosts, keep in mind that in any given process :py:func:`xmap`
    only expects the data slice that corresponds to its local devices to be
    specified. This is in line with the current multi-host :py:func:`pmap`
    programming model.
  '''
def xmap_impl(fun: lu.WrappedFun, *args, name, in_axes, out_axes_thunk, donated_invars, global_axis_sizes, axis_resources, resource_env, backend, spmd_in_axes, spmd_out_axes_thunk): ...
def make_xmap_callable(fun: lu.WrappedFun, name, in_axes, out_axes_thunk, donated_invars, global_axis_sizes, axis_resources, resource_env, backend, spmd_in_axes, spmd_out_axes_thunk, lowering_parameters: mlir.LoweringParameters, *in_avals): ...

class EvaluationPlan(NamedTuple):
    """Encapsulates preprocessing common to top-level xmap invocations and its translation rule."""
    resource_env: ResourceEnv
    physical_axis_resources: dict[AxisName, tuple[ResourceAxisName, ...]]
    loop_axis_resources: dict[AxisName, tuple[ResourceAxisName, ...]]
    axis_subst_dict: dict[AxisName, tuple[ResourceAxisName, ...]]
    axis_vmap_size: dict[AxisName, int | None]
    @property
    def axis_subst(self) -> core.AxisSubst: ...
    @property
    def resource_axis_env(self): ...
    @classmethod
    def from_axis_resources(cls, axis_resources: dict[AxisName, tuple[ResourceAxisName, ...]], resource_env: ResourceEnv, global_axis_sizes: dict[AxisName, int]): ...
    def subst_axes_with_resources(self, jaxpr): ...
    def vectorize_and_loop(self, f: lu.WrappedFun, in_axes, out_axes) -> lu.WrappedFun: ...
    def to_mesh_axes(self, in_axes, out_axes: Incomplete | None = None):
        """
    Convert in/out_axes parameters ranging over logical dimensions to
    in/out_axes that range over the mesh dimensions.
    """

class XMapPrimitive(core.MapPrimitive):
    def __init__(self) -> None: ...
    def bind(self, fun, *args, in_axes, **params): ...
    def process(self, trace, fun, tracers, params): ...
    def post_process(self, trace, out_tracers, params): ...
    def get_bind_params(self, params): ...

xmap_p: Incomplete

def out_local_named_shapes(local_axes, *args, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...

class ResourceCount(NamedTuple):
    nglobal: int
    nlocal: int | None
    distributed: bool
    def to_local(self, global_size): ...

def hide_mapped_axes(flat_in_axes, flat_out_axes, *flat_args) -> Generator[Incomplete, Incomplete, Incomplete]: ...

class NoQuotesStr(str): ...
