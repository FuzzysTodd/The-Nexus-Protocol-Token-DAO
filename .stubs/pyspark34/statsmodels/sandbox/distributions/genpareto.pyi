from _typeshed import Incomplete
from scipy.stats.distributions import rv_continuous

class genpareto2_gen(rv_continuous): ...

genpareto2: Incomplete
shape: Incomplete
loc: Incomplete
scale: Incomplete
rv: Incomplete
quant: Incomplete

def paramstopot(thresh, shape, scale):
    """transform shape scale for peak over threshold

    y = x-u|x>u ~ GPD(k, sigma-k*u) if x ~ GPD(k, sigma)
    notation of de Zea Bermudez, Kotz
    k, sigma is shape, scale
    """
def paramsfrompot(thresh, shape, scalepot): ...
def warnif(cond, msg) -> None: ...
def meanexcess(thresh, shape, scale):
    """mean excess function of genpareto

    assert are inequality conditions in de Zea Bermudez, Kotz
    """
def meanexcess_plot(data, params: Incomplete | None = None, lidx: int = 100, uidx: int = 10, method: str = 'emp', plot: int = 0): ...

data: Incomplete
tmp: Incomplete

def meanexcess_emp(data): ...
def meanexcess_dist(self, lb, *args, **kwds): ...

ds: Incomplete
me: Incomplete
mc: Incomplete
rvs: Incomplete
