from torch import nn as nn
from torch.ao.quantization.utils import MatchAllNode as MatchAllNode
from torch.fx import Node as Node
from torch.nn.utils import parametrize as parametrize
from typing import Any, Dict, List, Tuple

def apply_match(modules: Dict[str, nn.ModuleDict], pattern: Tuple[Any] | Any, node: Node, matched_node_pattern: List[Node]) -> List[Node] | None:
    """
    This function will return the matched nodes if the pattern matches the node given
    If there is no match, it will return None
    """
