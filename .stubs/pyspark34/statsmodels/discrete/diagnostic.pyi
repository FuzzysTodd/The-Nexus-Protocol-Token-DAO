from _typeshed import Incomplete
from statsmodels.discrete._diagnostics_count import plot_probs as plot_probs, test_chisquare_prob as test_chisquare_prob, test_poisson_dispersion as test_poisson_dispersion, test_poisson_zeroinflation_broek as test_poisson_zeroinflation_broek, test_poisson_zeroinflation_jh as test_poisson_zeroinflation_jh, test_poisson_zeros as test_poisson_zeros
from statsmodels.stats.diagnostic_gen import test_chisquare_binning as test_chisquare_binning
from statsmodels.tools.decorators import cache_readonly as cache_readonly

class CountDiagnostic:
    """Diagnostic and specification tests and plots for Count model

    status: experimental

    Parameters
    ----------
    results : Results instance of a count model.
    y_max : int
        Largest count to include when computing predicted probabilities for
        counts. Default is the largest observed count.

    """
    results: Incomplete
    y_max: Incomplete
    def __init__(self, results, y_max: Incomplete | None = None) -> None: ...
    def probs_predicted(self): ...
    def test_chisquare_prob(self, bin_edges: Incomplete | None = None, method: Incomplete | None = None):
        '''Moment test for binned probabilites using OPG.

        Paramters
        ---------
        binedges : array_like or None
            This defines which counts are included in the test on frequencies
            and how counts are combined in bins.
            The default if bin_edges is None will change in future.
            See Notes and Example sections below.
        method : str
            Currently only `method = "opg"` is available.
            If method is None, the OPG will be used, but the default might
            change in future versions.
            See Notes section below.

        Returns
        -------
        test result

        Notes
        -----
        Warning: The current default can have many empty or nearly empty bins.
        The default number of bins is given by max(endog).
        Currently it is recommended to limit the number of bins explicitly,
        see Examples below.
        Binning will change in future and automatic binning will be added.

        Currently only the outer product of gradient, OPG, method is
        implemented. In many case, the OPG version of a specification test
        overrejects in small samples.
        Specialized tests that use observed or expected information matrix
        often have better small sample properties.
        The default method will change if better methods are added.

        Examples
        --------
        The following call is a test for the probability of zeros
        `test_chisquare_prob(bin_edges=np.arange(3))`

        `test_chisquare_prob(bin_edges=np.arange(10))` tests the hypothesis
        that the frequencies for counts up to 7 correspond to the estimated
        Poisson distributions.
        In this case, edges are 0, ..., 9 which defines 9 bins for
        counts 0 to 8. The last bin is dropped, so the joint test hypothesis is
        that the observed aggregated frequencies for counts 0 to 7 correspond
        to the model prediction for those frequencies. Predicted probabilites
        Prob(y_i = k | x) are aggregated over observations ``i``.

        '''
    def plot_probs(self, label: str = 'predicted', upp_xlim: Incomplete | None = None, fig: Incomplete | None = None):
        """Plot observed versus predicted frequencies for entire sample.
        """

class PoissonDiagnostic(CountDiagnostic):
    """Diagnostic and specification tests and plots for Poisson model

    status: experimental

    Parameters
    ----------
    results : PoissonResults instance

    """
    def test_dispersion(self):
        """Test for excess (over or under) dispersion in Poisson.

        Returns
        -------
        dispersion results
        """
    def test_poisson_zeroinflation(self, method: str = 'prob', exog_infl: Incomplete | None = None):
        '''Test for excess zeros, zero inflation or deflation.

        Parameters
        ----------
        method : str
            Three methods ara available for the test:

             - "prob" : moment test for the probability of zeros
             - "broek" : score test against zero inflation with or without
                explanatory variables for inflation

        exog_infl : array_like or None
            Optional explanatory variables under the alternative of zero
            inflation, or deflation. Only used if method is "broek".

        Returns
        -------
        results

        Notes
        -----
        If method = "prob", then the moment test of He et al 1_ is used based
        on the explicit formula in Tang and Tang 2_.

        If method = "broek" and exog_infl is None, then the test by Van den
        Broek 3_ is used. This is a score test against and alternative of
        constant zero inflation or deflation.

        If method = "broek" and exog_infl is provided, then the extension of
        the broek test to varying zero inflation or deflation by Jansakul and
        Hinde is used.

        Warning: The Broek and the Jansakul and Hinde tests are not numerically
        stable when the probability of zeros in Poisson is small, i.e. if the
        conditional means of the estimated Poisson distribution are large.
        In these cases, p-values will not be accurate.
        '''
