from _typeshed import Incomplete
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, graph_pb2 as graph_pb2, tensor_shape_pb2 as tensor_shape_pb2, variable_pb2 as variable_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2, meta_graph_pb2 as meta_graph_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, errors as errors, graph_util as graph_util, ops as ops, tensor_util as tensor_util
from tensorflow.python.grappler import tf_optimizer as tf_optimizer
from tensorflow.python.ops import array_ops as array_ops, variables as variables
from tensorflow.python.training.saver import export_meta_graph as export_meta_graph
from tensorflow.python.util import deprecation as deprecation, lazy_loader as lazy_loader, object_identity as object_identity
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

wrap_function: Incomplete
VAR_ASSIGN_COLLECTION: str

class _TensorData(NamedTuple('_TensorData', [('numpy', Incomplete), ('dtype', Incomplete), ('index', Incomplete)])):
    """Data about a tensor that was converted to a constant."""
    @property
    def dtype_attr(self): ...

class _EndPoint(NamedTuple('_EndPoint', [('convertible', Incomplete), ('index', Incomplete)])):
    """An endpoint in a graph."""
class _Edge(NamedTuple('_Edge', [('source', Incomplete), ('destination', Incomplete)])):
    """A directed graph edge."""

class _Convertible:
    """An entity that can have variables converted to constants."""
    def __init__(self, enclosing_graph) -> None: ...
    def converted_self(self) -> None:
        """A copy of this Convertible to be modified during conversion.

    Returns:
      Implementations should return the copied instance, which in turn should
      be contained in converted_enclosing_graph(). This instance is the one that
      will be modified during conversion. Its main use will be in the
      implementations of convert_variable_to_constant().
    """
    def convert_variable_to_constant(self, incoming_edge, tensor_data) -> None:
        """Converts a variable in this Convertible and its dependencies.

    This method should make sure that a converted copy of itself is present in
    the converted graph, and that all Convertibles depending on this one also go
    through the same process.

    Args:
      incoming_edge: The graph edge into this Convertible that is being
        converted to a constant.
      tensor_data: The tensor representing the constant.
    """
    def create_edges(self) -> None:
        """Calls add_outgoing_edge for all edges known to this Convertible.

    This is used to build the graph dependencies, so that conversion of
    variables to constants can be properly propagated through the graph. Usually
    this method will call add_outgoing_edge() to all the Convertible inputs.
    """
    def add_outgoing_edge(self, edge) -> None:
        """Adds an outgoing edge to the Convertible's list of edges.

    Args:
      edge: The outgoing edge (its source should be 'self').
    """
    @property
    def converted_enclosing_graph(self):
        """The graph being converted."""
    @property
    def outgoing_edges(self):
        """The list of edges starting at this Convertible."""

class _Function(_Convertible):
    """A library function Convertible.

  Edges into functions are edges from node _inputs_ into function _inputs_:
  Functions get their input from their callers, not from node outputs, and the
  callers in turn get those values as inputs.
  """
    def __init__(self, function, enclosing_graph) -> None: ...
    @property
    def function(self): ...
    @property
    def nodes(self): ...
    def converted_self(self):
        """The Function copy to be converted.

    The copy will be renamed according to the graph's converted_function_name
    map, to ensure the name does not match anything currently in TensorFlow's
    function cache.

    Returns:
      The function instance to be converted.
    """
    def convert_variable_to_constant(self, incoming_edge, tensor_data) -> None:
        """Converts one function argument into a constant.

    Args:
      incoming_edge: The edge into the argument to be converted.
      tensor_data: The constant value.
    """
    def create_edges(self) -> None: ...

