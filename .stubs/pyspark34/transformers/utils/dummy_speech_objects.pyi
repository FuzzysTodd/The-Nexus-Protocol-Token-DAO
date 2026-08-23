from ..utils import DummyObject as DummyObject, requires_backends as requires_backends

class ASTFeatureExtractor(metaclass=DummyObject):
    def __init__(self, *args, **kwargs) -> None: ...

class MCTCTFeatureExtractor(metaclass=DummyObject):
    def __init__(self, *args, **kwargs) -> None: ...

class Speech2TextFeatureExtractor(metaclass=DummyObject):
    def __init__(self, *args, **kwargs) -> None: ...
