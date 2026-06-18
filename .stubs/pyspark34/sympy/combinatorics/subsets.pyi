from sympy.combinatorics.graycode import GrayCode as GrayCode

class Subset:
    """
    Represents a basic subset object.

    Explanation
    ===========

    We generate subsets using essentially two techniques,
    binary enumeration and lexicographic enumeration.
    The Subset class takes two arguments, the first one
    describes the initial subset to consider and the second
    describes the superset.

    Examples
    ========

    >>> from sympy.combinatorics import Subset
    >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
    >>> a.next_binary().subset
    ['b']
    >>> a.prev_binary().subset
    ['c']
    """
    def __new__(cls, subset, superset):
        """
        Default constructor.

        It takes the ``subset`` and its ``superset`` as its parameters.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.subset
        ['c', 'd']
        >>> a.superset
        ['a', 'b', 'c', 'd']
        >>> a.size
        2
        """
    def __eq__(self, other):
        """Return a boolean indicating whether a == b on the basis of
        whether both objects are of the class Subset and if the values
        of the subset and superset attributes are the same.
        """
    def iterate_binary(self, k):
        """
        This is a helper function. It iterates over the
        binary subsets by ``k`` steps. This variable can be
        both positive or negative.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.iterate_binary(-2).subset
        ['d']
        >>> a = Subset(['a', 'b', 'c'], ['a', 'b', 'c', 'd'])
        >>> a.iterate_binary(2).subset
        []

        See Also
        ========

        next_binary, prev_binary
        """
    def next_binary(self):
        """
        Generates the next binary ordered subset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.next_binary().subset
        ['b']
        >>> a = Subset(['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.next_binary().subset
        []

        See Also
        ========

        prev_binary, iterate_binary
        """
    def prev_binary(self):
        """
        Generates the previous binary ordered subset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset([], ['a', 'b', 'c', 'd'])
        >>> a.prev_binary().subset
        ['a', 'b', 'c', 'd']
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.prev_binary().subset
        ['c']

        See Also
        ========

        next_binary, iterate_binary
        """
    def next_lexicographic(self):
        """
        Generates the next lexicographically ordered subset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.next_lexicographic().subset
        ['d']
        >>> a = Subset(['d'], ['a', 'b', 'c', 'd'])
        >>> a.next_lexicographic().subset
        []

        See Also
        ========

        prev_lexicographic
        """
    def prev_lexicographic(self):
        """
        Generates the previous lexicographically ordered subset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset([], ['a', 'b', 'c', 'd'])
        >>> a.prev_lexicographic().subset
        ['d']
        >>> a = Subset(['c','d'], ['a', 'b', 'c', 'd'])
        >>> a.prev_lexicographic().subset
        ['c']

        See Also
        ========

        next_lexicographic
        """
    def iterate_graycode(self, k):
        """
        Helper function used for prev_gray and next_gray.
        It performs ``k`` step overs to get the respective Gray codes.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset([1, 2, 3], [1, 2, 3, 4])
        >>> a.iterate_graycode(3).subset
        [1, 4]
        >>> a.iterate_graycode(-2).subset
        [1, 2, 4]

        See Also
        ========

        next_gray, prev_gray
        """
    def next_gray(self):
        """
        Generates the next Gray code ordered subset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset([1, 2, 3], [1, 2, 3, 4])
        >>> a.next_gray().subset
        [1, 3]

        See Also
        ========

        iterate_graycode, prev_gray
        """
    def prev_gray(self):
        """
        Generates the previous Gray code ordered subset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset([2, 3, 4], [1, 2, 3, 4, 5])
        >>> a.prev_gray().subset
        [2, 3, 4, 5]

        See Also
        ========

        iterate_graycode, next_gray
        """
    @property
    def rank_binary(self):
        """
        Computes the binary ordered rank.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset([], ['a','b','c','d'])
        >>> a.rank_binary
        0
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.rank_binary
        3

        See Also
        ========

        iterate_binary, unrank_binary
        """
    @property
    def rank_lexicographic(self):
        """
        Computes the lexicographic ranking of the subset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.rank_lexicographic
        14
        >>> a = Subset([2, 4, 5], [1, 2, 3, 4, 5, 6])
        >>> a.rank_lexicographic
        43
        """
    @property
    def rank_gray(self):
        """
        Computes the Gray code ranking of the subset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c','d'], ['a','b','c','d'])
        >>> a.rank_gray
        2
        >>> a = Subset([2, 4, 5], [1, 2, 3, 4, 5, 6])
        >>> a.rank_gray
        27

        See Also
        ========

        iterate_graycode, unrank_gray
        """
    @property
    def subset(self):
        """
        Gets the subset represented by the current instance.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.subset
        ['c', 'd']

        See Also
        ========

        superset, size, superset_size, cardinality
        """
    @property
    def size(self):
        """
        Gets the size of the subset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.size
        2

        See Also
        ========

        subset, superset, superset_size, cardinality
        """
    @property
    def superset(self):
        """
        Gets the superset of the subset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.superset
        ['a', 'b', 'c', 'd']

        See Also
        ========

        subset, size, superset_size, cardinality
        """
    @property
    def superset_size(self):
        """
        Returns the size of the superset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.superset_size
        4

        See Also
        ========

        subset, superset, size, cardinality
        """
    @property
    def cardinality(self):
        """
        Returns the number of all possible subsets.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.cardinality
        16

        See Also
        ========

        subset, superset, size, superset_size
        """
    @classmethod
    def subset_from_bitlist(self, super_set, bitlist):
        """
        Gets the subset defined by the bitlist.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> Subset.subset_from_bitlist(['a', 'b', 'c', 'd'], '0011').subset
        ['c', 'd']

        See Also
        ========

        bitlist_from_subset
        """
    @classmethod
    def bitlist_from_subset(self, subset, superset):
        """
        Gets the bitlist corresponding to a subset.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> Subset.bitlist_from_subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        '0011'

        See Also
        ========

        subset_from_bitlist
        """
    @classmethod
    def unrank_binary(self, rank, superset):
        """
        Gets the binary ordered subset of the specified rank.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> Subset.unrank_binary(4, ['a', 'b', 'c', 'd']).subset
        ['b']

        See Also
        ========

        iterate_binary, rank_binary
        """
    @classmethod
    def unrank_gray(self, rank, superset):
        """
        Gets the Gray code ordered subset of the specified rank.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> Subset.unrank_gray(4, ['a', 'b', 'c']).subset
        ['a', 'b']
        >>> Subset.unrank_gray(0, ['a', 'b', 'c']).subset
        []

        See Also
        ========

        iterate_graycode, rank_gray
        """
    @classmethod
    def subset_indices(self, subset, superset):
        """Return indices of subset in superset in a list; the list is empty
        if all elements of ``subset`` are not in ``superset``.

        Examples
        ========

            >>> from sympy.combinatorics import Subset
            >>> superset = [1, 3, 2, 5, 4]
            >>> Subset.subset_indices([3, 2, 1], superset)
            [1, 2, 0]
            >>> Subset.subset_indices([1, 6], superset)
            []
            >>> Subset.subset_indices([], superset)
            []

        """

def ksubsets(superset, k):
    """
    Finds the subsets of size ``k`` in lexicographic order.

    This uses the itertools generator.

    Examples
    ========

    >>> from sympy.combinatorics.subsets import ksubsets
    >>> list(ksubsets([1, 2, 3], 2))
    [(1, 2), (1, 3), (2, 3)]
    >>> list(ksubsets([1, 2, 3, 4, 5], 2))
    [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4),     (2, 5), (3, 4), (3, 5), (4, 5)]

    See Also
    ========

    Subset
    """
