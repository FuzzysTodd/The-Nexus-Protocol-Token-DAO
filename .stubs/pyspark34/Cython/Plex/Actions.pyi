from _typeshed import Incomplete

class Action:
    def perform(self, token_stream, text) -> None: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...

class Return(Action):
    """
    Internal Plex action which causes |value| to
    be returned as the value of the associated token
    """
    value: Incomplete
    def __init__(self, value) -> None: ...
    def perform(self, token_stream, text): ...

class Call(Action):
    """
    Internal Plex action which causes a function to be called.
    """
    function: Incomplete
    def __init__(self, function) -> None: ...
    def perform(self, token_stream, text): ...

class Method(Action):
    """
    Plex action that calls a specific method on the token stream,
    passing the matched text and any provided constant keyword arguments.
    """
    name: Incomplete
    kwargs: Incomplete
    def __init__(self, name, **kwargs) -> None: ...
    def perform(self, token_stream, text): ...

class Begin(Action):
    """
    Begin(state_name) is a Plex action which causes the Scanner to
    enter the state |state_name|. See the docstring of Plex.Lexicon
    for more information.
    """
    state_name: Incomplete
    def __init__(self, state_name) -> None: ...
    def perform(self, token_stream, text) -> None: ...

class Ignore(Action):
    """
    IGNORE is a Plex action which causes its associated token
    to be ignored. See the docstring of Plex.Lexicon  for more
    information.
    """
    def perform(self, token_stream, text) -> None: ...

IGNORE: Incomplete

class Text(Action):
    """
    TEXT is a Plex action which causes the text of a token to
    be returned as the value of the token. See the docstring of
    Plex.Lexicon  for more information.
    """
    def perform(self, token_stream, text): ...

TEXT: Incomplete
