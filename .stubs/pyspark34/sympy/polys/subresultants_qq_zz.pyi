from sympy.concrete.summations import summation as summation
from sympy.core.function import expand as expand
from sympy.core.numbers import nan as nan
from sympy.core.singleton import S as S
from sympy.functions.elementary.complexes import Abs as Abs, sign as sign
from sympy.functions.elementary.integers import floor as floor
from sympy.matrices.dense import Matrix as Matrix, eye as eye, zeros as zeros
from sympy.polys.domains import QQ as QQ
from sympy.polys.polyerrors import PolynomialError as PolynomialError
from sympy.polys.polytools import LC as LC, Poly as Poly, degree as degree, pquo as pquo, prem as prem, quo as quo, rem as rem
from sympy.simplify.simplify import simplify as simplify

def sylvester(f, g, x, method: int = 1):
    """
      The input polynomials f, g are in Z[x] or in Q[x]. Let m = degree(f, x),
      n = degree(g, x) and mx = max(m, n).

      a. If method = 1 (default), computes sylvester1, Sylvester's matrix of 1840
          of dimension (m + n) x (m + n). The determinants of properly chosen
          submatrices of this matrix (a.k.a. subresultants) can be
          used to compute the coefficients of the Euclidean PRS of f, g.

      b. If method = 2, computes sylvester2, Sylvester's matrix of 1853
          of dimension (2*mx) x (2*mx). The determinants of properly chosen
          submatrices of this matrix (a.k.a. ``modified'' subresultants) can be
          used to compute the coefficients of the Sturmian PRS of f, g.

      Applications of these Matrices can be found in the references below.
      Especially, for applications of sylvester2, see the first reference!!

      References
      ==========
      1. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``On a Theorem
      by Van Vleck Regarding Sturm Sequences. Serdica Journal of Computing,
      Vol. 7, No 4, 101-134, 2013.

      2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Sturm Sequences
      and Modified Subresultant Polynomial Remainder Sequences.''
      Serdica Journal of Computing, Vol. 8, No 1, 29-46, 2014.

    """
def process_matrix_output(poly_seq, x):
    """
    poly_seq is a polynomial remainder sequence computed either by
    (modified_)subresultants_bezout or by (modified_)subresultants_sylv.

    This function removes from poly_seq all zero polynomials as well
    as all those whose degree is equal to the degree of a preceding
    polynomial in poly_seq, as we scan it from left to right.

    """
def subresultants_sylv(f, g, x):
    """
    The input polynomials f, g are in Z[x] or in Q[x]. It is assumed
    that deg(f) >= deg(g).

    Computes the subresultant polynomial remainder sequence (prs)
    of f, g by evaluating determinants of appropriately selected
    submatrices of sylvester(f, g, x, 1). The dimensions of the
    latter are (deg(f) + deg(g)) x (deg(f) + deg(g)).

    Each coefficient is computed by evaluating the determinant of the
    corresponding submatrix of sylvester(f, g, x, 1).

    If the subresultant prs is complete, then the output coincides
    with the Euclidean sequence of the polynomials f, g.

    References:
    ===========
    1. G.M.Diaz-Toca,L.Gonzalez-Vega: Various New Expressions for Subresultants
    and Their Applications. Appl. Algebra in Engin., Communic. and Comp.,
    Vol. 15, 233-266, 2004.

    """
def modified_subresultants_sylv(f, g, x):
    """
    The input polynomials f, g are in Z[x] or in Q[x]. It is assumed
    that deg(f) >= deg(g).

    Computes the modified subresultant polynomial remainder sequence (prs)
    of f, g by evaluating determinants of appropriately selected
    submatrices of sylvester(f, g, x, 2). The dimensions of the
    latter are (2*deg(f)) x (2*deg(f)).

    Each coefficient is computed by evaluating the determinant of the
    corresponding submatrix of sylvester(f, g, x, 2).

    If the modified subresultant prs is complete, then the output coincides
    with the Sturmian sequence of the polynomials f, g.

    References:
    ===========
    1. A. G. Akritas,G.I. Malaschonok and P.S. Vigklas:
    Sturm Sequences and Modified Subresultant Polynomial Remainder
    Sequences. Serdica Journal of Computing, Vol. 8, No 1, 29--46, 2014.

    """
