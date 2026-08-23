from ..compat import collections_abc as collections_abc
from _typeshed import Incomplete

def assertProtoEqual(self, a, b, check_initialized: bool = True, normalize_numbers: bool = False, msg: Incomplete | None = None) -> None:
    """Fails with a useful error if a and b aren't equal.

  Comparison of repeated fields matches the semantics of
  unittest.TestCase.assertEqual(), ie order and extra duplicates fields matter.

  Args:
    self: googletest.TestCase
    a: proto2 PB instance, or text string representing one.
    b: proto2 PB instance -- message.Message or subclass thereof.
    check_initialized: boolean, whether to fail if either a or b isn't
      initialized.
    normalize_numbers: boolean, whether to normalize types and precision of
      numbers before comparison.
    msg: if specified, is used as the error message on failure.
  """
def NormalizeNumberFields(pb):
    """Normalizes types and precisions of number fields in a protocol buffer.

  Due to subtleties in the python protocol buffer implementation, it is possible
  for values to have different types and precision depending on whether they
  were set and retrieved directly or deserialized from a protobuf. This function
  normalizes integer values to ints and longs based on width, 32-bit floats to
  five digits of precision to account for python always storing them as 64-bit,
  and ensures doubles are floating point for when they're set to integers.

  Modifies pb in place. Recurses into nested objects.

  Args:
    pb: proto2 message.

  Returns:
    the given pb, modified in place.
  """
def ProtoEq(a, b):
    """Compares two proto2 objects for equality.

  Recurses into nested messages. Uses list (not set) semantics for comparing
  repeated fields, ie duplicates and order matter.

  Args:
    a: A proto2 message or a primitive.
    b: A proto2 message or a primitive.

  Returns:
    `True` if the messages are equal.
  """

class ProtoAssertions:
    """Mix this into a googletest.TestCase class to get proto2 assertions.

  Usage:

  class SomeTestCase(compare.ProtoAssertions, googletest.TestCase):
    ...
    def testSomething(self):
      ...
      self.assertProtoEqual(a, b)

  See module-level definitions for method documentation.
  """
    def assertProtoEqual(self, *args, **kwargs): ...
