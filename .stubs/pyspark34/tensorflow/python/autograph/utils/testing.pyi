from _typeshed import Incomplete
from tensorflow.python.eager import def_function as def_function
from tensorflow.python.framework import op_callbacks as op_callbacks, ops as ops
from tensorflow.python.ops import variables as variables
from tensorflow.python.platform import test as test

class AutoGraphTestCase(test.TestCase):
    """Tests specialized for AutoGraph, which run as tf.functions.

  These tests use a staged programming-like approach: most of the test code runs
  as-is inside a tf.function, but the assertions are lifted outside the
  function, and run with the corresponding function values instead.

  For example, the test:

      def test_foo(self):
        baz = bar();
        self.assertEqual(baz, value)

  is equivalent to writing:

      def test_foo(self):
        @tf.function
        def test_fn():
          baz = bar();
          return baz, value

        baz_actual, value_actual = test_fn()
        self.assertEqual(baz_actual, value_actual)

  Only assertions that require evaluation outside the function are lifted
  outside the function scope. The rest execute inline, at function creation
  time.
  """
    def __new__(cls, *args): ...
    def variable(self, name, value, dtype): ...
    variables: Incomplete
    trace_log: Incomplete
    raises_cm: Incomplete
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def assertGraphContains(self, op_regex, n) -> None: ...
    def assertOpCreated(self, op_type) -> None: ...
    def assertOpsNotCreated(self, op_types) -> None: ...
    def assertNoOpsCreated(self) -> None: ...
    def assertEqual(self, *args) -> None: ...
    def assertLess(self, *args) -> None: ...
    def assertGreaterEqual(self, *args) -> None: ...
    def assertDictEqual(self, *args) -> None: ...
    def assertRaisesRuntime(self, *args) -> None: ...
