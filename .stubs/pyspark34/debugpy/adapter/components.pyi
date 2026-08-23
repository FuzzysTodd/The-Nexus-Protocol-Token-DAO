from _typeshed import Incomplete
from debugpy.common import json as json, log as log, messaging as messaging, util as util

ACCEPT_CONNECTIONS_TIMEOUT: int

class ComponentNotAvailable(Exception):
    def __init__(self, type) -> None: ...

class Component(util.Observable):
    """A component managed by a debug adapter: client, launcher, or debug server.

    Every component belongs to a Session, which is used for synchronization and
    shared data.

    Every component has its own message channel, and provides message handlers for
    that channel. All handlers should be decorated with @Component.message_handler,
    which ensures that Session is locked for the duration of the handler. Thus, only
    one handler is running at any given time across all components, unless the lock
    is released explicitly or via Session.wait_for().

    Components report changes to their attributes to Session, allowing one component
    to wait_for() a change caused by another component.
    """
    session: Incomplete
    channel: Incomplete
    is_connected: bool
    def __init__(self, session, stream: Incomplete | None = None, channel: Incomplete | None = None) -> None: ...
    @property
    def client(self): ...
    @property
    def launcher(self): ...
    @property
    def server(self): ...
    def wait_for(self, *args, **kwargs): ...
    @staticmethod
    def message_handler(f):
        """Applied to a message handler to automatically lock and unlock the session
        for its duration, and to validate the session state.

        If the handler raises ComponentNotAvailable or JsonIOError, converts it to
        Message.cant_handle().
        """
    def disconnect(self) -> None: ...

def missing(session, type): ...

class Capabilities(dict):
    '''A collection of feature flags for a component. Corresponds to JSON properties
    in the DAP "initialize" request or response, other than those that identify the
    party.
    '''
    PROPERTIES: Incomplete
    component: Incomplete
    def __init__(self, component, message) -> None:
        '''Parses an "initialize" request or response and extracts the feature flags.

        For every "X" in self.PROPERTIES, sets self["X"] to the corresponding value
        from message.payload if it\'s present there, or to the default value otherwise.
        '''
    def require(self, *keys) -> None: ...
