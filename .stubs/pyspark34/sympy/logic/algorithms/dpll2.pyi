from _typeshed import Incomplete
from sympy.assumptions.cnf import EncodedCNF as EncodedCNF
from sympy.core.sorting import ordered as ordered

def dpll_satisfiable(expr, all_models: bool = False):
    """
    Check satisfiability of a propositional sentence.
    It returns a model rather than True when it succeeds.
    Returns a generator of all models if all_models is True.

    Examples
    ========

    >>> from sympy.abc import A, B
    >>> from sympy.logic.algorithms.dpll2 import dpll_satisfiable
    >>> dpll_satisfiable(A & ~B)
    {A: True, B: False}
    >>> dpll_satisfiable(A & ~A)
    False

    """

class SATSolver:
    """
    Class for representing a SAT solver capable of
     finding a model to a boolean theory in conjunctive
     normal form.
    """
    var_settings: Incomplete
    heuristic: Incomplete
    is_unsatisfied: bool
    update_functions: Incomplete
    INTERVAL: Incomplete
    symbols: Incomplete
    heur_calculate: Incomplete
    heur_lit_assigned: Incomplete
    heur_lit_unset: Incomplete
    heur_clause_added: Incomplete
    add_learned_clause: Incomplete
    compute_conflict: Incomplete
    levels: Incomplete
    num_decisions: int
    num_learned_clauses: int
    original_num_clauses: Incomplete
    def __init__(self, clauses, variables, var_settings, symbols: Incomplete | None = None, heuristic: str = 'vsids', clause_learning: str = 'none', INTERVAL: int = 500) -> None: ...

class Level:
    """
    Represents a single level in the DPLL algorithm, and contains
    enough information for a sound backtracking procedure.
    """
    decision: Incomplete
    var_settings: Incomplete
    flipped: Incomplete
    def __init__(self, decision, flipped: bool = False) -> None: ...
