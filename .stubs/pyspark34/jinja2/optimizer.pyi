import typing as t
from . import nodes as nodes
from .environment import Environment as Environment
from .visitor import NodeTransformer as NodeTransformer
from _typeshed import Incomplete

def optimize(node: nodes.Node, environment: Environment) -> nodes.Node:
    """The context hint can be used to perform an static optimization
    based on the context given."""

class Optimizer(NodeTransformer):
    environment: Incomplete
    def __init__(self, environment: Environment | None) -> None: ...
    def generic_visit(self, node: nodes.Node, *args: t.Any, **kwargs: t.Any) -> nodes.Node: ...
