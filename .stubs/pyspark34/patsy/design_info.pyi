import numpy as np
from _typeshed import Incomplete
from patsy.util import no_pickling

__all__ = ['DesignInfo', 'FactorInfo', 'SubtermInfo', 'DesignMatrix']

class FactorInfo:
    '''A FactorInfo object is a simple class that provides some metadata about
    the role of a factor within a model. :attr:`DesignInfo.factor_infos` is
    a dictionary which maps factor objects to FactorInfo objects for each
    factor in the model.

    .. versionadded:: 0.4.0

    Attributes:

    .. attribute:: factor

       The factor object being described.

    .. attribute:: type

       The type of the factor -- either the string ``"numerical"`` or the
       string ``"categorical"``.

    .. attribute:: state

       An opaque object which holds the state needed to evaluate this
       factor on new data (e.g., for prediction). See
       :meth:`factor_protocol.eval`.

    .. attribute:: num_columns

       For numerical factors, the number of columns this factor produces. For
       categorical factors, this attribute will always be ``None``.

    .. attribute:: categories

       For categorical factors, a tuple of the possible categories this factor
       takes on, in order. For numerical factors, this attribute will always be
       ``None``.
    '''
    factor: Incomplete
    type: Incomplete
    state: Incomplete
    num_columns: Incomplete
    categories: Incomplete
    def __init__(self, factor, type, state, num_columns: Incomplete | None = None, categories: Incomplete | None = None) -> None: ...

class SubtermInfo:
    '''A SubtermInfo object is a simple metadata container describing a single
    primitive interaction and how it is coded in our design matrix. Our final
    design matrix is produced by coding each primitive interaction in order
    from left to right, and then stacking the resulting columns. For each
    :class:`Term`, we have one or more of these objects which describe how
    that term is encoded. :attr:`DesignInfo.term_codings` is a dictionary
    which maps term objects to lists of SubtermInfo objects.

    To code a primitive interaction, the following steps are performed:

    * Evaluate each factor on the provided data.
    * Encode each factor into one or more proto-columns. For numerical
      factors, these proto-columns are identical to whatever the factor
      evaluates to; for categorical factors, they are encoded using a
      specified contrast matrix.
    * Form all pairwise, elementwise products between proto-columns generated
      by different factors. (For example, if factor 1 generated proto-columns
      A and B, and factor 2 generated proto-columns C and D, then our final
      columns are ``A * C``, ``B * C``, ``A * D``, ``B * D``.)
    * The resulting columns are stored directly into the final design matrix.

    Sometimes multiple primitive interactions are needed to encode a single
    term; this occurs, for example, in the formula ``"1 + a:b"`` when ``a``
    and ``b`` are categorical. See :ref:`formulas-building` for full details.

    .. versionadded:: 0.4.0

    Attributes:

    .. attribute:: factors

       The factors which appear in this subterm\'s interaction.

    .. attribute:: contrast_matrices

       A dict mapping factor objects to :class:`ContrastMatrix` objects,
       describing how each categorical factor in this interaction is coded.

    .. attribute:: num_columns

       The number of design matrix columns which this interaction generates.

    '''
    factors: Incomplete
    contrast_matrices: Incomplete
    num_columns: Incomplete
    def __init__(self, factors, contrast_matrices, num_columns) -> None: ...

