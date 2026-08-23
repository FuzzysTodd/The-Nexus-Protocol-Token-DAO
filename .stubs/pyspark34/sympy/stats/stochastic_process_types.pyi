from _typeshed import Incomplete
from collections.abc import Generator
from sympy.core.basic import Basic
from sympy.core.function import Lambda
from sympy.core.numbers import Integer
from sympy.core.symbol import Symbol
from sympy.logic.boolalg import Boolean
from sympy.matrices.immutable import ImmutableMatrix
from sympy.sets.conditionset import ConditionSet
from sympy.sets.fancysets import Range
from sympy.sets.sets import FiniteSet
from typing import List as tList, Tuple as tTuple

__all__ = ['StochasticProcess', 'DiscreteTimeStochasticProcess', 'DiscreteMarkovChain', 'TransitionMatrixOf', 'StochasticStateSpaceOf', 'GeneratorMatrixOf', 'ContinuousMarkovChain', 'BernoulliProcess', 'PoissonProcess', 'WienerProcess', 'GammaProcess']

class StochasticProcess(Basic):
    """
    Base class for all the stochastic processes whether
    discrete or continuous.

    Parameters
    ==========

    sym: Symbol or str
    state_space: Set
        The state space of the stochastic process, by default S.Reals.
        For discrete sets it is zero indexed.

    See Also
    ========

    DiscreteTimeStochasticProcess
    """
    index_set: Incomplete
    def __new__(cls, sym, state_space=..., **kwargs): ...
    @property
    def symbol(self): ...
    @property
    def state_space(self) -> FiniteSet | Range: ...
    def distribution(self, key: Incomplete | None = None): ...
    def density(self, x): ...
    def __call__(self, time) -> None:
        """
        Overridden in ContinuousTimeStochasticProcess.
        """
    def __getitem__(self, time) -> None:
        """
        Overridden in DiscreteTimeStochasticProcess.
        """
    def probability(self, condition) -> None: ...
    def joint_distribution(self, *args):
        """
        Computes the joint distribution of the random indexed variables.

        Parameters
        ==========

        args: iterable
            The finite list of random indexed variables/the key of a stochastic
            process whose joint distribution has to be computed.

        Returns
        =======

        JointDistribution
            The joint distribution of the list of random indexed variables.
            An unevaluated object is returned if it is not possible to
            compute the joint distribution.

        Raises
        ======

        ValueError: When the arguments passed are not of type RandomIndexSymbol
        or Number.
        """
    def expectation(self, condition, given_condition) -> None: ...
    def sample(self) -> None: ...

class DiscreteTimeStochasticProcess(StochasticProcess):
    """
    Base class for all discrete stochastic processes.
    """
    def __getitem__(self, time):
        """
        For indexing discrete time stochastic processes.

        Returns
        =======

        RandomIndexedSymbol
        """

class ContinuousTimeStochasticProcess(StochasticProcess):
    """
    Base class for all continuous time stochastic process.
    """
    def __call__(self, time):
        """
        For indexing continuous time stochastic processes.

        Returns
        =======

        RandomIndexedSymbol
        """

class TransitionMatrixOf(Boolean):
    """
    Assumes that the matrix is the transition matrix
    of the process.
    """
    def __new__(cls, process, matrix): ...
    process: Incomplete
    matrix: Incomplete

class GeneratorMatrixOf(TransitionMatrixOf):
    """
    Assumes that the matrix is the generator matrix
    of the process.
    """
    def __new__(cls, process, matrix): ...

class StochasticStateSpaceOf(Boolean):
    def __new__(cls, process, state_space): ...
    process: Incomplete
    state_index: Incomplete

class MarkovProcess(StochasticProcess):
    """
    Contains methods that handle queries
    common to Markov processes.
    """
    @property
    def number_of_states(self) -> Integer | Symbol:
        """
        The number of states in the Markov Chain.
        """
    def replace_with_index(self, condition): ...
    def probability(self, condition, given_condition: Incomplete | None = None, evaluate: bool = True, **kwargs):
        """
        Handles probability queries for Markov process.

        Parameters
        ==========

        condition: Relational
        given_condition: Relational/And

        Returns
        =======
        Probability
            If the information is not sufficient.
        Expr
            In all other cases.

        Note
        ====
        Any information passed at the time of query overrides
        any information passed at the time of object creation like
        transition probabilities, state space.
        Pass the transition matrix using TransitionMatrixOf,
        generator matrix using GeneratorMatrixOf and state space
        using StochasticStateSpaceOf in given_condition using & or And.
        """
    def expectation(self, expr, condition: Incomplete | None = None, evaluate: bool = True, **kwargs):
        """
        Handles expectation queries for markov process.

        Parameters
        ==========

        expr: RandomIndexedSymbol, Relational, Logic
            Condition for which expectation has to be computed. Must
            contain a RandomIndexedSymbol of the process.
        condition: Relational, Logic
            The given conditions under which computations should be done.

        Returns
        =======

        Expectation
            Unevaluated object if computations cannot be done due to
            insufficient information.
        Expr
            In all other cases when the computations are successful.

        Note
        ====

        Any information passed at the time of query overrides
        any information passed at the time of object creation like
        transition probabilities, state space.

        Pass the transition matrix using TransitionMatrixOf,
        generator matrix using GeneratorMatrixOf and state space
        using StochasticStateSpaceOf in given_condition using & or And.
        """

