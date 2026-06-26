from _typeshed import Incomplete
from llvmlite.ir import types as types

class Context:
    scope: Incomplete
    identified_types: Incomplete
    def __init__(self) -> None: ...
    def get_identified_type(self, name): ...

global_context: Incomplete
