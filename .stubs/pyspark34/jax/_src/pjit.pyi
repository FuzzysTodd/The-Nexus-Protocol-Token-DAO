import dataclasses
import threading
from _typeshed import Incomplete
from collections.abc import Iterable, Sequence
from jax._src import api as api, core as core, dispatch as dispatch, op_shardings as op_shardings, sharding_impls as sharding_impls, source_info_util as source_info_util, stages as stages, traceback_util as traceback_util, tree_util as tree_util
from jax._src.api_util import argnames_partial_except as argnames_partial_except, argnums_partial_except as argnums_partial_except, check_callable as check_callable, debug_info as debug_info, donation_vector as donation_vector, flatten_axes as flatten_axes, flatten_fun as flatten_fun, flatten_fun_nokwargs as flatten_fun_nokwargs, jaxpr_debug_info as jaxpr_debug_info, resolve_argnums as resolve_argnums, result_paths as result_paths, shaped_abstractify as shaped_abstractify
from jax._src.config import config as config
from jax._src.errors import JAXTypeError as JAXTypeError
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, pxla as pxla, xla as xla
from jax._src.lib import xla_client as xc, xla_extension_version as xla_extension_version
from jax._src.lib.mlir import ir as ir
from jax._src.partition_spec import PartitionSpec as PartitionSpec
from jax._src.sharding_impls import AUTO as AUTO, GSPMDSharding as GSPMDSharding, NamedSharding as NamedSharding, ParsedPartitionSpec as ParsedPartitionSpec, PmapSharding as PmapSharding, SingleDeviceSharding as SingleDeviceSharding, SpecSync as SpecSync, UNSPECIFIED as UNSPECIFIED, UnspecifiedValue as UnspecifiedValue, XLACompatibleSharding as XLACompatibleSharding, XLADeviceAssignment as XLADeviceAssignment, get_single_pspec as get_single_pspec, is_auto as is_auto, is_unspecified as is_unspecified, is_unspecified_or_auto as is_unspecified_or_auto, parse_flatten_op_sharding as parse_flatten_op_sharding, prepare_axis_resources as prepare_axis_resources
from jax._src.traceback_util import api_boundary as api_boundary
from jax._src.tree_util import all_leaves as all_leaves, broadcast_prefix as broadcast_prefix, generate_key_paths as generate_key_paths, prefix_errors as prefix_errors, tree_flatten as tree_flatten, tree_map as tree_map, tree_structure as tree_structure, tree_unflatten as tree_unflatten, treedef_is_leaf as treedef_is_leaf, treedef_tuple as treedef_tuple
from jax._src.util import HashableFunction as HashableFunction, distributed_debug_log as distributed_debug_log, flatten as flatten, merge_lists as merge_lists, safe_map as safe_map, safe_zip as safe_zip, split_list as split_list, unflatten as unflatten, weakref_lru_cache as weakref_lru_cache, wraps as wraps
from typing import Any, Callable, NamedTuple

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
PjitSharding = GSPMDSharding | UnspecifiedValue | AUTO
PjitShardingMinusUnspecified = GSPMDSharding | AUTO
MeshSharding = NamedSharding | UnspecifiedValue | AUTO
MeshShardingMinusUnspecified = NamedSharding | AUTO
logger: Incomplete

class _MostRecentPjitCallExecutable(threading.local):
    weak_key_dict: Incomplete
    def __init__(self) -> None: ...

def pre_infer_params(fun, in_shardings, out_shardings, donate_argnums, donate_argnames, static_argnums, static_argnames, device, backend, abstracted_axes): ...
def post_infer_params(fun, infer_params_fn, static_argnums, static_argnames, donate_argnums, abstracted_axes, pjit_has_explicit_sharding): ...