class DiscreteMarkovChain(DiscreteTimeStochasticProcess, MarkovProcess):
    '''
    Represents a finite discrete time-homogeneous Markov chain.

    This type of Markov Chain can be uniquely characterised by
    its (ordered) state space and its one-step transition probability
    matrix.

    Parameters
    ==========

    sym:
        The name given to the Markov Chain
    state_space:
        Optional, by default, Range(n)
    trans_probs:
        Optional, by default, MatrixSymbol(\'_T\', n, n)

    Examples
    ========

    >>> from sympy.stats import DiscreteMarkovChain, TransitionMatrixOf, P, E
    >>> from sympy import Matrix, MatrixSymbol, Eq, symbols
    >>> T = Matrix([[0.5, 0.2, 0.3],[0.2, 0.5, 0.3],[0.2, 0.3, 0.5]])
    >>> Y = DiscreteMarkovChain("Y", [0, 1, 2], T)
    >>> YS = DiscreteMarkovChain("Y")

    >>> Y.state_space
    {0, 1, 2}
    >>> Y.transition_probabilities
    Matrix([
    [0.5, 0.2, 0.3],
    [0.2, 0.5, 0.3],
    [0.2, 0.3, 0.5]])
    >>> TS = MatrixSymbol(\'T\', 3, 3)
    >>> P(Eq(YS[3], 2), Eq(YS[1], 1) & TransitionMatrixOf(YS, TS))
    T[0, 2]*T[1, 0] + T[1, 1]*T[1, 2] + T[1, 2]*T[2, 2]
    >>> P(Eq(Y[3], 2), Eq(Y[1], 1)).round(2)
    0.36

    Probabilities will be calculated based on indexes rather
    than state names. For example, with the Sunny-Cloudy-Rainy
    model with string state names:

    >>> from sympy.core.symbol import Str
    >>> Y = DiscreteMarkovChain("Y", [Str(\'Sunny\'), Str(\'Cloudy\'), Str(\'Rainy\')], T)
    >>> P(Eq(Y[3], 2), Eq(Y[1], 1)).round(2)
    0.36

    This gives the same answer as the ``[0, 1, 2]`` state space.
    Currently, there is no support for state names within probability
    and expectation statements. Here is a work-around using ``Str``:

    >>> P(Eq(Str(\'Rainy\'), Y[3]), Eq(Y[1], Str(\'Cloudy\'))).round(2)
    0.36

    Symbol state names can also be used:

    >>> sunny, cloudy, rainy = symbols(\'Sunny, Cloudy, Rainy\')
    >>> Y = DiscreteMarkovChain("Y", [sunny, cloudy, rainy], T)
    >>> P(Eq(Y[3], rainy), Eq(Y[1], cloudy)).round(2)
    0.36

    Expectations will be calculated as follows:

    >>> E(Y[3], Eq(Y[1], cloudy))
    0.38*Cloudy + 0.36*Rainy + 0.26*Sunny

    Probability of expressions with multiple RandomIndexedSymbols
    can also be calculated provided there is only 1 RandomIndexedSymbol
    in the given condition. It is always better to use Rational instead
    of floating point numbers for the probabilities in the
    transition matrix to avoid errors.

    >>> from sympy import Gt, Le, Rational
    >>> T = Matrix([[Rational(5, 10), Rational(3, 10), Rational(2, 10)], [Rational(2, 10), Rational(7, 10), Rational(1, 10)], [Rational(3, 10), Rational(3, 10), Rational(4, 10)]])
    >>> Y = DiscreteMarkovChain("Y", [0, 1, 2], T)
    >>> P(Eq(Y[3], Y[1]), Eq(Y[0], 0)).round(3)
    0.409
    >>> P(Gt(Y[3], Y[1]), Eq(Y[0], 0)).round(2)
    0.36
    >>> P(Le(Y[15], Y[10]), Eq(Y[8], 2)).round(7)
    0.6963328

    Symbolic probability queries are also supported

    >>> a, b, c, d = symbols(\'a b c d\')
    >>> T = Matrix([[Rational(1, 10), Rational(4, 10), Rational(5, 10)], [Rational(3, 10), Rational(4, 10), Rational(3, 10)], [Rational(7, 10), Rational(2, 10), Rational(1, 10)]])
    >>> Y = DiscreteMarkovChain("Y", [0, 1, 2], T)
    >>> query = P(Eq(Y[a], b), Eq(Y[c], d))
    >>> query.subs({a:10, b:2, c:5, d:1}).round(4)
    0.3096
    >>> P(Eq(Y[10], 2), Eq(Y[5], 1)).evalf().round(4)
    0.3096
    >>> query_gt = P(Gt(Y[a], b), Eq(Y[c], d))
    >>> query_gt.subs({a:21, b:0, c:5, d:0}).evalf().round(5)
    0.64705
    >>> P(Gt(Y[21], 0), Eq(Y[5], 0)).round(5)
    0.64705

    There is limited support for arbitrarily sized states:

    >>> n = symbols(\'n\', nonnegative=True, integer=True)
    >>> T = MatrixSymbol(\'T\', n, n)
    >>> Y = DiscreteMarkovChain("Y", trans_probs=T)
    >>> Y.state_space
    Range(0, n, 1)
    >>> query = P(Eq(Y[a], b), Eq(Y[c], d))
    >>> query.subs({a:10, b:2, c:5, d:1})
    (T**5)[1, 2]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Markov_chain#Discrete-time_Markov_chain
    .. [2] https://web.archive.org/web/20201230182007/https://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/Chapter11.pdf
    '''
    index_set: Incomplete
    def __new__(cls, sym, state_space: Incomplete | None = None, trans_probs: Incomplete | None = None): ...
    @property
    def transition_probabilities(self):
        """
        Transition probabilities of discrete Markov chain,
        either an instance of Matrix or MatrixSymbol.
        """
    def communication_classes(self) -> tList[tTuple[tList[Basic], Boolean, Integer]]:
        """
        Returns the list of communication classes that partition
        the states of the markov chain.

        A communication class is defined to be a set of states
        such that every state in that set is reachable from
        every other state in that set. Due to its properties
        this forms a class in the mathematical sense.
        Communication classes are also known as recurrence
        classes.

        Returns
        =======

        classes
            The ``classes`` are a list of tuples. Each
            tuple represents a single communication class
            with its properties. The first element in the
            tuple is the list of states in the class, the
            second element is whether the class is recurrent
            and the third element is the period of the
            communication class.

        Examples
        ========

        >>> from sympy.stats import DiscreteMarkovChain
        >>> from sympy import Matrix
        >>> T = Matrix([[0, 1, 0],
        ...             [1, 0, 0],
        ...             [1, 0, 0]])
        >>> X = DiscreteMarkovChain('X', [1, 2, 3], T)
        >>> classes = X.communication_classes()
        >>> for states, is_recurrent, period in classes:
        ...     states, is_recurrent, period
        ([1, 2], True, 2)
        ([3], False, 1)

        From this we can see that states ``1`` and ``2``
        communicate, are recurrent and have a period
        of 2. We can also see state ``3`` is transient
        with a period of 1.

        Notes
        =====

        The algorithm used is of order ``O(n**2)`` where
        ``n`` is the number of states in the markov chain.
        It uses Tarjan's algorithm to find the classes
        themselves and then it uses a breadth-first search
        algorithm to find each class's periodicity.
        Most of the algorithm's components approach ``O(n)``
        as the matrix becomes more and more sparse.

        References
        ==========

        .. [1] https://web.archive.org/web/20220207032113/https://www.columbia.edu/~ww2040/4701Sum07/4701-06-Notes-MCII.pdf
        .. [2] https://cecas.clemson.edu/~shierd/Shier/markov.pdf
        .. [3] https://ujcontent.uj.ac.za/esploro/outputs/graduate/Markov-chains--a-graph-theoretical/999849107691#file-0
        .. [4] https://www.mathworks.com/help/econ/dtmc.classify.html
        """
    def fundamental_matrix(self):
        """
        Each entry fundamental matrix can be interpreted as
        the expected number of times the chains is in state j
        if it started in state i.

        References
        ==========

        .. [1] https://lips.cs.princeton.edu/the-fundamental-matrix-of-a-finite-markov-chain/

        """
    def absorbing_probabilities(self):
        """
        Computes the absorbing probabilities, i.e.
        the ij-th entry of the matrix denotes the
        probability of Markov chain being absorbed
        in state j starting from state i.
        """
    def absorbing_probabilites(self): ...
    def is_regular(self): ...
    def is_ergodic(self): ...
    def is_absorbing_state(self, state): ...
    def is_absorbing_chain(self): ...
    def stationary_distribution(self, condition_set: bool = False) -> ImmutableMatrix | ConditionSet | Lambda:
        """
        The stationary distribution is any row vector, p, that solves p = pP,
        is row stochastic and each element in p must be nonnegative.
        That means in matrix form: :math:`(P-I)^T p^T = 0` and
        :math:`(1, \\dots, 1) p = 1`
        where ``P`` is the one-step transition matrix.

        All time-homogeneous Markov Chains with a finite state space
        have at least one stationary distribution. In addition, if
        a finite time-homogeneous Markov Chain is irreducible, the
        stationary distribution is unique.

        Parameters
        ==========

        condition_set : bool
            If the chain has a symbolic size or transition matrix,
            it will return a ``Lambda`` if ``False`` and return a
            ``ConditionSet`` if ``True``.

        Examples
        ========

        >>> from sympy.stats import DiscreteMarkovChain
        >>> from sympy import Matrix, S

        An irreducible Markov Chain

        >>> T = Matrix([[S(1)/2, S(1)/2, 0],
        ...             [S(4)/5, S(1)/5, 0],
        ...             [1, 0, 0]])
        >>> X = DiscreteMarkovChain('X', trans_probs=T)
        >>> X.stationary_distribution()
        Matrix([[8/13, 5/13, 0]])

        A reducible Markov Chain

        >>> T = Matrix([[S(1)/2, S(1)/2, 0],
        ...             [S(4)/5, S(1)/5, 0],
        ...             [0, 0, 1]])
        >>> X = DiscreteMarkovChain('X', trans_probs=T)
        >>> X.stationary_distribution()
        Matrix([[8/13 - 8*tau0/13, 5/13 - 5*tau0/13, tau0]])

        >>> Y = DiscreteMarkovChain('Y')
        >>> Y.stationary_distribution()
        Lambda((wm, _T), Eq(wm*_T, wm))

        >>> Y.stationary_distribution(condition_set=True)
        ConditionSet(wm, Eq(wm*_T, wm))

        References
        ==========

        .. [1] https://www.probabilitycourse.com/chapter11/11_2_6_stationary_and_limiting_distributions.php
        .. [2] https://web.archive.org/web/20210508104430/https://galton.uchicago.edu/~yibi/teaching/stat317/2014/Lectures/Lecture4_6up.pdf

        See Also
        ========

        sympy.stats.DiscreteMarkovChain.limiting_distribution
        """
    def fixed_row_vector(self):
        """
        A wrapper for ``stationary_distribution()``.
        """
    @property
    def limiting_distribution(self):
        """
        The fixed row vector is the limiting
        distribution of a discrete Markov chain.
        """
    def decompose(self) -> tTuple[tList[Basic], ImmutableMatrix, ImmutableMatrix, ImmutableMatrix]:
        """
        Decomposes the transition matrix into submatrices with
        special properties.

        The transition matrix can be decomposed into 4 submatrices:
        - A - the submatrix from recurrent states to recurrent states.
        - B - the submatrix from transient to recurrent states.
        - C - the submatrix from transient to transient states.
        - O - the submatrix of zeros for recurrent to transient states.

        Returns
        =======

        states, A, B, C
            ``states`` - a list of state names with the first being
            the recurrent states and the last being
            the transient states in the order
            of the row names of A and then the row names of C.
            ``A`` - the submatrix from recurrent states to recurrent states.
            ``B`` - the submatrix from transient to recurrent states.
            ``C`` - the submatrix from transient to transient states.

        Examples
        ========

        >>> from sympy.stats import DiscreteMarkovChain
        >>> from sympy import Matrix, S

        One can decompose this chain for example:

        >>> T = Matrix([[S(1)/2, S(1)/2, 0,      0,      0],
        ...             [S(2)/5, S(1)/5, S(2)/5, 0,      0],
        ...             [0,      0,      1,      0,      0],
        ...             [0,      0,      S(1)/2, S(1)/2, 0],
        ...             [S(1)/2, 0,      0,      0, S(1)/2]])
        >>> X = DiscreteMarkovChain('X', trans_probs=T)
        >>> states, A, B, C = X.decompose()
        >>> states
        [2, 0, 1, 3, 4]

        >>> A   # recurrent to recurrent
        Matrix([[1]])

        >>> B  # transient to recurrent
        Matrix([
        [  0],
        [2/5],
        [1/2],
        [  0]])

        >>> C  # transient to transient
        Matrix([
        [1/2, 1/2,   0,   0],
        [2/5, 1/5,   0,   0],
        [  0,   0, 1/2,   0],
        [1/2,   0,   0, 1/2]])

        This means that state 2 is the only absorbing state
        (since A is a 1x1 matrix). B is a 4x1 matrix since
        the 4 remaining transient states all merge into reccurent
        state 2. And C is the 4x4 matrix that shows how the
        transient states 0, 1, 3, 4 all interact.

        See Also
        ========

        sympy.stats.DiscreteMarkovChain.communication_classes
        sympy.stats.DiscreteMarkovChain.canonical_form

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Absorbing_Markov_chain
        .. [2] https://people.brandeis.edu/~igusa/Math56aS08/Math56a_S08_notes015.pdf
        """
    def canonical_form(self) -> tTuple[tList[Basic], ImmutableMatrix]:
        """
        Reorders the one-step transition matrix
        so that recurrent states appear first and transient
        states appear last. Other representations include inserting
        transient states first and recurrent states last.

        Returns
        =======

        states, P_new
            ``states`` is the list that describes the order of the
            new states in the matrix
            so that the ith element in ``states`` is the state of the
            ith row of A.
            ``P_new`` is the new transition matrix in canonical form.

        Examples
        ========

        >>> from sympy.stats import DiscreteMarkovChain
        >>> from sympy import Matrix, S

        You can convert your chain into canonical form:

        >>> T = Matrix([[S(1)/2, S(1)/2, 0,      0,      0],
        ...             [S(2)/5, S(1)/5, S(2)/5, 0,      0],
        ...             [0,      0,      1,      0,      0],
        ...             [0,      0,      S(1)/2, S(1)/2, 0],
        ...             [S(1)/2, 0,      0,      0, S(1)/2]])
        >>> X = DiscreteMarkovChain('X', list(range(1, 6)), trans_probs=T)
        >>> states, new_matrix = X.canonical_form()
        >>> states
        [3, 1, 2, 4, 5]

        >>> new_matrix
        Matrix([
        [  1,   0,   0,   0,   0],
        [  0, 1/2, 1/2,   0,   0],
        [2/5, 2/5, 1/5,   0,   0],
        [1/2,   0,   0, 1/2,   0],
        [  0, 1/2,   0,   0, 1/2]])

        The new states are [3, 1, 2, 4, 5] and you can
        create a new chain with this and its canonical
        form will remain the same (since it is already
        in canonical form).

        >>> X = DiscreteMarkovChain('X', states, new_matrix)
        >>> states, new_matrix = X.canonical_form()
        >>> states
        [3, 1, 2, 4, 5]

        >>> new_matrix
        Matrix([
        [  1,   0,   0,   0,   0],
        [  0, 1/2, 1/2,   0,   0],
        [2/5, 2/5, 1/5,   0,   0],
        [1/2,   0,   0, 1/2,   0],
        [  0, 1/2,   0,   0, 1/2]])

        This is not limited to absorbing chains:

        >>> T = Matrix([[0, 5,  5, 0,  0],
        ...             [0, 0,  0, 10, 0],
        ...             [5, 0,  5, 0,  0],
        ...             [0, 10, 0, 0,  0],
        ...             [0, 3,  0, 3,  4]])/10
        >>> X = DiscreteMarkovChain('X', trans_probs=T)
        >>> states, new_matrix = X.canonical_form()
        >>> states
        [1, 3, 0, 2, 4]

        >>> new_matrix
        Matrix([
        [   0,    1,   0,   0,   0],
        [   1,    0,   0,   0,   0],
        [ 1/2,    0,   0, 1/2,   0],
        [   0,    0, 1/2, 1/2,   0],
        [3/10, 3/10,   0,   0, 2/5]])

        See Also
        ========

        sympy.stats.DiscreteMarkovChain.communication_classes
        sympy.stats.DiscreteMarkovChain.decompose

        References
        ==========

        .. [1] https://onlinelibrary.wiley.com/doi/pdf/10.1002/9780470316887.app1
        .. [2] http://www.columbia.edu/~ww2040/6711F12/lect1023big.pdf
        """
    def sample(self) -> Generator[Incomplete, None, None]:
        """
        Returns
        =======

        sample: iterator object
            iterator object containing the sample

        """

