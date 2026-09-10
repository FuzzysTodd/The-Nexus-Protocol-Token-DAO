from ..utils import DummyObject as DummyObject, requires_backends as requires_backends

class Speech2TextProcessor(metaclass=DummyObject):
    def __init__(self, *args, **kwargs) -> None: ...
