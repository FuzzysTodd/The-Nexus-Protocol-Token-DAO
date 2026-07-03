from _typeshed import Incomplete
from tensorflow.compiler.tf2xla.python import xla as xla
from tensorflow.core.framework import full_type_pb2 as full_type_pb2
from tensorflow.python.eager import context as context, def_function as def_function, execute as execute
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, func_graph as func_graph, ops as ops, smart_cond as smart_cond, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, data_flow_ops as data_flow_ops, gen_array_ops as gen_array_ops, gen_image_ops as gen_image_ops, gen_linalg_ops as gen_linalg_ops, gen_list_ops as gen_list_ops, gen_math_ops as gen_math_ops, gen_nn_ops as gen_nn_ops, gen_optional_ops as gen_optional_ops, gen_parsing_ops as gen_parsing_ops, gen_random_ops as gen_random_ops, gen_sparse_ops as gen_sparse_ops, gen_spectral_ops as gen_spectral_ops, handle_data_util as handle_data_util, linalg_ops as linalg_ops, list_ops as list_ops, manip_ops as manip_ops, map_fn as map_fn, math_ops as math_ops, nn_ops as nn_ops, parsing_ops as parsing_ops, resource_variable_ops as resource_variable_ops, sparse_ops as sparse_ops, special_math_ops as special_math_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.platform import flags as flags
from tensorflow.python.util import compat as compat, nest as nest, object_identity as object_identity
from typing import NamedTuple

passthrough_stateful_ops: Incomplete
force_stateful_ops: Incomplete

class WhileOp:
    """Object for storing state for converting the outputs of a while_loop."""
    def __init__(self, exit_node, pfor_ops, fallback_to_while_loop, pfor_config) -> None:
        """Initializer.

    Args:
      exit_node: A tensor output from the while_loop.
      pfor_ops: list of ops inside the current pfor loop.
      fallback_to_while_loop: If True, fallback to while loop when conversion of
        an op is not supported
      pfor_config: PForConfig object used while constructing loop body.
    """
    @property
    def inputs(self):
        """Input to all the Enter nodes."""
    @property
    def control_inputs(self):
        """Control input to all the Enter nodes."""
    @property
    def outputs(self):
        """Outputs of all the Exit nodes."""
    @property
    def name(self):
        """Context name for the while loop."""
    @property
    def is_inside_loop(self):
        """Returns true if the while_loop was created inside the pfor."""
    def op_is_inside_loop(self, op):
        """True if op was created inside the pfor loop body."""
    @property
    def is_stateful(self): ...
    @property
    def pfor_converter(self):
        """Return a converter for the while loop."""
    def __call__(self, pfor_input):
        """Converter for the while_loop.

    The conversion of a while_loop is another while_loop.

    The arguments to this converted while_loop are as follows:
    not_all_done: Boolean scalar Tensor indicating if all the pfor iterations
      are done.
    indices: int32 1-D Tensor storing the id of the iterations that are not
      done.
    args: Remaining arguments. These can be divided into 3 categories:
      - First set of arguments are the tensors that correspond to the initial
        elements of self._enters. The elements that appear in original while
        loop's `loop_vars`.
      - The second set of arguments are the tensors that correspond to the
        remaining elements of self._enters. These are the tensors that directly
        enter the original while loop body.
       - Finally, the last set of arguments are TensorArrays. These TensorArrays
         correspond to the outputs of the original while_loop, i.e. to the
         elements in self._outputs. Each TensorArray has `PFor.loop_len`
         elements, i.e. the number of pfor iterations. At the end, the i'th
         element of each TensorArray will contain the output computed by the
         i'th iteration of pfor. Note that elements can be written into these
         tensors arrays in any order, depending on when the corresponding pfor
         iteration is done.
      If the original while_loop had `k` tensors in its `loop_vars` and its body
      directly captured `m` tensors, the `args` will contain `2 * k + m` values.

    In each iteration, the while_loop body recomputes the condition for all
    active pfor iterations to see which of them are now done. It then partitions
    all the inputs and passes them along to the converted body. Values for all
    the iterations that are done are written to TensorArrays indexed by the pfor
    iteration number. When all iterations are done, the TensorArrays are stacked
    to get the final value.

    Args:
      pfor_input: A PForInput object corresponding to the output of any Exit
        node from this while loop.

    Returns:
      List of converted outputs.
    """