class _Node(_Convertible):
    """A Convertible NodeDef."""
    def __init__(self, node, function, enclosing_graph) -> None: ...
    @staticmethod
    def new(node, function, enclosing_graph):
        """Creates a new _Node base on its operation type."""
    @property
    def node(self): ...
    @property
    def container(self):
        """The node container (either a graph or a function)."""
    def converted_self(self):
        """The NodeDef to be converted.

    Returns:
      The NodeDef to be converted, which can come from either a graph for a
      function. Derived classes should call this (via 'super') to make sure the
      node is retrieved from the right place.
    """
    def convert_variable_to_constant(self, incoming_edge, tensor_data) -> None: ...
    def create_edges(self) -> None: ...
    def resolve_input(self, input_name):
        '''Resolves an input into its _EndPoint.

    A NodeDef\'s input name can refer to either global NodeDefs (in the
    GraphDef\'s node list), a NodeDef in a function\'s node list, or a Function
    (in the GraphDef\'s function library). The name can also carry semantic
    information, depending on whether it starts with "^". This method handles
    all that logic in order to find the object to which the input name refers
    to.

    Args:
      input_name: The input name to resolve.

    Returns:
      The object referred to by \'input_name\'.
    '''
    def update_dtype(self, attr_name, index, dtype) -> None:
        """Changes the type of a given input.

    Args:
      attr_name: The NodeDef attribute containing the type to change.
      index: The index of the input type to change.
      dtype: The type to change to.
    """

class _Intermediate(_Node):
    """Specialization of _Node to intermediate ops."""
    def convert_variable_to_constant(self, incoming_edge, tensor_data) -> None: ...

class _Merge(_Node):
    """Specialization of _Node to Merge ops."""
    def convert_variable_to_constant(self, incoming_edge, tensor_data) -> None: ...

class _VarHandle(_Node):
    """Specialization of _Node to VarHandleOp."""
    def convert_variable_to_constant(self, incoming_edge, tensor_data) -> None: ...

class _ResourceGather(_Node):
    """Specialization of _Node to ResourceGather."""
    def convert_variable_to_constant(self, incoming_edge, tensor_data) -> None: ...

class _ResourceGatherNd(_Node):
    """Specialization of _Node to ResourceGatherNd."""
    def convert_variable_to_constant(self, incoming_edge, tensor_data) -> None: ...

class _ReadVariable(_Node):
    """Specialization of _Node to ReadVariableOp."""
    def convert_variable_to_constant(self, incoming_edge, tensor_data) -> None: ...

class _FunctionCaller(_Node):
    """A base class for Convertibles that reference functions."""
    def __init__(self, node, function, enclosing_graph, first_function_input, type_attribute, function_attributes) -> None:
        """Initializes a _FunctionCaller.

    Args:
      node: As in _Node.
      function: As in _Node.
      enclosing_graph: As in _Node.
      first_function_input: The index of the first NodeDef input that is tied to
        the function inputs. It is assumed that the rest of the NodeDef inputs
        map one to one to function inputs.
      type_attribute: The name of the NodeDef attribute that defines the input
        types. It is assumed that the types listed here map one-to-one with the
        function inputs (that is, they do _not_ specify types for inputs that
        are not passed to functions).
      function_attributes: The names of the NodeDef attributes containing
        references to functions.
    """
    def converted_self(self): ...
    def convert_variable_to_constant(self, incoming_edge, tensor_data) -> None: ...
    def create_edges(self) -> None:
        """Creates edges related to a function caller.

    Edges from a function caller to its called functions are always edges from
    _inputs_ to _inputs_: a FunctionDef input is given by the caller, based on
    its own inputs.
    """

class _If(_FunctionCaller):
    """Specialization of _Node to If-like operations."""
    def __init__(self, node, function, enclosing_graph) -> None: ...

class _Case(_FunctionCaller):
    """Specialization of _Node to Case-like operations."""
    def __init__(self, node, function, enclosing_graph) -> None: ...

class _PartitionedCall(_FunctionCaller):
    """Specialization of _Node to PartitionedCall-like operations."""
    def __init__(self, node, function, enclosing_graph) -> None: ...

class _While(_FunctionCaller):
    """Specialization of _Node to While-like operations."""
    def __init__(self, node, function, enclosing_graph) -> None: ...
    def convert_variable_to_constant(self, incoming_edge, tensor_data) -> None: ...