def res(f, g, x):
    """
    The input polynomials f, g are in Z[x] or in Q[x].

    The output is the resultant of f, g computed by evaluating
    the determinant of the matrix sylvester(f, g, x, 1).

    References:
    ===========
    1. J. S. Cohen: Computer Algebra and Symbolic Computation
     - Mathematical Methods. A. K. Peters, 2003.

    """
def res_q(f, g, x):
    """
    The input polynomials f, g are in Z[x] or in Q[x].

    The output is the resultant of f, g computed recursively
    by polynomial divisions in Q[x], using the function rem.
    See Cohen's book p. 281.

    References:
    ===========
    1. J. S. Cohen: Computer Algebra and Symbolic Computation
     - Mathematical Methods. A. K. Peters, 2003.
    """
def res_z(f, g, x):
    """
    The input polynomials f, g are in Z[x] or in Q[x].

    The output is the resultant of f, g computed recursively
    by polynomial divisions in Z[x], using the function prem().
    See Cohen's book p. 283.

    References:
    ===========
    1. J. S. Cohen: Computer Algebra and Symbolic Computation
     - Mathematical Methods. A. K. Peters, 2003.
    """
def sign_seq(poly_seq, x):
    """
    Given a sequence of polynomials poly_seq, it returns
    the sequence of signs of the leading coefficients of
    the polynomials in poly_seq.

    """
def bezout(p, q, x, method: str = 'bz'):
    """
    The input polynomials p, q are in Z[x] or in Q[x]. Let
    mx = max(degree(p, x), degree(q, x)).

    The default option bezout(p, q, x, method='bz') returns Bezout's
    symmetric matrix of p and q, of dimensions (mx) x (mx). The
    determinant of this matrix is equal to the determinant of sylvester2,
    Sylvester's matrix of 1853, whose dimensions are (2*mx) x (2*mx);
    however the subresultants of these two matrices may differ.

    The other option, bezout(p, q, x, 'prs'), is of interest to us
    in this module because it returns a matrix equivalent to sylvester2.
    In this case all subresultants of the two matrices are identical.

    Both the subresultant polynomial remainder sequence (prs) and
    the modified subresultant prs of p and q can be computed by
    evaluating determinants of appropriately selected submatrices of
    bezout(p, q, x, 'prs') --- one determinant per coefficient of the
    remainder polynomials.

    The matrices bezout(p, q, x, 'bz') and bezout(p, q, x, 'prs')
    are related by the formula

    bezout(p, q, x, 'prs') =
    backward_eye(deg(p)) * bezout(p, q, x, 'bz') * backward_eye(deg(p)),

    where backward_eye() is the backward identity function.

    References
    ==========
    1. G.M.Diaz-Toca,L.Gonzalez-Vega: Various New Expressions for Subresultants
    and Their Applications. Appl. Algebra in Engin., Communic. and Comp.,
    Vol. 15, 233-266, 2004.

    """
def backward_eye(n):
    '''
    Returns the backward identity matrix of dimensions n x n.

    Needed to "turn" the Bezout matrices
    so that the leading coefficients are first.
    See docstring of the function bezout(p, q, x, method=\'bz\').
    '''
def subresultants_bezout(p, q, x):
    """
    The input polynomials p, q are in Z[x] or in Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the subresultant polynomial remainder sequence
    of p, q by evaluating determinants of appropriately selected
    submatrices of bezout(p, q, x, 'prs'). The dimensions of the
    latter are deg(p) x deg(p).

    Each coefficient is computed by evaluating the determinant of the
    corresponding submatrix of bezout(p, q, x, 'prs').

    bezout(p, q, x, 'prs) is used instead of sylvester(p, q, x, 1),
    Sylvester's matrix of 1840, because the dimensions of the latter
    are (deg(p) + deg(q)) x (deg(p) + deg(q)).

    If the subresultant prs is complete, then the output coincides
    with the Euclidean sequence of the polynomials p, q.

    References
    ==========
    1. G.M.Diaz-Toca,L.Gonzalez-Vega: Various New Expressions for Subresultants
    and Their Applications. Appl. Algebra in Engin., Communic. and Comp.,
    Vol. 15, 233-266, 2004.

    """