class ContinuousMarkovChain(ContinuousTimeStochasticProcess, MarkovProcess):
    """
    Represents continuous time Markov chain.

    Parameters
    ==========

    sym : Symbol/str
    state_space : Set
        Optional, by default, S.Reals
    gen_mat : Matrix/ImmutableMatrix/MatrixSymbol
        Optional, by default, None

    Examples
    ========

    >>> from sympy.stats import ContinuousMarkovChain, P
    >>> from sympy import Matrix, S, Eq, Gt
    >>> G = Matrix([[-S(1), S(1)], [S(1), -S(1)]])
    >>> C = ContinuousMarkovChain('C', state_space=[0, 1], gen_mat=G)
    >>> C.limiting_distribution()
    Matrix([[1/2, 1/2]])
    >>> C.state_space
    {0, 1}
    >>> C.generator_matrix
    Matrix([
    [-1,  1],
    [ 1, -1]])

    Probability queries are supported

    >>> P(Eq(C(1.96), 0), Eq(C(0.78), 1)).round(5)
    0.45279
    >>> P(Gt(C(1.7), 0), Eq(C(0.82), 1)).round(5)
    0.58602

    Probability of expressions with multiple RandomIndexedSymbols
    can also be calculated provided there is only 1 RandomIndexedSymbol
    in the given condition. It is always better to use Rational instead
    of floating point numbers for the probabilities in the
    generator matrix to avoid errors.

    >>> from sympy import Gt, Le, Rational
    >>> G = Matrix([[-S(1), Rational(1, 10), Rational(9, 10)], [Rational(2, 5), -S(1), Rational(3, 5)], [Rational(1, 2), Rational(1, 2), -S(1)]])
    >>> C = ContinuousMarkovChain('C', state_space=[0, 1, 2], gen_mat=G)
    >>> P(Eq(C(3.92), C(1.75)), Eq(C(0.46), 0)).round(5)
    0.37933
    >>> P(Gt(C(3.92), C(1.75)), Eq(C(0.46), 0)).round(5)
    0.34211
    >>> P(Le(C(1.57), C(3.14)), Eq(C(1.22), 1)).round(4)
    0.7143

    Symbolic probability queries are also supported

    >>> from sympy import symbols
    >>> a,b,c,d = symbols('a b c d')
    >>> G = Matrix([[-S(1), Rational(1, 10), Rational(9, 10)], [Rational(2, 5), -S(1), Rational(3, 5)], [Rational(1, 2), Rational(1, 2), -S(1)]])
    >>> C = ContinuousMarkovChain('C', state_space=[0, 1, 2], gen_mat=G)
    >>> query = P(Eq(C(a), b), Eq(C(c), d))
    >>> query.subs({a:3.65, b:2, c:1.78, d:1}).evalf().round(10)
    0.4002723175
    >>> P(Eq(C(3.65), 2), Eq(C(1.78), 1)).round(10)
    0.4002723175
    >>> query_gt = P(Gt(C(a), b), Eq(C(c), d))
    >>> query_gt.subs({a:43.2, b:0, c:3.29, d:2}).evalf().round(10)
    0.6832579186
    >>> P(Gt(C(43.2), 0), Eq(C(3.29), 2)).round(10)
    0.6832579186

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Markov_chain#Continuous-time_Markov_chain
    .. [2] https://u.math.biu.ac.il/~amirgi/CTMCnotes.pdf
    """
    index_set: Incomplete
    def __new__(cls, sym, state_space: Incomplete | None = None, gen_mat: Incomplete | None = None): ...
    @property
    def generator_matrix(self): ...
    def transition_probabilities(self, gen_mat: Incomplete | None = None): ...
    def limiting_distribution(self): ...

