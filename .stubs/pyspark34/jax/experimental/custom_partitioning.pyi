from _typeshed import Incomplete
from jax import tree_util as tree_util
from jax._src import core as core, custom_api_util as custom_api_util, sharding_impls as sharding_impls
from jax._src.api_util import argnums_partial as argnums_partial, flatten_fun_nokwargs as flatten_fun_nokwargs
from jax._src.interpreters import mlir as mlir
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax.errors import UnexpectedTracerError as UnexpectedTracerError

class _ShardingCallbackInfo:
    propagate_user_sharding: Incomplete
    partition: Incomplete
    to_mesh_pspec_sharding: Incomplete
    in_tree: Incomplete
    out_tree: Incomplete
    infer_sharding_from_operands: Incomplete
    module_context: Incomplete
    mesh: Incomplete
    static_args: Incomplete
    def __init__(self, propagate_user_sharding, partition, to_mesh_pspec_sharding, in_tree, out_tree, infer_sharding_from_operands, module_context, mesh, static_args) -> None: ...
    def unflatten_arg_shape(self, s, sharding): ...
    def unflatten_arg_shapes(self, arg_shapes, arg_shardings): ...

custom_partitioning_p: Incomplete

class custom_partitioning:
    """Inserts a CustomCallOp into the XLA graph with custom SPMD lowering rules.

  .. code-block:: python

    @custom_partitioning
    def f(*args):
      return ...

    def propagate_user_sharding(mesh, user_shape):
      '''Update the sharding of the op from a user's shape.sharding.'''
      user_sharding = jax.tree_map(lambda x: x.sharding, user_shape)

    def partition(mesh, arg_shapes, result_shape):
      def lower_fn(*args):
        ... builds computation on per-device shapes ...
      result_shardings = jax.tree_map(lambda x: x.sharding, result_shape)
      arg_shardings = jax.tree_map(lambda x: x.sharding, arg_shapes)
      # result_sharding and arg_shardings may optionally be modified and the
      # partitioner will insert collectives to reshape.
      return mesh, lower_fn, result_sharding, arg_shardings

    def infer_sharding_from_operands(mesh, arg_shapes, shape):
      '''Compute the result sharding from the sharding of the operands.'''
      arg_shardings = jax.tree_map(lambda x: x.sharding, arg_shapes)


    f.def_partition(partition, propagate_user_sharding, infer_sharding_from_operands)

  The args to ``def_partition`` are as follows:

  * ``propagate_user_sharding``: Callable which takes the sharding of a user (in the dag)
    and returns a suggestion for a new `NamedSharding`. The default
    implementation is just to return the suggested sharding.
  * ``partition``: Callable which takes the SPMD suggested partition shapes and
    partition specs and returns the mesh, a per-shard lowering function, and the final
    input and output sharding specs (the SPMD partitioner will repartition the
    inputs to match). The mesh is returned to allow configuring axis_names for
    collectives when no mesh is provided.
  * ``infer_sharding_from_operands``: Callable which computes an output ``NamedSharding``
    from the ``NamedSharding`` chosen for each argument.
  * ``decode_shardings``: When set to True, convert input ``GSPMDSharding``s to
    ``NamedSharding`` if possible. This may not be possible if the user does not
    provide a contextual mesh.

  Positional arguments can be specified as static using static_argnums. JAX uses
  :code:`inspect.signature(fun)` to resolve these positional arguments.

  Example:

    As an example, assume we want to enhance the existing ``jax.numpy.fft.fft``. This function computes
    the discrete Fourier transform of an N-dimensional input along the last dimension, and is batched
    along the first N-1 dimensions.
    By default, however, it will ignore the sharding of the input and gather the input on all devices.
    However, since ``jax.numpy.fft.fft`` is batched along the first N-1 dimensions,
    this is unnecessary. We will create a new ``my_fft`` op that, instead, does not alter the sharding
    along the first `N-1` dimensions, and only gathers the input along the last dimension if needed.

    .. code-block:: python

      import jax
      from jax.sharding import NamedSharding
      from jax.experimental.custom_partitioning import custom_partitioning
      from jax.experimental.pjit import pjit
      from jax.sharding import PartitionSpec as P
      from jax.sharding import Mesh
      from jax.numpy.fft import fft
      import regex as re
      import numpy as np

      # Pattern to detect all-gather or dynamic-slice in the generated HLO
      _PATTERN = '(dynamic-slice|all-gather)'

      # For an N-D input, keeps sharding along the first N-1 dimensions
      # but replicate along the last dimension
      def supported_sharding(sharding, shape):
          rank = len(shape.shape)
          max_shared_dims = min(len(sharding.spec), rank-1)
          names = tuple(sharding.spec[:max_shared_dims]) + tuple(None for _ in range(rank - max_shared_dims))
          return NamedSharding(sharding.mesh, P(*names))

      def partition(mesh, arg_shapes, result_shape):
          result_shardings = jax.tree_map(lambda x: x.sharding, result_shape)
          arg_shardings = jax.tree_map(lambda x: x.sharding, arg_shapes)
          return mesh, fft,               supported_sharding(arg_shardings[0], arg_shapes[0]),               (supported_sharding(arg_shardings[0], arg_shapes[0]),)

      def infer_sharding_from_operands(mesh, arg_shapes, result_shape):
          arg_shardings = jax.tree_map(lambda x: x.sharding, arg_shapes)
          return supported_sharding(arg_shardings[0], arg_shapes[0])

      @custom_partitioning
      def my_fft(x):
          return fft(x)

      my_fft.def_partition(
          infer_sharding_from_operands=infer_sharding_from_operands,
          partition=partition)

    Now create a 2D array sharded along the first axis, pass it through ``my_fft``
    and notice how it is still sharded as expected, and identical to the output
    of ``fft``. However, inspecting the HLO
    (using ``lower(x).compile().runtime_executable().hlo_modules()``) reveals that
    ``my_fft`` does not create any all-gather or dynamic-slice, while ``fft`` does.

    .. code-block::

      with Mesh(np.array(jax.devices()), ('x',)):
        x = np.asarray(np.random.randn(32*1024, 1024), dtype=np.complex64)
        y = pjit(lambda x: x, in_shardings=None, out_shardings=P('x'))(x)
        pjit_my_fft = pjit(my_fft, in_shardings=P('x'), out_shardings=P('x'))
        pjit_fft    = pjit(fft,    in_shardings=P('x'), out_shardings=P('x'))
        print(pjit_my_fft(y))
        print(pjit_fft(y))
        # dynamic-slice or all-gather are not present in the HLO for my_fft, because x is a 2D array
        assert(re.search(_PATTERN, pjit_my_fft.lower(x).compile().runtime_executable().hlo_modules()[0].to_string()) is None)
        # dynamic-slice or all-gather are present in the HLO for fft
        assert(re.search(_PATTERN, pjit_fft.lower(x).compile().runtime_executable().hlo_modules()[0].to_string())    is not None)

    .. code-block::

      # my_fft
      [[-38.840824   +0.j        -40.649452  +11.845365j
      ...
        -1.6937828  +0.8402481j  15.999859   -4.0156755j]]

      # jax.numpy.fft.fft
      [[-38.840824   +0.j        -40.649452  +11.845365j
        ...
        -1.6937828  +0.8402481j  15.999859   -4.0156755j]]

    Because of the logic in ``supported_sharding``, ``my_fft`` also works on 1-dimensional arrays.
    However, in this case, the HLO of ``my_fft`` does show a a dynamic-slice, since the last dimension
    is the dimension along which FFTs are calculated and needs to be replicated on all devices before
    the computation can be done.

    .. code-block::

      with Mesh(np.array(jax.devices()), ('x',)):
        x = np.asarray(np.random.randn(32*1024*1024), dtype=np.complex64)
        y = pjit(lambda x: x, in_shardings=None, out_shardings=P('x'))(x)
        pjit_my_fft = pjit(my_fft, in_shardings=P('x'), out_shardings=P('x'))
        pjit_fft    = pjit(fft,    in_shardings=P('x'), out_shardings=P('x'))
        print(pjit_my_fft(y))
        print(pjit_fft(y))
        # dynamic-slice or all-gather are present in the HLO for my_fft, because x is a 1D array
        assert(re.search(_PATTERN, pjit_my_fft.lower(x).compile().runtime_executable().hlo_modules()[0].to_string()) is None)
        # dynamic-slice or all-gather are present in the HLO for fft
        assert(re.search(_PATTERN, pjit_fft.lower(x).compile().runtime_executable().hlo_modules()[0].to_string())    is not None)

    .. code-block::

      # my_fft
      [    7.217285   +0.j     -3012.4937  +4287.635j   -405.83594 +3042.984j
      ...  1422.4502  +7271.4297j  -405.84033 -3042.983j
      -3012.4963  -4287.6343j]

      # jax.numpy.fft.fft
      [    7.217285   +0.j     -3012.4937  +4287.635j   -405.83594 +3042.984j
      ...  1422.4502  +7271.4297j  -405.84033 -3042.983j
      -3012.4963  -4287.6343j]

  """
    fun: Incomplete
    partition: Incomplete
    static_argnums: Incomplete
    propagate_user_sharding: Incomplete
    infer_sharding_from_operands: Incomplete
    def __init__(self, fun, static_argnums=()) -> None: ...
    __getattr__: Incomplete
    decode_shardings: Incomplete
    def def_partition(self, partition, infer_sharding_from_operands, propagate_user_sharding: Incomplete | None = None, decode_shardings: bool = True): ...
    def __call__(self, *args, **kwargs): ...
