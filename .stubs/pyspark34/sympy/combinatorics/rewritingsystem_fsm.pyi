from _typeshed import Incomplete

class State:
    """
    A representation of a state managed by a ``StateMachine``.

    Attributes:
        name (instance of FreeGroupElement or string) -- State name which is also assigned to the Machine.
        transisitons (OrderedDict) -- Represents all the transitions of the state object.
        state_type (string) -- Denotes the type (accept/start/dead) of the state.
        rh_rule (instance of FreeGroupElement) -- right hand rule for dead state.
        state_machine (instance of StateMachine object) -- The finite state machine that the state belongs to.
    """
    name: Incomplete
    transitions: Incomplete
    state_machine: Incomplete
    state_type: Incomplete
    rh_rule: Incomplete
    def __init__(self, name, state_machine, state_type: Incomplete | None = None, rh_rule: Incomplete | None = None) -> None: ...
    def add_transition(self, letter, state) -> None:
        """
        Add a transition from the current state to a new state.

        Keyword Arguments:
            letter -- The alphabet element the current state reads to make the state transition.
            state -- This will be an instance of the State object which represents a new state after in the transition after the alphabet is read.

        """

class StateMachine:
    """
    Representation of a finite state machine the manages the states and the transitions of the automaton.

    Attributes:
        states (dictionary) -- Collection of all registered `State` objects.
        name (str) -- Name of the state machine.
    """
    name: Incomplete
    automaton_alphabet: Incomplete
    states: Incomplete
    def __init__(self, name, automaton_alphabet) -> None: ...
    def add_state(self, state_name, state_type: Incomplete | None = None, rh_rule: Incomplete | None = None) -> None:
        """
        Instantiate a state object and stores it in the 'states' dictionary.

        Arguments:
            state_name (instance of FreeGroupElement or string) -- name of the new states.
            state_type (string) -- Denotes the type (accept/start/dead) of the state added.
            rh_rule (instance of FreeGroupElement) -- right hand rule for dead state.

        """
