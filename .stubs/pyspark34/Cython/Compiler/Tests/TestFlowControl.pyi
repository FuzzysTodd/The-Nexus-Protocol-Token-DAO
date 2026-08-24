from Cython.Compiler.FlowControl import Argument as Argument, NameAssignment as NameAssignment, NameDeletion as NameDeletion, StaticAssignment as StaticAssignment
from _typeshed import Incomplete
from unittest import TestCase

class FakeType:
    is_pyobject: bool

class FakeNode:
    pos: Incomplete
    cf_state: Incomplete
    type: Incomplete
    def infer_type(self, scope): ...

class FakeEntry:
    type: Incomplete

class TestGraph(TestCase):
    def test_deepcopy(self) -> None: ...