class ConversionNotImplementedError(Exception): ...

class _PforInput:
    """Input object passed to registered pfor converters."""
    pfor: Incomplete
    def __init__(self, pfor, op, inputs) -> None:
        """Creates a _PforInput object.

    Args:
      pfor: PFor converter object.
      op: the Operation object that is being converted.
      inputs: list of WrappedTensor objects representing converted values of the
        inputs of `op`.
    """
    def stack_inputs(self, stack_indices: Incomplete | None = None, tile_variants: bool = False) -> None:
        """Stacks unstacked inputs at `stack_indices`.

    Args:
      stack_indices: indices of inputs at which stacking is done. If None,
        stacking is done at all indices.
      tile_variants: If True, affected indices which have a variant dtype will
        be tiled after this operation to match the expected shape of a
        vectorized tensor. Variants generally need to be un-tiled when they are
        inputs to operations and tiled when returned.
    """
    def expanddim_inputs_for_broadcast(self):
        """Reshapes stacked inputs to prepare them for broadcast.

    Since stacked inputs have an extra leading dimension, automatic broadcasting
    rules could incorrectly try to expand dimensions before that leading
    dimension. To avoid that, we reshape these stacked inputs to the maximum
    rank they will need to be broadcasted to.
    """
    @property
    def inputs(self): ...
    @property
    def num_inputs(self): ...
    def input(self, index): ...
    def stacked_input(self, index): ...
    def unstacked_input(self, index): ...
    @property
    def op(self): ...
    @property
    def op_type(self): ...
    def get_attr(self, attr): ...
    @property
    def outputs(self): ...
    def output(self, index): ...

class RegisterPFor:
    '''Utility to register converters for pfor.

  Usage:
  @RegisterPFor(foo_op_type)
  def _foo_converter(pfor_input):
    ...

  The above will register conversion function `_foo_converter` for handling
  conversion of `foo_op_type`. These converters are called during vectorization
  of a `pfor` loop body. For each operation node in this loop body,
  the vectorization process will call the converter corresponding to the
  operation type of the node.

  During conversion, the registered function will be called with a single
  argument `pfor_input`, of type `PForInput`, which will contain state needed
  for the conversion.  When the converter is called for a node, all its inputs
  should already have been converted and these converted values are stored in
  `pfor_input.inputs`.  This registered function should output a list of
  WrappedTensor objects with the same length as the number of outputs of the
  node being converted. If the node had zero outputs, then it should return an
  ops.Operation object.  These new sets of nodes should implement the
  functionality of running that operation for the number of iterations specified
  by `pfor_input.pfor.loop_len_vector[0]` where the inputs of the node for each
  iteration are picked from `pfor_inputs.inputs()`.

  One tricky aspect of the conversion process is keeping track of, and
  leveraging loop invariance of computation. Each converted input is a
  WrappedTensor which indicates whether the input was loop invariant or not. If
  the converted value is loop invariant, its rank should match the rank of the
  corresponding tensor in the loop body, else its rank is larger by 1. The
  converter should look at the loop invariance of the inputs and generate new
  nodes based on that. Note that the converter will not be called if all inputs
  are loop invariant and the operation is not stateful. The converter should
  determine if its own output is loop invariant and `wrap` its output
  accordingly.

  Example:

  Here, the converter is trying to convert a Reshape node in the loop body. This
  node will have two inputs: the tensor to reshape, and the new shape.  The
  example here only handles the case where the shape is loop invariant.

  @RegisterPFor("Reshape")
  def _convert_reshape(pfor_input):
    # We assume that input is not loop invariant. Call to `stacked_input`
    # asserts that and returns the converted value. This value will have a rank
    # larger by 1 compared to the rank of the input in the loop body.
    t = pfor_input.stacked_input(0)

    # We assume that shape input is loop invariant. Call to `unstacked_input`
    # asserts that and returns the converted value.
    shape = pfor_input.unstacked_input(1)

    # We compute `new_shape` by prepending the number of iterations to the
    # original shape.
    new_shape = array_ops.concat([pfor_input.pfor.loop_len_vector, shape],
                                 axis=0)

    # The vectorized output involves reshaping the converted input `t` using
    # `new_shape`.
    new_output = array_ops.reshape(t, new_shape)

    # The converted output is marked as not loop invariant using the call to
    # wrap.
    return wrap(new_output, True)
  '''
    op_type: Incomplete
    def __init__(self, op_type) -> None:
        """Creates an object to register a converter for op with type `op_type`."""
    def __call__(self, converter): ...

