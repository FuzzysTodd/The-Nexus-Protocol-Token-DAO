import unittest

class TestCase(unittest.TestCase):
    def checkAstsEqual(self, a, b) -> None:
        """Compares two ASTs and fails if there are differences.

    Ignores `ctx` fields and formatting info.
    """

def requires_features(*features): ...
def supports_feature(feature): ...
