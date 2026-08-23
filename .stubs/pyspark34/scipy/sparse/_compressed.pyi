from ._base import SparseEfficiencyWarning as SparseEfficiencyWarning, isspmatrix as isspmatrix, spmatrix as spmatrix
from ._data import _data_matrix, _minmax_mixin
from ._index import IndexMixin as IndexMixin
from ._sparsetools import csr_column_index1 as csr_column_index1, csr_column_index2 as csr_column_index2, csr_row_index as csr_row_index, csr_row_slice as csr_row_slice, csr_sample_offsets as csr_sample_offsets, csr_sample_values as csr_sample_values, csr_todense as csr_todense, get_csr_submatrix as get_csr_submatrix
from ._sputils import check_shape as check_shape, downcast_intp_index as downcast_intp_index, get_index_dtype as get_index_dtype, get_sum_dtype as get_sum_dtype, getdtype as getdtype, is_pydata_spmatrix as is_pydata_spmatrix, isdense as isdense, isintlike as isintlike, isscalarlike as isscalarlike, isshape as isshape, to_native as to_native, upcast as upcast, upcast_char as upcast_char
from _typeshed import Incomplete

class _cs_matrix(_data_matrix, _minmax_mixin, IndexMixin):
    """base matrix class for compressed row- and column-oriented matrices"""
    data: Incomplete
    indices: Incomplete
    indptr: Incomplete
    def __init__(self, arg1, shape: Incomplete | None = None, dtype: Incomplete | None = None, copy: bool = False) -> None: ...
    def getnnz(self, axis: Incomplete | None = None): ...
    def check_format(self, full_check: bool = True) -> None:
        """check whether the matrix format is valid

        Parameters
        ----------
        full_check : bool, optional
            If `True`, rigorous check, O(N) operations. Otherwise
            basic check, O(1) operations (default True).
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __gt__(self, other): ...
    def __le__(self, other): ...
    def __ge__(self, other): ...
    def multiply(self, other):
        """Point-wise multiplication by another matrix, vector, or
        scalar.
        """
    def diagonal(self, k: int = 0): ...
    def maximum(self, other): ...
    def minimum(self, other): ...
    def sum(self, axis: Incomplete | None = None, dtype: Incomplete | None = None, out: Incomplete | None = None):
        """Sum the matrix over the given axis.  If the axis is None, sum
        over both rows and columns, returning a scalar.
        """
    def tocoo(self, copy: bool = True): ...
    def toarray(self, order: Incomplete | None = None, out: Incomplete | None = None): ...
    def eliminate_zeros(self) -> None:
        """Remove zero entries from the matrix

        This is an *in place* operation.
        """
    has_canonical_format: Incomplete
    def sum_duplicates(self) -> None:
        """Eliminate duplicate matrix entries by adding them together

        This is an *in place* operation.
        """
    has_sorted_indices: Incomplete
    def sorted_indices(self):
        """Return a copy of this matrix with sorted indices
        """
    def sort_indices(self) -> None:
        """Sort the indices of this matrix *in place*
        """
    def prune(self) -> None:
        """Remove empty space after all non-zero elements.
        """
    def resize(self, *shape) -> None: ...
