from _typeshed import Incomplete
from tensorflow.python.util.all_util import remove_undocumented as remove_undocumented

class OpHint:
    '''A class that helps build tflite function invocations.

  It allows you to take a bunch of TensorFlow ops and annotate the construction
  such that toco knows how to convert it to tflite. This embeds a pseudo
  function in a TensorFlow graph. This allows embedding high-level API usage
  information in a lower level TensorFlow implementation so that an alternative
  implementation can be substituted later.

  Essentially, any "input" into this pseudo op is fed into an identity, and
  attributes are added to that input before being used by the constituent ops
  that make up the pseudo op. A similar process is done to any output that
  is to be exported from the current op.

  '''
    FUNCTION_NAME_ATTR: str
    FUNCTION_UUID_ATTR: str
    FUNCTION_INPUT_INDEX_ATTR: str
    FUNCTION_OUTPUT_INDEX_ATTR: str
    FUNCTION_SORT_INDEX_ATTR: str
    FUNCTION_AGGREGATE_ATTR: str
    TFLITE_INPUT_INDICES: str
    FUNCTION_LEVEL_ATTR: str
    CHILDREN_INPUTS_MAPPINGS: str
    AGGREGATE_STACK: str
    AGGREGATE_FIRST: str
    AGGREGATE_LAST: str
    class OpHintArgumentTracker:
        '''Conceptually tracks indices of arguments of "OpHint functions".

    The inputs and arguments of these functions both use an instance
    of the class so they can have independent numbering.
    '''
        def __init__(self, function_name, unique_function_id, node_name_prefix, attr_name, level: int = 1, children_inputs_mappings: Incomplete | None = None) -> None:
            """Initialize ophint argument.

      Args:
        function_name: Name of the function that this tracks arguments for.
        unique_function_id: UUID of function that this tracks arguments for.
        node_name_prefix: How identities that are created are named.
        attr_name: Name of attribute to use to store the index for this hint.
          i.e. FUNCTION_INPUT_INDEX or FUNCTION_OUTPUT_INDEX
        level: Hierarchical level of the Ophint node, a number.
        children_inputs_mappings: Inputs/Outputs mapping for children hints.
      """
        def add(self, arg, tag: Incomplete | None = None, name: Incomplete | None = None, aggregate: Incomplete | None = None, index_override: Incomplete | None = None):
            """Return a wrapped tensor of an input tensor as an argument.

      Args:
        arg: A TensorFlow tensor that should be considered an argument.
        tag: String tag to identify arguments that should be packed.
        name: Name of argument. This is included in the Identity hint op names.
        aggregate: Strategy to aggregate.
        Acceptable values are OpHint.AGGREGATE_FIRST, OpHint.AGGREGATE_LAST,
          and OpHint.AGGREGATE_STACK.
          Note, aggregate is only valid if tag is specified.
        index_override: Specify what input/output index should this be in the
          final stub. i.e. add(arg0, index=1); add(arg1, index=0) will make the
          final stub be as stub_func(inputs[arg1, arg0], outputs=[]) rather than
          the default call order based ordering.

      Returns:
        A tensor representing the wrapped argument.

      Raises:
        ValueError: When indices are not consistent.
      """
    def __init__(self, function_name, level: int = 1, children_inputs_mappings: Incomplete | None = None, **kwargs) -> None:
        '''Create a OpHint.

    Args:
      function_name: Name of the function (the custom op name in tflite)
      level: OpHint level.
      children_inputs_mappings: Children OpHint inputs/outputs mapping.
        children_inputs_mappings should like below:
        "parent_first_child_input":
            [{"parent_input_index": num, "child_input_index": num}, ...]
        "parent_last_child_output":
            [{"parent_output_index": num, "child_output_index": num}, ...]
        "internal_children_input_output":
            [{"child_input_index": num, "child_output_index": num}, ...]
      **kwargs: Keyword arguments of any constant attributes for the function.
    '''
    def add_input(self, *args, **kwargs):
        '''Add a wrapped input argument to the hint.

    Args:
      *args: The input tensor.
      **kwargs:
        "name" label
        "tag" a tag to group multiple arguments that will be aggregated. I.e.
          a string like \'cool_input\'. Basically multiple inputs can be added
          to the same hint for parallel operations that will eventually be
          combined. An example would be static_rnn which creates multiple copies
          of state or inputs.
        "aggregate" aggregation strategy that is valid only for tag non None.
          Acceptable values are OpHint.AGGREGATE_FIRST, OpHint.AGGREGATE_LAST,
          and OpHint.AGGREGATE_STACK.
        "index_override" The global index to use. This corresponds to the
          argument order in the final stub that will be generated.
    Returns:
      The wrapped input tensor.
    '''
    def add_output(self, *args, **kwargs):
        '''Add a wrapped output argument to the hint.

    Args:
      *args: The output tensor.
      **kwargs:
        "name" label
        "tag" a tag to group multiple arguments that will be aggregated. I.e.
          a string like \'cool_input\'. Basically multiple inputs can be added
          to the same hint for parallel operations that will eventually be
          combined. An example would be static_rnn which creates multiple copies
          of state or inputs.
        "aggregate" aggregation strategy that is valid only for tag non None.
          Acceptable values are OpHint.AGGREGATE_FIRST, OpHint.AGGREGATE_LAST,
          and OpHint.AGGREGATE_STACK.
        "index_override" The global index to use. This corresponds to the
          argument order in the final stub that will be generated.
    Returns:
      The wrapped output tensor.
    '''
    def add_inputs(self, *args, **kwargs):
        """Add a sequence of inputs to the function invocation.

    Args:
      *args: List of inputs to be converted (should be Tf.Tensor).
      **kwargs: This allows 'names' which should be a list of names.

    Returns:
      Wrapped inputs (identity standins that have additional metadata). These
      are also are also tf.Tensor's.
    """
    def add_outputs(self, *args, **kwargs):
        """Add a sequence of outputs to the function invocation.

    Args:
      *args: List of outputs to be converted (should be tf.Tensor).
      **kwargs: See

    Returns:
      Wrapped outputs (identity standins that have additional metadata). These
      are also tf.Tensor's.
    """

