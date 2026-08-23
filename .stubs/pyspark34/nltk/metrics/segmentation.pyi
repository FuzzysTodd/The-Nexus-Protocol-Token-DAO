from _typeshed import Incomplete

def windowdiff(seg1, seg2, k, boundary: str = '1', weighted: bool = False):
    '''
    Compute the windowdiff score for a pair of segmentations.  A
    segmentation is any sequence over a vocabulary of two items
    (e.g. "0", "1"), where the specified boundary value is used to
    mark the edge of a segmentation.

        >>> s1 = "000100000010"
        >>> s2 = "000010000100"
        >>> s3 = "100000010000"
        >>> \'%.2f\' % windowdiff(s1, s1, 3)
        \'0.00\'
        >>> \'%.2f\' % windowdiff(s1, s2, 3)
        \'0.30\'
        >>> \'%.2f\' % windowdiff(s2, s3, 3)
        \'0.80\'

    :param seg1: a segmentation
    :type seg1: str or list
    :param seg2: a segmentation
    :type seg2: str or list
    :param k: window width
    :type k: int
    :param boundary: boundary value
    :type boundary: str or int or bool
    :param weighted: use the weighted variant of windowdiff
    :type weighted: boolean
    :rtype: float
    '''
def ghd(ref, hyp, ins_cost: float = 2.0, del_cost: float = 2.0, shift_cost_coeff: float = 1.0, boundary: str = '1'):
    '''
    Compute the Generalized Hamming Distance for a reference and a hypothetical
    segmentation, corresponding to the cost related to the transformation
    of the hypothetical segmentation into the reference segmentation
    through boundary insertion, deletion and shift operations.

    A segmentation is any sequence over a vocabulary of two items
    (e.g. "0", "1"), where the specified boundary value is used to
    mark the edge of a segmentation.

    Recommended parameter values are a shift_cost_coeff of 2.
    Associated with a ins_cost, and del_cost equal to the mean segment
    length in the reference segmentation.

        >>> # Same examples as Kulyukin C++ implementation
        >>> ghd(\'1100100000\', \'1100010000\', 1.0, 1.0, 0.5)
        0.5
        >>> ghd(\'1100100000\', \'1100000001\', 1.0, 1.0, 0.5)
        2.0
        >>> ghd(\'011\', \'110\', 1.0, 1.0, 0.5)
        1.0
        >>> ghd(\'1\', \'0\', 1.0, 1.0, 0.5)
        1.0
        >>> ghd(\'111\', \'000\', 1.0, 1.0, 0.5)
        3.0
        >>> ghd(\'000\', \'111\', 1.0, 2.0, 0.5)
        6.0

    :param ref: the reference segmentation
    :type ref: str or list
    :param hyp: the hypothetical segmentation
    :type hyp: str or list
    :param ins_cost: insertion cost
    :type ins_cost: float
    :param del_cost: deletion cost
    :type del_cost: float
    :param shift_cost_coeff: constant used to compute the cost of a shift.
        ``shift cost = shift_cost_coeff * |i - j|`` where ``i`` and ``j``
        are the positions indicating the shift
    :type shift_cost_coeff: float
    :param boundary: boundary value
    :type boundary: str or int or bool
    :rtype: float
    '''
def pk(ref, hyp, k: Incomplete | None = None, boundary: str = '1'):
    '''
    Compute the Pk metric for a pair of segmentations A segmentation
    is any sequence over a vocabulary of two items (e.g. "0", "1"),
    where the specified boundary value is used to mark the edge of a
    segmentation.

    >>> \'%.2f\' % pk(\'0100\'*100, \'1\'*400, 2)
    \'0.50\'
    >>> \'%.2f\' % pk(\'0100\'*100, \'0\'*400, 2)
    \'0.50\'
    >>> \'%.2f\' % pk(\'0100\'*100, \'0100\'*100, 2)
    \'0.00\'

    :param ref: the reference segmentation
    :type ref: str or list
    :param hyp: the segmentation to evaluate
    :type hyp: str or list
    :param k: window size, if None, set to half of the average reference segment length
    :type boundary: str or int or bool
    :param boundary: boundary value
    :type boundary: str or int or bool
    :rtype: float
    '''