def modified_subresultants_bezout(p, q, x):
    """
    The input polynomials p, q are in Z[x] or in Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the modified subresultant polynomial remainder sequence
    of p, q by evaluating determinants of appropriately selected
    submatrices of bezout(p, q, x, 'prs'). The dimensions of the
    latter are deg(p) x deg(p).

    Each coefficient is computed by evaluating the determinant of the
    corresponding submatrix of bezout(p, q, x, 'prs').

    bezout(p, q, x, 'prs') is used instead of sylvester(p, q, x, 2),
    Sylvester's matrix of 1853, because the dimensions of the latter
    are 2*deg(p) x 2*deg(p).

    If the modified subresultant prs is complete, and LC( p ) > 0, the output
    coincides with the (generalized) Sturm's sequence of the polynomials p, q.

    References
    ==========
    1. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Sturm Sequences
    and Modified Subresultant Polynomial Remainder Sequences.''
    Serdica Journal of Computing, Vol. 8, No 1, 29-46, 2014.

    2. G.M.Diaz-Toca,L.Gonzalez-Vega: Various New Expressions for Subresultants
    and Their Applications. Appl. Algebra in Engin., Communic. and Comp.,
    Vol. 15, 233-266, 2004.


    """
def sturm_pg(p, q, x, method: int = 0):
    """
    p, q are polynomials in Z[x] or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the (generalized) Sturm sequence of p and q in Z[x] or Q[x].
    If q = diff(p, x, 1) it is the usual Sturm sequence.

    A. If method == 0, default, the remainder coefficients of the sequence
       are (in absolute value) ``modified'' subresultants, which for non-monic
       polynomials are greater than the coefficients of the corresponding
       subresultants by the factor Abs(LC(p)**( deg(p)- deg(q))).

    B. If method == 1, the remainder coefficients of the sequence are (in
       absolute value) subresultants, which for non-monic polynomials are
       smaller than the coefficients of the corresponding ``modified''
       subresultants by the factor Abs(LC(p)**( deg(p)- deg(q))).

    If the Sturm sequence is complete, method=0 and LC( p ) > 0, the coefficients
    of the polynomials in the sequence are ``modified'' subresultants.
    That is, they are  determinants of appropriately selected submatrices of
    sylvester2, Sylvester's matrix of 1853. In this case the Sturm sequence
    coincides with the ``modified'' subresultant prs, of the polynomials
    p, q.

    If the Sturm sequence is incomplete and method=0 then the signs of the
    coefficients of the polynomials in the sequence may differ from the signs
    of the coefficients of the corresponding polynomials in the ``modified''
    subresultant prs; however, the absolute values are the same.

    To compute the coefficients, no determinant evaluation takes place. Instead,
    polynomial divisions in Q[x] are performed, using the function rem(p, q, x);
    the coefficients of the remainders computed this way become (``modified'')
    subresultants with the help of the Pell-Gordon Theorem of 1917.
    See also the function euclid_pg(p, q, x).

    References
    ==========
    1. Pell A. J., R. L. Gordon. The Modified Remainders Obtained in Finding
    the Highest Common Factor of Two Polynomials. Annals of MatheMatics,
    Second Series, 18 (1917), No. 4, 188-193.

    2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Sturm Sequences
    and Modified Subresultant Polynomial Remainder Sequences.''
    Serdica Journal of Computing, Vol. 8, No 1, 29-46, 2014.

    """
def sturm_q(p, q, x):
    """
    p, q are polynomials in Z[x] or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the (generalized) Sturm sequence of p and q in Q[x].
    Polynomial divisions in Q[x] are performed, using the function rem(p, q, x).

    The coefficients of the polynomials in the Sturm sequence can be uniquely
    determined from the corresponding coefficients of the polynomials found
    either in:

        (a) the ``modified'' subresultant prs, (references 1, 2)

    or in

        (b) the subresultant prs (reference 3).

    References
    ==========
    1. Pell A. J., R. L. Gordon. The Modified Remainders Obtained in Finding
    the Highest Common Factor of Two Polynomials. Annals of MatheMatics,
    Second Series, 18 (1917), No. 4, 188-193.

    2 Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Sturm Sequences
    and Modified Subresultant Polynomial Remainder Sequences.''
    Serdica Journal of Computing, Vol. 8, No 1, 29-46, 2014.

    3. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``A Basic Result
    on the Theory of Subresultants.'' Serdica Journal of Computing 10 (2016), No.1, 31-48.

    """
