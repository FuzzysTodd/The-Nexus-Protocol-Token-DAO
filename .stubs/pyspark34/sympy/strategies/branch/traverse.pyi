from .core import chain as chain, do_one as do_one, identity as identity
from sympy.strategies.util import basic_fns as basic_fns

def top_down(brule, fns=...):
    """ Apply a rule down a tree running it on the top nodes first """
def sall(brule, fns=...):
    """ Strategic all - apply rule to args """
