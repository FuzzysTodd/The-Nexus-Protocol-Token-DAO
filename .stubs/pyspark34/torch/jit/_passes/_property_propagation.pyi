from torch import TensorType as TensorType
from torch._C import Graph as Graph
from typing import Any, List

def apply_input_props_using_example(graph: Graph, example_input: List[Any]):
    """
    Applies properties for each tensor in the graph inputs
    using the example supplied.
    """
