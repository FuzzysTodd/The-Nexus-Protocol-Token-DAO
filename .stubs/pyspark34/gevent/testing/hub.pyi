from .exception import ExpectedException as ExpectedException
from _typeshed import Incomplete
from collections.abc import Generator
from gevent.hub import Hub as Hub

class QuietHub(Hub):
    EXPECTED_TEST_ERROR: Incomplete
    IGNORE_EXPECTED_TEST_ERROR: bool
    def ignoring_expected_test_error(self) -> Generator[None, None, None]:
        """
        Code in the body of this context manager will ignore
        ``EXPECTED_TEST_ERROR`` objects reported to ``handle_error``;
        they will not get a chance to go to the hub's parent.

        This completely changes the semantics of normal error handling
        by avoiding some switches (to the main greenlet, and eventually
        once a callback is processed, back to the hub). This should be used
        in narrow ways for test compatibility for tests that assume
        ``ExpectedException`` objects behave this way.
        """
    def handle_error(self, context, type, value, tb): ...
    def print_exception(self, context, t, v, tb): ...