class RegisterPForWithArgs(RegisterPFor):
    """Utility to register converters for pfor.

  Usage:
  @RegisteRPFor(foo_op_type, foo=value, ....)
  def _foo_converter(pfor_input, foo=None, ....):
    ...

  See RegisterPFor for details on the conversion function.
  `RegisterPForWithArgs` allows binding extra arguments to the
  conversion function at registration time.
  """
    def __init__(self, op_type, *args, **kw_args) -> None: ...
    def __call__(self, converter): ...

class WrappedTensor(NamedTuple):
    t: Incomplete
    is_stacked: Incomplete
    is_sparse_stacked: Incomplete

def wrap(tensor, is_stacked: bool = True, is_sparse_stacked: bool = False):
    """Helper to create a WrappedTensor object."""

class PForConfig:
    """A configuration object used to communicate with loop body function."""
    def __init__(self) -> None: ...
    def reduce(self, fn, *args):
        """Performs reduction `fn` on `args` vectorized across pfor iterations.

    Note that `fn` is traced once inside the loop function context. Hence any
    captures or side-effects will happen in that context. Call to the traced
    version of `fn` happens during the construction of the vectorized code.

    Note that this currently may not work inside a control flow construct.
    Args:
      fn: a reduction function. It will be called with arguments that have the
        same structure as *args but with individual values whose rank may be
        higher by 1 since they represent loop invariant vectorized versions of
        the corresponding Tensors in *args.
      *args: unvectorized Tensors.

    Returns:
      The result of running `fn` on the vectorized versions of `*args`. These
      outputs will be available as loop invariant values to all the iterations.
    """
    def reduce_concat(self, x):
        """Performs a concat reduction on `x` across pfor iterations.

    Note that this currently may not work inside a control flow construct.
    Args:
      x: an unvectorized Tensor.

    Returns:
      A Tensor that has rank one higher than `x`. The value is the vectorized
      version of `x`, i.e. stacking the value of `x` across different pfor
      iterations.
    """
    def reduce_mean(self, x):
        """Performs a mean reduction on `x` across pfor iterations.

    Note that this currently may not work inside a control flow construct.
    Args:
      x: an unvectorized Tensor.

    Returns:
      A Tensor that has same rank as `x`. The value is the mean of the values
      of `x` across the pfor iterations.
    """
    def reduce_sum(self, x):
        """Performs a sum reduction on `x` across pfor iterations.

    Note that this currently may not work inside a control flow construct.
    Args:
      x: an unvectorized Tensor.

    Returns:
      A Tensor that has same rank as `x`. The value is the sum of the values
      of `x` across the pfor iterations.
    """

