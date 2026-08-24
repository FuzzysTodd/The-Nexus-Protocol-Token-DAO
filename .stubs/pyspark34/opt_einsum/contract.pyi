from _typeshed import Incomplete
from typing import NamedTuple

__all__ = ['contract_path', 'contract', 'format_const_einsum_str', 'ContractExpression', 'shape_only']

class PathInfo:
    """A printable object to contain information about a contraction path.

    Attributes
    ----------
    naive_cost : int
        The estimate FLOP cost of a naive einsum contraction.
    opt_cost : int
        The estimate FLOP cost of this optimized contraction path.
    largest_intermediate : int
        The number of elements in the largest intermediate array that will be
        produced during the contraction.
    """
    contraction_list: Incomplete
    input_subscripts: Incomplete
    output_subscript: Incomplete
    path: Incomplete
    indices: Incomplete
    scale_list: Incomplete
    naive_cost: Incomplete
    opt_cost: Incomplete
    speedup: Incomplete
    size_list: Incomplete
    size_dict: Incomplete
    shapes: Incomplete
    eq: Incomplete
    largest_intermediate: Incomplete
    def __init__(self, contraction_list, input_subscripts, output_subscript, indices, path, scale_list, naive_cost, opt_cost, size_list, size_dict) -> None: ...

def contract_path(*operands, **kwargs):
    """
    Find a contraction order 'path', without performing the contraction.

    Parameters
    ----------
    subscripts : str
        Specifies the subscripts for summation.
    *operands : list of array_like
        These are the arrays for the operation.
    optimize : str, list or bool, optional (default: ``auto``)
        Choose the type of path.

        - if a list is given uses this as the path.
        - ``'optimal'`` An algorithm that explores all possible ways of
          contracting the listed tensors. Scales factorially with the number of
          terms in the contraction.
        - ``'branch-all'`` An algorithm like optimal but that restricts itself
          to searching 'likely' paths. Still scales factorially.
        - ``'branch-2'`` An even more restricted version of 'branch-all' that
          only searches the best two options at each step. Scales exponentially
          with the number of terms in the contraction.
        - ``'greedy'`` An algorithm that heuristically chooses the best pair
          contraction at each step.
        - ``'auto'`` Choose the best of the above algorithms whilst aiming to
          keep the path finding time below 1ms.

    use_blas : bool
        Use BLAS functions or not
    memory_limit : int, optional (default: None)
        Maximum number of elements allowed in intermediate arrays.
    shapes : bool, optional
        Whether ``contract_path`` should assume arrays (the default) or array
        shapes have been supplied.

    Returns
    -------
    path : list of tuples
        The einsum path
    PathInfo : str
        A printable object containing various information about the path found.

    Notes
    -----
    The resulting path indicates which terms of the input contraction should be
    contracted first, the result of this contraction is then appended to the end of
    the contraction list.

    Examples
    --------

    We can begin with a chain dot example. In this case, it is optimal to
    contract the b and c tensors represented by the first element of the path (1,
    2). The resulting tensor is added to the end of the contraction and the
    remaining contraction, ``(0, 1)``, is then executed.

    >>> a = np.random.rand(2, 2)
    >>> b = np.random.rand(2, 5)
    >>> c = np.random.rand(5, 2)
    >>> path_info = opt_einsum.contract_path('ij,jk,kl->il', a, b, c)
    >>> print(path_info[0])
    [(1, 2), (0, 1)]
    >>> print(path_info[1])
      Complete contraction:  ij,jk,kl->il
             Naive scaling:  4
         Optimized scaling:  3
          Naive FLOP count:  1.600e+02
      Optimized FLOP count:  5.600e+01
       Theoretical speedup:  2.857
      Largest intermediate:  4.000e+00 elements
    -------------------------------------------------------------------------
    scaling                  current                                remaining
    -------------------------------------------------------------------------
       3                   kl,jk->jl                                ij,jl->il
       3                   jl,ij->il                                   il->il


    A more complex index transformation example.

    >>> I = np.random.rand(10, 10, 10, 10)
    >>> C = np.random.rand(10, 10)
    >>> path_info = oe.contract_path('ea,fb,abcd,gc,hd->efgh', C, C, I, C, C)

    >>> print(path_info[0])
    [(0, 2), (0, 3), (0, 2), (0, 1)]
    >>> print(path_info[1])
      Complete contraction:  ea,fb,abcd,gc,hd->efgh
             Naive scaling:  8
         Optimized scaling:  5
          Naive FLOP count:  8.000e+08
      Optimized FLOP count:  8.000e+05
       Theoretical speedup:  1000.000
      Largest intermediate:  1.000e+04 elements
    --------------------------------------------------------------------------
    scaling                  current                                remaining
    --------------------------------------------------------------------------
       5               abcd,ea->bcde                      fb,gc,hd,bcde->efgh
       5               bcde,fb->cdef                         gc,hd,cdef->efgh
       5               cdef,gc->defg                            hd,defg->efgh
       5               defg,hd->efgh                               efgh->efgh
    """
