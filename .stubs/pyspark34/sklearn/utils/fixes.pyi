from .deprecation import deprecated as deprecated
from _typeshed import Incomplete
from scipy.optimize.linesearch import line_search_wolfe1 as line_search_wolfe1, line_search_wolfe2 as line_search_wolfe2

np_version: Incomplete
sp_version: Incomplete
sp_base_version: Incomplete
percentile: Incomplete

def threadpool_limits(limits: Incomplete | None = None, user_api: Incomplete | None = None): ...
def threadpool_info(): ...
def delayed(function): ...
