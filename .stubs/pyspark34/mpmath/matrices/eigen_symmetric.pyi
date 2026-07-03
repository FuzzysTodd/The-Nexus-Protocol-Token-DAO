from ..libmp.backend import xrange as xrange
from .eigen import defun as defun

def r_sy_tridiag(ctx, A, D, E, calc_ev: bool = True) -> None:
    """
    This routine transforms a real symmetric matrix A to a real symmetric
    tridiagonal matrix T using an orthogonal similarity transformation:
          Q' * A * Q = T     (here ' denotes the matrix transpose).
    The orthogonal matrix Q is build up from Householder reflectors.

    parameters:
      A         (input/output) On input, A contains the real symmetric matrix of
                dimension (n,n). On output, if calc_ev is true, A contains the
                orthogonal matrix Q, otherwise A is destroyed.

      D         (output) real array of length n, contains the diagonal elements
                of the tridiagonal matrix

      E         (output) real array of length n, contains the offdiagonal elements
                of the tridiagonal matrix in E[0:(n-1)] where is the dimension of
                the matrix A. E[n-1] is undefined.

      calc_ev   (input) If calc_ev is true, this routine explicitly calculates the
                orthogonal matrix Q which is then returned in A. If calc_ev is
                false, Q is not explicitly calculated resulting in a shorter run time.

    This routine is a python translation of the fortran routine tred2.f in the
    software library EISPACK (see netlib.org) which itself is based on the algol
    procedure tred2 described in:
      - Num. Math. 11, p.181-195 (1968) by Martin, Reinsch and Wilkonson
      - Handbook for auto. comp., Vol II, Linear Algebra, p.212-226 (1971)

    For a good introduction to Householder reflections, see also
      Stoer, Bulirsch - Introduction to Numerical Analysis.
    """
def c_he_tridiag_0(ctx, A, D, E, T) -> None:
    """
    This routine transforms a complex hermitian matrix A to a real symmetric
    tridiagonal matrix T using an unitary similarity transformation:
          Q' * A * Q = T     (here ' denotes the hermitian matrix transpose,
                              i.e. transposition und conjugation).
    The unitary matrix Q is build up from Householder reflectors and
    an unitary diagonal matrix.

    parameters:
      A         (input/output) On input, A contains the complex hermitian matrix
                of dimension (n,n). On output, A contains the unitary matrix Q
                in compressed form.

      D         (output) real array of length n, contains the diagonal elements
                of the tridiagonal matrix.

      E         (output) real array of length n, contains the offdiagonal elements
                of the tridiagonal matrix in E[0:(n-1)] where is the dimension of
                the matrix A. E[n-1] is undefined.

      T         (output) complex array of length n, contains a unitary diagonal
                matrix.

    This routine is a python translation (in slightly modified form) of the fortran
    routine htridi.f in the software library EISPACK (see netlib.org) which itself
    is a complex version of the algol procedure tred1 described in:
      - Num. Math. 11, p.181-195 (1968) by Martin, Reinsch and Wilkonson
      - Handbook for auto. comp., Vol II, Linear Algebra, p.212-226 (1971)

    For a good introduction to Householder reflections, see also
      Stoer, Bulirsch - Introduction to Numerical Analysis.
    """
def c_he_tridiag_1(ctx, A, T) -> None:
    """
    This routine forms the unitary matrix Q described in c_he_tridiag_0.

    parameters:
      A    (input/output) On input, A is the same matrix as delivered by
           c_he_tridiag_0. On output, A is set to Q.

      T    (input) On input, T is the same array as delivered by c_he_tridiag_0.

    """
def c_he_tridiag_2(ctx, A, T, B) -> None:
    """
    This routine applied the unitary matrix Q described in c_he_tridiag_0
    onto the the matrix B, i.e. it forms Q*B.

    parameters:
      A    (input) On input, A is the same matrix as delivered by c_he_tridiag_0.

      T    (input) On input, T is the same array as delivered by c_he_tridiag_0.

      B    (input/output) On input, B is a complex matrix. On output B is replaced
           by Q*B.

    This routine is a python translation of the fortran routine htribk.f in the
    software library EISPACK (see netlib.org). See c_he_tridiag_0 for more
    references.
    """
