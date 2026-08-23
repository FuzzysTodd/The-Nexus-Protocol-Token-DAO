from pypika.terms import Function as Function

class If(Function):
    def __init__(self, *conditions, **kwargs) -> None: ...

class MultiIf(Function):
    def __init__(self, *conditions, **kwargs) -> None: ...
