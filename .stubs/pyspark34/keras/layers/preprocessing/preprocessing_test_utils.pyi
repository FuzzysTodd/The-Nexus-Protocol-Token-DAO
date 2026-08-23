import tensorflow.compat.v2 as tf
from _typeshed import Incomplete

class ArrayLike:
    values: Incomplete
    def __init__(self, values) -> None: ...
    def __array__(self): ...

class PreprocessingLayerTest(tf.test.TestCase):
    """Base test class for preprocessing layer API validation."""
    def assertAllCloseOrEqual(self, a, b, msg: Incomplete | None = None) -> None:
        """Asserts that elements are close (if numeric) or equal (if string)."""
    def assert_extracted_output_equal(self, combiner, acc1, acc2, msg: Incomplete | None = None) -> None: ...
    compare_accumulators = assertAllCloseOrEqual
    def validate_accumulator_computation(self, combiner, data, expected) -> None:
        """Validate that various combinations of compute and merge are
        identical."""
    def validate_accumulator_extract(self, combiner, data, expected) -> None:
        """Validate that the expected results of computing and extracting."""
    def validate_accumulator_extract_and_restore(self, combiner, data, expected) -> None:
        """Validate that the extract<->restore loop loses no data."""
    def validate_accumulator_serialize_and_deserialize(self, combiner, data, expected) -> None:
        """Validate that the serialize<->deserialize loop loses no data."""
    def validate_accumulator_uniqueness(self, combiner, data) -> None:
        """Validate that every call to compute creates a unique accumulator."""
