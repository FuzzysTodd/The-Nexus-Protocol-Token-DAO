from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.autograph.core import config as config, converter as converter
from tensorflow.python.autograph.impl import api as api
from tensorflow.python.framework import ops as ops
from tensorflow.python.platform import test as test

def allowlist(f) -> None:
    """Helper that marks a callable as whtelitisted."""
def is_inside_generated_code():
    """Tests whether the caller is generated code. Implementation-specific."""

class TestingTranspiler(api.PyToTF):
    """Testing version that only applies given transformations."""
    transformed_ast: Incomplete
    def __init__(self, converters, ag_overrides) -> None: ...
    def get_extra_locals(self): ...
    transform_ctx: Incomplete
    def transform_ast(self, node, ctx): ...

class TestCase(test.TestCase):
    """Base class for unit tests in this module. Contains relevant utilities."""
    graph: Incomplete
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def assertPrints(self, expected_result) -> Generator[None, None, None]: ...
    def transform(self, f, converter_module, include_ast: bool = False, ag_overrides: Incomplete | None = None): ...
