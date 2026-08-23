from torch.fx.graph import Graph as Graph
from torch.fx.graph_module import GraphModule as GraphModule
from torch.fx.node import Node as Node
from torch.fx.passes.tools_common import NodeList as NodeList, NodeSet as NodeSet, legalize_graph as legalize_graph
from torch.fx.passes.utils import lift_subgraph_as_module as lift_subgraph_as_module
from typing import List, Tuple

def topo_sort(nodes: NodeList) -> NodeList: ...
def validate_partition(partition: NodeList) -> bool: ...
def fuse_as_graphmodule(gm: GraphModule, nodes: NodeList, module_name: str) -> Tuple[GraphModule, Tuple[Node, ...], Tuple[Node, ...]]:
    """
    Fuse nodes in graph_module into a GraphModule.

    Args:
        gm (GraphModule): target graph_module

        nodes (List[Node]): list of nodes in `gm` to fuse, where the node must be topologically sorted

        module_name: class name for the fused GraphModule

    Returns:
        fused_gm (GraphModule): fused graph module, where its node is a copy of `nodes` in `gm`

        original_inputs (Tuple[Node, ...]): input nodes to `nodes` in original `gm`

        original_outputs (Tuple[Node, ...]): consumer nodes of `nodes` in original `gm`

    """
def insert_subgm(gm: GraphModule, sub_gm: GraphModule, orig_inputs: Tuple[Node, ...], orig_outputs: Tuple[Node, ...]): ...
def erase_nodes(gm: GraphModule, nodes: NodeList): ...
def fuse_by_partitions(gm: GraphModule, partitions: List[NodeList]) -> GraphModule: ...
