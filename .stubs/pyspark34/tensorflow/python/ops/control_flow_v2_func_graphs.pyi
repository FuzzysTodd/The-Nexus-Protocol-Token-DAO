from tensorflow.python.framework import func_graph as func_graph, ops as ops

class ControlFlowFuncGraph(func_graph.FuncGraph):
    """Contains control flow-specific FuncGraph logic."""
    is_control_flow_graph: bool
    def __init__(self, *args, **kwargs) -> None: ...

class CondBranchFuncGraph(ControlFlowFuncGraph):
    """FuncGraph for branches of tf.cond().

  This is used to distinguish cond branches from other functions.
  """
class WhileCondFuncGraph(ControlFlowFuncGraph):
    """FuncGraph for the condition of tf.while_loop().

  This is used to distinguish while conditions from other functions.
  """
class WhileBodyFuncGraph(ControlFlowFuncGraph):
    """FuncGraph for the body of tf.while_loop().

  This is used to distinguish while bodies from other functions.
  """
