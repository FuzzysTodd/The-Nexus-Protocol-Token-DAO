__all__ = ['operators_to_state', 'state_to_operators']

def operators_to_state(operators, **options):
    """ Returns the eigenstate of the given operator or set of operators

    A global function for mapping operator classes to their associated
    states. It takes either an Operator or a set of operators and
    returns the state associated with these.

    This function can handle both instances of a given operator or
    just the class itself (i.e. both XOp() and XOp)

    There are multiple use cases to consider:

    1) A class or set of classes is passed: First, we try to
    instantiate default instances for these operators. If this fails,
    then the class is simply returned. If we succeed in instantiating
    default instances, then we try to call state._operators_to_state
    on the operator instances. If this fails, the class is returned.
    Otherwise, the instance returned by _operators_to_state is returned.

    2) An instance or set of instances is passed: In this case,
    state._operators_to_state is called on the instances passed. If
    this fails, a state class is returned. If the method returns an
    instance, that instance is returned.

    In both cases, if the operator class or set does not exist in the
    state_mapping dictionary, None is returned.

    Parameters
    ==========

    arg: Operator or set
         The class or instance of the operator or set of operators
         to be mapped to a state

    Examples
    ========

    >>> from sympy.physics.quantum.cartesian import XOp, PxOp
    >>> from sympy.physics.quantum.operatorset import operators_to_state
    >>> from sympy.physics.quantum.operator import Operator
    >>> operators_to_state(XOp)
    |x>
    >>> operators_to_state(XOp())
    |x>
    >>> operators_to_state(PxOp)
    |px>
    >>> operators_to_state(PxOp())
    |px>
    >>> operators_to_state(Operator)
    |psi>
    >>> operators_to_state(Operator())
    |psi>
    """
def state_to_operators(state, **options):
    """ Returns the operator or set of operators corresponding to the
    given eigenstate

    A global function for mapping state classes to their associated
    operators or sets of operators. It takes either a state class
    or instance.

    This function can handle both instances of a given state or just
    the class itself (i.e. both XKet() and XKet)

    There are multiple use cases to consider:

    1) A state class is passed: In this case, we first try
    instantiating a default instance of the class. If this succeeds,
    then we try to call state._state_to_operators on that instance.
    If the creation of the default instance or if the calling of
    _state_to_operators fails, then either an operator class or set of
    operator classes is returned. Otherwise, the appropriate
    operator instances are returned.

    2) A state instance is returned: Here, state._state_to_operators
    is called for the instance. If this fails, then a class or set of
    operator classes is returned. Otherwise, the instances are returned.

    In either case, if the state's class does not exist in
    state_mapping, None is returned.

    Parameters
    ==========

    arg: StateBase class or instance (or subclasses)
         The class or instance of the state to be mapped to an
         operator or set of operators

    Examples
    ========

    >>> from sympy.physics.quantum.cartesian import XKet, PxKet, XBra, PxBra
    >>> from sympy.physics.quantum.operatorset import state_to_operators
    >>> from sympy.physics.quantum.state import Ket, Bra
    >>> state_to_operators(XKet)
    X
    >>> state_to_operators(XKet())
    X
    >>> state_to_operators(PxKet)
    Px
    >>> state_to_operators(PxKet())
    Px
    >>> state_to_operators(PxBra)
    Px
    >>> state_to_operators(XBra)
    X
    >>> state_to_operators(Ket)
    O
    >>> state_to_operators(Bra)
    O
    """
