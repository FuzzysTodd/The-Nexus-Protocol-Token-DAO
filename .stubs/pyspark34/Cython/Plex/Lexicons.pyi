from . import Actions as Actions, DFA as DFA, Errors as Errors, Machines as Machines, Regexps as Regexps
from _typeshed import Incomplete

DUMP_NFA: int
DUMP_DFA: int

class State:
    """
    This class is used as part of a Plex.Lexicon specification to
    introduce a user-defined state.

    Constructor:

       State(name, token_specifications)
    """
    name: Incomplete
    tokens: Incomplete
    def __init__(self, name, tokens) -> None: ...

class Lexicon:
    """
    Lexicon(specification) builds a lexical analyser from the given
    |specification|. The specification consists of a list of
    specification items. Each specification item may be either:

       1) A token definition, which is a tuple:

             (pattern, action)

          The |pattern| is a regular axpression built using the
          constructors defined in the Plex module.

          The |action| is the action to be performed when this pattern
          is recognised (see below).

       2) A state definition:

             State(name, tokens)

          where |name| is a character string naming the state,
          and |tokens| is a list of token definitions as
          above. The meaning and usage of states is described
          below.

    Actions
    -------

    The |action| in a token specification may be one of three things:

       1) A function, which is called as follows:

             function(scanner, text)

          where |scanner| is the relevant Scanner instance, and |text|
          is the matched text. If the function returns anything
          other than None, that value is returned as the value of the
          token. If it returns None, scanning continues as if the IGNORE
          action were specified (see below).

        2) One of the following special actions:

           IGNORE means that the recognised characters will be treated as
                  white space and ignored. Scanning will continue until
                  the next non-ignored token is recognised before returning.

           TEXT   causes the scanned text itself to be returned as the
                  value of the token.

        3) Any other value, which is returned as the value of the token.

    States
    ------

    At any given time, the scanner is in one of a number of states.
    Associated with each state is a set of possible tokens. When scanning,
    only tokens associated with the current state are recognised.

    There is a default state, whose name is the empty string. Token
    definitions which are not inside any State definition belong to
    the default state.

    The initial state of the scanner is the default state. The state can
    be changed in one of two ways:

       1) Using Begin(state_name) as the action of a token.

       2) Calling the begin(state_name) method of the Scanner.

    To change back to the default state, use '' as the state name.
    """
    machine: Incomplete
    tables: Incomplete
    def __init__(self, specifications, debug: Incomplete | None = None, debug_flags: int = 7) -> None: ...
    def add_token_to_machine(self, machine, initial_state, token_spec, token_number) -> None: ...
    def parse_token_definition(self, token_spec): ...
    def get_initial_state(self, name): ...
