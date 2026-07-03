from ._base import spmatrix as spmatrix
from ._sputils import isscalarlike as isscalarlike, matrix as matrix, validateaxis as validateaxis
from _typeshed import Incomplete

class _data_matrix(spmatrix):
    def __init__(self) -> None: ...
    dtype: Incomplete
    def __abs__(self): ...
    def __round__(self, ndigits: int = 0): ...
    def __neg__(self): ...
    def __imul__(self, other): ...
    def __itruediv__(self, other): ...
    def astype(self, dtype, casting: str = 'unsafe', copy: bool = True): ...
    def conj(self, copy: bool = True): ...
    def copy(self): ...
    def count_nonzero(self): ...
    def power(self, n, dtype: Incomplete | None = None):
        """
        This function performs element-wise power.

        Parameters
        ----------
        n : n is a scalar

        dtype : If dtype is not specified, the current dtype will be preserved.
        """

name: Incomplete

class _minmax_mixin:
    """Mixin for min and max methods.

    These are not implemented for dia_matrix, hence the separate class.
    """
    def max(self, axis: Incomplete | None = None, out: Incomplete | None = None):
        """
        Return the maximum of the matrix or maximum along an axis.
        This takes all elements into account, not just the non-zero ones.

        Parameters
        ----------
        axis : {-2, -1, 0, 1, None} optional
            Axis along which the sum is computed. The default is to
            compute the maximum over all the matrix elements, returning
            a scalar (i.e., `axis` = `None`).

        out : None, optional
            This argument is in the signature *solely* for NumPy
            compatibility reasons. Do not pass in anything except
            for the default value, as this argument is not used.

        Returns
        -------
        amax : coo_matrix or scalar
            Maximum of `a`. If `axis` is None, the result is a scalar value.
            If `axis` is given, the result is a sparse.coo_matrix of dimension
            ``a.ndim - 1``.

        See Also
        --------
        min : The minimum value of a sparse matrix along a given axis.
        numpy.matrix.max : NumPy's implementation of 'max' for matrices

        """
    def min(self, axis: Incomplete | None = None, out: Incomplete | None = None):
        """
        Return the minimum of the matrix or maximum along an axis.
        This takes all elements into account, not just the non-zero ones.

        Parameters
        ----------
        axis : {-2, -1, 0, 1, None} optional
            Axis along which the sum is computed. The default is to
            compute the minimum over all the matrix elements, returning
            a scalar (i.e., `axis` = `None`).

        out : None, optional
            This argument is in the signature *solely* for NumPy
            compatibility reasons. Do not pass in anything except for
            the default value, as this argument is not used.

        Returns
        -------
        amin : coo_matrix or scalar
            Minimum of `a`. If `axis` is None, the result is a scalar value.
            If `axis` is given, the result is a sparse.coo_matrix of dimension
            ``a.ndim - 1``.

        See Also
        --------
        max : The maximum value of a sparse matrix along a given axis.
        numpy.matrix.min : NumPy's implementation of 'min' for matrices

        """
    def argmax(self, axis: Incomplete | None = None, out: Incomplete | None = None):
        """Return indices of maximum elements along an axis.

        Implicit zero elements are also taken into account. If there are
        several maximum values, the index of the first occurrence is returned.

        Parameters
        ----------
        axis : {-2, -1, 0, 1, None}, optional
            Axis along which the argmax is computed. If None (default), index
            of the maximum element in the flatten data is returned.
        out : None, optional
            This argument is in the signature *solely* for NumPy
            compatibility reasons. Do not pass in anything except for
            the default value, as this argument is not used.

        Returns
        -------
        ind : numpy.matrix or int
            Indices of maximum elements. If matrix, its size along `axis` is 1.
        """
    def argmin(self, axis: Incomplete | None = None, out: Incomplete | None = None):
        """Return indices of minimum elements along an axis.

        Implicit zero elements are also taken into account. If there are
        several minimum values, the index of the first occurrence is returned.

        Parameters
        ----------
        axis : {-2, -1, 0, 1, None}, optional
            Axis along which the argmin is computed. If None (default), index
            of the minimum element in the flatten data is returned.
        out : None, optional
            This argument is in the signature *solely* for NumPy
            compatibility reasons. Do not pass in anything except for
            the default value, as this argument is not used.

        Returns
        -------
         ind : numpy.matrix or int
            Indices of minimum elements. If matrix, its size along `axis` is 1.
        """
