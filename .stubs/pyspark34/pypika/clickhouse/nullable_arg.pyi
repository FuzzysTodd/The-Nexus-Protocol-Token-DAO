from pypika.terms import Function as Function

class IfNull(Function):
    def __init__(self, term, alt, **kwargs) -> None: ...