class _LiteOperand:
    """Abstract operand for a tflite hint function._dynamic_rnn_loop.

  This is a base class that handles representing arguments to an OpHint.
  It also is able to serialize operands to the stubbed graph_def.
  Child classes are responsible for being able to
  store information about the hint identity operators. They are also responsible
  for knowing how to serialize to output graphdefs.

  Typically this will be implemented by holding one or more identity nodes
  that were previously discovered as hints.
  """
    def aggregate_and_return_name_for_input(self, out_graphdef) -> None:
        """This adds the node(s) to out_graphdef and returns the input node name.

    Args:
      out_graphdef: A graphdef that is ready to have this input added.

    Returns:
      The output that the stub should use as an input for this operand.

    Raises:
      RuntimeError: if the method is not implemented.
    """
    def aggregate_and_return_name_for_output(self, fused_op_name, output_index, out_graphdef) -> None:
        """Add node(s) to graph representing output operands and returns type.

    Args:
      fused_op_name: name of the fused op stub name.
      output_index: Output index that we are currently processing from stub.
      out_graphdef: The destination graphdef we are currently building up.

    Returns:
      The datatype of this identity.

    Raises:
      RuntimeError: if the method is not implemented.
    """

class _LiteSingleOperand(_LiteOperand):
    """A simple operand that is non-aggregated (i.e. most hints)."""
    node: Incomplete
    name: Incomplete
    def __init__(self, node) -> None: ...
    def flatten(self): ...
    def aggregate_and_return_name_for_input(self, out_graphdef): ...
    def aggregate_and_return_name_for_output(self, fused_op_name, index, out_graphdef): ...