class _GraphDef(_Convertible):
    """A convertible GraphDef."""
    def __init__(self, graph_def) -> None: ...
    @property
    def graph_def(self): ...
    @property
    def nodes(self): ...
    @property
    def functions(self): ...
    @property
    def converted_function_names(self):
        """Map from original to new function names.

    In order to avoid conflicts (two functions with the same name, one converted
    and one not), we need to change the name of every converted function to
    something that is hopefully unique.

    Returns:
      Map from original to new suggested function names.
    """
    def rename_function(self, old_name, new_name) -> None: ...
    def is_converted_function(self, function_name): ...
    def converted_self(self): ...
    def create_edges(self) -> None: ...

class _ConverterData:
    """Container for constant conversion supporting data.

  The data includes the graph being converted, and the pre-converted
  tensors. This class will be specialized for ConcreteFunction and Session-based
  conversions, as the means to obtain that data is different for each case.
  """
    def __init__(self, graph_def, variable_names_allowlist: Incomplete | None = None, variable_names_denylist: Incomplete | None = None) -> None: ...
    @property
    def graph_def(self):
        """The graph to be converted."""
    @property
    def node_defs(self):
        """All the node defs in the graph to be converted.

    Returns:
      A map from node name to the NodeDef for all NodeDefs in the graph, as well
      as all control flow NodeDefs in the functions.
    """
    @property
    def tensor_data(self):
        """A map from tensor name to its converted _TensorData."""

class _FunctionConverterData(_ConverterData):
    """Container for ConcreteFunction-based conversion data."""
    def __init__(self, func, lower_control_flow, aggressive_inlining, variable_names_allowlist: Incomplete | None = None, variable_names_denylist: Incomplete | None = None) -> None:
        """Creates the conversion data for the given function.

    Args:
      func: ConcreteFunction.
      lower_control_flow: Boolean indicating whether or not to lower control
        flow ops such as If and While.
      aggressive_inlining: Boolean indicating whether or not to do aggressive
        function inlining (might be unsafe if function has stateful ops, not
        properly connected to control outputs).
      variable_names_allowlist: The set of variable names to convert (by
        default, all variables are converted).
      variable_names_denylist: The set of variable names to omit converting to
        constants.
    """

class _FunctionConverterDataInEager(_FunctionConverterData):
    """Container for ConcreteFunction-based conversion data in Eager mode."""

class _FunctionConverterDataInGraph(_FunctionConverterData):
    """Container for ConcreteFunction-based conversion data in Graph mode."""
    def __init__(self, func, lower_control_flow, aggressive_inlining, variable_names_allowlist: Incomplete | None = None, variable_names_denylist: Incomplete | None = None, session: Incomplete | None = None) -> None:
        """Creates the conversion data for the given function.

    Args:
      func: ConcreteFunction.
      lower_control_flow: Boolean indicating whether or not to lower control
        flow ops such as If and While.
      aggressive_inlining: Boolean indicating whether or not to do aggressive
        function inlining (might be unsafe if function has stateful ops, not
        properly connected to control outputs).
      variable_names_allowlist: The set of variable names to convert (by
        default, all variables are converted).
      variable_names_denylist: The set of variable names to omit converting to
        constants.
      session: Session object.
    """

class _SessionConverterData(_ConverterData):
    """Container for Session-based conversion data."""
    def __init__(self, session, graph_def, output_node_names, variable_names_allowlist: Incomplete | None = None, variable_names_denylist: Incomplete | None = None) -> None: ...

def disable_lower_using_switch_merge(graph_def):
    """Set '_lower_using_switch_merge' attributes to False.

  Sets the attribute to False in the NodeDefs in the main graph and the NodeDefs
  in each function's graph.

  Args:
    graph_def: GraphDef proto.

  Returns:
    GraphDef
  """
def convert_variables_to_constants_v2(func, lower_control_flow: bool = True, aggressive_inlining: bool = False):
    """Replaces all the variables in a graph with constants of the same values.

  TensorFlow 2.0 function for converting all Variable ops into Const ops holding
  the same values. This makes it possible to describe the network fully with a
  single GraphDef file, and allows the removal of a lot of ops related to
  loading and saving the variables. This function runs Grappler's function
  inlining optimization in order to return a single subgraph.

  The current implementation only works for graphs that do not contain any
  control flow or embedding related ops.

  Args:
    func: ConcreteFunction.
    lower_control_flow: Boolean indicating whether or not to lower control flow
      ops such as If and While. (default True)
    aggressive_inlining: Boolean indicating whether or not to do aggressive
      function inlining (might be unsafe if function has stateful ops, not
      properly connected to control outputs). (default False)

  Returns:
    ConcreteFunction containing a simplified version of the original.
  """