class PjitInfo(NamedTuple):
    fun: Callable
    in_shardings: Any
    out_shardings: Any
    static_argnums: tuple[int, ...]
    static_argnames: tuple[str, ...]
    donate_argnums: tuple[int, ...]
    donate_argnames: tuple[str, ...]
    device: xc.Device | None
    backend: str | None
    keep_unused: bool
    inline: bool
    resource_env: Any
    abstracted_axes: Any | None

def common_infer_params(pjit_info_args, *args, **kwargs): ...
def pjit(fun: Callable, in_shardings=..., out_shardings=..., static_argnums: int | Sequence[int] | None = None, static_argnames: str | Iterable[str] | None = None, donate_argnums: int | Sequence[int] | None = None, donate_argnames: str | Iterable[str] | None = None, keep_unused: bool = False, device: xc.Device | None = None, backend: str | None = None, inline: bool = False, abstracted_axes: Any | None = None) -> stages.Wrapped:
    '''Makes ``fun`` compiled and automatically partitioned across multiple devices.

  NOTE: This function is now equivalent to jax.jit please use that instead.
  The returned function has semantics equivalent to those of ``fun``, but is
  compiled to an XLA computation that runs across multiple devices
  (e.g. multiple GPUs or multiple TPU cores). This can be useful if the jitted
  version of ``fun`` would not fit in a single device\'s memory, or to speed up
  ``fun`` by running each operation in parallel across multiple devices.

  The partitioning over devices happens automatically based on the
  propagation of the input partitioning specified in ``in_shardings`` and
  the output partitioning specified in ``out_shardings``. The resources
  specified in those two arguments must refer to mesh axes, as defined by
  the :py:func:`jax.sharding.Mesh` context manager. Note that the mesh
  definition at :func:`~pjit` application time is ignored, and the returned function
  will use the mesh definition available at each call site.

  Inputs to a :func:`~pjit`\'d function will be automatically partitioned across devices
  if they\'re not already correctly partitioned based on ``in_shardings``.
  In some scenarios, ensuring that the inputs are already correctly pre-partitioned
  can increase performance. For example, if passing the output of one
  :func:`~pjit`\'d function to another :func:`~pjit`’d function (or the same
  :func:`~pjit`’d function in a loop), make sure the relevant
  ``out_shardings`` match the corresponding ``in_shardings``.

  .. note::
    **Multi-process platforms:** On multi-process platforms such as TPU pods,
    :func:`~pjit` can be used to run computations across all available devices across
    processes. To achieve this, :func:`~pjit` is designed to be used in SPMD Python
    programs, where every process is running the same Python code such that all
    processes run the same :func:`~pjit`\'d function in the same order.

    When running in this configuration, the mesh should contain devices across
    all processes. However, any input argument dimensions partitioned over
    multi-process mesh axes should be of size equal to the corresponding *local*
    mesh axis size, and outputs will be similarly sized according to the local
    mesh. ``fun`` will still be executed across *all* devices in the mesh,
    including those from other processes, and will be given a global view of the
    data spread across multiple processes as a single array. However, outside
    of :func:`~pjit` every process only "sees" its local piece of the input and output,
    corresponding to its local sub-mesh.

    This means that each process\'s participating local devices must form a
    _contiguous_ local sub-mesh within the full global mesh. A contiguous
    sub-mesh is one where all of its devices are adjacent within the global
    mesh, and form a rectangular prism.

    The SPMD model also requires that the same multi-process :func:`~pjit`\'d
    functions must be run in the same order on all processes, but they can be
    interspersed with arbitrary operations running in a single process.

  Args:
    fun: Function to be compiled. Should be a pure function, as side-effects may
      only be executed once. Its arguments and return value should be arrays,
      scalars, or (nested) standard Python containers (tuple/list/dict) thereof.
      Positional arguments indicated by ``static_argnums`` can be anything at
      all, provided they are hashable and have an equality operation defined.
      Static arguments are included as part of a compilation cache key, which is
      why hash and equality operators must be defined.
    in_shardings: Pytree of structure matching that of arguments to ``fun``,
      with all actual arguments replaced by resource assignment specifications.
      It is also valid to specify a pytree prefix (e.g. one value in place of a
      whole subtree), in which case the leaves get broadcast to all values in
      that subtree.

      The ``in_shardings`` argument is optional. JAX will infer the shardings
      from the input :py:class:`jax.Array`\'s, and defaults to replicating the input
      if the sharding cannot be inferred.

      The valid resource assignment specifications are:

      - :py:class:`XLACompatibleSharding`, which will decide how the value
        will be partitioned. With this, using a mesh context manager is not
        required.
      - :py:obj:`None` is a special case whose semantics are:
          - if the mesh context manager is *not* provided, JAX has the freedom to
            choose whatever sharding it wants.
            For in_shardings, JAX will mark is as replicated but this behavior
            can change in the future.
            For out_shardings, we will rely on the XLA GSPMD partitioner to
            determine the output shardings.
          - If the mesh context manager is provided, None will imply that the
            value will be replicated on all devices of the mesh.
      - For backwards compatibility, in_shardings still supports ingesting
        :py:class:`PartitionSpec`. This option can *only* be used with the
        mesh context manager.

        - :py:class:`PartitionSpec`, a tuple of length at most equal to the rank
          of the partitioned value. Each element can be a :py:obj:`None`, a mesh
          axis or a tuple of mesh axes, and specifies the set of resources assigned
          to partition the value\'s dimension matching its position in the spec.

      The size of every dimension has to be a multiple of the total number of
      resources assigned to it.
    out_shardings: Like ``in_shardings``, but specifies resource
      assignment for function outputs.
      The ``out_shardings`` argument is optional. If not specified, :py:func:`jax.jit`
      will use GSPMD\'s sharding propagation to determine how to shard the outputs.
    static_argnums: An optional int or collection of ints that specify which
      positional arguments to treat as static (compile-time constant).
      Operations that only depend on static arguments will be constant-folded in
      Python (during tracing), and so the corresponding argument values can be
      any Python object.

      Static arguments should be hashable, meaning both ``__hash__`` and
      ``__eq__`` are implemented, and immutable. Calling the jitted function
      with different values for these constants will trigger recompilation.
      Arguments that are not arrays or containers thereof must be marked as
      static.

      If ``static_argnums`` is not provided, no arguments are treated as static.
    static_argnames: An optional string or collection of strings specifying
      which named arguments to treat as static (compile-time constant). See the
      comment on ``static_argnums`` for details. If not
      provided but ``static_argnums`` is set, the default is based on calling
      ``inspect.signature(fun)`` to find corresponding named arguments.
    donate_argnums: Specify which positional argument buffers are "donated" to
      the computation. It is safe to donate argument buffers if you no longer
      need them once the computation has finished. In some cases XLA can make
      use of donated buffers to reduce the amount of memory needed to perform a
      computation, for example recycling one of your input buffers to store a
      result. You should not reuse buffers that you donate to a computation, JAX
      will raise an error if you try to. By default, no argument buffers are
      donated.

      If neither ``donate_argnums`` nor ``donate_argnames`` is provided, no
      arguments are donated. If ``donate_argnums`` is not provided but
      ``donate_argnames`` is, or vice versa, JAX uses
      :code:`inspect.signature(fun)` to find any positional arguments that
      correspond to ``donate_argnames``
      (or vice versa). If both ``donate_argnums`` and ``donate_argnames`` are
      provided, ``inspect.signature`` is not used, and only actual
      parameters listed in either ``donate_argnums`` or ``donate_argnames`` will
      be donated.

      For more details on buffer donation see the
      `FAQ <https://jax.readthedocs.io/en/latest/faq.html#buffer-donation>`_.
    donate_argnames: An optional string or collection of strings specifying
      which named arguments are donated to the computation. See the
      comment on ``donate_argnums`` for details. If not
      provided but ``donate_argnums`` is set, the default is based on calling
      ``inspect.signature(fun)`` to find corresponding named arguments.
    keep_unused: If `False` (the default), arguments that JAX determines to be
      unused by `fun` *may* be dropped from resulting compiled XLA executables.
      Such arguments will not be transferred to the device nor provided to the
      underlying executable. If `True`, unused arguments will not be pruned.
    device: This argument is deprecated. Please put your arguments on the
      device you want before passing them to jit.
      Optional, the Device the jitted function will run on. (Available devices
      can be retrieved via :py:func:`jax.devices`.) The default is inherited
      from XLA\'s DeviceAssignment logic and is usually to use
      ``jax.devices()[0]``.
    backend: This argument is deprecated. Please put your arguments on the
      backend you want before passing them to jit.
      Optional, a string representing the XLA backend: ``\'cpu\'``, ``\'gpu\'``, or
      ``\'tpu\'``.

  Returns:
    A wrapped version of ``fun``, set up for just-in-time compilation and
    automatically partitioned by the mesh available at each call site.

  For example, a convolution operator can be automatically partitioned over
  an arbitrary set of devices by a single :func:`~pjit` application:

  >>> import jax
  >>> import jax.numpy as jnp
  >>> import numpy as np
  >>> from jax.sharding import Mesh, PartitionSpec
  >>> from jax.experimental.pjit import pjit
  >>>
  >>> x = jnp.arange(8, dtype=jnp.float32)
  >>> f = pjit(lambda x: jax.numpy.convolve(x, jnp.asarray([0.5, 1.0, 0.5]), \'same\'),
  ...         in_shardings=None, out_shardings=PartitionSpec(\'devices\'))
  >>> with Mesh(np.array(jax.devices()), (\'devices\',)):
  ...   print(f(x))  # doctest: +SKIP
  [ 0.5  2.   4.   6.   8.  10.  12.  10. ]
  '''
