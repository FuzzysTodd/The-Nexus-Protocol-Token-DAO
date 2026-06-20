import torch._dynamo.test_case
from _typeshed import Incomplete
from torch._dynamo.debug_utils import TEST_REPLACEABLE_COMMENT as TEST_REPLACEABLE_COMMENT

class MinifierTestBase(torch._dynamo.test_case.TestCase):
    DEBUG_DIR: Incomplete
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