def sturm_amv(p, q, x, method: int = 0):
    '''
    p, q are polynomials in Z[x] or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the (generalized) Sturm sequence of p and q in Z[x] or Q[x].
    If q = diff(p, x, 1) it is the usual Sturm sequence.

    A. If method == 0, default, the remainder coefficients of the
       sequence are (in absolute value) ``modified\'\' subresultants, which
       for non-monic polynomials are greater than the coefficients of the
       corresponding subresultants by the factor Abs(LC(p)**( deg(p)- deg(q))).

    B. If method == 1, the remainder coefficients of the sequence are (in
       absolute value) subresultants, which for non-monic polynomials are
       smaller than the coefficients of the corresponding ``modified\'\'
       subresultants by the factor Abs( LC(p)**( deg(p)- deg(q)) ).

    If the Sturm sequence is complete, method=0 and LC( p ) > 0, then the
    coefficients of the polynomials in the sequence are ``modified\'\' subresultants.
    That is, they are  determinants of appropriately selected submatrices of
    sylvester2, Sylvester\'s matrix of 1853. In this case the Sturm sequence
    coincides with the ``modified\'\' subresultant prs, of the polynomials
    p, q.

    If the Sturm sequence is incomplete and method=0 then the signs of the
    coefficients of the polynomials in the sequence may differ from the signs
    of the coefficients of the corresponding polynomials in the ``modified\'\'
    subresultant prs; however, the absolute values are the same.

    To compute the coefficients, no determinant evaluation takes place.
    Instead, we first compute the euclidean sequence  of p and q using
    euclid_amv(p, q, x) and then: (a) change the signs of the remainders in the
    Euclidean sequence according to the pattern "-, -, +, +, -, -, +, +,..."
    (see Lemma 1 in the 1st reference or Theorem 3 in the 2nd reference)
    and (b) if method=0, assuming deg(p) > deg(q), we multiply the remainder
    coefficients of the Euclidean sequence times the factor
    Abs( LC(p)**( deg(p)- deg(q)) ) to make them modified subresultants.
    See also the function sturm_pg(p, q, x).

    References
    ==========
    1. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``A Basic Result
    on the Theory of Subresultants.\'\' Serdica Journal of Computing 10 (2016), No.1, 31-48.

    2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``On the Remainders
    Obtained in Finding the Greatest Common Divisor of Two Polynomials.\'\' Serdica
    Journal of Computing 9(2) (2015), 123-138.

    3. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Subresultant Polynomial
    Remainder Sequences Obtained by Polynomial Divisions in Q[x] or in Z[x].\'\'
    Serdica Journal of Computing 10 (2016), No.3-4, 197-217.

    '''
def euclid_pg(p, q, x):
    '''
    p, q are polynomials in Z[x] or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the Euclidean sequence of p and q in Z[x] or Q[x].

    If the Euclidean sequence is complete the coefficients of the polynomials
    in the sequence are subresultants. That is, they are  determinants of
    appropriately selected submatrices of sylvester1, Sylvester\'s matrix of 1840.
    In this case the Euclidean sequence coincides with the subresultant prs
    of the polynomials p, q.

    If the Euclidean sequence is incomplete the signs of the coefficients of the
    polynomials in the sequence may differ from the signs of the coefficients of
    the corresponding polynomials in the subresultant prs; however, the absolute
    values are the same.

    To compute the Euclidean sequence, no determinant evaluation takes place.
    We first compute the (generalized) Sturm sequence  of p and q using
    sturm_pg(p, q, x, 1), in which case the coefficients are (in absolute value)
    equal to subresultants. Then we change the signs of the remainders in the
    Sturm sequence according to the pattern "-, -, +, +, -, -, +, +,..." ;
    see Lemma 1 in the 1st reference or Theorem 3 in the 2nd reference as well as
    the function sturm_pg(p, q, x).

    References
    ==========
    1. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``A Basic Result
    on the Theory of Subresultants.\'\' Serdica Journal of Computing 10 (2016), No.1, 31-48.

    2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``On the Remainders
    Obtained in Finding the Greatest Common Divisor of Two Polynomials.\'\' Serdica
    Journal of Computing 9(2) (2015), 123-138.

    3. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Subresultant Polynomial
    Remainder Sequences Obtained by Polynomial Divisions in Q[x] or in Z[x].\'\'
    Serdica Journal of Computing 10 (2016), No.3-4, 197-217.
    '''