def hashable_pytree(pytree): ...
def flatten_axis_resources(what, tree, shardings, tupled_args): ...

class PytreeLeaf: ...

def pjit_check_aval_sharding(shardings, flat_avals, names: tuple[str, ...] | None, what_aval: str, allow_uneven_sharding: bool): ...

pjit_p: Incomplete

@dataclasses.dataclass(frozen=True)
class SameDeviceAssignmentTuple:
    shardings: tuple[PjitSharding, ...]
    device_assignment: XLADeviceAssignment | None
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __init__(self, shardings, device_assignment) -> None: ...

def pjit_staging_rule(trace, *args, **params): ...
def dce_jaxpr_pjit_rule(used_outputs: list[bool], eqn: core.JaxprEqn) -> tuple[list[bool], core.JaxprEqn | None]: ...
def with_sharding_constraint(x, shardings):
    """Mechanism to constrain the sharding of an Array inside a jitted computation

  This is a strict constraint for the GSPMD partitioner and not a hint. For examples
  of how to use this function, see `Distributed arrays and automatic parallelization`_.

  Args:
    x: PyTree of jax.Arrays which will have their shardings constrained
    shardings: PyTree of sharding specifications. Valid values are the same as for
      the ``in_shardings`` argument of :func:`jax.experimental.pjit`.
  Returns:
    x_with_shardings: PyTree of jax.Arrays with specified sharding constraints.

  .. _Distributed arrays and automatic parallelization: https://jax.readthedocs.io/en/latest/notebooks/Distributed_arrays_and_automatic_parallelization.html
  """

sharding_constraint_p: Incomplete

def to_gspmd_sharding(s: XLACompatibleSharding, ndim: int, device_or_backend_set: bool = False) -> GSPMDSharding: ...
def get_unconstrained_dims(sharding: NamedSharding): ...
def get_op_sharding_from_executable(executable) -> tuple[Sequence[xc.OpSharding], Sequence[xc.OpSharding]]: ...
def get_pspec_from_executable(executable, mesh: pxla.Mesh) -> tuple[tuple[PartitionSpec, ...], tuple[PartitionSpec, ...]]: ...
