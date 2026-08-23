from _typeshed import Incomplete
from zmq.log.handlers import PUBHandler

class EnginePUBHandler(PUBHandler):
    """A simple PUBHandler subclass that sets root_topic"""
    engine: Incomplete
    def __init__(self, engine, *args, **kwargs) -> None:
        """Initialize the handler."""
    @property
    def root_topic(self):
        """this is a property, in case the handler is created
        before the engine gets registered with an id"""
