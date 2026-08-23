from _typeshed import Incomplete
from nni.common.device import CPUDevice as CPUDevice, Device as Device
from nni.nas.execution.common.graph import Cell as Cell, Edge as Edge, Graph as Graph, Model as Model, Node as Node
from nni.nas.execution.common.graph_op import Operation as Operation
from nni.retiarii.utils import uid as uid
from typing import Dict, Tuple

class AbstractLogicalNode(Node):
    related_models: Incomplete
    def __init__(self, graph, node_id, name, operation, _internal: bool = False) -> None: ...
    def assemble(self, multi_model_placement: Dict[Model, Device]) -> Tuple[Node, Device]:
        """
        Given a set of models to be formed in a physical model and their device placement,
        this function replaces the logical node with an executable physical node for the physical model.

        Parameters
        ----------
        multi_model_placement : dict
            a dict of models and device placement.
            These models will be assembled into the same physical model to run.

        Returns
        -------
        node : Node
            the physical node to replace the logical node in the physical model
        placement : Device
            the device placement of the returned physical node
        """

class LogicalGraph(Graph):
    def __init__(self, model: Model, graph_id: int, name: str = None, _internal: bool = False) -> None: ...

class OriginNode(AbstractLogicalNode):
    """
    This is logical node representing the original node without any modification.
    In assemble, just return the original node along with the physical placement given by multi_model_placement.
    """
    original_graph: Incomplete
    original_node: Incomplete
    def __init__(self, logical_graph: LogicalGraph, original_graph: Graph, original_node: Node, name: str, operation, _internal: bool = False) -> None: ...
    def assemble(self, multi_model_placement: Dict[Model, Device]) -> Tuple[Node, Device]: ...

class LogicalPlan:
    lp_model: Incomplete
    id: Incomplete
    logical_graph: Incomplete
    models: Incomplete
    def __init__(self, plan_id: int = 0) -> None: ...
    def add_model(self, model: Model): ...
    def assemble(self, multi_model_placement: Dict[Model, Device]) -> Tuple[Model, Dict[Node, Device]]:
        """
        Given a set of models to be formed in a physical model and their device placement,
        this function replaces all the logical node in this LogicalPlan with executable physical nodes
        for the physical model.

        Parameters
        ----------
        multi_model_placement : dict
            a dict of models and device placement.
            These models will be assembled into the same physical model to run.

        Returns
        -------
        phy_model : Model
            the physical model formed by models in `multi_model_placement`
            all logical node are replaced by physical nodes
        node_placements : dict
            the device placement of the nodes in `phy_model`
        """
    def node_replace(self, old_node: Node, new_node: Node, input_slot_mapping: Incomplete | None = None, output_slot_mapping: Incomplete | None = None): ...