class BernoulliProcess(DiscreteTimeStochasticProcess):
    '''
    The Bernoulli process consists of repeated
    independent Bernoulli process trials with the same parameter `p`.
    It\'s assumed that the probability `p` applies to every
    trial and that the outcomes of each trial
    are independent of all the rest. Therefore Bernoulli Process
    is Discrete State and Discrete Time Stochastic Process.

    Parameters
    ==========

    sym : Symbol/str
    success : Integer/str
            The event which is considered to be success. Default: 1.
    failure: Integer/str
            The event which is considered to be failure. Default: 0.
    p : Real Number between 0 and 1
            Represents the probability of getting success.

    Examples
    ========

    >>> from sympy.stats import BernoulliProcess, P, E
    >>> from sympy import Eq, Gt
    >>> B = BernoulliProcess("B", p=0.7, success=1, failure=0)
    >>> B.state_space
    {0, 1}
    >>> (B.p).round(2)
    0.70
    >>> B.success
    1
    >>> B.failure
    0
    >>> X = B[1] + B[2] + B[3]
    >>> P(Eq(X, 0)).round(2)
    0.03
    >>> P(Eq(X, 2)).round(2)
    0.44
    >>> P(Eq(X, 4)).round(2)
    0
    >>> P(Gt(X, 1)).round(2)
    0.78
    >>> P(Eq(B[1], 0) & Eq(B[2], 1) & Eq(B[3], 0) & Eq(B[4], 1)).round(2)
    0.04
    >>> B.joint_distribution(B[1], B[2])
    JointDistributionHandmade(Lambda((B[1], B[2]), Piecewise((0.7, Eq(B[1], 1)),
    (0.3, Eq(B[1], 0)), (0, True))*Piecewise((0.7, Eq(B[2], 1)), (0.3, Eq(B[2], 0)),
    (0, True))))
    >>> E(2*B[1] + B[2]).round(2)
    2.10
    >>> P(B[1] < 1).round(2)
    0.30

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Bernoulli_process
    .. [2] https://mathcs.clarku.edu/~djoyce/ma217/bernoulli.pdf

    '''
    index_set: Incomplete
    def __new__(cls, sym, p, success: int = 1, failure: int = 0): ...
    @property
    def symbol(self): ...
    @property
    def p(self): ...
    @property
    def success(self): ...
    @property
    def failure(self): ...
    @property
    def state_space(self): ...
    def distribution(self, key: Incomplete | None = None): ...
    def simple_rv(self, rv): ...
    def expectation(self, expr, condition: Incomplete | None = None, evaluate: bool = True, **kwargs):
        """
        Computes expectation.

        Parameters
        ==========

        expr : RandomIndexedSymbol, Relational, Logic
            Condition for which expectation has to be computed. Must
            contain a RandomIndexedSymbol of the process.
        condition : Relational, Logic
            The given conditions under which computations should be done.

        Returns
        =======

        Expectation of the RandomIndexedSymbol.

        """
    def probability(self, condition, given_condition: Incomplete | None = None, evaluate: bool = True, **kwargs):
        """
        Computes probability.

        Parameters
        ==========

        condition : Relational
                Condition for which probability has to be computed. Must
                contain a RandomIndexedSymbol of the process.
        given_condition : Relational, Logic
                The given conditions under which computations should be done.

        Returns
        =======

        Probability of the condition.

        """
    def density(self, x): ...