def euclid_q(p, q, x):
    """
    p, q are polynomials in Z[x] or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the Euclidean sequence of p and q in Q[x].
    Polynomial divisions in Q[x] are performed, using the function rem(p, q, x).

    The coefficients of the polynomials in the Euclidean sequence can be uniquely
    determined from the corresponding coefficients of the polynomials found
    either in:

        (a) the ``modified'' subresultant polynomial remainder sequence,
    (references 1, 2)

    or in

        (b) the subresultant polynomial remainder sequence (references 3).

    References
    ==========
    1. Pell A. J., R. L. Gordon. The Modified Remainders Obtained in Finding
    the Highest Common Factor of Two Polynomials. Annals of MatheMatics,
    Second Series, 18 (1917), No. 4, 188-193.

    2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Sturm Sequences
    and Modified Subresultant Polynomial Remainder Sequences.''
    Serdica Journal of Computing, Vol. 8, No 1, 29-46, 2014.

    3. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``A Basic Result
    on the Theory of Subresultants.'' Serdica Journal of Computing 10 (2016), No.1, 31-48.

    """
def euclid_amv(f, g, x):
    """
    f, g are polynomials in Z[x] or Q[x]. It is assumed
    that degree(f, x) >= degree(g, x).

    Computes the Euclidean sequence of p and q in Z[x] or Q[x].

    If the Euclidean sequence is complete the coefficients of the polynomials
    in the sequence are subresultants. That is, they are  determinants of
    appropriately selected submatrices of sylvester1, Sylvester's matrix of 1840.
    In this case the Euclidean sequence coincides with the subresultant prs,
    of the polynomials p, q.

    If the Euclidean sequence is incomplete the signs of the coefficients of the
    polynomials in the sequence may differ from the signs of the coefficients of
    the corresponding polynomials in the subresultant prs; however, the absolute
    values are the same.

    To compute the coefficients, no determinant evaluation takes place.
    Instead, polynomial divisions in Z[x] or Q[x] are performed, using
    the function rem_z(f, g, x);  the coefficients of the remainders
    computed this way become subresultants with the help of the
    Collins-Brown-Traub formula for coefficient reduction.

    References
    ==========
    1. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``A Basic Result
    on the Theory of Subresultants.'' Serdica Journal of Computing 10 (2016), No.1, 31-48.

    2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Subresultant Polynomial
    remainder Sequences Obtained by Polynomial Divisions in Q[x] or in Z[x].''
    Serdica Journal of Computing 10 (2016), No.3-4, 197-217.

    """
def modified_subresultants_pg(p, q, x):
    """
    p, q are polynomials in Z[x] or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the ``modified'' subresultant prs of p and q in Z[x] or Q[x];
    the coefficients of the polynomials in the sequence are
    ``modified'' subresultants. That is, they are  determinants of appropriately
    selected submatrices of sylvester2, Sylvester's matrix of 1853.

    To compute the coefficients, no determinant evaluation takes place. Instead,
    polynomial divisions in Q[x] are performed, using the function rem(p, q, x);
    the coefficients of the remainders computed this way become ``modified''
    subresultants with the help of the Pell-Gordon Theorem of 1917.

    If the ``modified'' subresultant prs is complete, and LC( p ) > 0, it coincides
    with the (generalized) Sturm sequence of the polynomials p, q.

    References
    ==========
    1. Pell A. J., R. L. Gordon. The Modified Remainders Obtained in Finding
    the Highest Common Factor of Two Polynomials. Annals of MatheMatics,
    Second Series, 18 (1917), No. 4, 188-193.

    2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Sturm Sequences
    and Modified Subresultant Polynomial Remainder Sequences.''
    Serdica Journal of Computing, Vol. 8, No 1, 29-46, 2014.

    """
def subresultants_pg(p, q, x):
    '''
    p, q are polynomials in Z[x] or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the subresultant prs of p and q in Z[x] or Q[x], from
    the modified subresultant prs of p and q.

    The coefficients of the polynomials in these two sequences differ only
    in sign and the factor LC(p)**( deg(p)- deg(q)) as stated in
    Theorem 2 of the reference.

    The coefficients of the polynomials in the output sequence are
    subresultants. That is, they are  determinants of appropriately
    selected submatrices of sylvester1, Sylvester\'s matrix of 1840.

    If the subresultant prs is complete, then it coincides with the
    Euclidean sequence of the polynomials p, q.

    References
    ==========
    1. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: "On the Remainders
    Obtained in Finding the Greatest Common Divisor of Two Polynomials."
    Serdica Journal of Computing 9(2) (2015), 123-138.

    '''
