from _typeshed import Incomplete

inf: Incomplete
C_skip: int
C_sub: int
C_exp: int
C_vwl: int
consonants: Incomplete
R_c: Incomplete
R_v: Incomplete
similarity_matrix: Incomplete
salience: Incomplete
feature_matrix: Incomplete

def align(str1, str2, epsilon: int = 0):
    """
    Compute the alignment of two phonetic strings.

    :param str str1: First string to be aligned
    :param str str2: Second string to be aligned

    :type epsilon: float (0.0 to 1.0)
    :param epsilon: Adjusts threshold similarity score for near-optimal alignments

    :rtype: list(list(tuple(str, str)))
    :return: Alignment(s) of str1 and str2

    (Kondrak 2002: 51)
    """
def sigma_skip(p):
    """
    Returns score of an indel of P.

    (Kondrak 2002: 54)
    """
def sigma_sub(p, q):
    """
    Returns score of a substitution of P with Q.

    (Kondrak 2002: 54)
    """
def sigma_exp(p, q):
    """
    Returns score of an expansion/compression.

    (Kondrak 2002: 54)
    """
def delta(p, q):
    """
    Return weighted sum of difference between P and Q.

    (Kondrak 2002: 54)
    """
def diff(p, q, f):
    """
    Returns difference between phonetic segments P and Q for feature F.

    (Kondrak 2002: 52, 54)
    """
def R(p, q):
    """
    Return relevant features for segment comparison.

    (Kondrak 2002: 54)
    """
def V(p):
    """
    Return vowel weight if P is vowel.

    (Kondrak 2002: 54)
    """
def demo() -> None:
    """
    A demonstration of the result of aligning phonetic sequences
    used in Kondrak's (2002) dissertation.
    """

cognate_data: str