class PFor:
    '''Implementation of rewrite of parallel-for loops.

  This class takes a DAG or a set of DAGs representing the body of a
  parallel-for loop, and adds new operations to the graph that implements
  functionality equivalent to running that loop body for a specified number of
  iterations. This new set of nodes may or may not use a tensorflow loop
  construct.

  The process of conversion does not delete or change any existing operations.
  It only adds operations that efficiently implement the equivalent
  functionality. We refer to the added ops as "converted ops".

  The conversion process uses a simple greedy heuristic. It walks the loop body
  and tries to express the functionality of running each node in a loop with a
  new set of nodes. When converting an op several cases are possible:
  - The op is not inside the loop body. Hence it can be used as is.
  - The op does not depend on the iteration number and is stateless. In this
    case, it can be used as is.
  - The op is not stateful, and depends on iteration number only through control
    dependencies. In this case, we can create a single op with same inputs and
    attributes, but with "converted" control dependencies.
  - The op is not stateful, and all its inputs are loop invariant. In this
    case, similar to above, we can create a single op with same inputs and
    attributes, but with "converted" control dependencies.
  - The op is stateful or at least one of the inputs is not loop invariant. In
    this case, we run the registered converter for that op to create a set of
    converted ops. All nodes in the set will have converted control dependencies
    corresponding to control dependencies of the original op. If the op returned
    multiple outputs, "converted outputs" could be produced by different ops in
    this set.
  '''
    all_indices: Incomplete
    def __init__(self, loop_var, loop_len, pfor_ops, fallback_to_while_loop, all_indices: Incomplete | None = None, all_indices_partitioned: bool = False, pfor_config: Incomplete | None = None, warn: bool = False) -> None:
        """Creates an object to rewrite a parallel-for loop.

    Args:
      loop_var: ops.Tensor output of a Placeholder operation. The value should
        be an int32 scalar representing the loop iteration number.
      loop_len: A scalar or scalar Tensor representing the number of iterations
        the loop is run for.
      pfor_ops: List of all ops inside the loop body.
      fallback_to_while_loop: If True, on failure to vectorize an op, a while
        loop is used to sequentially execute that op.
      all_indices: If not None, an int32 vector with size `loop_len`
        representing the iteration ids that are still active. These values
        should be unique and sorted. However they may not be contiguous. This is
        typically the case when inside a control flow construct which has
        partitioned the indices of the iterations that are being converted.
      all_indices_partitioned: If True, this object is being constructed from a
        control flow construct where not all the pfor iterations are guaranteed
        to be active.
      pfor_config: PForConfig object used while constructing the loop body.
      warn: Whether or not to warn on while loop conversions.
    """
    def op_is_inside_loop(self, op):
        """True if op was created inside the pfor loop body."""
    def convert(self, y):
        '''Returns the converted value corresponding to y.

    Args:
      y: A ops.Tensor or a ops.Operation object. If latter, y should not have
        any outputs.

    Returns:
      If y does not need to be converted, it returns y as is. Else it returns
      the "converted value" corresponding to y.
    '''
    @property
    def loop_len_vector(self):
        """Returns a single element vector whose value is number of iterations."""
    @property
    def loop_var(self):
        """Returns placeholder loop variable."""
    @property
    def pfor_ops(self): ...
    @property
    def pfor_config(self): ...
    @property
    def all_indices_partitioned(self):
        """all_indices_partitioned property.

    Returns:
      True if we are inside a control flow construct and not all pfor iterations
      may be active.
    """
    @property
    def fallback_to_while_loop(self): ...

class WhileV2:
    """Object for vectorizing V2 while_loop op."""
    def __init__(self, pfor_input) -> None: ...
    def __call__(self):
        """Converter for the V2 while_loop.

    The conversion of a while_loop is another while_loop.

    The arguments to this converted while_loop are as follows:
    not_all_done: Boolean scalar Tensor indicating if all the pfor iterations
      are done.
    indices: int32 1-D Tensor storing the id of the pfor iterations that are not
      done.
    args: Remaining arguments. These can be divided into 2 categories:
      - The first set of arguments correspond one-to-one to the inputs to the
        unvectorized while_loop.
      - The second set are TensorArrays, corresponding one-to-one to each output
        of the unvectorized while_loop. Each TensorArray has `PFor.loop_len`
        elements, i.e. the number of pfor iterations. At the end, the i'th
        element of each TensorArray will contain the output computed by the i'th
        iteration of pfor. Note that elements can be written into these tensors
        arrays in any order, depending on when the corresponding pfor iteration
        is done.
    In each iteration, the while_loop body recomputes the condition for all
    active pfor iterations to see which of them are now done. It then partitions
    all the inputs and passes them along to the converted body. Values for all
    the iterations that are done are written to TensorArrays indexed by the pfor
    iteration number. When all iterations are done, the TensorArrays are stacked
    to get the final value.

    Returns:
      List of converted outputs.
    """