class _LiteAggregateOperand(_LiteOperand):
    """An operand for a tflite hint function that is aggregated from many.

  For example, an LSTM is a grid of operators that are all related. Inputs
  going into them may need to be fused, so they should all be tracked as
  related arguments.
  """
    aggregation: Incomplete
    names: Incomplete
    nodes: Incomplete
    flattened: Incomplete
    def __init__(self, aggregation) -> None: ...
    def add(self, sort, node) -> None: ...
    def flatten_nodes(self):
        """Return a list of all the node protos in aggregation sorted order."""
    def flatten(self):
        """Return a list of all node names in aggregation sorted sorter."""
    def aggregate_and_return_name_for_input(self, out_graphdef):
        """This adds the nodes to out_graphdef and returns an aggregated output.

    In particular, if you have 4 inputs to a hint stub, this will be the
    node that you can use as an output. I.e. you have 4 timesteps from a
    static rnn, then a fused UnidirectionalLSTM will expect 1 input with
    all 4 time steps. So here we make a pack and return the output name of
    that pack.

    Args:
      out_graphdef: A graphdef that is ready to have this input added.

    Returns:
      The name of a pack that aggregates this node.
    """
    def aggregate_and_return_name_for_output(self, fused_op_name, output_index, out_graphdef):
        """This adds to `out_graphdef` all the unaggregated outputs.

    I.e. we are outputting from a fused stub, but we need to make it compatible
    with the unfused original graph so we insert an unpack. Ideally in a later
    stage the unpack -> pack sequences will be removed.

    Args:
      fused_op_name: The name of the stub we are in the process of fusing.
      output_index: The output output_index this object represents.
      out_graphdef: The graphdef we are in the process of buildings

    Returns:
      The type of the aggregated output (so we can finish building the stub
      op).
    """

class _LiteFuncCall:
    """Represent a TensorFlow Lite custom function.

  This is uses to accumulate found hints in the graphdef into a single
  conceptual unit.

  Attributes:
    inputs: inputs to the op (hash from index # to argument)
    outputs: outputs to the op (hash from index # to argument)
    function_name: the tflite custom op name to use
    uuid: a unique call id for this particular call  (i.e. multiple function
      calls would have the same function_name but different uuids.
    params: A param name to key value for op constant data. I.e. for axis on a
      reduction, strides on a convolution, etc.
    level: Level of the OpHint.
    children_inputs_mappings: If the Ophint has children, children inputs
      mappings indicate how their inputs & outputs are mapped.
  """
    inputs: Incomplete
    outputs: Incomplete
    function_name: Incomplete
    uuid: Incomplete
    params: Incomplete
    level: int
    children_inputs_mappings: Incomplete
    def __init__(self) -> None: ...
    def flattened_inputs_and_outputs(self):
        """Return a list of inputs and outputs in a flattened format.

    Returns:
      Tuple of (inputs, outputs). where input and output i a list of names.
    """

def find_all_hinted_output_nodes(session: Incomplete | None = None, graph_def: Incomplete | None = None):
    """Find all Ophints output nodes in the graph.

  This is used to get all the output nodes those are ophinted, it is important
  for operation like convert_variables_to_constants keep all ophints structure.
  Note: only one of session or graph_def should be used, not both.
  Why this can be useful? Some TensorFlow ops (e.g. bidirectional rnn), can
  generate multiple outputs for unfused subgraph. If not all output nodes are
  consumed, graph optimization can potentially drop the unused nodes and cause
  ophints in an invalid states (due to missing ophinted output nodes). So it's
  important for us to find all those hinted output nodes and make sure they're
  not discarded away.

  Args:
    session: A TensorFlow session that contains the graph to convert.
    graph_def: A graph def that we should convert.

  Returns:
    A list of OpHints output nodes.
  Raises:
    ValueError: If both session and graph_def are provided.
  """
def is_ophint_converted(graph_def): ...
def convert_op_hints_to_stubs(session: Incomplete | None = None, graph_def: Incomplete | None = None, write_callback=...):
    """Converts a graphdef with LiteOp hints into stub operations.

  This is used to prepare for toco conversion of complex intrinsic usages.
  Note: only one of session or graph_def should be used, not both.

  Args:
    session: A TensorFlow session that contains the graph to convert.
    graph_def: A graph def that we should convert.
    write_callback: A function pointer that can be used to write intermediate
      steps of graph transformation (optional).

  Returns:
    A new graphdef with all ops contained in OpHints being replaced by
    a single op call with the right parameters.
  Raises:
    ValueError: If both session and graph_def are provided.
  """