def subresultants_amv_q(p, q, x):
    """
    p, q are polynomials in Z[x] or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the subresultant prs of p and q in Q[x];
    the coefficients of the polynomials in the sequence are
    subresultants. That is, they are  determinants of appropriately
    selected submatrices of sylvester1, Sylvester's matrix of 1840.

    To compute the coefficients, no determinant evaluation takes place.
    Instead, polynomial divisions in Q[x] are performed, using the
    function rem(p, q, x);  the coefficients of the remainders
    computed this way become subresultants with the help of the
    Akritas-Malaschonok-Vigklas Theorem of 2015.

    If the subresultant prs is complete, then it coincides with the
    Euclidean sequence of the polynomials p, q.

    References
    ==========
    1. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``A Basic Result
    on the Theory of Subresultants.'' Serdica Journal of Computing 10 (2016), No.1, 31-48.

    2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Subresultant Polynomial
    remainder Sequences Obtained by Polynomial Divisions in Q[x] or in Z[x].''
    Serdica Journal of Computing 10 (2016), No.3-4, 197-217.

    """
def compute_sign(base, expo):
    """
    base != 0 and expo >= 0 are integers;

    returns the sign of base**expo without
    evaluating the power itself!
    """
def rem_z(p, q, x):
    """
    Intended mainly for p, q polynomials in Z[x] so that,
    on dividing p by q, the remainder will also be in Z[x]. (However,
    it also works fine for polynomials in Q[x].) It is assumed
    that degree(p, x) >= degree(q, x).

    It premultiplies p by the _absolute_ value of the leading coefficient
    of q, raised to the power deg(p) - deg(q) + 1 and then performs
    polynomial division in Q[x], using the function rem(p, q, x).

    By contrast the function prem(p, q, x) does _not_ use the absolute
    value of the leading coefficient of q.
    This results not only in ``messing up the signs'' of the Euclidean and
    Sturmian prs's as mentioned in the second reference,
    but also in violation of the main results of the first and third
    references --- Theorem 4 and Theorem 1 respectively. Theorems 4 and 1
    establish a one-to-one correspondence between the Euclidean and the
    Sturmian prs of p, q, on one hand, and the subresultant prs of p, q,
    on the other.

    References
    ==========
    1. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``On the Remainders
    Obtained in Finding the Greatest Common Divisor of Two Polynomials.''
    Serdica Journal of Computing, 9(2) (2015), 123-138.

    2. https://planetMath.org/sturmstheorem

    3. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``A Basic Result on
    the Theory of Subresultants.'' Serdica Journal of Computing 10 (2016), No.1, 31-48.

    """
def quo_z(p, q, x):
    """
    Intended mainly for p, q polynomials in Z[x] so that,
    on dividing p by q, the quotient will also be in Z[x]. (However,
    it also works fine for polynomials in Q[x].) It is assumed
    that degree(p, x) >= degree(q, x).

    It premultiplies p by the _absolute_ value of the leading coefficient
    of q, raised to the power deg(p) - deg(q) + 1 and then performs
    polynomial division in Q[x], using the function quo(p, q, x).

    By contrast the function pquo(p, q, x) does _not_ use the absolute
    value of the leading coefficient of q.

    See also function rem_z(p, q, x) for additional comments and references.

    """
def subresultants_amv(f, g, x):
    """
    p, q are polynomials in Z[x] or Q[x]. It is assumed
    that degree(f, x) >= degree(g, x).

    Computes the subresultant prs of p and q in Z[x] or Q[x];
    the coefficients of the polynomials in the sequence are
    subresultants. That is, they are  determinants of appropriately
    selected submatrices of sylvester1, Sylvester's matrix of 1840.

    To compute the coefficients, no determinant evaluation takes place.
    Instead, polynomial divisions in Z[x] or Q[x] are performed, using
    the function rem_z(p, q, x);  the coefficients of the remainders
    computed this way become subresultants with the help of the
    Akritas-Malaschonok-Vigklas Theorem of 2015 and the Collins-Brown-
    Traub formula for coefficient reduction.

    If the subresultant prs is complete, then it coincides with the
    Euclidean sequence of the polynomials p, q.

    References
    ==========
    1. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``A Basic Result
    on the Theory of Subresultants.'' Serdica Journal of Computing 10 (2016), No.1, 31-48.

    2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Subresultant Polynomial
    remainder Sequences Obtained by Polynomial Divisions in Q[x] or in Z[x].''
    Serdica Journal of Computing 10 (2016), No.3-4, 197-217.

    """