def tridiag_eigen(ctx, d, e, z: bool = False) -> None:
    """
    This subroutine find the eigenvalues and the first components of the
    eigenvectors of a real symmetric tridiagonal matrix using the implicit
    QL method.

    parameters:

      d (input/output) real array of length n. on input, d contains the diagonal
        elements of the input matrix. on output, d contains the eigenvalues in
        ascending order.

      e (input) real array of length n. on input, e contains the offdiagonal
        elements of the input matrix in e[0:(n-1)]. On output, e has been
        destroyed.

      z (input/output) If z is equal to False, no eigenvectors will be computed.
        Otherwise on input z should have the format z[0:m,0:n] (i.e. a real or
        complex matrix of dimension (m,n) ). On output this matrix will be
        multiplied by the matrix of the eigenvectors (i.e. the columns of this
        matrix are the eigenvectors): z --> z*EV
        That means if z[i,j]={1 if j==j; 0 otherwise} on input, then on output
        z will contain the first m components of the eigenvectors. That means
        if m is equal to n, the i-th eigenvector will be z[:,i].

    This routine is a python translation (in slightly modified form) of the
    fortran routine imtql2.f in the software library EISPACK (see netlib.org)
    which itself is based on the algol procudure imtql2 desribed in:
     - num. math. 12, p. 377-383(1968) by matrin and wilkinson
     - modified in num. math. 15, p. 450(1970) by dubrulle
     - handbook for auto. comp., vol. II-linear algebra, p. 241-248 (1971)
    See also the routine gaussq.f in netlog.org or acm algorithm 726.
    """
def eigsy(ctx, A, eigvals_only: bool = False, overwrite_a: bool = False):
    """
    This routine solves the (ordinary) eigenvalue problem for a real symmetric
    square matrix A. Given A, an orthogonal matrix Q is calculated which
    diagonalizes A:

          Q' A Q = diag(E)               and                Q Q' = Q' Q = 1

    Here diag(E) is a diagonal matrix whose diagonal is E.
    ' denotes the transpose.

    The columns of Q are the eigenvectors of A and E contains the eigenvalues:

          A Q[:,i] = E[i] Q[:,i]


    input:

      A: real matrix of format (n,n) which is symmetric
         (i.e. A=A' or A[i,j]=A[j,i])

      eigvals_only: if true, calculates only the eigenvalues E.
                    if false, calculates both eigenvectors and eigenvalues.

      overwrite_a: if true, allows modification of A which may improve
                   performance. if false, A is not modified.

    output:

      E: vector of format (n). contains the eigenvalues of A in ascending order.

      Q: orthogonal matrix of format (n,n). contains the eigenvectors
         of A as columns.

    return value:

          E          if eigvals_only is true
         (E, Q)      if eigvals_only is false

    example:
      >>> from mpmath import mp
      >>> A = mp.matrix([[3, 2], [2, 0]])
      >>> E = mp.eigsy(A, eigvals_only = True)
      >>> print(E)
      [-1.0]
      [ 4.0]

      >>> A = mp.matrix([[1, 2], [2, 3]])
      >>> E, Q = mp.eigsy(A)
      >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
      [0.0]
      [0.0]

    see also: eighe, eigh, eig
    """
def eighe(ctx, A, eigvals_only: bool = False, overwrite_a: bool = False):
    """
    This routine solves the (ordinary) eigenvalue problem for a complex
    hermitian square matrix A. Given A, an unitary matrix Q is calculated which
    diagonalizes A:

        Q' A Q = diag(E)               and                Q Q' = Q' Q = 1

    Here diag(E) a is diagonal matrix whose diagonal is E.
    ' denotes the hermitian transpose (i.e. ordinary transposition and
    complex conjugation).

    The columns of Q are the eigenvectors of A and E contains the eigenvalues:

        A Q[:,i] = E[i] Q[:,i]


    input:

      A: complex matrix of format (n,n) which is hermitian
         (i.e. A=A' or A[i,j]=conj(A[j,i]))

      eigvals_only: if true, calculates only the eigenvalues E.
                    if false, calculates both eigenvectors and eigenvalues.

      overwrite_a: if true, allows modification of A which may improve
                   performance. if false, A is not modified.

    output:

      E: vector of format (n). contains the eigenvalues of A in ascending order.

      Q: unitary matrix of format (n,n). contains the eigenvectors
         of A as columns.

    return value:

           E         if eigvals_only is true
          (E, Q)     if eigvals_only is false

    example:
      >>> from mpmath import mp
      >>> A = mp.matrix([[1, -3 - 1j], [-3 + 1j, -2]])
      >>> E = mp.eighe(A, eigvals_only = True)
      >>> print(E)
      [-4.0]
      [ 3.0]

      >>> A = mp.matrix([[1, 2 + 5j], [2 - 5j, 3]])
      >>> E, Q = mp.eighe(A)
      >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
      [0.0]
      [0.0]

    see also: eigsy, eigh, eig
    """
