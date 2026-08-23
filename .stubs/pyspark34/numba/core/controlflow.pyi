import collections
from _typeshed import Incomplete
from collections.abc import Generator
from numba.core.errors import UnsupportedError as UnsupportedError
from numba.core.ir import Loc as Loc
from typing import NamedTuple

NEW_BLOCKERS: Incomplete

class CFBlock:
    offset: Incomplete
    body: Incomplete
    outgoing_jumps: Incomplete
    incoming_jumps: Incomplete
    terminating: bool
    def __init__(self, offset) -> None: ...
    def __iter__(self): ...

class Loop(NamedTuple('Loop', [('entries', Incomplete), ('exits', Incomplete), ('header', Incomplete), ('body', Incomplete)])):
    """
    A control flow loop, as detected by a CFGraph object.
    """
    def __eq__(self, other): ...
    def __hash__(self): ...

class _DictOfContainers(collections.defaultdict):
    """A defaultdict with customized equality checks that ignore empty values.

    Non-empty value is checked by: `bool(value_item) == True`.
    """
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class CFGraph:
    """
    Generic (almost) implementation of a Control Flow Graph.
    """
    def __init__(self) -> None: ...
    def add_node(self, node) -> None:
        """
        Add *node* to the graph.  This is necessary before adding any
        edges from/to the node.  *node* can be any hashable object.
        """
    def add_edge(self, src, dest, data: Incomplete | None = None) -> None:
        """
        Add an edge from node *src* to node *dest*, with optional
        per-edge *data*.
        If such an edge already exists, it is replaced (duplicate edges
        are not possible).
        """
    def successors(self, src) -> Generator[Incomplete, None, None]:
        """
        Yield (node, data) pairs representing the successors of node *src*.
        (*data* will be None if no data was specified when adding the edge)
        """
    def predecessors(self, dest) -> Generator[Incomplete, None, None]:
        """
        Yield (node, data) pairs representing the predecessors of node *dest*.
        (*data* will be None if no data was specified when adding the edge)
        """
    def set_entry_point(self, node) -> None:
        """
        Set the entry point of the graph to *node*.
        """
    def process(self) -> None:
        """
        Compute essential properties of the control flow graph.  The graph
        must have been fully populated, and its entry point specified. Other
        graph properties are computed on-demand.
        """
    def dominators(self):
        """
        Return a dictionary of {node -> set(nodes)} mapping each node to
        the nodes dominating it.

        A node D dominates a node N when any path leading to N must go through D
        """
    def post_dominators(self):
        """
        Return a dictionary of {node -> set(nodes)} mapping each node to
        the nodes post-dominating it.

        A node P post-dominates a node N when any path starting from N must go
        through P.
        """
    def immediate_dominators(self):
        """
        Return a dictionary of {node -> node} mapping each node to its
        immediate dominator (idom).

        The idom(B) is the closest strict dominator of V
        """
    def dominance_frontier(self):
        """
        Return a dictionary of {node -> set(nodes)} mapping each node to
        the nodes in its dominance frontier.

        The dominance frontier _df(N) is the set of all nodes that are
        immediate successors to blocks dominated by N but which aren't
        strictly dominated by N
        """
    def dominator_tree(self):
        """
        return a dictionary of {node -> set(nodes)} mapping each node to
        the set of nodes it immediately dominates

        The domtree(B) is the closest strict set of nodes that B dominates
        """
    def descendents(self, node):
        """
        Return the set of descendents of the given *node*, in topological
        order (ignoring back edges).
        """
    def entry_point(self):
        """
        Return the entry point node.
        """
    def exit_points(self):
        """
        Return the computed set of exit nodes (may be empty).
        """
    def backbone(self):
        """
        Return the set of nodes constituting the graph's backbone.
        (i.e. the nodes that every path starting from the entry point
         must go through).  By construction, it is non-empty: it contains
         at least the entry point.
        """
    def loops(self):
        """
        Return a dictionary of {node -> loop} mapping each loop header
        to the loop (a Loop instance) starting with it.
        """
    def in_loops(self, node):
        """
        Return the list of Loop objects the *node* belongs to,
        from innermost to outermost.
        """
    def dead_nodes(self):
        """
        Return the set of dead nodes (eliminated from the graph).
        """
    def nodes(self):
        """
        Return the set of live nodes.
        """
    def topo_order(self):
        """
        Return the sequence of nodes in topological order (ignoring back
        edges).
        """
    def topo_sort(self, nodes, reverse: bool = False) -> Generator[Incomplete, None, None]:
        """
        Iterate over the *nodes* in topological order (ignoring back edges).
        The sort isn't guaranteed to be stable.
        """
    def dump(self, file: Incomplete | None = None) -> None:
        """
        Dump extensive debug information.
        """
    def render_dot(self, filename: str = 'numba_cfg.dot'):
        """Render the controlflow graph with GraphViz DOT via the
        ``graphviz`` python binding.

        Returns
        -------
        g : graphviz.Digraph
            Use `g.view()` to open the graph in the default PDF application.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class ControlFlowAnalysis:
    """
    Attributes
    ----------
    - bytecode

    - blocks

    - blockseq

    - doms: dict of set
        Dominators

    - backbone: set of block offsets
        The set of block that is common to all possible code path.

    """
    bytecode: Incomplete
    blocks: Incomplete
    liveblocks: Incomplete
    blockseq: Incomplete
    doms: Incomplete
    backbone: Incomplete
    def __init__(self, bytecode) -> None: ...
    def iterblocks(self) -> Generator[Incomplete, None, None]:
        """
        Return all blocks in sequence of occurrence
        """
    def iterliveblocks(self) -> Generator[Incomplete, None, None]:
        """
        Return all live blocks in sequence of occurrence
        """
    def incoming_blocks(self, block) -> Generator[Incomplete, None, None]:
        """
        Yield (incoming block, number of stack pops) pairs for *block*.
        """
    def dump(self, file: Incomplete | None = None) -> None: ...
    graph: Incomplete
    def run(self) -> None: ...
    def jump(self, target, pops: int = 0) -> None:
        """
        Register a jump (conditional or not) to *target* offset.
        *pops* is the number of stack pops implied by the jump (default 0).
        """
    def op_SETUP_LOOP(self, inst) -> None: ...
    def op_SETUP_WITH(self, inst) -> None: ...
    def op_POP_BLOCK(self, inst) -> None: ...
    def op_FOR_ITER(self, inst) -> None: ...
    op_POP_JUMP_IF_FALSE: Incomplete
    op_POP_JUMP_IF_TRUE: Incomplete
    op_JUMP_IF_FALSE: Incomplete
    op_JUMP_IF_TRUE: Incomplete
    op_POP_JUMP_FORWARD_IF_FALSE: Incomplete
    op_POP_JUMP_BACKWARD_IF_FALSE: Incomplete
    op_POP_JUMP_FORWARD_IF_TRUE: Incomplete
    op_POP_JUMP_BACKWARD_IF_TRUE: Incomplete
    op_JUMP_IF_FALSE_OR_POP: Incomplete
    op_JUMP_IF_TRUE_OR_POP: Incomplete
    def op_JUMP_ABSOLUTE(self, inst) -> None: ...
    def op_JUMP_FORWARD(self, inst) -> None: ...
    op_JUMP_BACKWARD = op_JUMP_FORWARD
    def op_RETURN_VALUE(self, inst) -> None: ...
    def op_RAISE_VARARGS(self, inst) -> None: ...
    def op_BREAK_LOOP(self, inst) -> None: ...
