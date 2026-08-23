from .Nodes import StatListNode as StatListNode
from .Visitor import VisitorTransform as VisitorTransform
from _typeshed import Incomplete

class ExtractPxdCode(VisitorTransform):
    """
    Finds nodes in a pxd file that should generate code, and
    returns them in a StatListNode.

    The result is a tuple (StatListNode, ModuleScope), i.e.
    everything that is needed from the pxd after it is processed.

    A purer approach would be to separately compile the pxd code,
    but the result would have to be slightly more sophisticated
    than pure strings (functions + wanted interned strings +
    wanted utility code + wanted cached objects) so for now this
    approach is taken.
    """
    funcs: Incomplete
    def __call__(self, root): ...
    def visit_FuncDefNode(self, node): ...
    def visit_Node(self, node): ...