def eigh(ctx, A, eigvals_only: bool = False, overwrite_a: bool = False):
    '''
    "eigh" is a unified interface for "eigsy" and "eighe". Depending on
    whether A is real or complex the appropriate function is called.

    This routine solves the (ordinary) eigenvalue problem for a real symmetric
    or complex hermitian square matrix A. Given A, an orthogonal (A real) or
    unitary (A complex) matrix Q is calculated which diagonalizes A:

        Q\' A Q = diag(E)               and                Q Q\' = Q\' Q = 1

    Here diag(E) a is diagonal matrix whose diagonal is E.
    \' denotes the hermitian transpose (i.e. ordinary transposition and
    complex conjugation).

    The columns of Q are the eigenvectors of A and E contains the eigenvalues:

        A Q[:,i] = E[i] Q[:,i]

    input:

      A: a real or complex square matrix of format (n,n) which is symmetric
         (i.e. A[i,j]=A[j,i]) or hermitian (i.e. A[i,j]=conj(A[j,i])).

      eigvals_only: if true, calculates only the eigenvalues E.
                    if false, calculates both eigenvectors and eigenvalues.

      overwrite_a: if true, allows modification of A which may improve
                   performance. if false, A is not modified.

    output:

      E: vector of format (n). contains the eigenvalues of A in ascending order.

      Q: an orthogonal or unitary matrix of format (n,n). contains the
         eigenvectors of A as columns.

    return value:

          E         if eigvals_only is true
         (E, Q)     if eigvals_only is false

    example:
      >>> from mpmath import mp
      >>> A = mp.matrix([[3, 2], [2, 0]])
      >>> E = mp.eigh(A, eigvals_only = True)
      >>> print(E)
      [-1.0]
      [ 4.0]

      >>> A = mp.matrix([[1, 2], [2, 3]])
      >>> E, Q = mp.eigh(A)
      >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
      [0.0]
      [0.0]

      >>> A = mp.matrix([[1, 2 + 5j], [2 - 5j, 3]])
      >>> E, Q = mp.eigh(A)
      >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
      [0.0]
      [0.0]

    see also: eigsy, eighe, eig
    '''
def gauss_quadrature(ctx, n, qtype: str = 'legendre', alpha: int = 0, beta: int = 0):
    '''
    This routine calulates gaussian quadrature rules for different
    families of orthogonal polynomials. Let (a, b) be an interval,
    W(x) a positive weight function and n a positive integer.
    Then the purpose of this routine is to calculate pairs (x_k, w_k)
    for k=0, 1, 2, ... (n-1) which give

      int(W(x) * F(x), x = a..b) = sum(w_k * F(x_k),k = 0..(n-1))

    exact for all polynomials F(x) of degree (strictly) less than 2*n. For all
    integrable functions F(x) the sum is a (more or less) good approximation to
    the integral. The x_k are called nodes (which are the zeros of the
    related orthogonal polynomials) and the w_k are called the weights.

    parameters
       n        (input) The degree of the quadrature rule, i.e. its number of
                nodes.

       qtype    (input) The family of orthogonal polynmomials for which to
                compute the quadrature rule. See the list below.

       alpha    (input) real number, used as parameter for some orthogonal
                polynomials

       beta     (input) real number, used as parameter for some orthogonal
                polynomials.

    return value

      (X, W)    a pair of two real arrays where x_k = X[k] and w_k = W[k].


    orthogonal polynomials:

      qtype           polynomial
      -----           ----------

      "legendre"      Legendre polynomials, W(x)=1 on the interval (-1, +1)
      "legendre01"    shifted Legendre polynomials, W(x)=1 on the interval (0, +1)
      "hermite"       Hermite polynomials, W(x)=exp(-x*x) on (-infinity,+infinity)
      "laguerre"      Laguerre polynomials, W(x)=exp(-x) on (0,+infinity)
      "glaguerre"     generalized Laguerre polynomials, W(x)=exp(-x)*x**alpha
                      on (0, +infinity)
      "chebyshev1"    Chebyshev polynomials of the first kind, W(x)=1/sqrt(1-x*x)
                      on (-1, +1)
      "chebyshev2"    Chebyshev polynomials of the second kind, W(x)=sqrt(1-x*x)
                      on (-1, +1)
      "jacobi"        Jacobi polynomials, W(x)=(1-x)**alpha * (1+x)**beta on (-1, +1)
                      with alpha>-1 and beta>-1

    examples:
      >>> from mpmath import mp
      >>> f = lambda x: x**8 + 2 * x**6 - 3 * x**4 + 5 * x**2 - 7
      >>> X, W = mp.gauss_quadrature(5, "hermite")
      >>> A = mp.fdot([(f(x), w) for x, w in zip(X, W)])
      >>> B = mp.sqrt(mp.pi) * 57 / 16
      >>> C = mp.quad(lambda x: mp.exp(- x * x) * f(x), [-mp.inf, +mp.inf])
      >>> mp.nprint((mp.chop(A-B, tol = 1e-10), mp.chop(A-C, tol = 1e-10)))
      (0.0, 0.0)

      >>> f = lambda x: x**5 - 2 * x**4 + 3 * x**3 - 5 * x**2 + 7 * x - 11
      >>> X, W = mp.gauss_quadrature(3, "laguerre")
      >>> A = mp.fdot([(f(x), w) for x, w in zip(X, W)])
      >>> B = 76
      >>> C = mp.quad(lambda x: mp.exp(-x) * f(x), [0, +mp.inf])
      >>> mp.nprint(mp.chop(A-B, tol = 1e-10), mp.chop(A-C, tol = 1e-10))
      .0

      # orthogonality of the chebyshev polynomials:
      >>> f = lambda x: mp.chebyt(3, x) * mp.chebyt(2, x)
      >>> X, W = mp.gauss_quadrature(3, "chebyshev1")
      >>> A = mp.fdot([(f(x), w) for x, w in zip(X, W)])
      >>> print(mp.chop(A, tol = 1e-10))
      0.0

    references:
      - golub and welsch, "calculations of gaussian quadrature rules", mathematics of
        computation 23, p. 221-230 (1969)
      - golub, "some modified matrix eigenvalue problems", siam review 15, p. 318-334 (1973)
      - stroud and secrest, "gaussian quadrature formulas", prentice-hall (1966)

    See also the routine gaussq.f in netlog.org or ACM Transactions on
    Mathematical Software algorithm 726.
    '''
