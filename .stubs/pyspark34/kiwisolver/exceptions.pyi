from _typeshed import Incomplete

class BadRequiredStrength(Exception): ...

class DuplicateConstraint(Exception):
    constraint: Incomplete
    def __init__(self, constraint) -> None: ...

class DuplicateEditVariable(Exception):
    edit_variable: Incomplete
    def __init__(self, edit_variable) -> None: ...

class UnknownConstraint(Exception):
    constraint: Incomplete
    def __init__(self, constraint) -> None: ...

class UnknownEditVariable(Exception):
    edit_variable: Incomplete
    def __init__(self, edit_variable) -> None: ...

class UnsatisfiableConstraint(Exception):
    constraint: Incomplete
    def __init__(self, constraint) -> None: ...
