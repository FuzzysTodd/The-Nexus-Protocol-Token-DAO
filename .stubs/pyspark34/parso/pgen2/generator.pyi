from _typeshed import Incomplete
from parso.pgen2.grammar_parser import GrammarParser as GrammarParser, NFAState as NFAState
from typing import Generic, Mapping, Sequence, Set

class Grammar(Generic[_TokenTypeT]):
    """
    Once initialized, this class supplies the grammar tables for the
    parsing engine implemented by parse.py.  The parsing engine
    accesses the instance variables directly.

    The only important part in this parsers are dfas and transitions between
    dfas.
    """
    nonterminal_to_dfas: Incomplete
    reserved_syntax_strings: Incomplete
    start_nonterminal: Incomplete
    def __init__(self, start_nonterminal: str, rule_to_dfas: Mapping[str, Sequence['DFAState[_TokenTypeT]']], reserved_syntax_strings: Mapping[str, 'ReservedString']) -> None: ...

class DFAPlan:
    """
    Plans are used for the parser to create stack nodes and do the proper
    DFA state transitions.
    """
    next_dfa: Incomplete
    dfa_pushes: Incomplete
    def __init__(self, next_dfa: DFAState, dfa_pushes: Sequence['DFAState'] = []) -> None: ...

class DFAState(Generic[_TokenTypeT]):
    """
    The DFAState object is the core class for pretty much anything. DFAState
    are the vertices of an ordered graph while arcs and transitions are the
    edges.

    Arcs are the initial edges, where most DFAStates are not connected and
    transitions are then calculated to connect the DFA state machines that have
    different nonterminals.
    """
    from_rule: Incomplete
    nfa_set: Incomplete
    arcs: Incomplete
    nonterminal_arcs: Incomplete
    transitions: Incomplete
    is_final: Incomplete
    def __init__(self, from_rule: str, nfa_set: Set[NFAState], final: NFAState) -> None: ...
    def add_arc(self, next_, label) -> None: ...
    def unifystate(self, old, new) -> None: ...
    def __eq__(self, other): ...

class ReservedString:
    '''
    Most grammars will have certain keywords and operators that are mentioned
    in the grammar as strings (e.g. "if") and not token types (e.g. NUMBER).
    This class basically is the former.
    '''
    value: Incomplete
    def __init__(self, value: str) -> None: ...

def generate_grammar(bnf_grammar: str, token_namespace) -> Grammar:
    """
    ``bnf_text`` is a grammar in extended BNF (using * for repetition, + for
    at-least-once repetition, [] for optional parts, | for alternatives and ()
    for grouping).

    It's not EBNF according to ISO/IEC 14977. It's a dialect Python uses in its
    own parser.
    """