def svd_r_raw(ctx, A, V: bool = False, calc_u: bool = False):
    """
    This routine computes the singular value decomposition of a matrix A.
    Given A, two orthogonal matrices U and V are calculated such that

                    A = U S V

    where S is a suitable shaped matrix whose off-diagonal elements are zero.
    The diagonal elements of S are the singular values of A, i.e. the
    squareroots of the eigenvalues of A' A or A A'. Here ' denotes the transpose.
    Householder bidiagonalization and a variant of the QR algorithm is used.

    overview of the matrices :

      A : m*n       A gets replaced by U
      U : m*n       U replaces A. If n>m then only the first m*m block of U is
                    non-zero. column-orthogonal: U' U = B
                    here B is a n*n matrix whose first min(m,n) diagonal
                    elements are 1 and all other elements are zero.
      S : n*n       diagonal matrix, only the diagonal elements are stored in
                    the array S. only the first min(m,n) diagonal elements are non-zero.
      V : n*n       orthogonal: V V' = V' V = 1

    parameters:
      A        (input/output) On input, A contains a real matrix of shape m*n.
               On output, if calc_u is true A contains the column-orthogonal
               matrix U; otherwise A is simply used as workspace and thus destroyed.

      V        (input/output) if false, the matrix V is not calculated. otherwise
               V must be a matrix of shape n*n.

      calc_u   (input) If true, the matrix U is calculated and replaces A.
               if false, U is not calculated and A is simply destroyed

    return value:
      S        an array of length n containing the singular values of A sorted by
               decreasing magnitude. only the first min(m,n) elements are non-zero.

    This routine is a python translation of the fortran routine svd.f in the
    software library EISPACK (see netlib.org) which itself is based on the
    algol procedure svd described in:
      - num. math. 14, 403-420(1970) by golub and reinsch.
      - wilkinson/reinsch: handbook for auto. comp., vol ii-linear algebra, 134-151(1971).

    """
