from scipy.special._mptestutils import mpf2float as mpf2float

def gammainc(a, x, dps: int = 50, maxterms=...):
    """Compute gammainc exactly like mpmath does but allow for more
    summands in hypercomb. See

    mpmath/functions/expintegrals.py#L134

    in the mpmath github repository.

    """
def gammaincc(a, x, dps: int = 50, maxterms=...):
    """Compute gammaincc exactly like mpmath does but allow for more
    terms in hypercomb. See

    mpmath/functions/expintegrals.py#L187

    in the mpmath github repository.

    """
def main() -> None: ...
