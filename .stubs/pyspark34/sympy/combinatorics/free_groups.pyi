from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.expr import Expr as Expr
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import CantSympify as CantSympify
from sympy.printing.defaults import DefaultPrinting as DefaultPrinting
from sympy.utilities import public as public
from sympy.utilities.iterables import flatten as flatten, is_sequence as is_sequence
from sympy.utilities.magic import pollute as pollute
from sympy.utilities.misc import as_int as as_int

def free_group(symbols):
    '''Construct a free group returning ``(FreeGroup, (f_0, f_1, ..., f_(n-1))``.

    Parameters
    ==========

    symbols : str, Symbol/Expr or sequence of str, Symbol/Expr (may be empty)

    Examples
    ========

    >>> from sympy.combinatorics import free_group
    >>> F, x, y, z = free_group("x, y, z")
    >>> F
    <free group on the generators (x, y, z)>
    >>> x**2*y**-1
    x**2*y**-1
    >>> type(_)
    <class \'sympy.combinatorics.free_groups.FreeGroupElement\'>

    '''
def xfree_group(symbols):
    '''Construct a free group returning ``(FreeGroup, (f_0, f_1, ..., f_(n-1)))``.

    Parameters
    ==========

    symbols : str, Symbol/Expr or sequence of str, Symbol/Expr (may be empty)

    Examples
    ========

    >>> from sympy.combinatorics.free_groups import xfree_group
    >>> F, (x, y, z) = xfree_group("x, y, z")
    >>> F
    <free group on the generators (x, y, z)>
    >>> y**2*x**-2*z**-1
    y**2*x**-2*z**-1
    >>> type(_)
    <class \'sympy.combinatorics.free_groups.FreeGroupElement\'>

    '''
def vfree_group(symbols):
    '''Construct a free group and inject ``f_0, f_1, ..., f_(n-1)`` as symbols
    into the global namespace.

    Parameters
    ==========

    symbols : str, Symbol/Expr or sequence of str, Symbol/Expr (may be empty)

    Examples
    ========

    >>> from sympy.combinatorics.free_groups import vfree_group
    >>> vfree_group("x, y, z")
    <free group on the generators (x, y, z)>
    >>> x**2*y**-2*z # noqa: F821
    x**2*y**-2*z
    >>> type(_)
    <class \'sympy.combinatorics.free_groups.FreeGroupElement\'>

    '''

class FreeGroup(DefaultPrinting):
    """
    Free group with finite or infinite number of generators. Its input API
    is that of a str, Symbol/Expr or a sequence of one of
    these types (which may be empty)

    See Also
    ========

    sympy.polys.rings.PolyRing

    References
    ==========

    .. [1] https://www.gap-system.org/Manuals/doc/ref/chap37.html

    .. [2] https://en.wikipedia.org/wiki/Free_group

    """
    is_associative: bool
    is_group: bool
    is_FreeGroup: bool
    is_PermutationGroup: bool
    relators: list[Expr]
    def __new__(cls, symbols): ...
    def clone(self, symbols: Incomplete | None = None): ...
    def __contains__(self, i) -> bool:
        """Return True if ``i`` is contained in FreeGroup."""
    def __hash__(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, index): ...
    def __eq__(self, other):
        '''No ``FreeGroup`` is equal to any "other" ``FreeGroup``.
        '''
    def index(self, gen):
        '''Return the index of the generator `gen` from ``(f_0, ..., f_(n-1))``.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> F.index(y)
        1
        >>> F.index(x)
        0

        '''
    def order(self):
        '''Return the order of the free group.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> F.order()
        oo

        >>> free_group("")[0].order()
        1

        '''
    @property
    def elements(self):
        '''
        Return the elements of the free group.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> (z,) = free_group("")
        >>> z.elements
        {<identity>}

        '''
    @property
    def rank(self):
        """
        In group theory, the `rank` of a group `G`, denoted `G.rank`,
        can refer to the smallest cardinality of a generating set
        for G, that is

        \\operatorname{rank}(G)=\\min\\{ |X|: X\\subseteq G, \\left\\langle X\\right\\rangle =G\\}.

        """
    @property
    def is_abelian(self):
        '''Returns if the group is Abelian.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, x, y, z = free_group("x y z")
        >>> f.is_abelian
        False

        '''
    @property
    def identity(self):
        """Returns the identity element of free group."""
    def contains(self, g):
        '''Tests if Free Group element ``g`` belong to self, ``G``.

        In mathematical terms any linear combination of generators
        of a Free Group is contained in it.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, x, y, z = free_group("x y z")
        >>> f.contains(x**3*y**2)
        True

        '''
    def center(self):
        """Returns the center of the free group `self`."""

