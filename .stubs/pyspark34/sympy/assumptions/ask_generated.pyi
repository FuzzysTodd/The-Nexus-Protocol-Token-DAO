from sympy.assumptions.ask import Q as Q
from sympy.assumptions.cnf import Literal as Literal
from sympy.core.cache import cacheit as cacheit

def get_all_known_facts():
    """
    Known facts between unary predicates as CNF clauses.
    """
def get_known_facts_dict():
    """
    Logical relations between unary predicates as dictionary.

    Each key is a predicate, and item is two groups of predicates.
    First group contains the predicates which are implied by the key, and
    second group contains the predicates which are rejected by the key.

    """
