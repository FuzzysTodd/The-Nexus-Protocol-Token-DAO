from . import config as config
from .external_utils import is_compiling as is_compiling
from .utils import HAS_NUMPY as HAS_NUMPY, is_safe_constant as is_safe_constant, np as np
from torch.fx._symbolic_trace import is_fx_tracing as is_fx_tracing

def make_function_id_set(lazy_initializer):
    """
    Track a set of `id()`s of objects which are either allowed or not
    allowed to go into the generated FX graph.  Use to test for torch.*,
    numpy.*, builtins.*, etc.

    Support user modification to permit customization of what can be
    added to the graph and what will cause a graph break.
    """
def is_allowed(obj):
    """Is this safe to trace like torch.add ?"""
def torch_get_name(obj, default):
    """Convert a torch.* funcion to a string"""
def is_builtin_callable(obj): ...
def is_builtin_constant(obj): ...
def is_numpy(obj): ...
