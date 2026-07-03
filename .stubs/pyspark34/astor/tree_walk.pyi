from .node_util import iter_node as iter_node
from _typeshed import Incomplete

class MetaFlatten(type):
    """This metaclass is used to flatten classes to remove
    class hierarchy.

    This makes it easier to manipulate classes (find
    attributes in a single dict, etc.)

    """
    def __new__(clstype, name, bases, clsdict): ...

class TreeWalk(MetaFlatten):
    """The TreeWalk class can be used as a superclass in order
    to walk an AST or similar tree.

    Unlike other treewalkers, this class can walk a tree either
    recursively or non-recursively.  Subclasses can define
    methods with the following signatures::

        def pre_xxx(self):
            pass

        def post_xxx(self):
            pass

        def init_xxx(self):
            pass

    Where 'xxx' is one of:

      - A class name
      - An attribute member name concatenated with '_name'
        For example, 'pre_targets_name' will process nodes
        that are referenced by the name 'targets' in their
        parent's node.
      - An attribute member name concatenated with '_item'
        For example, 'pre_targets_item'  will process nodes
        that are in a list that is the targets attribute
        of some node.

    pre_xxx will process a node before processing any of its subnodes.
    if the return value from pre_xxx evalates to true, then walk
    will not process any of the subnodes.  Those can be manually
    processed, if desired, by calling self.walk(node) on the subnodes
    before returning True.

    post_xxx will process a node after processing all its subnodes.

    init_xxx methods can decorate the class instance with subclass-specific
    information.  A single init_whatever method could be written, but to
    make it easy to keep initialization with use, any number of init_xxx
    methods can be written.  They will be called in alphabetical order.

    """
    nodestack: Incomplete
    def __init__(self, node: Incomplete | None = None) -> None: ...
    pre_handlers: Incomplete
    post_handlers: Incomplete
    def setup(self) -> None:
        """All the node-specific handlers are setup at
        object initialization time.

        """
    cur_node: Incomplete
    cur_name: Incomplete
    def walk(self, node, name: str = '', list=..., len=..., type=...) -> None:
        """Walk the tree starting at a given node.

        Maintain a stack of nodes.

        """
    @property
    def parent(self):
        """Return the parent node of the current node."""
    @property
    def parent_name(self):
        """Return the parent node and name."""
    def replace(self, new_node) -> None:
        """Replace a node after first checking integrity of node stack."""
