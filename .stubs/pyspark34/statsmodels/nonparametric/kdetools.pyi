from _typeshed import Incomplete

def forrt(X, m: Incomplete | None = None):
    """
    RFFT with order like Munro (1976) FORTT routine.
    """
def revrt(X, m: Incomplete | None = None):
    """
    Inverse of forrt. Equivalent to Munro (1976) REVRT routine.
    """
def silverman_transform(bw, M, RANGE):
    """
    FFT of Gaussian kernel following to Silverman AS 176.

    Notes
    -----
    Underflow is intentional as a dampener.
    """
def counts(x, v):
    """
    Counts the number of elements of x that fall within the grid points v

    Notes
    -----
    Using np.digitize and np.bincount
    """
def kdesum(x, axis: int = 0): ...
