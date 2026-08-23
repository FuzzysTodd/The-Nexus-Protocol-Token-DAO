from sympy.strategies.core import chain as chain, do_one as do_one
from sympy.strategies.util import basic_fns as basic_fns

def top_down(rule, fns=...):
    """Apply a rule down a tree running it on the top nodes first."""
def bottom_up(rule, fns=...):
    """Apply a rule down a tree running it on the bottom nodes first."""
def top_down_once(rule, fns=...):
    """Apply a rule down a tree - stop on success."""
def bottom_up_once(rule, fns=...):
    """Apply a rule up a tree - stop on success."""
def sall(rule, fns=...):
    """Strategic all - apply rule to args."""