class DesignInfo:
    """A DesignInfo object holds metadata about a design matrix.

    This is the main object that Patsy uses to pass metadata about a design
    matrix to statistical libraries, in order to allow further downstream
    processing like intelligent tests, prediction on new data, etc. Usually
    encountered as the `.design_info` attribute on design matrices.

    """
    column_name_indexes: Incomplete
    factor_infos: Incomplete
    term_codings: Incomplete
    term_slices: Incomplete
    term_name_slices: Incomplete
    def __init__(self, column_names, factor_infos: Incomplete | None = None, term_codings: Incomplete | None = None) -> None: ...
    @property
    def column_names(self):
        """A list of the column names, in order."""
    @property
    def terms(self):
        """A list of :class:`Terms`, in order, or else None."""
    @property
    def term_names(self):
        """A list of terms, in order."""
    @property
    def builder(self):
        """.. deprecated:: 0.4.0"""
    @property
    def design_info(self):
        """.. deprecated:: 0.4.0"""
    def slice(self, columns_specifier):
        '''Locate a subset of design matrix columns, specified symbolically.

        A patsy design matrix has two levels of structure: the individual
        columns (which are named), and the :ref:`terms <formulas>` in
        the formula that generated those columns. This is a one-to-many
        relationship: a single term may span several columns. This method
        provides a user-friendly API for locating those columns.

        (While we talk about columns here, this is probably most useful for
        indexing into other arrays that are derived from the design matrix,
        such as regression coefficients or covariance matrices.)

        The `columns_specifier` argument can take a number of forms:

        * A term name
        * A column name
        * A :class:`Term` object
        * An integer giving a raw index
        * A raw slice object

        In all cases, a Python :func:`slice` object is returned, which can be
        used directly for indexing.

        Example::

          y, X = dmatrices("y ~ a", demo_data("y", "a", nlevels=3))
          betas = np.linalg.lstsq(X, y)[0]
          a_betas = betas[X.design_info.slice("a")]

        (If you want to look up a single individual column by name, use
        ``design_info.column_name_indexes[name]``.)
        '''
    def linear_constraint(self, constraint_likes):
        '''Construct a linear constraint in matrix form from a (possibly
        symbolic) description.

        Possible inputs:

        * A dictionary which is taken as a set of equality constraint. Keys
          can be either string column names, or integer column indexes.
        * A string giving a arithmetic expression referring to the matrix
          columns by name.
        * A list of such strings which are ANDed together.
        * A tuple (A, b) where A and b are array_likes, and the constraint is
          Ax = b. If necessary, these will be coerced to the proper
          dimensionality by appending dimensions with size 1.

        The string-based language has the standard arithmetic operators, / * +
        - and parentheses, plus "=" is used for equality and "," is used to
        AND together multiple constraint equations within a string. You can
        If no = appears in some expression, then that expression is assumed to
        be equal to zero. Division is always float-based, even if
        ``__future__.true_division`` isn\'t in effect.

        Returns a :class:`LinearConstraint` object.

        Examples::

          di = DesignInfo(["x1", "x2", "x3"])

          # Equivalent ways to write x1 == 0:
          di.linear_constraint({"x1": 0})  # by name
          di.linear_constraint({0: 0})  # by index
          di.linear_constraint("x1 = 0")  # string based
          di.linear_constraint("x1")  # can leave out "= 0"
          di.linear_constraint("2 * x1 = (x1 + 2 * x1) / 3")
          di.linear_constraint(([1, 0, 0], 0))  # constraint matrices

          # Equivalent ways to write x1 == 0 and x3 == 10
          di.linear_constraint({"x1": 0, "x3": 10})
          di.linear_constraint({0: 0, 2: 10})
          di.linear_constraint({0: 0, "x3": 10})
          di.linear_constraint("x1 = 0, x3 = 10")
          di.linear_constraint("x1, x3 = 10")
          di.linear_constraint(["x1", "x3 = 0"])  # list of strings
          di.linear_constraint("x1 = 0, x3 - 10 = x1")
          di.linear_constraint([[1, 0, 0], [0, 0, 1]], [0, 10])

          # You can also chain together equalities, just like Python:
          di.linear_constraint("x1 = x2 = 3")
        '''
    def describe(self):
        '''Returns a human-readable string describing this design info.

        Example:

        .. ipython::

          In [1]: y, X = dmatrices("y ~ x1 + x2", demo_data("y", "x1", "x2"))

          In [2]: y.design_info.describe()
          Out[2]: \'y\'

          In [3]: X.design_info.describe()
          Out[3]: \'1 + x1 + x2\'

        .. warning::

           There is no guarantee that the strings returned by this function
           can be parsed as formulas, or that if they can be parsed as a
           formula that they will produce a model equivalent to the one you
           started with. This function produces a best-effort description
           intended for humans to read.

        '''
    def subset(self, which_terms):
        '''Create a new :class:`DesignInfo` for design matrices that contain a
        subset of the terms that the current :class:`DesignInfo` does.

        For example, if ``design_info`` has terms ``x``, ``y``, and ``z``,
        then::

          design_info2 = design_info.subset(["x", "z"])

        will return a new DesignInfo that can be used to construct design
        matrices with only the columns corresponding to the terms ``x`` and
        ``z``. After we do this, then in general these two expressions will
        return the same thing (here we assume that ``x``, ``y``, and ``z``
        each generate a single column of the output)::

          build_design_matrix([design_info], data)[0][:, [0, 2]]
          build_design_matrix([design_info2], data)[0]

        However, a critical difference is that in the second case, ``data``
        need not contain any values for ``y``. This is very useful when doing
        prediction using a subset of a model, in which situation R usually
        forces you to specify dummy values for ``y``.

        If using a formula to specify the terms to include, remember that like
        any formula, the intercept term will be included by default, so use
        ``0`` or ``-1`` in your formula if you want to avoid this.

        This method can also be used to reorder the terms in your design
        matrix, in case you want to do that for some reason. I can\'t think of
        any.

        Note that this method will generally *not* produce the same result as
        creating a new model directly. Consider these DesignInfo objects::

            design1 = dmatrix("1 + C(a)", data)
            design2 = design1.subset("0 + C(a)")
            design3 = dmatrix("0 + C(a)", data)

        Here ``design2`` and ``design3`` will both produce design matrices
        that contain an encoding of ``C(a)`` without any intercept term. But
        ``design3`` uses a full-rank encoding for the categorical term
        ``C(a)``, while ``design2`` uses the same reduced-rank encoding as
        ``design1``.

        :arg which_terms: The terms which should be kept in the new
          :class:`DesignMatrixBuilder`. If this is a string, then it is parsed
          as a formula, and then the names of the resulting terms are taken as
          the terms to keep. If it is a list, then it can contain a mixture of
          term names (as strings) and :class:`Term` objects.

        .. versionadded: 0.2.0
           New method on the class DesignMatrixBuilder.

        .. versionchanged: 0.4.0
           Moved from DesignMatrixBuilder to DesignInfo, as part of the
           removal of DesignMatrixBuilder.

        '''
    @classmethod
    def from_array(cls, array_like, default_column_prefix: str = 'column'):
        """Find or construct a DesignInfo appropriate for a given array_like.

        If the input `array_like` already has a ``.design_info``
        attribute, then it will be returned. Otherwise, a new DesignInfo
        object will be constructed, using names either taken from the
        `array_like` (e.g., for a pandas DataFrame with named columns), or
        constructed using `default_column_prefix`.

        This is how :func:`dmatrix` (for example) creates a DesignInfo object
        if an arbitrary matrix is passed in.

        :arg array_like: An ndarray or pandas container.
        :arg default_column_prefix: If it's necessary to invent column names,
          then this will be used to construct them.
        :returns: a DesignInfo object
        """

