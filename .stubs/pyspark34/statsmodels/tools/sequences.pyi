from _typeshed import Incomplete

def discrepancy(sample, bounds: Incomplete | None = None):
    '''Discrepancy.

    Compute the centered discrepancy on a given sample.
    It is a measure of the uniformity of the points in the parameter space.
    The lower the value is, the better the coverage of the parameter space is.

    Parameters
    ----------
    sample : array_like (n_samples, k_vars)
        The sample to compute the discrepancy from.
    bounds : tuple or array_like ([min, k_vars], [max, k_vars])
        Desired range of transformed data. The transformation apply the bounds
        on the sample and not the theoretical space, unit cube. Thus min and
        max values of the sample will coincide with the bounds.

    Returns
    -------
    discrepancy : float
        Centered discrepancy.

    References
    ----------
    [1] Fang et al. "Design and modeling for computer experiments",
      Computer Science and Data Analysis Series Science and Data Analysis
      Series, 2006.
    '''
def primes_from_2_to(n):
    """Prime numbers from 2 to *n*.

    Parameters
    ----------
    n : int
        Sup bound with ``n >= 6``.

    Returns
    -------
    primes : list(int)
        Primes in ``2 <= p < n``.

    References
    ----------
    [1] `StackOverflow <https://stackoverflow.com/questions/2068372>`_.
    """
def n_primes(n):
    """List of the n-first prime numbers.

    Parameters
    ----------
    n : int
        Number of prime numbers wanted.

    Returns
    -------
    primes : list(int)
        List of primes.
    """
def van_der_corput(n_sample, base: int = 2, start_index: int = 0):
    """Van der Corput sequence.

    Pseudo-random number generator based on a b-adic expansion.

    Parameters
    ----------
    n_sample : int
        Number of element of the sequence.
    base : int
        Base of the sequence.
    start_index : int
        Index to start the sequence from.

    Returns
    -------
    sequence : list (n_samples,)
        Sequence of Van der Corput.
    """
def halton(dim, n_sample, bounds: Incomplete | None = None, start_index: int = 0):
    '''Halton sequence.

    Pseudo-random number generator that generalize the Van der Corput sequence
    for multiple dimensions. Halton sequence use base-two Van der Corput
    sequence for the first dimension, base-three for its second and base-n for
    its n-dimension.

    Parameters
    ----------
    dim : int
        Dimension of the parameter space.
    n_sample : int
        Number of samples to generate in the parametr space.
    bounds : tuple or array_like ([min, k_vars], [max, k_vars])
        Desired range of transformed data. The transformation apply the bounds
        on the sample and not the theoretical space, unit cube. Thus min and
        max values of the sample will coincide with the bounds.
    start_index : int
        Index to start the sequence from.

    Returns
    -------
    sequence : array_like (n_samples, k_vars)
        Sequence of Halton.

    References
    ----------
    [1] Halton, "On the efficiency of certain quasi-random sequences of points
      in evaluating multi-dimensional integrals", Numerische Mathematik, 1960.

    Examples
    --------
    Generate samples from a low discrepancy sequence of Halton.

    >>> from statsmodels.tools import sequences
    >>> sample = sequences.halton(dim=2, n_sample=5)

    Compute the quality of the sample using the discrepancy criterion.

    >>> uniformity = sequences.discrepancy(sample)

    If some wants to continue an existing design, extra points can be obtained.

    >>> sample_continued = sequences.halton(dim=2, n_sample=5, start_index=5)
    '''
