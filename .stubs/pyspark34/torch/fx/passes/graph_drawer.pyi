import pydot
import torch.fx
from _typeshed import Incomplete
from typing import Dict

__all__ = ['FxGraphDrawer']

class FxGraphDrawer:
    '''
        Visualize a torch.fx.Graph with graphviz
        Basic usage:
            g = FxGraphDrawer(symbolic_traced, "resnet18")
            with open("a.svg", "w") as f:
                f.write(g.get_dot_graph().create_svg())
        '''
    def __init__(self, graph_module: torch.fx.GraphModule, name: str, ignore_getattr: bool = False, ignore_parameters_and_buffers: bool = False, skip_node_names_in_args: bool = True) -> None: ...
    def get_dot_graph(self, submod_name: Incomplete | None = None) -> pydot.Dot: ...
    def get_main_dot_graph(self) -> pydot.Dot: ...
    def get_submod_dot_graph(self, submod_name) -> pydot.Dot: ...
    def get_all_dot_graphs(self) -> Dict[str, pydot.Dot]: ...
