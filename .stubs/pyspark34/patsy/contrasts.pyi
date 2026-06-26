from _typeshed import Incomplete

__all__ = ['ContrastMatrix', 'Treatment', 'Poly', 'Sum', 'Helmert', 'Diff']

class ContrastMatrix:
    '''A simple container for a matrix used for coding categorical factors.

    Attributes:

    .. attribute:: matrix

       A 2d ndarray, where each column corresponds to one column of the
       resulting design matrix, and each row contains the entries for a single
       categorical variable level. Usually n-by-n for a full rank coding or
       n-by-(n-1) for a reduced rank coding, though other options are
       possible.

    .. attribute:: column_suffixes

       A list of strings to be appended to the factor name, to produce the
       final column names. E.g. for treatment coding the entries will look
       like ``"[T.level1]"``.
    '''
    matrix: Incomplete
    column_suffixes: Incomplete
    def __init__(self, matrix, column_suffixes) -> None: ...

class Treatment:
    '''Treatment coding (also known as dummy coding).

    This is the default coding.

    For reduced-rank coding, one level is chosen as the "reference", and its
    mean behaviour is represented by the intercept. Each column of the
    resulting matrix represents the difference between the mean of one level
    and this reference level.

    For full-rank coding, classic "dummy" coding is used, and each column of
    the resulting matrix represents the mean of the corresponding level.

    The reference level defaults to the first level, or can be specified
    explicitly.

    .. ipython:: python

       # reduced rank
       dmatrix("C(a, Treatment)", balanced(a=3))
       # full rank
       dmatrix("0 + C(a, Treatment)", balanced(a=3))
       # Setting a reference level
       dmatrix("C(a, Treatment(1))", balanced(a=3))
       dmatrix("C(a, Treatment(\'a2\'))", balanced(a=3))

    Equivalent to R ``contr.treatment``. The R documentation suggests that
    using ``Treatment(reference=-1)`` will produce contrasts that are
    "equivalent to those produced by many (but not all) SAS procedures".
    '''
    reference: Incomplete
    def __init__(self, reference: Incomplete | None = None) -> None: ...
    def code_with_intercept(self, levels): ...
    def code_without_intercept(self, levels): ...

class Poly:
    '''Orthogonal polynomial contrast coding.

    This coding scheme treats the levels as ordered samples from an underlying
    continuous scale, whose effect takes an unknown functional form which is
    `Taylor-decomposed`__ into the sum of a linear, quadratic, etc. components.

    .. __: https://en.wikipedia.org/wiki/Taylor_series

    For reduced-rank coding, you get a linear column, a quadratic column,
    etc., up to the number of levels provided.

    For full-rank coding, the same scheme is used, except that the zero-order
    constant polynomial is also included. I.e., you get an intercept column
    included as part of your categorical term.

    By default the levels are treated as equally spaced, but you can override
    this by providing a value for the `scores` argument.

    Examples:

    .. ipython:: python

       # Reduced rank
       dmatrix("C(a, Poly)", balanced(a=4))
       # Full rank
       dmatrix("0 + C(a, Poly)", balanced(a=3))
       # Explicit scores
       dmatrix("C(a, Poly([1, 2, 10]))", balanced(a=3))

    This is equivalent to R\'s ``contr.poly``. (But note that in R, reduced
    rank encodings are always dummy-coded, regardless of what contrast you
    have set.)
    '''
    scores: Incomplete
    def __init__(self, scores: Incomplete | None = None) -> None: ...
    def code_with_intercept(self, levels): ...
    def code_without_intercept(self, levels): ...

class Sum:
    '''Deviation coding (also known as sum-to-zero coding).

    Compares the mean of each level to the mean-of-means. (In a balanced
    design, compares the mean of each level to the overall mean.)

    For full-rank coding, a standard intercept term is added.

    One level must be omitted to avoid redundancy; by default this is the last
    level, but this can be adjusted via the `omit` argument.

    .. warning:: There are multiple definitions of \'deviation coding\' in
       use. Make sure this is the one you expect before trying to interpret
       your results!

    Examples:

    .. ipython:: python

       # Reduced rank
       dmatrix("C(a, Sum)", balanced(a=4))
       # Full rank
       dmatrix("0 + C(a, Sum)", balanced(a=4))
       # Omit a different level
       dmatrix("C(a, Sum(1))", balanced(a=3))
       dmatrix("C(a, Sum(\'a1\'))", balanced(a=3))

    This is equivalent to R\'s `contr.sum`.
    '''
    omit: Incomplete
    def __init__(self, omit: Incomplete | None = None) -> None: ...
    def code_with_intercept(self, levels): ...
    def code_without_intercept(self, levels): ...

class Helmert:
    '''Helmert contrasts.

    Compares the second level with the first, the third with the average of
    the first two, and so on.

    For full-rank coding, a standard intercept term is added.

    .. warning:: There are multiple definitions of \'Helmert coding\' in
       use. Make sure this is the one you expect before trying to interpret
       your results!

    Examples:

    .. ipython:: python

       # Reduced rank
       dmatrix("C(a, Helmert)", balanced(a=4))
       # Full rank
       dmatrix("0 + C(a, Helmert)", balanced(a=4))

    This is equivalent to R\'s `contr.helmert`.
    '''
    def code_with_intercept(self, levels): ...
    def code_without_intercept(self, levels): ...

class Diff:
    '''Backward difference coding.

    This coding scheme is useful for ordered factors, and compares the mean of
    each level with the preceding level. So you get the second level minus the
    first, the third level minus the second, etc.

    For full-rank coding, a standard intercept term is added (which gives the
    mean value for the first level).

    Examples:

    .. ipython:: python

       # Reduced rank
       dmatrix("C(a, Diff)", balanced(a=3))
       # Full rank
       dmatrix("0 + C(a, Diff)", balanced(a=3))
    '''
    def code_with_intercept(self, levels): ...
    def code_without_intercept(self, levels): ...
