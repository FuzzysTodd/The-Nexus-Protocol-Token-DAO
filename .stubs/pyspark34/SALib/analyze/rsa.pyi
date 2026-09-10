import numpy as np
from . import common_args as common_args
from ..util import ResultDict as ResultDict, extract_group_names as extract_group_names, read_param_file as read_param_file
from _typeshed import Incomplete
from typing import Dict

def analyze(problem: Dict, X: np.ndarray, Y: np.ndarray, bins: int = 20, target: str = 'Y', print_to_console: bool = False, seed: int = None):
    '''
    Perform Regional Sensitivity Analysis (RSA), also known as Monte Carlo Filtering.

    In a usual RSA, a desirable region of output space is defined. Outputs which fall
    within this region is categorized as being "behavioral" (:math:`B`), and those
    outside are described as being "non-behavioral" (:math:`\\bar{B}`). The input
    factors are also partitioned into behavioral and non-behavioral subsets, such that
    :math:`f(X_{i}|B) \\rightarrow (Y|B)` and :math:`f(X_{i}|\\bar{B}) \\rightarrow
    (Y|\\bar{B})`. The distribution between the two sub-samples are compared for each
    factor. The greater the difference between the two distributions, the more
    important the given factor is in driving model outputs.

    The approach implemented in SALib partitions factor or output space into :math:`b`
    bins (default: 20) according to their percentile values. Output space is targeted
    for analysis by default (:code:`target="Y"`), such that :math:`(Y|b_{i})` is
    mapped back to :math:`(X_{i}|b_{i})`. In other words, we treat outputs falling
    within a given bin (:math:`b_{i}`) corresponding to their inputs as behavioral, and
    those outside the bin as non-behavioral. This aids in answering the question
    "Which :math:`X_{i}` contributes most toward a given range of outputs?". Factor
    space can also be assessed (:code:`target="X"`), such that :math:`f(X_{i}|b_{i})
    \\rightarrow (Y|b_{i})` and :math:`f(X_{i}|b_{\\sim i}) \\rightarrow
    (Y|b_{\\sim i})`. This aids in answering the question "where in factor space are
    outputs most sensitive to?"

    The two-sample Cramér-von Mises (CvM) test is used to compare distributions.
    Results of the analysis indicate sensitivity across factor/output space. As the
    Cramér-von Mises criterion ranges from 0 to :math:`\\infty`, a value of zero will
    indicates the two distributions being compared are identical, with larger values
    indicating greater differences.

    Notes
    -----
    Compatible with:
        all samplers

    When applied to grouped factors, the analysis is conducted on each factor
    individually, and the mean of the results for a group are reported.

    Increasing the value of :code:`bins` increases the granularity of the analysis
    (across factor space), but necessitates larger sample sizes.

    This analysis will produce NaNs, indicating areas of factor space that did not have
    any samples, or for which the outputs were constant.

    Analysis results are normalized against the maximum value such that 1.0 indicates
    the greatest sensitivity.

    Parameters
    ----------
    problem : dict
        The problem definition
    X : numpy.array
        A NumPy array containing the model inputs
    Y : numpy.array
        A NumPy array containing the model outputs
    bins : int
        The number of bins to use (default: 20)
    target : str
        Assess factor space ("X") or output space ("Y")
        (default: "Y")
    print_to_console : bool
        Print results directly to console (default False)
    seed : int
        Seed value to ensure deterministic results
        Unused, but defined to maintain compatibility.

    References
    ----------
    1. Hornberger, G. M., and R. C. Spear. 1981.
        Approach to the preliminary analysis of environmental systems.
        Journal of Environmental Management 12:1.
        https://www.osti.gov/biblio/6396608-approach-preliminary-analysis-environmental-systems

    2. Pianosi, F., K. Beven, J. Freer, J. W. Hall, J. Rougier, D. B. Stephenson, and
        T. Wagener. 2016.
        Sensitivity analysis of environmental models:
        A systematic review with practical workflow.
        Environmental Modelling & Software 79:214-232.
        https://dx.doi.org/10.1016/j.envsoft.2016.02.008

    3. Saltelli, A., M. Ratto, T. Andres, F. Campolongo, J. Cariboni, D. Gatelli,
        M. Saisana, and S. Tarantola. 2008.
        Global Sensitivity Analysis: The Primer.
        Wiley, West Sussex, U.K.
        https://dx.doi.org/10.1002/9780470725184
        Accessible at:
        http://www.andreasaltelli.eu/file/repository/Primer_Corrected_2022.pdf
    '''
def rsa(X: np.ndarray, y: np.ndarray, bins: int = 10, target: str = 'X') -> np.ndarray: ...
def to_df(self):
    """Conversion to Pandas DataFrame specific to Regional Sensitivity Analysis results.

    Overrides the conversion method attached to the SALib problem spec.

    Returns
    -------
    Pandas DataFrame
    """
def plot(self, factors: Incomplete | None = None):
    """Plotting for Regional Sensitivity Analysis.

    Overrides the plot method attached to the SALib problem spec.
    """
def cli_parse(parser): ...
def cli_action(args) -> None: ...