class FreeGroupElement(CantSympify, DefaultPrinting, tuple):
    """Used to create elements of FreeGroup. It cannot be used directly to
    create a free group element. It is called by the `dtype` method of the
    `FreeGroup` class.

    """
    is_assoc_word: bool
    def new(self, init): ...
    def __hash__(self): ...
    def copy(self): ...
    @property
    def is_identity(self): ...
    @property
    def array_form(self):
        '''
        SymPy provides two different internal kinds of representation
        of associative words. The first one is called the `array_form`
        which is a tuple containing `tuples` as its elements, where the
        size of each tuple is two. At the first position the tuple
        contains the `symbol-generator`, while at the second position
        of tuple contains the exponent of that generator at the position.
        Since elements (i.e. words) do not commute, the indexing of tuple
        makes that property to stay.

        The structure in ``array_form`` of ``FreeGroupElement`` is of form:

        ``( ( symbol_of_gen, exponent ), ( , ), ... ( , ) )``

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, x, y, z = free_group("x y z")
        >>> (x*z).array_form
        ((x, 1), (z, 1))
        >>> (x**2*z*y*x**2).array_form
        ((x, 2), (z, 1), (y, 1), (x, 2))

        See Also
        ========

        letter_repr

        '''
    @property
    def letter_form(self):
        '''
        The letter representation of a ``FreeGroupElement`` is a tuple
        of generator symbols, with each entry corresponding to a group
        generator. Inverses of the generators are represented by
        negative generator symbols.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, a, b, c, d = free_group("a b c d")
        >>> (a**3).letter_form
        (a, a, a)
        >>> (a**2*d**-2*a*b**-4).letter_form
        (a, a, -d, -d, a, -b, -b, -b, -b)
        >>> (a**-2*b**3*d).letter_form
        (-a, -a, b, b, b, d)

        See Also
        ========

        array_form

        '''
    def __getitem__(self, i): ...
    def index(self, gen): ...
    @property
    def letter_form_elm(self):
        """
        """
    @property
    def ext_rep(self):
        """This is called the External Representation of ``FreeGroupElement``
        """
    def __contains__(self, gen) -> bool: ...
    def __pow__(self, n): ...
    def __mul__(self, other):
        '''Returns the product of elements belonging to the same ``FreeGroup``.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, x, y, z = free_group("x y z")
        >>> x*y**2*y**-4
        x*y**-2
        >>> z*y**-2
        z*y**-2
        >>> x**2*y*y**-1*x**-2
        <identity>

        '''
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __add__(self, other): ...
    def inverse(self):
        '''
        Returns the inverse of a ``FreeGroupElement`` element

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, x, y, z = free_group("x y z")
        >>> x.inverse()
        x**-1
        >>> (x*y).inverse()
        y**-1*x**-1

        '''
    def order(self):
        '''Find the order of a ``FreeGroupElement``.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, x, y = free_group("x y")
        >>> (x**2*y*y**-1*x**-2).order()
        1

        '''
    def commutator(self, other):
        """
        Return the commutator of `self` and `x`: ``~x*~self*x*self``

        """
    def eliminate_words(self, words, _all: bool = False, inverse: bool = True):
        """
        Replace each subword from the dictionary `words` by words[subword].
        If words is a list, replace the words by the identity.

        """
    def eliminate_word(self, gen, by: Incomplete | None = None, _all: bool = False, inverse: bool = True):
        '''
        For an associative word `self`, a subword `gen`, and an associative
        word `by` (identity by default), return the associative word obtained by
        replacing each occurrence of `gen` in `self` by `by`. If `_all = True`,
        the occurrences of `gen` that may appear after the first substitution will
        also be replaced and so on until no occurrences are found. This might not
        always terminate (e.g. `(x).eliminate_word(x, x**2, _all=True)`).

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, x, y = free_group("x y")
        >>> w = x**5*y*x**2*y**-4*x
        >>> w.eliminate_word( x, x**2 )
        x**10*y*x**4*y**-4*x**2
        >>> w.eliminate_word( x, y**-1 )
        y**-11
        >>> w.eliminate_word(x**5)
        y*x**2*y**-4*x
        >>> w.eliminate_word(x*y, y)
        x**4*y*x**2*y**-4*x

        See Also
        ========
        substituted_word

        '''
    def __len__(self) -> int:
        '''
        For an associative word `self`, returns the number of letters in it.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, a, b = free_group("a b")
        >>> w = a**5*b*a**2*b**-4*a
        >>> len(w)
        13
        >>> len(a**17)
        17
        >>> len(w**0)
        0

        '''
    def __eq__(self, other):
        '''
        Two  associative words are equal if they are words over the
        same alphabet and if they are sequences of the same letters.
        This is equivalent to saying that the external representations
        of the words are equal.
        There is no "universal" empty word, every alphabet has its own
        empty word.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, swapnil0, swapnil1 = free_group("swapnil0 swapnil1")
        >>> f
        <free group on the generators (swapnil0, swapnil1)>
        >>> g, swap0, swap1 = free_group("swap0 swap1")
        >>> g
        <free group on the generators (swap0, swap1)>

        >>> swapnil0 == swapnil1
        False
        >>> swapnil0*swapnil1 == swapnil1/swapnil1*swapnil0*swapnil1
        True
        >>> swapnil0*swapnil1 == swapnil1*swapnil0
        False
        >>> swapnil1**0 == swap0**0
        False

        '''
    def __lt__(self, other):
        '''
        The  ordering  of  associative  words is defined by length and
        lexicography (this ordering is called short-lex ordering), that
        is, shorter words are smaller than longer words, and words of the
        same length are compared w.r.t. the lexicographical ordering induced
        by the ordering of generators. Generators  are  sorted  according
        to the order in which they were created. If the generators are
        invertible then each generator `g` is larger than its inverse `g^{-1}`,
        and `g^{-1}` is larger than every generator that is smaller than `g`.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, a, b = free_group("a b")
        >>> b < a
        False
        >>> a < a.inverse()
        False

        '''
    def __le__(self, other): ...
    def __gt__(self, other):
        '''

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, x, y, z = free_group("x y z")
        >>> y**2 > x**2
        True
        >>> y*z > z*y
        False
        >>> x > x.inverse()
        True

        '''
    def __ge__(self, other): ...
    def exponent_sum(self, gen):
        '''
        For an associative word `self` and a generator or inverse of generator
        `gen`, ``exponent_sum`` returns the number of times `gen` appears in
        `self` minus the number of times its inverse appears in `self`. If
        neither `gen` nor its inverse occur in `self` then 0 is returned.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> w = x**2*y**3
        >>> w.exponent_sum(x)
        2
        >>> w.exponent_sum(x**-1)
        -2
        >>> w = x**2*y**4*x**-3
        >>> w.exponent_sum(x)
        -1

        See Also
        ========

        generator_count

        '''
    def generator_count(self, gen):
        '''
        For an associative word `self` and a generator `gen`,
        ``generator_count`` returns the multiplicity of generator
        `gen` in `self`.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> w = x**2*y**3
        >>> w.generator_count(x)
        2
        >>> w = x**2*y**4*x**-3
        >>> w.generator_count(x)
        5

        See Also
        ========

        exponent_sum

        '''
    def subword(self, from_i, to_j, strict: bool = True):
        '''
        For an associative word `self` and two positive integers `from_i` and
        `to_j`, `subword` returns the subword of `self` that begins at position
        `from_i` and ends at `to_j - 1`, indexing is done with origin 0.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, a, b = free_group("a b")
        >>> w = a**5*b*a**2*b**-4*a
        >>> w.subword(2, 6)
        a**3*b

        '''
    def subword_index(self, word, start: int = 0):
        '''
        Find the index of `word` in `self`.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, a, b = free_group("a b")
        >>> w = a**2*b*a*b**3
        >>> w.subword_index(a*b*a*b)
        1

        '''
    def is_dependent(self, word):
        '''
        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> (x**4*y**-3).is_dependent(x**4*y**-2)
        True
        >>> (x**2*y**-1).is_dependent(x*y)
        False
        >>> (x*y**2*x*y**2).is_dependent(x*y**2)
        True
        >>> (x**12).is_dependent(x**-4)
        True

        See Also
        ========

        is_independent

        '''
    def is_independent(self, word):
        """

        See Also
        ========

        is_dependent

        """
    def contains_generators(self):
        '''
        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y, z = free_group("x, y, z")
        >>> (x**2*y**-1).contains_generators()
        {x, y}
        >>> (x**3*z).contains_generators()
        {x, z}

        '''
    def cyclic_subword(self, from_i, to_j): ...
    def cyclic_conjugates(self):
        '''Returns a words which are cyclic to the word `self`.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> w = x*y*x*y*x
        >>> w.cyclic_conjugates()
        {x*y*x**2*y, x**2*y*x*y, y*x*y*x**2, y*x**2*y*x, x*y*x*y*x}
        >>> s = x*y*x**2*y*x
        >>> s.cyclic_conjugates()
        {x**2*y*x**2*y, y*x**2*y*x**2, x*y*x**2*y*x}

        References
        ==========

        .. [1] https://planetmath.org/cyclicpermutation

        '''
    def is_cyclic_conjugate(self, w):
        '''
        Checks whether words ``self``, ``w`` are cyclic conjugates.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> w1 = x**2*y**5
        >>> w2 = x*y**5*x
        >>> w1.is_cyclic_conjugate(w2)
        True
        >>> w3 = x**-1*y**5*x**-1
        >>> w3.is_cyclic_conjugate(w2)
        False

        '''
    def number_syllables(self):
        '''Returns the number of syllables of the associative word `self`.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, swapnil0, swapnil1 = free_group("swapnil0 swapnil1")
        >>> (swapnil1**3*swapnil0*swapnil1**-1).number_syllables()
        3

        '''
    def exponent_syllable(self, i):
        '''
        Returns the exponent of the `i`-th syllable of the associative word
        `self`.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, a, b = free_group("a b")
        >>> w = a**5*b*a**2*b**-4*a
        >>> w.exponent_syllable( 2 )
        2

        '''
    def generator_syllable(self, i):
        '''
        Returns the symbol of the generator that is involved in the
        i-th syllable of the associative word `self`.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, a, b = free_group("a b")
        >>> w = a**5*b*a**2*b**-4*a
        >>> w.generator_syllable( 3 )
        b

        '''
    def sub_syllables(self, from_i, to_j):
        '''
        `sub_syllables` returns the subword of the associative word `self` that
        consists of syllables from positions `from_to` to `to_j`, where
        `from_to` and `to_j` must be positive integers and indexing is done
        with origin 0.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> f, a, b = free_group("a, b")
        >>> w = a**5*b*a**2*b**-4*a
        >>> w.sub_syllables(1, 2)
        b
        >>> w.sub_syllables(3, 3)
        <identity>

        '''
    def substituted_word(self, from_i, to_j, by):
        """
        Returns the associative word obtained by replacing the subword of
        `self` that begins at position `from_i` and ends at position `to_j - 1`
        by the associative word `by`. `from_i` and `to_j` must be positive
        integers, indexing is done with origin 0. In other words,
        `w.substituted_word(w, from_i, to_j, by)` is the product of the three
        words: `w.subword(0, from_i)`, `by`, and
        `w.subword(to_j len(w))`.

        See Also
        ========

        eliminate_word

        """
    def is_cyclically_reduced(self):
        '''Returns whether the word is cyclically reduced or not.
        A word is cyclically reduced if by forming the cycle of the
        word, the word is not reduced, i.e a word w = `a_1 ... a_n`
        is called cyclically reduced if `a_1 \\ne a_n^{-1}`.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> (x**2*y**-1*x**-1).is_cyclically_reduced()
        False
        >>> (y*x**2*y**2).is_cyclically_reduced()
        True

        '''
    def identity_cyclic_reduction(self):
        '''Return a unique cyclically reduced version of the word.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> (x**2*y**2*x**-1).identity_cyclic_reduction()
        x*y**2
        >>> (x**-3*y**-1*x**5).identity_cyclic_reduction()
        x**2*y**-1

        References
        ==========

        .. [1] https://planetmath.org/cyclicallyreduced

        '''
    def cyclic_reduction(self, removed: bool = False):
        '''Return a cyclically reduced version of the word. Unlike
        `identity_cyclic_reduction`, this will not cyclically permute
        the reduced word - just remove the "unreduced" bits on either
        side of it. Compare the examples with those of
        `identity_cyclic_reduction`.

        When `removed` is `True`, return a tuple `(word, r)` where
        self `r` is such that before the reduction the word was either
        `r*word*r**-1`.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> (x**2*y**2*x**-1).cyclic_reduction()
        x*y**2
        >>> (x**-3*y**-1*x**5).cyclic_reduction()
        y**-1*x**2
        >>> (x**-3*y**-1*x**5).cyclic_reduction(removed=True)
        (y**-1*x**2, x**-3)

        '''
    def power_of(self, other):
        '''
        Check if `self == other**n` for some integer n.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> F, x, y = free_group("x, y")
        >>> ((x*y)**2).power_of(x*y)
        True
        >>> (x**-3*y**-2*x**3).power_of(x**-3*y*x**3)
        True

        '''

def letter_form_to_array_form(array_form, group):
    """
    This method converts a list given with possible repetitions of elements in
    it. It returns a new list such that repetitions of consecutive elements is
    removed and replace with a tuple element of size two such that the first
    index contains `value` and the second index contains the number of
    consecutive repetitions of `value`.

    """
def zero_mul_simp(l, index) -> None:
    """Used to combine two reduced words."""
