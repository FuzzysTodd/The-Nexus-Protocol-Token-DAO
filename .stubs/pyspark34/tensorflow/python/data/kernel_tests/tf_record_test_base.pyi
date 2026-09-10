from _typeshed import Incomplete
from tensorflow.core.example import example_pb2 as example_pb2, feature_pb2 as feature_pb2
from tensorflow.python.data.experimental.ops import readers as readers
from tensorflow.python.data.kernel_tests import test_base as test_base
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.lib.io import python_io as python_io
from tensorflow.python.ops import parsing_ops as parsing_ops
from tensorflow.python.util import compat as compat

class FeaturesTestBase(test_base.DatasetTestBase):
    """Base class for testing TFRecord-based features."""
    def setUp(self) -> None: ...
    filenames: Incomplete
    num_epochs: Incomplete
    batch_size: Incomplete
    def make_batch_feature(self, filenames, num_epochs, batch_size, label_key: Incomplete | None = None, reader_num_threads: int = 1, parser_num_threads: int = 1, shuffle: bool = False, shuffle_seed: Incomplete | None = None, drop_final_batch: bool = False): ...

class TFRecordTestBase(test_base.DatasetTestBase):
    """Base class for TFRecord-based tests."""
    def setUp(self) -> None: ...
