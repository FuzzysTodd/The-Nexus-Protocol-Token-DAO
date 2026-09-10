import enum
from torch.fx.graph import Node as Node
from typing import Any, Callable, Dict, List, NamedTuple

class NSSingleResultValuesType(str, enum.Enum):
    WEIGHT: str
    NODE_OUTPUT: str
    NODE_INPUT: str

class NSSubgraph(NamedTuple):
    start_node: Node
    end_node: Node
    base_op_node: Node
NSSingleResultType = Dict[str, Any]
NSResultsType = Dict[str, Dict[str, Dict[str, List[NSSingleResultType]]]]
NSNodeTargetType = Callable | str
