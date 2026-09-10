from _typeshed import Incomplete
from statsmodels.compat.python import lrange as lrange
from statsmodels.sandbox.tools.mctools import StatTestMC as StatTestMC
from statsmodels.stats.diagnostic import acorr_ljungbox as acorr_ljungbox
from statsmodels.tsa.stattools import adfuller as adfuller

def normalnoisesim(nobs: int = 500, loc: float = 0.0): ...
def lb(x): ...

mc1: Incomplete
frac: Incomplete
crit: Incomplete

def randwalksim(nobs: int = 500, drift: float = 0.0): ...
def adf20(x): ...

mc2: Incomplete
doplot: int