def modified_subresultants_amv(p, q, x):
    '''
    p, q are polynomials in Z[x] or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the modified subresultant prs of p and q in Z[x] or Q[x],
    from the subresultant prs of p and q.
    The coefficients of the polynomials in the two sequences differ only
    in sign and the factor LC(p)**( deg(p)- deg(q)) as stated in
    Theorem 2 of the reference.

    The coefficients of the polynomials in the output sequence are
    modified subresultants. That is, they are  determinants of appropriately
    selected submatrices of sylvester2, Sylvester\'s matrix of 1853.

    If the modified subresultant prs is complete, and LC( p ) > 0, it coincides
    with the (generalized) Sturm\'s sequence of the polynomials p, q.

    References
    ==========
    1. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: "On the Remainders
    Obtained in Finding the Greatest Common Divisor of Two Polynomials."
    Serdica Journal of Computing, Serdica Journal of Computing, 9(2) (2015), 123-138.

    '''
def correct_sign(deg_f, deg_g, s1, rdel, cdel):
    """
    Used in various subresultant prs algorithms.

    Evaluates the determinant, (a.k.a. subresultant) of a properly selected
    submatrix of s1, Sylvester's matrix of 1840, to get the correct sign
    and value of the leading coefficient of a given polynomial remainder.

    deg_f, deg_g are the degrees of the original polynomials p, q for which the
    matrix s1 = sylvester(p, q, x, 1) was constructed.

    rdel denotes the expected degree of the remainder; it is the number of
    rows to be deleted from each group of rows in s1 as described in the
    reference below.

    cdel denotes the expected degree minus the actual degree of the remainder;
    it is the number of columns to be deleted --- starting with the last column
    forming the square matrix --- from the matrix resulting after the row deletions.

    References
    ==========
    Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``Sturm Sequences
    and Modified Subresultant Polynomial Remainder Sequences.''
    Serdica Journal of Computing, Vol. 8, No 1, 29-46, 2014.

    """
def subresultants_rem(p, q, x):
    """
    p, q are polynomials in Z[x] or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the subresultant prs of p and q in Z[x] or Q[x];
    the coefficients of the polynomials in the sequence are
    subresultants. That is, they are  determinants of appropriately
    selected submatrices of sylvester1, Sylvester's matrix of 1840.

    To compute the coefficients polynomial divisions in Q[x] are
    performed, using the function rem(p, q, x). The coefficients
    of the remainders computed this way become subresultants by evaluating
    one subresultant per remainder --- that of the leading coefficient.
    This way we obtain the correct sign and value of the leading coefficient
    of the remainder and we easily ``force'' the rest of the coefficients
    to become subresultants.

    If the subresultant prs is complete, then it coincides with the
    Euclidean sequence of the polynomials p, q.

    References
    ==========
    1. Akritas, A. G.:``Three New Methods for Computing Subresultant
    Polynomial Remainder Sequences (PRS's).'' Serdica Journal of Computing 9(1) (2015), 1-26.

    """
def pivot(M, i, j):
    """
    M is a matrix, and M[i, j] specifies the pivot element.

    All elements below M[i, j], in the j-th column, will
    be zeroed, if they are not already 0, according to
    Dodgson-Bareiss' integer preserving transformations.

    References
    ==========
    1. Akritas, A. G.: ``A new method for computing polynomial greatest
    common divisors and polynomial remainder sequences.''
    Numerische MatheMatik 52, 119-127, 1988.

    2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``On a Theorem
    by Van Vleck Regarding Sturm Sequences.''
    Serdica Journal of Computing, 7, No 4, 101-134, 2013.

    """
def rotate_r(L, k):
    """
    Rotates right by k. L is a row of a matrix or a list.

    """
def rotate_l(L, k):
    """
    Rotates left by k. L is a row of a matrix or a list.

    """
def row2poly(row, deg, x):
    """
    Converts the row of a matrix to a poly of degree deg and variable x.
    Some entries at the beginning and/or at the end of the row may be zero.

    """
