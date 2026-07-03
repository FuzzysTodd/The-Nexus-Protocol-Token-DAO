from .try_ols_anova import data2dummy as data2dummy
from _typeshed import Incomplete
from statsmodels.compat.python import lmap as lmap
from statsmodels.regression.linear_model import OLS as OLS
from statsmodels.tools.tools import add_constant as add_constant

filenameli: Incomplete

def getnist(filename): ...
def anova_oneway(y, x, seq: int = 0): ...
def anova_ols(y, x): ...