class _SubstituteRV:
    """
    Internal class to handle the queries of expectation and probability
    by substitution.
    """

class CountingProcess(ContinuousTimeStochasticProcess):
    """
    This class handles the common methods of the Counting Processes
    such as Poisson, Wiener and Gamma Processes
    """
    index_set: Incomplete
    @property
    def symbol(self): ...
    def expectation(self, expr, condition: Incomplete | None = None, evaluate: bool = True, **kwargs):
        """
        Computes expectation

        Parameters
        ==========

        expr: RandomIndexedSymbol, Relational, Logic
            Condition for which expectation has to be computed. Must
            contain a RandomIndexedSymbol of the process.
        condition: Relational, Boolean
            The given conditions under which computations should be done, i.e,
            the intervals on which each variable time stamp in expr is defined

        Returns
        =======

        Expectation of the given expr

        """
    def probability(self, condition, given_condition: Incomplete | None = None, evaluate: bool = True, **kwargs):
        """
        Computes probability.

        Parameters
        ==========

        condition: Relational
            Condition for which probability has to be computed. Must
            contain a RandomIndexedSymbol of the process.
        given_condition: Relational, Boolean
            The given conditions under which computations should be done, i.e,
            the intervals on which each variable time stamp in expr is defined

        Returns
        =======

        Probability of the condition

        """

