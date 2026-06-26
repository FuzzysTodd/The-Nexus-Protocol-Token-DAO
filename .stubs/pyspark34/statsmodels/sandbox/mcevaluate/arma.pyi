from _typeshed import Incomplete
from statsmodels.tsa.arima_process import arma_generate_sample as arma_generate_sample
from statsmodels.tsa.arma_mle import Arma as Arma

def mcarma22(niter: int = 10, nsample: int = 1000, ar: Incomplete | None = None, ma: Incomplete | None = None, sig: float = 0.5):
    """run Monte Carlo for ARMA(2,2)

    DGP parameters currently hard coded
    also sample size `nsample`

    was not a self contained function, used instances from outer scope
      now corrected

    """
def mc_summary(res, rt: Incomplete | None = None) -> None: ...
