from _typeshed import Incomplete
from nni.nas.execution.common import Cell as Cell, Edge as Edge, Graph as Graph, Model as Model, Node as Node
from typing_extensions import TypeGuard

def build_full_name(prefix, name, seq: Incomplete | None = None): ...
def build_python_name(prefix, name): ...
def build_cand_name(name, label): ...
def is_layerchoice_node(ir_node: Node | None) -> TypeGuard[Node]: ...
def get_full_name_by_scope_name(ir_model: Model, scope_names, prefix: str = ''): ...
def match_node(ir_model: Model, torch_node, prefix: str = ''):
    """
    Match the corresponding node of a torch._C.Value
    """
def flatten_model_graph(ir_model: Model):
    """
    Flatten the subgraph into root graph.
    """
def flatten_model_graph_without_layerchoice(ir_model: Model):
    """
    Flatten the subgraph into root graph and jump all layerchoice
    """