class PoissonProcess(CountingProcess):
    '''
    The Poisson process is a counting process. It is usually used in scenarios
    where we are counting the occurrences of certain events that appear
    to happen at a certain rate, but completely at random.

    Parameters
    ==========

    sym : Symbol/str
    lamda : Positive number
        Rate of the process, ``lambda > 0``

    Examples
    ========

    >>> from sympy.stats import PoissonProcess, P, E
    >>> from sympy import symbols, Eq, Ne, Contains, Interval
    >>> X = PoissonProcess("X", lamda=3)
    >>> X.state_space
    Naturals0
    >>> X.lamda
    3
    >>> t1, t2 = symbols(\'t1 t2\', positive=True)
    >>> P(X(t1) < 4)
    (9*t1**3/2 + 9*t1**2/2 + 3*t1 + 1)*exp(-3*t1)
    >>> P(Eq(X(t1), 2) | Ne(X(t1), 4), Contains(t1, Interval.Ropen(2, 4)))
    1 - 36*exp(-6)
    >>> P(Eq(X(t1), 2) & Eq(X(t2), 3), Contains(t1, Interval.Lopen(0, 2))
    ... & Contains(t2, Interval.Lopen(2, 4)))
    648*exp(-12)
    >>> E(X(t1))
    3*t1
    >>> E(X(t1)**2 + 2*X(t2),  Contains(t1, Interval.Lopen(0, 1))
    ... & Contains(t2, Interval.Lopen(1, 2)))
    18
    >>> P(X(3) < 1, Eq(X(1), 0))
    exp(-6)
    >>> P(Eq(X(4), 3), Eq(X(2), 3))
    exp(-6)
    >>> P(X(2) <= 3, X(1) > 1)
    5*exp(-3)

    Merging two Poisson Processes

    >>> Y = PoissonProcess("Y", lamda=4)
    >>> Z = X + Y
    >>> Z.lamda
    7

    Splitting a Poisson Process into two independent Poisson Processes

    >>> N, M = Z.split(l1=2, l2=5)
    >>> N.lamda, M.lamda
    (2, 5)

    References
    ==========

    .. [1] https://www.probabilitycourse.com/chapter11/11_0_0_intro.php
    .. [2] https://en.wikipedia.org/wiki/Poisson_point_process

    '''
    def __new__(cls, sym, lamda): ...
    @property
    def lamda(self): ...
    @property
    def state_space(self): ...
    def distribution(self, key): ...
    def density(self, x): ...
    def simple_rv(self, rv): ...
    def __add__(self, other): ...
    def split(self, l1, l2): ...

