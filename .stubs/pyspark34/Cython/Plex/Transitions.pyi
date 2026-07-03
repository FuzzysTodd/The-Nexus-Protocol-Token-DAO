from _typeshed import Incomplete

maxint: Incomplete

class TransitionMap:
    """
    A TransitionMap maps an input event to a set of states.
    An input event is one of: a range of character codes,
    the empty string (representing an epsilon move), or one
    of the special symbols BOL, EOL, EOF.

    For characters, this implementation compactly represents
    the map by means of a list:

      [code_0, states_0, code_1, states_1, code_2, states_2,
        ..., code_n-1, states_n-1, code_n]

    where |code_i| is a character code, and |states_i| is a
    set of states corresponding to characters with codes |c|
    in the range |code_i| <= |c| <= |code_i+1|.

    The following invariants hold:
      n >= 1
      code_0 == -maxint
      code_n == maxint
      code_i < code_i+1 for i in 0..n-1
      states_0 == states_n-1

    Mappings for the special events '', BOL, EOL, EOF are
    kept separately in a dictionary.
    """
    map: Incomplete
    special: Incomplete
    def __init__(self, map: Incomplete | None = None, special: Incomplete | None = None) -> None: ...
    def add(self, event, new_state) -> None:
        """
        Add transition to |new_state| on |event|.
        """
    def add_set(self, event, new_set) -> None:
        """
        Add transitions to the states in |new_set| on |event|.
        """
    def get_epsilon(self):
        """
        Return the mapping for epsilon, or None.
        """
    def iteritems(self):
        """
        Return the mapping as an iterable of ((code1, code2), state_set) and
        (special_event, state_set) pairs.
        """
    items = iteritems
    def split(self, code):
        """
        Search the list for the position of the split point for |code|,
        inserting a new split point if necessary. Returns index |i| such
        that |code| == |map[i]|.
        """
    def get_special(self, event):
        """
        Get state set for special event, adding a new entry if necessary.
        """
    def check(self) -> None:
        """Check data structure integrity."""
    def dump(self, file) -> None: ...
    def dump_range(self, code0, code1, set, file) -> None: ...
    def dump_char(self, code): ...
    def dump_trans(self, key, set, file) -> None: ...
    def dump_set(self, set): ...

def state_set_str(set): ...
