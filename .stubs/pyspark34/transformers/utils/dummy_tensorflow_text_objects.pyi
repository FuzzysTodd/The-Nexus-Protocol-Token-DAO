from ..utils import DummyObject as DummyObject, requires_backends as requires_backends

class TFBertTokenizer(metaclass=DummyObject):
    def __init__(self, *args, **kwargs) -> None: ...