class WienerProcess(CountingProcess):
    '''
    The Wiener process is a real valued continuous-time stochastic process.
    In physics it is used to study Brownian motion and it is often also called
    Brownian motion due to its historical connection with physical process of the
    same name originally observed by Scottish botanist Robert Brown.

    Parameters
    ==========

    sym : Symbol/str

    Examples
    ========

    >>> from sympy.stats import WienerProcess, P, E
    >>> from sympy import symbols, Contains, Interval
    >>> X = WienerProcess("X")
    >>> X.state_space
    Reals
    >>> t1, t2 = symbols(\'t1 t2\', positive=True)
    >>> P(X(t1) < 7).simplify()
    erf(7*sqrt(2)/(2*sqrt(t1)))/2 + 1/2
    >>> P((X(t1) > 2) | (X(t1) < 4), Contains(t1, Interval.Ropen(2, 4))).simplify()
    -erf(1)/2 + erf(2)/2 + 1
    >>> E(X(t1))
    0
    >>> E(X(t1) + 2*X(t2),  Contains(t1, Interval.Lopen(0, 1))
    ... & Contains(t2, Interval.Lopen(1, 2)))
    0

    References
    ==========

    .. [1] https://www.probabilitycourse.com/chapter11/11_4_0_brownian_motion_wiener_process.php
    .. [2] https://en.wikipedia.org/wiki/Wiener_process

    '''
    def __new__(cls, sym): ...
    @property
    def state_space(self): ...
    def distribution(self, key): ...
    def density(self, x): ...
    def simple_rv(self, rv): ...