def svd_c_raw(ctx, A, V: bool = False, calc_u: bool = False):
    """
    This routine computes the singular value decomposition of a matrix A.
    Given A, two unitary matrices U and V are calculated such that

                    A = U S V

    where S is a suitable shaped matrix whose off-diagonal elements are zero.
    The diagonal elements of S are the singular values of A, i.e. the
    squareroots of the eigenvalues of A' A or A A'. Here ' denotes the hermitian
    transpose (i.e. transposition and conjugation). Householder bidiagonalization
    and a variant of the QR algorithm is used.

    overview of the matrices :

      A : m*n       A gets replaced by U
      U : m*n       U replaces A. If n>m then only the first m*m block of U is
                    non-zero. column-unitary: U' U = B
                    here B is a n*n matrix whose first min(m,n) diagonal
                    elements are 1 and all other elements are zero.
      S : n*n       diagonal matrix, only the diagonal elements are stored in
                    the array S. only the first min(m,n) diagonal elements are non-zero.
      V : n*n       unitary: V V' = V' V = 1

    parameters:
      A        (input/output) On input, A contains a complex matrix of shape m*n.
               On output, if calc_u is true A contains the column-unitary
               matrix U; otherwise A is simply used as workspace and thus destroyed.

      V        (input/output) if false, the matrix V is not calculated. otherwise
               V must be a matrix of shape n*n.

      calc_u   (input) If true, the matrix U is calculated and replaces A.
               if false, U is not calculated and A is simply destroyed

    return value:
      S        an array of length n containing the singular values of A sorted by
               decreasing magnitude. only the first min(m,n) elements are non-zero.

    This routine is a python translation of the fortran routine svd.f in the
    software library EISPACK (see netlib.org) which itself is based on the
    algol procedure svd described in:
      - num. math. 14, 403-420(1970) by golub and reinsch.
      - wilkinson/reinsch: handbook for auto. comp., vol ii-linear algebra, 134-151(1971).

    """
def svd_r(ctx, A, full_matrices: bool = False, compute_uv: bool = True, overwrite_a: bool = False):
    """
    This routine computes the singular value decomposition of a matrix A.
    Given A, two orthogonal matrices U and V are calculated such that

           A = U S V        and        U' U = 1         and         V V' = 1

    where S is a suitable shaped matrix whose off-diagonal elements are zero.
    Here ' denotes the transpose. The diagonal elements of S are the singular
    values of A, i.e. the squareroots of the eigenvalues of A' A or A A'.

    input:
      A             : a real matrix of shape (m, n)
      full_matrices : if true, U and V are of shape (m, m) and (n, n).
                      if false, U and V are of shape (m, min(m, n)) and (min(m, n), n).
      compute_uv    : if true, U and V are calculated. if false, only S is calculated.
      overwrite_a   : if true, allows modification of A which may improve
                      performance. if false, A is not modified.

    output:
      U : an orthogonal matrix: U' U = 1. if full_matrices is true, U is of
          shape (m, m). ortherwise it is of shape (m, min(m, n)).

      S : an array of length min(m, n) containing the singular values of A sorted by
          decreasing magnitude.

      V : an orthogonal matrix: V V' = 1. if full_matrices is true, V is of
          shape (n, n). ortherwise it is of shape (min(m, n), n).

    return value:

           S          if compute_uv is false
       (U, S, V)      if compute_uv is true

    overview of the matrices:

      full_matrices true:
        A           : m*n
        U           : m*m     U' U  = 1
        S as matrix : m*n
        V           : n*n     V  V' = 1

     full_matrices false:
        A           : m*n
        U           : m*min(n,m)             U' U  = 1
        S as matrix : min(m,n)*min(m,n)
        V           : min(m,n)*n             V  V' = 1

    examples:

       >>> from mpmath import mp
       >>> A = mp.matrix([[2, -2, -1], [3, 4, -2], [-2, -2, 0]])
       >>> S = mp.svd_r(A, compute_uv = False)
       >>> print(S)
       [6.0]
       [3.0]
       [1.0]

       >>> U, S, V = mp.svd_r(A)
       >>> print(mp.chop(A - U * mp.diag(S) * V))
       [0.0  0.0  0.0]
       [0.0  0.0  0.0]
       [0.0  0.0  0.0]


    see also: svd, svd_c
    """
