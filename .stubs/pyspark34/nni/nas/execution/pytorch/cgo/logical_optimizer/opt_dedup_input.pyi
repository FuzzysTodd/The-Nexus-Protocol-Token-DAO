from .interface import AbstractOptimizer as AbstractOptimizer
from .logical_plan import AbstractLogicalNode as AbstractLogicalNode, LogicalGraph as LogicalGraph, LogicalPlan as LogicalPlan, OriginNode as OriginNode
from _typeshed import Incomplete
from nni.common.device import GPUDevice as GPUDevice
from nni.nas.evaluator.pytorch.cgo.evaluator import MultiModelSupervisedLearningModule as MultiModelSupervisedLearningModule
from nni.nas.execution.common.graph import Graph as Graph, Model as Model, Node as Node
from nni.nas.utils import uid as uid
from typing import Dict, List, Tuple

class DedupInputNode(AbstractLogicalNode):
    """
    This is logical node representing the node for deduplication.
    In assemble, just return one copy of the original node when multiple models are assembled.
    These models will share the result of once calculation.
    """
    origin_nodes: Incomplete
    related_models: Incomplete
    def __init__(self, logical_graph: LogicalGraph, node_id: int, nodes_to_dedup: List[Node], _internal: bool = False) -> None: ...
    def assemble(self, multi_model_placement: Dict[Model, GPUDevice]) -> Tuple[Node, GPUDevice]: ...

class DedupInputOptimizer(AbstractOptimizer):
    def __init__(self) -> None: ...
    def convert(self, logical_plan: LogicalPlan) -> None: ...