class GammaProcess(CountingProcess):
    '''
    A Gamma process is a random process with independent gamma distributed
    increments. It is a pure-jump increasing Levy process.

    Parameters
    ==========

    sym : Symbol/str
    lamda : Positive number
        Jump size of the process, ``lamda > 0``
    gamma : Positive number
        Rate of jump arrivals, `\\gamma > 0`

    Examples
    ========

    >>> from sympy.stats import GammaProcess, E, P, variance
    >>> from sympy import symbols, Contains, Interval, Not
    >>> t, d, x, l, g = symbols(\'t d x l g\', positive=True)
    >>> X = GammaProcess("X", l, g)
    >>> E(X(t))
    g*t/l
    >>> variance(X(t)).simplify()
    g*t/l**2
    >>> X = GammaProcess(\'X\', 1, 2)
    >>> P(X(t) < 1).simplify()
    lowergamma(2*t, 1)/gamma(2*t)
    >>> P(Not((X(t) < 5) & (X(d) > 3)), Contains(t, Interval.Ropen(2, 4)) &
    ... Contains(d, Interval.Lopen(7, 8))).simplify()
    -4*exp(-3) + 472*exp(-8)/3 + 1
    >>> E(X(2) + x*E(X(5)))
    10*x + 4

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gamma_process

    '''
    def __new__(cls, sym, lamda, gamma): ...
    @property
    def lamda(self): ...
    @property
    def gamma(self): ...
    @property
    def state_space(self): ...
    def distribution(self, key): ...
    def density(self, x): ...
    def simple_rv(self, rv): ...