def svd_c(ctx, A, full_matrices: bool = False, compute_uv: bool = True, overwrite_a: bool = False):
    """
    This routine computes the singular value decomposition of a matrix A.
    Given A, two unitary matrices U and V are calculated such that

           A = U S V        and        U' U = 1         and         V V' = 1

    where S is a suitable shaped matrix whose off-diagonal elements are zero.
    Here ' denotes the hermitian transpose (i.e. transposition and complex
    conjugation). The diagonal elements of S are the singular values of A,
    i.e. the squareroots of the eigenvalues of A' A or A A'.

    input:
      A             : a complex matrix of shape (m, n)
      full_matrices : if true, U and V are of shape (m, m) and (n, n).
                      if false, U and V are of shape (m, min(m, n)) and (min(m, n), n).
      compute_uv    : if true, U and V are calculated. if false, only S is calculated.
      overwrite_a   : if true, allows modification of A which may improve
                      performance. if false, A is not modified.

    output:
      U : an unitary matrix: U' U = 1. if full_matrices is true, U is of
          shape (m, m). ortherwise it is of shape (m, min(m, n)).

      S : an array of length min(m, n) containing the singular values of A sorted by
          decreasing magnitude.

      V : an unitary matrix: V V' = 1. if full_matrices is true, V is of
          shape (n, n). ortherwise it is of shape (min(m, n), n).

    return value:

           S          if compute_uv is false
       (U, S, V)      if compute_uv is true

    overview of the matrices:

      full_matrices true:
        A           : m*n
        U           : m*m     U' U  = 1
        S as matrix : m*n
        V           : n*n     V  V' = 1

     full_matrices false:
        A           : m*n
        U           : m*min(n,m)             U' U  = 1
        S as matrix : min(m,n)*min(m,n)
        V           : min(m,n)*n             V  V' = 1

    example:
      >>> from mpmath import mp
      >>> A = mp.matrix([[-2j, -1-3j, -2+2j], [2-2j, -1-3j, 1], [-3+1j,-2j,0]])
      >>> S = mp.svd_c(A, compute_uv = False)
      >>> print(mp.chop(S - mp.matrix([mp.sqrt(34), mp.sqrt(15), mp.sqrt(6)])))
      [0.0]
      [0.0]
      [0.0]

      >>> U, S, V = mp.svd_c(A)
      >>> print(mp.chop(A - U * mp.diag(S) * V))
      [0.0  0.0  0.0]
      [0.0  0.0  0.0]
      [0.0  0.0  0.0]

    see also: svd, svd_r
    """
def svd(ctx, A, full_matrices: bool = False, compute_uv: bool = True, overwrite_a: bool = False):
    '''
    "svd" is a unified interface for "svd_r" and "svd_c". Depending on
    whether A is real or complex the appropriate function is called.

    This routine computes the singular value decomposition of a matrix A.
    Given A, two orthogonal (A real) or unitary (A complex) matrices U and V
    are calculated such that

           A = U S V        and        U\' U = 1         and         V V\' = 1

    where S is a suitable shaped matrix whose off-diagonal elements are zero.
    Here \' denotes the hermitian transpose (i.e. transposition and complex
    conjugation). The diagonal elements of S are the singular values of A,
    i.e. the squareroots of the eigenvalues of A\' A or A A\'.

    input:
      A             : a real or complex matrix of shape (m, n)
      full_matrices : if true, U and V are of shape (m, m) and (n, n).
                      if false, U and V are of shape (m, min(m, n)) and (min(m, n), n).
      compute_uv    : if true, U and V are calculated. if false, only S is calculated.
      overwrite_a   : if true, allows modification of A which may improve
                      performance. if false, A is not modified.

    output:
      U : an orthogonal or unitary matrix: U\' U = 1. if full_matrices is true, U is of
          shape (m, m). ortherwise it is of shape (m, min(m, n)).

      S : an array of length min(m, n) containing the singular values of A sorted by
          decreasing magnitude.

      V : an orthogonal or unitary matrix: V V\' = 1. if full_matrices is true, V is of
          shape (n, n). ortherwise it is of shape (min(m, n), n).

    return value:

           S          if compute_uv is false
       (U, S, V)      if compute_uv is true

    overview of the matrices:

      full_matrices true:
        A           : m*n
        U           : m*m     U\' U  = 1
        S as matrix : m*n
        V           : n*n     V  V\' = 1

     full_matrices false:
        A           : m*n
        U           : m*min(n,m)             U\' U  = 1
        S as matrix : min(m,n)*min(m,n)
        V           : min(m,n)*n             V  V\' = 1

    examples:

       >>> from mpmath import mp
       >>> A = mp.matrix([[2, -2, -1], [3, 4, -2], [-2, -2, 0]])
       >>> S = mp.svd(A, compute_uv = False)
       >>> print(S)
       [6.0]
       [3.0]
       [1.0]

       >>> U, S, V = mp.svd(A)
       >>> print(mp.chop(A - U * mp.diag(S) * V))
       [0.0  0.0  0.0]
       [0.0  0.0  0.0]
       [0.0  0.0  0.0]

    see also: svd_r, svd_c
    '''