def create_ma(deg_f, deg_g, row1, row2, col_num):
    """
    Creates a ``small'' matrix M to be triangularized.

    deg_f, deg_g are the degrees of the divident and of the
    divisor polynomials respectively, deg_g > deg_f.

    The coefficients of the divident poly are the elements
    in row2 and those of the divisor poly are the elements
    in row1.

    col_num defines the number of columns of the matrix M.

    """
def find_degree(M, deg_f):
    """
    Finds the degree of the poly corresponding (after triangularization)
    to the _last_ row of the ``small'' matrix M, created by create_ma().

    deg_f is the degree of the divident poly.
    If _last_ row is all 0's returns None.

    """
def final_touches(s2, r, deg_g):
    """
    s2 is sylvester2, r is the row pointer in s2,
    deg_g is the degree of the poly last inserted in s2.

    After a gcd of degree > 0 has been found with Van Vleck's
    method, and was inserted into s2, if its last term is not
    in the last column of s2, then it is inserted as many
    times as needed, rotated right by one each time, until
    the condition is met.

    """
def subresultants_vv(p, q, x, method: int = 0):
    """
    p, q are polynomials in Z[x] (intended) or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the subresultant prs of p, q by triangularizing,
    in Z[x] or in Q[x], all the smaller matrices encountered in the
    process of triangularizing sylvester2, Sylvester's matrix of 1853;
    see references 1 and 2 for Van Vleck's method. With each remainder,
    sylvester2 gets updated and is prepared to be printed if requested.

    If sylvester2 has small dimensions and you want to see the final,
    triangularized matrix use this version with method=1; otherwise,
    use either this version with method=0 (default) or the faster version,
    subresultants_vv_2(p, q, x), where sylvester2 is used implicitly.

    Sylvester's matrix sylvester1  is also used to compute one
    subresultant per remainder; namely, that of the leading
    coefficient, in order to obtain the correct sign and to
    force the remainder coefficients to become subresultants.

    If the subresultant prs is complete, then it coincides with the
    Euclidean sequence of the polynomials p, q.

    If the final, triangularized matrix s2 is printed, then:
        (a) if deg(p) - deg(q) > 1 or deg( gcd(p, q) ) > 0, several
            of the last rows in s2 will remain unprocessed;
        (b) if deg(p) - deg(q) == 0, p will not appear in the final matrix.

    References
    ==========
    1. Akritas, A. G.: ``A new method for computing polynomial greatest
    common divisors and polynomial remainder sequences.''
    Numerische MatheMatik 52, 119-127, 1988.

    2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``On a Theorem
    by Van Vleck Regarding Sturm Sequences.''
    Serdica Journal of Computing, 7, No 4, 101-134, 2013.

    3. Akritas, A. G.:``Three New Methods for Computing Subresultant
    Polynomial Remainder Sequences (PRS's).'' Serdica Journal of Computing 9(1) (2015), 1-26.

    """
def subresultants_vv_2(p, q, x):
    """
    p, q are polynomials in Z[x] (intended) or Q[x]. It is assumed
    that degree(p, x) >= degree(q, x).

    Computes the subresultant prs of p, q by triangularizing,
    in Z[x] or in Q[x], all the smaller matrices encountered in the
    process of triangularizing sylvester2, Sylvester's matrix of 1853;
    see references 1 and 2 for Van Vleck's method.

    If the sylvester2 matrix has big dimensions use this version,
    where sylvester2 is used implicitly. If you want to see the final,
    triangularized matrix sylvester2, then use the first version,
    subresultants_vv(p, q, x, 1).

    sylvester1, Sylvester's matrix of 1840, is also used to compute
    one subresultant per remainder; namely, that of the leading
    coefficient, in order to obtain the correct sign and to
    ``force'' the remainder coefficients to become subresultants.

    If the subresultant prs is complete, then it coincides with the
    Euclidean sequence of the polynomials p, q.

    References
    ==========
    1. Akritas, A. G.: ``A new method for computing polynomial greatest
    common divisors and polynomial remainder sequences.''
    Numerische MatheMatik 52, 119-127, 1988.

    2. Akritas, A. G., G.I. Malaschonok and P.S. Vigklas: ``On a Theorem
    by Van Vleck Regarding Sturm Sequences.''
    Serdica Journal of Computing, 7, No 4, 101-134, 2013.

    3. Akritas, A. G.:``Three New Methods for Computing Subresultant
    Polynomial Remainder Sequences (PRS's).'' Serdica Journal of Computing 9(1) (2015), 1-26.

    """
