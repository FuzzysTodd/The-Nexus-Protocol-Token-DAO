import abc
import torch
from ..utils import NodePattern, Pattern
from .custom_config import FuseCustomConfig
from abc import ABC, abstractmethod
from torch.fx.graph import Graph, Node
from typing import Any, Callable, Dict, List

__all__ = ['DefaultFuseHandler', 'FuseHandler']

class FuseHandler(ABC, metaclass=abc.ABCMeta):
    """ Base handler class for the fusion patterns
    """
    def __init__(self, node: Node) -> None: ...
    @abstractmethod
    def fuse(self, load_arg: Callable, named_modules: Dict[str, torch.nn.Module], fused_graph: Graph, root_node: Node, extra_inputs: List[Any], matched_node_pattern: NodePattern, fuse_custom_config: FuseCustomConfig, fuser_method_mapping: Dict[Pattern, torch.nn.Sequential | Callable], is_qat: bool) -> Node: ...

class DefaultFuseHandler(FuseHandler):
    def __init__(self, node: Node) -> None: ...
    def fuse(self, load_arg: Callable, named_modules: Dict[str, torch.nn.Module], fused_graph: Graph, root_node: Node, extra_inputs: List[Any], matched_node_pattern: NodePattern, fuse_custom_config: FuseCustomConfig, fuser_method_mapping: Dict[Pattern, torch.nn.Sequential | Callable], is_qat: bool) -> Node: ...
