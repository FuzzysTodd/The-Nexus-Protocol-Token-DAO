from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_v2_func_graphs as control_flow_v2_func_graphs, default_gradient as default_gradient, gen_data_flow_ops as gen_data_flow_ops, gen_resource_variable_ops as gen_resource_variable_ops, resource_variable_ops as resource_variable_ops

class _GradLoopState:
    """The state used for constructing the gradient graph for a while loop.

  We create a _GradLoopState for each while loop in forward and its
  corresponding while loop in backprop. This gives us access to both
  the forward and the backprop WhileContexts.

  During the construction of gradient graph, any time when we detect
  a forward value that is needed for backprop, we create a history
  accumulator and add it to `history_map`. Any time when we backprop
  a loop switch op (in _SwitchGrad), we add the grad merge op in
  `switch_map`.
  """
    def __init__(self, forward_ctxt, outer_grad_state) -> None: ...
    @property
    def outer_grad_state(self):
        """The grad loop state for outer loop."""
    @property
    def forward_context(self):
        """The while loop context for forward."""
    @property
    def forward_index(self):
        """The loop index of forward loop."""
    @property
    def forward_sync(self):
        """A control trigger node for synchronization in the forward loop.

    One main use is to keep the push ops of a stack executed in the
    iteration order.
    """
    @property
    def grad_context(self):
        """The corresponding WhileContext for gradient."""
    @property
    def grad_index(self):
        """The loop index of backprop loop."""
    @property
    def grad_sync(self):
        """A control trigger node for synchronization in the grad loop.

    One main use is to keep the pop ops of a stack executed in the
    iteration order.
    """
    @property
    def history_map(self):
        """The map that records all the tensors needed for backprop."""
    @property
    def switch_map(self):
        """The map that records all the Switch ops for the while loop."""
    @property
    def unused_exits(self):
        '''The list of "unused" exits.'''
    @property
    def deferred_exits(self):
        '''The list of "deferred" exits.'''
    @property
    def forward_loop_exits(self):
        """The list of exits of the forward loop."""
    @property
    def pending_exits_count(self):
        """The number of exits we expect to see but haven't."""
    @pending_exits_count.setter
    def pending_exits_count(self, cnt) -> None:
        """Set the pending count to cnt."""
    def AddForwardAccumulator(self, value, dead_branch: bool = False):
        """Add an accumulator for each forward tensor that is needed in backprop.

    This is added to the forward loop at the first time when a tensor
    in the forward loop is used by backprop gradient computation loop.
    We create an accumulator that accumulates the value of tensor at each
    iteration. Called in the control flow context where gradients() is called.

    The pseudocode is:
    ```
      acc = stack();
      while (_pivot) {
        acc = stack_push(acc, value);
      }
    ```

    We make sure that the stack push op in one iteration is executed before
    next iteration. This is achieved by adding a control edge from
    `forward_index.op.inputs[0].op` to the push op, and another control
    edge from the push op to either `forward_index.op` or `forward_sync`.

    Args:
      value: The source tensor in forward that is to be accumulated.
      dead_branch: True iff the tensor is on a dead branch of a cond.

    Returns:
      The stack that contains the accumulated history of the tensor.

    Raises:
      TypeError: For internal errors involving the value condition context.
      ValueError: If `value` is inside a XLA scope and a valid max size
        for the stack can't be found.
    """
    def AddBackpropAccumulatedValue(self, history_value, value, dead_branch: bool = False):
        """Add the getter for an accumulated value in the grad context.

    This is added to the backprop loop. Called in the grad context to
    get the value of an accumulated value. The stack pop op must be guarded
    by the pred of the controlling cond.

    Args:
      history_value: The history (a stack) of a value.
      value: The value that is pushed onto the stack.
      dead_branch: True iff the tensor is on a dead branch of a cond.

    Returns:
      The current value (the top of the stack).
    """
    def GetRealValue(self, value):
        '''Get the real value of `value`.

    If backprop "uses" a value produced by forward inference, an accumulator
    is added in the forward loop to accumulate its values.  We use the
    accumulated value. This method must be called in the grad loop context.
    `value` must be in forward and needed for backprop.

    Args:
      value: A tensor to be captured.

    Returns:
      The same tensor obtained from the saved history.
    '''

class _ControlFlowState:
    """Maintain the mapping from the loops to their grad states."""
    def __init__(self) -> None: ...
    def GetGradState(self, op, before):
        """Return the grad state for this op if it's in a forward loop context."""
    def ProcessUnusedLoopExits(self, pending_count, to_ops_set):
        '''Process all the "unused" loop exits.

    The "unused" exits of the loops are added to `unused_exits`. An exit is
    unused if its pending_count is 0. If there is an exit with real gradient,
    all these deferred exits will enter the backprop loop with zero gradient.
    Otherwise, they will enter the backprop loop with None. As an example,
    people often write:

    ```python
    v1, _ = tf.while_loop(p, b, [x1, x2])
    result = gradients(v1, x1)
    ```

    The exit node for x2 is not included by the betweenness analysis. But we
    need to backprop x2 if x2 is involved in computing v1.

    Args:
      pending_count: The number of backprop inputs for every op.
      to_ops_set: The set of ops for ys in gradients(ys, xs)

    Returns:
      The set of unused loop exits that we know at this point we need
      to backprop.
    '''
    def EnterGradWhileContext(self, op, before) -> None:
        """Enter the WhileContext for gradient computation."""
    def ExitGradWhileContext(self, op, before) -> None:
        """Exit the WhileContext for gradient computation."""
    def AddWhileContext(self, op, between_op_list, between_ops) -> None:
        """Add the grad state for the while loop that op belongs to.

    Note that op is an Exit, and this method must be called in
    the control flow context where gradients() is called.

    Note that this method modifies `between_op_list` and `between_ops`.
    """
    def ZerosLikeForExit(self, val):
        """Create zeros_like gradient for a loop exit.

    If the result of a loop variable is not used but is involved in
    computing the result of some needed loop variable, we create a
    zero-valued tensor that is fed as gradient for the Exit node of that
    loop variable. Note that val.op is an Exit, and this method must be
    called in the control flow context where gradients() is called.

    Args:
      val: The output tensor of an Exit op.

    Returns:
      A zero tensor of the same shape of val.
    """
    def ZerosLikeV1WhileLoop(self, op, index):
        """Create zeros_like for the specified output of an op.

    If op is in a while loop that is part of gradients(), this method
    must be called in its grad loop context.

    Args:
      op: A tensorflow operation.
      index: the index for a specific output of the op.

    Returns:
      A zero tensor of the same shape of op.outputs[index].
    """
    def PostProcessing(self) -> None:
        """Perform postprocessing at the end of gradients().

    We have created the gradient graph at this point. So this function
    can be used to perform any postprocessing on the gradient graph.
    We currently perform the following postprocessing:
      1. Patch the gradient graph if the output of a loop variable
         doesn't depend on its input.
    """

def MaybeCreateControlFlowState(between_op_list, between_ops, colocate_gradients_with_ops):
    """Create the state for all the while loops involved in one gradients().

  We create a _ControlFlowState when there are while loops involved in
  gradients(). In gradients(), control flow logic is only invoked when
  the _ControlFlowState is not None.

  Note that this method modifies `between_op_list` and `between_ops`.
  """
def ZerosLike(op, index):
    """Create zeros_like for the specified output of an op."""
