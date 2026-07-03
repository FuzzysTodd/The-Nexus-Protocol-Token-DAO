from . import Machines as Machines
from .Machines import LOWEST_PRIORITY as LOWEST_PRIORITY
from .Transitions import TransitionMap as TransitionMap
from _typeshed import Incomplete

def nfa_to_dfa(old_machine, debug: Incomplete | None = None):
    """
    Given a nondeterministic Machine, return a new equivalent
    Machine which is deterministic.
    """
def set_epsilon_closure(state_set):
    """
    Given a set of states, return the union of the epsilon
    closures of its member states.
    """
def epsilon_closure(state):
    """
    Return the set of states reachable from the given state
    by epsilon moves.
    """
def add_to_epsilon_closure(state_set, state) -> None:
    """
    Recursively add to |state_set| states reachable from the given state
    by epsilon moves.
    """

class StateMap:
    """
    Helper class used by nfa_to_dfa() to map back and forth between
    sets of states from the old machine and states of the new machine.
    """
    new_machine: Incomplete
    old_to_new_dict: Incomplete
    new_to_old_dict: Incomplete
    def __init__(self, new_machine) -> None: ...
    def old_to_new(self, old_state_set):
        """
        Return the state of the new machine corresponding to the
        set of old machine states represented by |state_set|. A new
        state will be created if necessary. If any of the old states
        are accepting states, the new state will be an accepting state
        with the highest priority action from the old states.
        """
    def highest_priority_action(self, state_set): ...
    def new_to_old(self, new_state):
        """Given a new state, return a set of corresponding old states."""
    def make_key(self, state_set):
        """
        Convert a set of states into a uniquified
        sorted tuple suitable for use as a dictionary key.
        """
    def dump(self, file) -> None: ...