def convert_var_to_const_function_in_v1(func, lower_control_flow: bool = True, aggressive_inlining: bool = False):
    """Replaces all the variables in a graph with constants of the same values.

  This function works as same as convert_variables_to_constants_v2, but it
  should be used in Graph mode. It is a temporary solution when users want to
  integrate their models written in TF2 with infra that requires TF1 mode.

  The current implementation only works for graphs that do not contain any
  control flow or embedding related ops.

  The function must be called in a Session context.

  Args:
    func: ConcreteFunction.
    lower_control_flow: Boolean indicating whether or not to lower control flow
      ops such as If and While. (default True)
    aggressive_inlining: Boolean indicating whether or not to do aggressive
      function inlining (might be unsafe if function has stateful ops, not
      properly connected to control outputs). (default False)

  Raises:
      RuntimeError: If no Session context is present.

  Returns:
    ConcreteFunction containing a simplified version of the original.
  """
def convert_variables_to_constants_v2_as_graph(func, lower_control_flow: bool = True, aggressive_inlining: bool = False):
    """Replaces all the variables in a graph with constants of the same values.

  This function works as same as convert_variables_to_constants_v2, but it
  returns the intermediate `GraphDef` as well. This `GraphDef` contains all the
  debug information after all the transformations in the frozen phase.

  Args:
    func: ConcreteFunction.
    lower_control_flow: Boolean indicating whether or not to lower control flow
      ops such as If and While. (default True)
    aggressive_inlining: Boolean indicating whether or not to do aggressive
      function inlining (might be unsafe if function has stateful ops, not
      properly connected to control outputs).

  Returns:
    ConcreteFunction containing a simplified version of the original, and also
    the intermediate GraphDef containing the node debug information for the
    transformations in the frozen phase.
  """
def convert_variables_to_constants_from_session_graph(session, graph_def, output_node_names, variable_names_allowlist: Incomplete | None = None, variable_names_denylist: Incomplete | None = None):
    """Replaces all the variables in a graph with constants of the same values.

  This function works similarly to convert_variables_to_constants_v2, but it
  retrieves the constant values from a Session instead of from a
  ConcreteFunction. This is useful when converting graphs generated from
  TensorFlow V1, where ConcreteFunctions are not available. This also differs
  from graph_util.convert_variables_to_constants in that it supports resource
  variables when V2 control flow constructions are present.

  Args:
    session: Active TensorFlow session containing the variables.
    graph_def: A GraphDef to convert.
    output_node_names: List of name strings for the result nodes of the graph.
    variable_names_allowlist: The set of variable names to convert (by default,
      all variables are converted).
    variable_names_denylist: The set of variable names to omit converting to
      constants.

  Returns:
    An optimized GraphDef.
  """
def convert_variables_to_constants(sess, input_graph_def, output_node_names, variable_names_whitelist: Incomplete | None = None, variable_names_blacklist: Incomplete | None = None):
    """Replaces all the variables in a graph with constants of the same values.

  If you have a trained graph containing Variable ops, it can be convenient to
  convert them all to Const ops holding the same values. This makes it possible
  to describe the network fully with a single GraphDef file, and allows the
  removal of a lot of ops related to loading and saving the variables.

  Args:
    sess: Active TensorFlow session containing the variables.
    input_graph_def: GraphDef object holding the network.
    output_node_names: List of name strings for the result nodes of the graph.
    variable_names_whitelist: The set of variable names to convert (by default,
      all variables are converted).
    variable_names_blacklist: The set of variable names to omit converting to
      constants.

  Returns:
    GraphDef containing a simplified version of the original.

  Raises:
    RuntimeError: if a DT_RESOURCE op is found whose ancestor Variables are both
      denylisted AND whitelisted for freezing.
  """