def contract(*operands, **kwargs):
    """
    contract(subscripts, *operands, out=None, dtype=None, order='K', casting='safe', use_blas=True, optimize=True, memory_limit=None, backend='numpy')

    Evaluates the Einstein summation convention on the operands. A drop in
    replacement for NumPy's einsum function that optimizes the order of contraction
    to reduce overall scaling at the cost of several intermediate arrays.

    Parameters
    ----------
    subscripts : str
        Specifies the subscripts for summation.
    *operands : list of array_like
        These are the arrays for the operation.
    out : array_like
        A output array in which set the resulting output.
    dtype : str
        The dtype of the given contraction, see np.einsum.
    order : str
        The order of the resulting contraction, see np.einsum.
    casting : str
        The casting procedure for operations of different dtype, see np.einsum.
    use_blas : bool
        Do you use BLAS for valid operations, may use extra memory for more intermediates.
    optimize : str, list or bool, optional (default: ``auto``)
        Choose the type of path.

        - if a list is given uses this as the path.
        - ``'optimal'`` An algorithm that explores all possible ways of
          contracting the listed tensors. Scales factorially with the number of
          terms in the contraction.
        - ``'dp'`` A faster (but essentially optimal) algorithm that uses
          dynamic programming to exhaustively search all contraction paths
          without outer-products.
        - ``'greedy'`` An cheap algorithm that heuristically chooses the best
          pairwise contraction at each step. Scales linearly in the number of
          terms in the contraction.
        - ``'random-greedy'`` Run a randomized version of the greedy algorithm
          32 times and pick the best path.
        - ``'random-greedy-128'`` Run a randomized version of the greedy
          algorithm 128 times and pick the best path.
        - ``'branch-all'`` An algorithm like optimal but that restricts itself
          to searching 'likely' paths. Still scales factorially.
        - ``'branch-2'`` An even more restricted version of 'branch-all' that
          only searches the best two options at each step. Scales exponentially
          with the number of terms in the contraction.
        - ``'auto'`` Choose the best of the above algorithms whilst aiming to
          keep the path finding time below 1ms.
        - ``'auto-hq'`` Aim for a high quality contraction, choosing the best
          of the above algorithms whilst aiming to keep the path finding time
          below 1sec.

    memory_limit : {None, int, 'max_input'} (default: None)
        Give the upper bound of the largest intermediate tensor contract will build.

        - None or -1 means there is no limit
        - 'max_input' means the limit is set as largest input tensor
        - a positive integer is taken as an explicit limit on the number of elements

        The default is None. Note that imposing a limit can make contractions
        exponentially slower to perform.
    backend : str, optional (default: ``auto``)
        Which library to use to perform the required ``tensordot``, ``transpose``
        and ``einsum`` calls. Should match the types of arrays supplied, See
        :func:`contract_expression` for generating expressions which convert
        numpy arrays to and from the backend library automatically.

    Returns
    -------
    out : array_like
        The result of the einsum expression.

    Notes
    -----
    This function should produce a result identical to that of NumPy's einsum
    function. The primary difference is ``contract`` will attempt to form
    intermediates which reduce the overall scaling of the given einsum contraction.
    By default the worst intermediate formed will be equal to that of the largest
    input array. For large einsum expressions with many input arrays this can
    provide arbitrarily large (1000 fold+) speed improvements.

    For contractions with just two tensors this function will attempt to use
    NumPy's built-in BLAS functionality to ensure that the given operation is
    preformed optimally. When NumPy is linked to a threaded BLAS, potential
    speedups are on the order of 20-100 for a six core machine.

    Examples
    --------

    See :func:`opt_einsum.contract_path` or :func:`numpy.einsum`

    """
def format_const_einsum_str(einsum_str, constants):
    """Add brackets to the constant terms in ``einsum_str``. For example:

        >>> format_const_einsum_str('ab,bc,cd->ad', [0, 2])
        'bc,[ab,cd]->ad'

    No-op if there are no constants.
    """

class ContractExpression:
    """Helper class for storing an explicit ``contraction_list`` which can
    then be repeatedly called solely with the array arguments.
    """
    contraction_list: Incomplete
    einsum_kwargs: Incomplete
    contraction: Incomplete
    num_args: Incomplete
    def __init__(self, contraction, contraction_list, constants_dict, **einsum_kwargs) -> None: ...
    def evaluate_constants(self, backend: str = 'auto') -> None:
        """Convert any constant operands to the correct backend form, and
        perform as many contractions as possible to create a new list of
        operands, stored in ``self._evaluated_constants[backend]``. This also
        makes sure ``self.contraction_list`` only contains the remaining,
        non-const operations.
        """
    def __call__(self, *arrays, **kwargs):
        """Evaluate this expression with a set of arrays.

        Parameters
        ----------
        arrays : seq of array
            The arrays to supply as input to the expression.
        out : array, optional (default: ``None``)
            If specified, output the result into this array.
        backend : str, optional  (default: ``numpy``)
            Perform the contraction with this backend library. If numpy arrays
            are supplied then try to convert them to and from the correct
            backend array type.
        """

class Shaped(NamedTuple):
    shape: Incomplete

def shape_only(shape):
    """Dummy ``numpy.ndarray`` which has a shape only - for generating
    contract expressions.
    """
