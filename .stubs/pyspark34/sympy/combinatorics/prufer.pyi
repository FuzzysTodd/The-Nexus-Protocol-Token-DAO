from sympy.core import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.tensor.array import Array as Array
from sympy.utilities.iterables import flatten as flatten, iterable as iterable
from sympy.utilities.misc import as_int as as_int

class Prufer(Basic):
    """
    The Prufer correspondence is an algorithm that describes the
    bijection between labeled trees and the Prufer code. A Prufer
    code of a labeled tree is unique up to isomorphism and has
    a length of n - 2.

    Prufer sequences were first used by Heinz Prufer to give a
    proof of Cayley's formula.

    References
    ==========

    .. [1] https://mathworld.wolfram.com/LabeledTree.html

    """
    @property
    def prufer_repr(self):
        """Returns Prufer sequence for the Prufer object.

        This sequence is found by removing the highest numbered vertex,
        recording the node it was attached to, and continuing until only
        two vertices remain. The Prufer sequence is the list of recorded nodes.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> Prufer([[0, 3], [1, 3], [2, 3], [3, 4], [4, 5]]).prufer_repr
        [3, 3, 3, 4]
        >>> Prufer([1, 0, 0]).prufer_repr
        [1, 0, 0]

        See Also
        ========

        to_prufer

        """
    @property
    def tree_repr(self):
        """Returns the tree representation of the Prufer object.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> Prufer([[0, 3], [1, 3], [2, 3], [3, 4], [4, 5]]).tree_repr
        [[0, 3], [1, 3], [2, 3], [3, 4], [4, 5]]
        >>> Prufer([1, 0, 0]).tree_repr
        [[1, 2], [0, 1], [0, 3], [0, 4]]

        See Also
        ========

        to_tree

        """
    @property
    def nodes(self):
        """Returns the number of nodes in the tree.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> Prufer([[0, 3], [1, 3], [2, 3], [3, 4], [4, 5]]).nodes
        6
        >>> Prufer([1, 0, 0]).nodes
        5

        """
    @property
    def rank(self):
        """Returns the rank of the Prufer sequence.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> p = Prufer([[0, 3], [1, 3], [2, 3], [3, 4], [4, 5]])
        >>> p.rank
        778
        >>> p.next(1).rank
        779
        >>> p.prev().rank
        777

        See Also
        ========

        prufer_rank, next, prev, size

        """
    @property
    def size(self):
        """Return the number of possible trees of this Prufer object.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> Prufer([0]*4).size == Prufer([6]*4).size == 1296
        True

        See Also
        ========

        prufer_rank, rank, next, prev

        """
    @staticmethod
    def to_prufer(tree, n):
        """Return the Prufer sequence for a tree given as a list of edges where
        ``n`` is the number of nodes in the tree.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> a = Prufer([[0, 1], [0, 2], [0, 3]])
        >>> a.prufer_repr
        [0, 0]
        >>> Prufer.to_prufer([[0, 1], [0, 2], [0, 3]], 4)
        [0, 0]

        See Also
        ========
        prufer_repr: returns Prufer sequence of a Prufer object.

        """
    @staticmethod
    def to_tree(prufer):
        """Return the tree (as a list of edges) of the given Prufer sequence.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> a = Prufer([0, 2], 4)
        >>> a.tree_repr
        [[0, 1], [0, 2], [2, 3]]
        >>> Prufer.to_tree([0, 2])
        [[0, 1], [0, 2], [2, 3]]

        References
        ==========

        .. [1] https://hamberg.no/erlend/posts/2010-11-06-prufer-sequence-compact-tree-representation.html

        See Also
        ========
        tree_repr: returns tree representation of a Prufer object.

        """
    @staticmethod
    def edges(*runs):
        """Return a list of edges and the number of nodes from the given runs
        that connect nodes in an integer-labelled tree.

        All node numbers will be shifted so that the minimum node is 0. It is
        not a problem if edges are repeated in the runs; only unique edges are
        returned. There is no assumption made about what the range of the node
        labels should be, but all nodes from the smallest through the largest
        must be present.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> Prufer.edges([1, 2, 3], [2, 4, 5]) # a T
        ([[0, 1], [1, 2], [1, 3], [3, 4]], 5)

        Duplicate edges are removed:

        >>> Prufer.edges([0, 1, 2, 3], [1, 4, 5], [1, 4, 6]) # a K
        ([[0, 1], [1, 2], [1, 4], [2, 3], [4, 5], [4, 6]], 7)

        """
    def prufer_rank(self):
        """Computes the rank of a Prufer sequence.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> a = Prufer([[0, 1], [0, 2], [0, 3]])
        >>> a.prufer_rank()
        0

        See Also
        ========

        rank, next, prev, size

        """
    @classmethod
    def unrank(self, rank, n):
        """Finds the unranked Prufer sequence.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> Prufer.unrank(0, 4)
        Prufer([0, 0])

        """
    def __new__(cls, *args, **kw_args):
        """The constructor for the Prufer object.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer

        A Prufer object can be constructed from a list of edges:

        >>> a = Prufer([[0, 1], [0, 2], [0, 3]])
        >>> a.prufer_repr
        [0, 0]

        If the number of nodes is given, no checking of the nodes will
        be performed; it will be assumed that nodes 0 through n - 1 are
        present:

        >>> Prufer([[0, 1], [0, 2], [0, 3]], 4)
        Prufer([[0, 1], [0, 2], [0, 3]], 4)

        A Prufer object can be constructed from a Prufer sequence:

        >>> b = Prufer([1, 3])
        >>> b.tree_repr
        [[0, 1], [1, 3], [2, 3]]

        """
    def next(self, delta: int = 1):
        """Generates the Prufer sequence that is delta beyond the current one.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> a = Prufer([[0, 1], [0, 2], [0, 3]])
        >>> b = a.next(1) # == a.next()
        >>> b.tree_repr
        [[0, 2], [0, 1], [1, 3]]
        >>> b.rank
        1

        See Also
        ========

        prufer_rank, rank, prev, size

        """
    def prev(self, delta: int = 1):
        """Generates the Prufer sequence that is -delta before the current one.

        Examples
        ========

        >>> from sympy.combinatorics.prufer import Prufer
        >>> a = Prufer([[0, 1], [1, 2], [2, 3], [1, 4]])
        >>> a.rank
        36
        >>> b = a.prev()
        >>> b
        Prufer([1, 2, 0])
        >>> b.rank
        35

        See Also
        ========

        prufer_rank, rank, next, size

        """