class DesignMatrix(np.ndarray):
    '''A simple numpy array subclass that carries design matrix metadata.

    .. attribute:: design_info

       A :class:`DesignInfo` object containing metadata about this design
       matrix.

    This class also defines a fancy __repr__ method with labeled
    columns. Otherwise it is identical to a regular numpy ndarray.

    .. warning::

       You should never check for this class using
       :func:`isinstance`. Limitations of the numpy API mean that it is
       impossible to prevent the creation of numpy arrays that have type
       DesignMatrix, but that are not actually design matrices (and such
       objects will behave like regular ndarrays in every way). Instead, check
       for the presence of a ``.design_info`` attribute -- this will be
       present only on "real" DesignMatrix objects.
    '''
    design_info: Incomplete
    def __new__(cls, input_array, design_info: Incomplete | None = None, default_column_prefix: str = 'column'):
        """Create a DesignMatrix, or cast an existing matrix to a DesignMatrix.

        A call like::

          DesignMatrix(my_array)

        will convert an arbitrary array_like object into a DesignMatrix.

        The return from this function is guaranteed to be a two-dimensional
        ndarray with a real-valued floating point dtype, and a
        ``.design_info`` attribute which matches its shape. If the
        `design_info` argument is not given, then one is created via
        :meth:`DesignInfo.from_array` using the given
        `default_column_prefix`.

        Depending on the input array, it is possible this will pass through
        its input unchanged, or create a view.
        """
    __reduce__ = no_pickling
