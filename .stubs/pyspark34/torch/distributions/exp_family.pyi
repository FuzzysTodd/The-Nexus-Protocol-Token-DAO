from torch.distributions.distribution import Distribution

__all__ = ['ExponentialFamily']

class ExponentialFamily(Distribution):
    """
    ExponentialFamily is the abstract base class for probability distributions belonging to an
    exponential family, whose probability mass/density function has the form is defined below

    .. math::

        p_{F}(x; \\theta) = \\exp(\\langle t(x), \\theta\\rangle - F(\\theta) + k(x))

    where :math:`\\theta` denotes the natural parameters, :math:`t(x)` denotes the sufficient statistic,
    :math:`F(\\theta)` is the log normalizer function for a given family and :math:`k(x)` is the carrier
    measure.

    Note:
        This class is an intermediary between the `Distribution` class and distributions which belong
        to an exponential family mainly to check the correctness of the `.entropy()` and analytic KL
        divergence methods. We use this class to compute the entropy and KL divergence using the AD
        framework and Bregman divergences (courtesy of: Frank Nielsen and Richard Nock, Entropies and
        Cross-entropies of Exponential Families).
    """
    def entropy(self):
        """
        Method to compute the entropy using Bregman divergence of the log normalizer.
        """
